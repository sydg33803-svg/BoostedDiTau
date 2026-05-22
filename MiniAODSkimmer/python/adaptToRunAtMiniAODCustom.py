import FWCore.ParameterSet.Config as cms
import six, sys

import PhysicsTools.PatAlgos.tools.helpers as configtools
from PhysicsTools.PatAlgos.tools.helpers import cloneProcessingSnippet
from PhysicsTools.PatAlgos.tools.helpers import massSearchReplaceAnyInputTag
from PhysicsTools.PatAlgos.tools.helpers import removeIfInSequence
from PhysicsTools.PatUtils.l1PrefiringWeightProducer_cfi import l1PrefiringWeightProducer

##############
#Tools to adapt Tau sequences to run tau ReReco+PAT at MiniAOD samples
#With cleaned PackedPFCandidate Collection
##############



def addTauReRecoCustom(process):
    #PAT
    process.load('PhysicsTools.PatAlgos.producersLayer1.tauProducer_cff')
    process.load('PhysicsTools.PatAlgos.selectionLayer1.tauSelector_cfi')
    process.selectedPatTaus.cut="pt > 18. && tauID(\'decayModeFindingNewDMs\')> 0.5"
    #Tau RECO
    process.load("RecoTauTag.Configuration.RecoPFTauTag_cff")    
    process.miniAODTausTask = cms.Task(
        process.PFTauTask, 
        process.makePatTausTask,
        process.selectedPatTaus
    )
    process.miniAODTausSequence =cms.Sequence(process.miniAODTausTask)
    
    #######Boosted########
    transfermods=[]
    transferlabels=[]
    for mods in process.miniAODTausTask.moduleNames():
        transfermods.append(mods)
    transfermodsnew=[]
    process.miniAODTausTaskBoosted=cms.Task()
    #loop over the modules, rename and remake the task by hand
    for mod in transfermods:
        module=getattr(process,mod)
        transferlabels.append(module.label())
        newmod=module.clone()
        namepostfix='Boosted'
        newname=mod+namepostfix
        setattr(process,newname,newmod)
        process.miniAODTausTaskBoosted.add(getattr(process,newname))
    for names in process.miniAODTausTaskBoosted.moduleNames():
        if 'ak4PFJetTracksAssociatorAtVertexBoosted' in names or 'pfRecoTauTagInfoProducerBoosted' in names or 'recoTauAK4PFJets08RegionBoosted' in names:
            process.miniAODTausTaskBoosted.remove(getattr(process, names))

    from RecoTauTag.Configuration.boostedHPSPFTaus_cff import ca8PFJetsCHSprunedForBoostedTaus
    setattr(process,'ca8PFJetsCHSprunedForBoostedTausPAT',ca8PFJetsCHSprunedForBoostedTaus.clone(
        src = 'packedPFCandidates',
        jetCollInstanceName = 'subJetsForSeedingBoostedTausPAT'
    ))
    setattr(process,'boostedTauSeedsPAT',
            cms.EDProducer("PATBoostedTauSeedsProducer",
                           subjetSrc = cms.InputTag('ca8PFJetsCHSprunedForBoostedTausPAT','subJetsForSeedingBoostedTausPAT'),
                           pfCandidateSrc = cms.InputTag('packedPFCandidates'),
                           verbosity = cms.int32(0)
            ))
    process.miniAODTausTaskBoosted.add(getattr(process,'ca8PFJetsCHSprunedForBoostedTausPAT'))
    process.miniAODTausTaskBoosted.add(getattr(process,'boostedTauSeedsPAT'))

    
    process.miniAODTausSequenceBoosted=cms.Sequence(process.miniAODTausTaskBoosted)

    massSearchReplaceAnyInputTag(process.miniAODTausSequenceBoosted,cms.InputTag("ak4PFJets"),cms.InputTag("boostedTauSeedsPAT"))
    massSearchReplaceAnyInputTag(process.miniAODTausSequenceBoosted,cms.InputTag("genParticles"),cms.InputTag("prunedGenParticles"))
    massSearchReplaceAnyInputTag(process.miniAODTausSequenceBoosted,cms.InputTag("particleFlow"),cms.InputTag("packedPFCandidates"))
    massSearchReplaceAnyInputTag(process.miniAODTausSequenceBoosted,cms.InputTag("offlinePrimaryVertices"),cms.InputTag("offlineSlimmedPrimaryVertices"))

    labelpostfix='Boosted'
    renamedict={}
    for label in transferlabels:
        renamedict[label]=label+labelpostfix
    for label_old,label_new in renamedict.items():
        #print("old label: ", label_old)
        #print("new label: ", label_new)
        massSearchReplaceAnyInputTag(process.miniAODTausSequenceBoosted,label_old,label_new)    
        massSearchReplaceAnyInputTag(process.miniAODTausSequenceBoosted,cms.InputTag(label_old,"category"),cms.InputTag(label_new,"category"))
    
    #######ElectronCleaned#########
    transfermods=[]
    transferlabels=[]
    for mods in process.miniAODTausTask.moduleNames():
        transfermods.append(mods)
    transfermodsnew=[]
    process.miniAODTausTaskElectronCleaned=cms.Task()
    #loop over the modules, rename and remake the task by hand
    for mod in transfermods:
        module=getattr(process,mod)
        transferlabels.append(module.label())
        newmod=module.clone()
        namepostfix='ElectronCleaned'
        newname=mod+namepostfix
        setattr(process,newname,newmod)
        process.miniAODTausTaskElectronCleaned.add(getattr(process,newname))
    for names in process.miniAODTausTaskElectronCleaned.moduleNames():
        if 'ak4PFJetTracksAssociatorAtVertexElectronCleaned' in names or 'pfRecoTauTagInfoProducerElectronCleaned' in names or 'recoTauAK4PFJets08RegionElectronCleaned' in names:
            process.miniAODTausTaskElectronCleaned.remove(getattr(process, names))
    
        
    process.LooseFilter = cms.EDFilter("ElectronFilter",
                                   vertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                   Rho = cms.InputTag("fixedGridRhoFastjetAll"),
                                   electrons = cms.InputTag("slimmedElectrons"),
                                   conv = cms.InputTag("reducedConversions"),
                                   BM = cms.InputTag("offlineBeamSpot"),
                                   #Tracks = cms.InputTag("electronGsfTracks"),                                                       
    )    
    process.PackedCandsElectronCleaned =cms.EDProducer(
        'ElectronCleanedPackedCandidateProducer',
        electronSrc = cms.InputTag("LooseFilter","LooseElectronRef"),
        packedCandSrc = cms.InputTag("packedPFCandidates"),
    )
    
    process.electronCleanedPackedCandidateTask=cms.Task(process.LooseFilter,process.PackedCandsElectronCleaned)
    process.miniAODTausTaskElectronCleaned.add(process.electronCleanedPackedCandidateTask)
    
    labelpostfix='ElectronCleaned'
    renamedict={}
    for label in transferlabels:
        renamedict[label]=label+labelpostfix
        #print renamedict
    
    process.miniAODTausSequenceElectronCleaned =  cms.Sequence(process.miniAODTausTaskElectronCleaned)
    for label_old,label_new in renamedict.items():
        #print(" old label: ", label_old)
        #print("new label: ", label_new)
        massSearchReplaceAnyInputTag(process.miniAODTausSequenceElectronCleaned,label_old,label_new)    
        massSearchReplaceAnyInputTag(process.miniAODTausSequenceElectronCleaned,cms.InputTag(label_old,"category"),cms.InputTag(label_new,"category"))
        
    #########MuonCleaned########
    process.miniAODTausTaskMuonCleaned=cms.Task()
    for mod in transfermods:
        module=getattr(process,mod)
        #print mod
        #=============== name ==================="
        #print module.label()
        #print "=================== label ================"
        transferlabels.append(module.label())
        newmod=module.clone()
        namepostfix='MuonCleaned'
        newname=mod+namepostfix
        setattr(process,newname,newmod)
        process.miniAODTausTaskMuonCleaned.add(getattr(process,newname))
    for names in process.miniAODTausTaskMuonCleaned.moduleNames():
        if 'ak4PFJetTracksAssociatorAtVertexMuonCleaned' in names or 'pfRecoTauTagInfoProducerMuonCleaned' in names or 'recoTauAK4PFJets08RegionMuonCleaned' in names:
            process.miniAODTausTaskMuonCleaned.remove(getattr(process, names))
    

    
    process.LooseMuonFilter = cms.EDFilter('PATMuonRefSelector',
                                           src = cms.InputTag('slimmedMuons'),
                                           cut = cms.string('pt > 3.0 && isPFMuon && (isGlobalMuon || isTrackerMuon)'),
    )
    
    process.PackedCandsMuonCleaned =cms.EDProducer(
        'MuonCleanedPackedCandidateProducer',
        muonSrc = cms.InputTag("LooseMuonFilter"),
        packedCandSrc = cms.InputTag("packedPFCandidates"),
    )
    
    process.muonCleanedPackedCandidateTask=cms.Task(process.LooseMuonFilter,process.PackedCandsMuonCleaned)
    process.miniAODTausTaskMuonCleaned.add(process.muonCleanedPackedCandidateTask)
    
    labelmupostfix='MuonCleaned'
    renamedictmu={}
    for label in transferlabels:
        renamedictmu[label]=label+labelmupostfix
        #print renamedictmu
    
    process.miniAODTausSequenceMuonCleaned =  cms.Sequence(process.miniAODTausTaskMuonCleaned)
    for label_old,label_new in renamedictmu.items():
        #print " old label: ", label_old
        #print "new label: ", label_new
        massSearchReplaceAnyInputTag(process.miniAODTausSequenceMuonCleaned,label_old,label_new)    
        massSearchReplaceAnyInputTag(process.miniAODTausSequenceMuonCleaned,cms.InputTag(label_old,"category"),cms.InputTag(label_new,"category"))

    #######LowPtElectronCleaned#########
    transfermods=[]
    transferlabels=[]
    for mods in process.miniAODTausTask.moduleNames():
        transfermods.append(mods)
    transfermodsnew=[]
    process.miniAODTausTaskLowPtElectronCleaned=cms.Task()
    #loop over the modules, rename and remake the task by hand
    for mod in transfermods:
        module=getattr(process,mod)
        transferlabels.append(module.label())
        newmod=module.clone()
        namepostfix='LowPtElectronCleaned'
        newname=mod+namepostfix
        setattr(process,newname,newmod)
        process.miniAODTausTaskLowPtElectronCleaned.add(getattr(process,newname))
    for names in process.miniAODTausTaskLowPtElectronCleaned.moduleNames():
        if 'ak4PFJetTracksAssociatorAtVertexLowPtElectronCleaned' in names or 'pfRecoTauTagInfoProducerLowPtElectronCleaned' in names or 'recoTauAK4PFJets08RegionLowPtElectronCleaned' in names:
            process.miniAODTausTaskLowPtElectronCleaned.remove(getattr(process, names))
    
        
    process.LowPtFilter = cms.EDFilter("LowPtElectronFilter",
                                       electrons = cms.InputTag("slimmedLowPtElectrons"),
                                       LowPtEIdScoreCut = cms.string("4")
    )    
    process.PackedCandsLowPtElectronCleaned =cms.EDProducer(
        'LowPtElectronCleanedPackedCandidateProducer',
        electronSrc = cms.InputTag("LowPtFilter","LowPtElectronRef"),
        packedCandSrc = cms.InputTag("packedPFCandidates"),
    )
    
    process.lowPtElectronCleanedPackedCandidateTask=cms.Task(process.LowPtFilter,process.PackedCandsLowPtElectronCleaned)
    process.miniAODTausTaskLowPtElectronCleaned.add(process.lowPtElectronCleanedPackedCandidateTask)
    
    labelpostfix='LowPtElectronCleaned'
    renamedict={}
    for label in transferlabels:
        renamedict[label]=label+labelpostfix
        #print renamedict
    
    process.miniAODTausSequenceLowPtElectronCleaned =  cms.Sequence(process.miniAODTausTaskLowPtElectronCleaned)
    for label_old,label_new in renamedict.items():
        #print(" old label: ", label_old)
        #print("new label: ", label_new)
        massSearchReplaceAnyInputTag(process.miniAODTausSequenceLowPtElectronCleaned,label_old,label_new)    
        massSearchReplaceAnyInputTag(process.miniAODTausSequenceLowPtElectronCleaned,cms.InputTag(label_old,"category"),cms.InputTag(label_new,"category"))
    

    process.prefiringweight = l1PrefiringWeightProducer.clone(
        TheJets = cms.InputTag("updatedJets"), #this should be the slimmedJets collection with up to date JECs !                                       
        DataEraECAL = cms.string("UL2017BtoF"),
        DataEraMuon = cms.string("20172018"),
        UseJetEMPt = cms.bool(False),
        PrefiringRateSystematicUnctyECAL = cms.double(0.2),
        PrefiringRateSystematicUnctyMuon = cms.double(0.2)
    )

    process.prefiringweightMaker = cms.Path(process.prefiringweight)

    ######## Tau-Reco Path ####### 
    process.TauReco = cms.Path(process.miniAODTausSequence)
    process.TauRecoElectronCleaned = cms.Path(process.miniAODTausSequenceElectronCleaned)
    process.TauRecoMuonCleaned = cms.Path(process.miniAODTausSequenceMuonCleaned)
    process.TauRecoBoosted = cms.Path(process.miniAODTausSequenceBoosted)
    process.TauRecoLowPtElectronCleaned = cms.Path(process.miniAODTausSequenceLowPtElectronCleaned)
    process.schedule = cms.Schedule(process.prefiringweightMaker,process.TauReco,process.TauRecoElectronCleaned,process.TauRecoMuonCleaned, process.TauRecoBoosted, process.TauRecoLowPtElectronCleaned) 
    
    
def convertModuleToMiniAODInput(process, name):
    module = getattr(process, name)
    if hasattr(module, 'particleFlowSrc'):
        if "ElectronCleanedPackedCandidateProducer" in name or "MuonCleanedPackeCandidateProducer" in name:
            module.particleFlowSrc = cms.InputTag("packedPFCandidates", "", "")
        elif "LowPtElectronCleaned" in name:
            module.particleFlowSrc = cms.InputTag('PackedCandsLowPtElectronCleaned','packedPFCandidatesLowPtElectronCleaned')
        elif "ElectronCleaned" in name:
            module.particleFlowSrc = cms.InputTag('PackedCandsElectronCleaned','packedPFCandidatesElectronCleaned')
        elif "MuonCleaned" in name:
            module.particleFlowSrc = cms.InputTag('PackedCandsMuonCleaned','packedPFCandidatesMuonCleaned')
        else:
            module.particleFlowSrc = cms.InputTag("packedPFCandidates", "", "")
    if hasattr(module, 'vertexSrc'):
        module.vertexSrc = cms.InputTag('offlineSlimmedPrimaryVertices')
    if hasattr(module, 'qualityCuts') and hasattr(module.qualityCuts, 'primaryVertexSrc'):
        module.qualityCuts.primaryVertexSrc = cms.InputTag('offlineSlimmedPrimaryVertices')
    
def adaptTauToMiniAODReReco(process, runType, reclusterJets=True):
    #runType=kwargs.pop('runType')
    
    jetCollection = 'slimmedJets'
    # Add new jet collections if reclustering is demanded
    if reclusterJets:
        jetCollection = 'patJetsPAT'
        from RecoJets.JetProducers.ak4PFJets_cfi import ak4PFJets
        process.ak4PFJetsPAT = ak4PFJets.clone(
            src=cms.InputTag("packedPFCandidates")
        )
        # trivial PATJets
        from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import _patJets
        process.patJetsPAT = _patJets.clone(
            jetSource            = cms.InputTag("ak4PFJetsPAT"),
            addJetCorrFactors    = cms.bool(False),
            jetCorrFactorsSource = cms.VInputTag(),
            addBTagInfo          = cms.bool(False),
            addDiscriminators    = cms.bool(False),
            discriminatorSources = cms.VInputTag(),
            addAssociatedTracks  = cms.bool(False),
            addJetCharge         = cms.bool(False),
            addGenPartonMatch    = cms.bool(False),
            embedGenPartonMatch  = cms.bool(False),
            addGenJetMatch       = cms.bool(False),
            getJetMCFlavour      = cms.bool(False),
            addJetFlavourInfo    = cms.bool(False),
        )
        process.miniAODTausTask.add(process.ak4PFJetsPAT)
        process.miniAODTausTask.add(process.patJetsPAT)
        
        ###################### ElectronCleaned MuonCleaned Boosted LowPtElectronCleaned ######################
        jetCollectionElectronCleaned = 'patJetsPATElectronCleaned'
        jetCollectionLowPtElectronCleaned = 'patJetsPATLowPtElectronCleaned'
        jetCollectionMuonCleaned = 'patJetsPATMuonCleaned'
        from RecoJets.JetProducers.ak4PFJets_cfi import ak4PFJets

        ### ElectronCleaned
        process.ak4PFJetsPATElectronCleaned = ak4PFJets.clone(
            src=cms.InputTag('PackedCandsElectronCleaned','packedPFCandidatesElectronCleaned')

        )
        from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import _patJets
        process.patJetsPATElectronCleaned = _patJets.clone(
            jetSource            = cms.InputTag("ak4PFJetsPATElectronCleaned"),
            addJetCorrFactors    = cms.bool(False),
            jetCorrFactorsSource = cms.VInputTag(),
            addBTagInfo          = cms.bool(False),
            addDiscriminators    = cms.bool(False),
            discriminatorSources = cms.VInputTag(),
            addAssociatedTracks  = cms.bool(False),
            addJetCharge         = cms.bool(False),
            addGenPartonMatch    = cms.bool(False),
            embedGenPartonMatch  = cms.bool(False),
            addGenJetMatch       = cms.bool(False),
            getJetMCFlavour      = cms.bool(False),
            addJetFlavourInfo    = cms.bool(False),
        )
       
        process.miniAODTausTaskElectronCleaned.add(process.ak4PFJetsPATElectronCleaned)
        process.miniAODTausTaskElectronCleaned.add(process.patJetsPATElectronCleaned)

        ### MuonCleaned
        process.ak4PFJetsPATMuonCleaned = ak4PFJets.clone(
            src=cms.InputTag('PackedCandsMuonCleaned','packedPFCandidatesMuonCleaned')

        )
        from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import _patJets
        process.patJetsPATMuonCleaned = _patJets.clone(
            jetSource            = cms.InputTag("ak4PFJetsPATMuonCleaned"),
            addJetCorrFactors    = cms.bool(False),
            jetCorrFactorsSource = cms.VInputTag(),
            addBTagInfo          = cms.bool(False),
            addDiscriminators    = cms.bool(False),
            discriminatorSources = cms.VInputTag(),
            addAssociatedTracks  = cms.bool(False),
            addJetCharge         = cms.bool(False),
            addGenPartonMatch    = cms.bool(False),
            embedGenPartonMatch  = cms.bool(False),
            addGenJetMatch       = cms.bool(False),
            getJetMCFlavour      = cms.bool(False),
            addJetFlavourInfo    = cms.bool(False),
        )
       
        process.miniAODTausTaskMuonCleaned.add(process.ak4PFJetsPATMuonCleaned)
        process.miniAODTausTaskMuonCleaned.add(process.patJetsPATMuonCleaned)

        ### LowPtElectronCleaned
        process.ak4PFJetsPATLowPtElectronCleaned = ak4PFJets.clone(
            src=cms.InputTag('PackedCandsLowPtElectronCleaned','packedPFCandidatesLowPtElectronCleaned')

        )
        from PhysicsTools.PatAlgos.producersLayer1.jetProducer_cfi import _patJets
        process.patJetsPATLowPtElectronCleaned = _patJets.clone(
            jetSource            = cms.InputTag("ak4PFJetsPATLowPtElectronCleaned"),
            addJetCorrFactors    = cms.bool(False),
            jetCorrFactorsSource = cms.VInputTag(),
            addBTagInfo          = cms.bool(False),
            addDiscriminators    = cms.bool(False),
            discriminatorSources = cms.VInputTag(),
            addAssociatedTracks  = cms.bool(False),
            addJetCharge         = cms.bool(False),
            addGenPartonMatch    = cms.bool(False),
            embedGenPartonMatch  = cms.bool(False),
            addGenJetMatch       = cms.bool(False),
            getJetMCFlavour      = cms.bool(False),
            addJetFlavourInfo    = cms.bool(False),
        )
        
        process.miniAODTausTaskLowPtElectronCleaned.add(process.ak4PFJetsPATLowPtElectronCleaned)
        process.miniAODTausTaskLowPtElectronCleaned.add(process.patJetsPATLowPtElectronCleaned)

    process.recoTauAK4Jets08RegionPAT = cms.EDProducer("RecoTauPatJetRegionProducer",
                                                       deltaR = process.recoTauAK4PFJets08Region.deltaR,
                                                       maxJetAbsEta = process.recoTauAK4PFJets08Region.maxJetAbsEta,
                                                       minJetPt = process.recoTauAK4PFJets08Region.minJetPt,
                                                       pfCandAssocMapSrc = cms.InputTag(""),
                                                       pfCandSrc = cms.InputTag("packedPFCandidates"),
                                                       src = cms.InputTag(jetCollection)
                                                       )

    process.recoTauPileUpVertices.src = cms.InputTag("offlineSlimmedPrimaryVertices")
    # Redefine recoTauCommonTask 
    # with redefined region and PU vertices, and w/o track-to-vertex associator and tauTagInfo (the two latter are probably obsolete and not needed at all)
    process.recoTauCommonTask = cms.Task(
        process.recoTauAK4Jets08RegionPAT,
        process.recoTauPileUpVertices
    )

    # Redefine recoTauCommonTask-Boosted
    process.recoTauAK4Jets08RegionPATBoosted = cms.EDProducer("RecoTauPatJetRegionProducer",
                                                       deltaR = process.recoTauAK4PFJets08Region.deltaR,
                                                       maxJetAbsEta = process.recoTauAK4PFJets08Region.maxJetAbsEta,
                                                       minJetPt = process.recoTauAK4PFJets08Region.minJetPt,
                                                       pfCandAssocMapSrc = cms.InputTag(""),
                                                       pfCandSrc = cms.InputTag("packedPFCandidates"),
                                                       src = cms.InputTag("boostedTauSeedsPAT")
                                                       )

    process.miniAODTausTaskBoosted.add(process.recoTauAK4Jets08RegionPATBoosted)
    process.miniAODTausTaskBoosted.add(process.recoTauPileUpVerticesBoosted)

   
    # Redefine recoTauCommonTask-ElectronCleaned 
    process.recoTauAK4Jets08RegionPATElectronCleaned = cms.EDProducer("RecoTauPatJetRegionProducer",
                                                                      deltaR = process.recoTauAK4PFJets08RegionElectronCleaned.deltaR,
                                                                      maxJetAbsEta = process.recoTauAK4PFJets08RegionElectronCleaned.maxJetAbsEta,
                                                                      minJetPt = process.recoTauAK4PFJets08RegionElectronCleaned.minJetPt,
                                                                      pfCandAssocMapSrc = cms.InputTag(""),
                                                                      pfCandSrc = cms.InputTag('PackedCandsElectronCleaned','packedPFCandidatesElectronCleaned'),
                                                                      src = cms.InputTag(jetCollectionElectronCleaned)
                                                                  )

    process.recoTauPileUpVerticesElectronCleaned.src = cms.InputTag("offlineSlimmedPrimaryVertices")
    
    process.miniAODTausTaskElectronCleaned.add(process.recoTauAK4Jets08RegionPATElectronCleaned)
    process.miniAODTausTaskElectronCleaned.add(process.recoTauPileUpVerticesElectronCleaned)

    # Redefine recoTauCommonTask-MuonCleaned 
    process.recoTauAK4Jets08RegionPATMuonCleaned = cms.EDProducer("RecoTauPatJetRegionProducer",
                                                                      deltaR = process.recoTauAK4PFJets08RegionMuonCleaned.deltaR,
                                                                      maxJetAbsEta = process.recoTauAK4PFJets08RegionMuonCleaned.maxJetAbsEta,
                                                                      minJetPt = process.recoTauAK4PFJets08RegionMuonCleaned.minJetPt,
                                                                      pfCandAssocMapSrc = cms.InputTag(""),
                                                                      pfCandSrc = cms.InputTag('PackedCandsMuonCleaned','packedPFCandidatesMuonCleaned'),
                                                                      src = cms.InputTag(jetCollectionMuonCleaned)
                                                                  )

    process.recoTauPileUpVerticesMuonCleaned.src = cms.InputTag("offlineSlimmedPrimaryVertices")
    
    process.miniAODTausTaskMuonCleaned.add(process.recoTauAK4Jets08RegionPATMuonCleaned)
    process.miniAODTausTaskMuonCleaned.add(process.recoTauPileUpVerticesMuonCleaned)

    # Redefine recoTauCommonTask-LowPtElectronCleaned 
    process.recoTauAK4Jets08RegionPATLowPtElectronCleaned = cms.EDProducer("RecoTauPatJetRegionProducer",
                                                                      deltaR = process.recoTauAK4PFJets08RegionLowPtElectronCleaned.deltaR,
                                                                      maxJetAbsEta = process.recoTauAK4PFJets08RegionLowPtElectronCleaned.maxJetAbsEta,
                                                                      minJetPt = process.recoTauAK4PFJets08RegionLowPtElectronCleaned.minJetPt,
                                                                      pfCandAssocMapSrc = cms.InputTag(""),
                                                                      pfCandSrc = cms.InputTag('PackedCandsLowPtElectronCleaned','packedPFCandidatesLowPtElectronCleaned'),
                                                                      src = cms.InputTag(jetCollectionLowPtElectronCleaned)
                                                                  )

    process.recoTauPileUpVerticesLowPtElectronCleaned.src = cms.InputTag("offlineSlimmedPrimaryVertices")
    
    process.miniAODTausTaskLowPtElectronCleaned.add(process.recoTauAK4Jets08RegionPATLowPtElectronCleaned)
    process.miniAODTausTaskLowPtElectronCleaned.add(process.recoTauPileUpVerticesLowPtElectronCleaned)
    
    for moduleName in process.TauReco.moduleNames(): 
        convertModuleToMiniAODInput(process, moduleName)
        
    for moduleName in process.TauRecoElectronCleaned.moduleNames(): 
        convertModuleToMiniAODInput(process, moduleName)

    for moduleName in process.TauRecoLowPtElectronCleaned.moduleNames(): 
        convertModuleToMiniAODInput(process, moduleName)
        
    for moduleName in process.TauRecoMuonCleaned.moduleNames(): 
        convertModuleToMiniAODInput(process, moduleName)
    
    # Adapt TauPiZeros producer
    process.ak4PFJetsLegacyHPSPiZeros.builders[0].qualityCuts.primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices")
    process.ak4PFJetsLegacyHPSPiZeros.jetSrc = cms.InputTag(jetCollection)

    # Adapt TauPiZeros producer-ElectronCleaned
    process.ak4PFJetsLegacyHPSPiZerosElectronCleaned.builders[0].qualityCuts.primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices")
    process.ak4PFJetsLegacyHPSPiZerosElectronCleaned.jetSrc = cms.InputTag(jetCollectionElectronCleaned)

    # Adapt TauPiZeros producer-MuonCleaned
    process.ak4PFJetsLegacyHPSPiZerosMuonCleaned.builders[0].qualityCuts.primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices")
    process.ak4PFJetsLegacyHPSPiZerosMuonCleaned.jetSrc = cms.InputTag(jetCollectionMuonCleaned)

    # Adapt TauPiZeros producer-LowPtElectronCleaned
    process.ak4PFJetsLegacyHPSPiZerosLowPtElectronCleaned.builders[0].qualityCuts.primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices")
    process.ak4PFJetsLegacyHPSPiZerosLowPtElectronCleaned.jetSrc = cms.InputTag(jetCollectionLowPtElectronCleaned)

     

    # Adapt TauChargedHadrons producer
    for builder in process.ak4PFJetsRecoTauChargedHadrons.builders:
        builder.qualityCuts.primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices")
        if builder.name.value() == 'tracks': #replace plugin based on generalTracks by one based on lostTracks
            builder.name = 'lostTracks'
            builder.plugin = 'PFRecoTauChargedHadronFromLostTrackPlugin'
            builder.srcTracks = cms.InputTag("lostTracks")
    process.ak4PFJetsRecoTauChargedHadrons.jetSrc = cms.InputTag(jetCollection)

    # Adapt TauChargedHadrons producer-boosted
    for builder in process.ak4PFJetsRecoTauChargedHadronsBoosted.builders:
        if builder.name.value() == 'tracks': #replace plugin based on generalTracks by one based on lostTracks
            builder.name = 'lostTracks'
            builder.plugin = 'PFRecoTauChargedHadronFromLostTrackPlugin'
            builder.srcTracks = cms.InputTag("lostTracks")
    
    # Adapt TauChargedHadrons producer-ElectronCleaned
    for builder in process.ak4PFJetsRecoTauChargedHadronsElectronCleaned.builders:
        builder.qualityCuts.primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices")
        if builder.name.value() == 'tracks': #replace plugin based on generalTracks by one based on lostTracks
            builder.name = 'lostTracks'
            builder.plugin = 'PFRecoTauChargedHadronFromLostTrackPlugin'
            builder.srcTracks = cms.InputTag("lostTracks")
    process.ak4PFJetsRecoTauChargedHadronsElectronCleaned.jetSrc = cms.InputTag(jetCollectionElectronCleaned)
    
    # Adapt TauChargedHadrons producer-MuonCleaned
    for builder in process.ak4PFJetsRecoTauChargedHadronsMuonCleaned.builders:
        builder.qualityCuts.primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices")
        if builder.name.value() == 'tracks': #replace plugin based on generalTracks by one based on lostTracks
            builder.name = 'lostTracks'
            builder.plugin = 'PFRecoTauChargedHadronFromLostTrackPlugin'
            builder.srcTracks = cms.InputTag("lostTracks")
    process.ak4PFJetsRecoTauChargedHadronsMuonCleaned.jetSrc = cms.InputTag(jetCollectionMuonCleaned)

    # Adapt TauChargedHadrons producer-LowPtElectronCleaned
    for builder in process.ak4PFJetsRecoTauChargedHadronsLowPtElectronCleaned.builders:
        builder.qualityCuts.primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices")
        if builder.name.value() == 'tracks': #replace plugin based on generalTracks by one based on lostTracks
            builder.name = 'lostTracks'
            builder.plugin = 'PFRecoTauChargedHadronFromLostTrackPlugin'
            builder.srcTracks = cms.InputTag("lostTracks")
    process.ak4PFJetsRecoTauChargedHadronsLowPtElectronCleaned.jetSrc = cms.InputTag(jetCollectionLowPtElectronCleaned)
    
    
    # Adapt combinatoricRecoTau producer
    process.combinatoricRecoTaus.jetRegionSrc = 'recoTauAK4Jets08RegionPAT'
    process.combinatoricRecoTaus.jetSrc = jetCollection
    # Adapt builders
    for builder in process.combinatoricRecoTaus.builders:
        for name,value in six.iteritems(builder.parameters_()):
            if name == 'qualityCuts':
                builder.qualityCuts.primaryVertexSrc = 'offlineSlimmedPrimaryVertices'
            elif name == 'pfCandSrc':
                builder.pfCandSrc = 'packedPFCandidates'

    # Adapt combinatoricRecoTauBoosted producer
    process.combinatoricRecoTausBoosted.jetRegionSrc = 'recoTauAK4Jets08RegionPATBoosted'
                
    # Adapt combinatoricRecoTau producer - ElectronCleaned
    process.combinatoricRecoTausElectronCleaned.jetRegionSrc = 'recoTauAK4Jets08RegionPATElectronCleaned'
    process.combinatoricRecoTausElectronCleaned.jetSrc = jetCollectionElectronCleaned
    # Adapt builders - ElectronCleaned                                                                                                                 
    for builder in process.combinatoricRecoTausElectronCleaned.builders:
        for name,value in six.iteritems(builder.parameters_()):
            if name == 'qualityCuts':
                builder.qualityCuts.primaryVertexSrc = 'offlineSlimmedPrimaryVertices'
            elif name == 'pfCandSrc':
                builder.pfCandSrc =cms.InputTag('PackedCandsElectronCleaned','packedPFCandidatesElectronCleaned')
    
    # Adapt combinatoricRecoTau producer - MuonCleaned
    process.combinatoricRecoTausMuonCleaned.jetRegionSrc = 'recoTauAK4Jets08RegionPATMuonCleaned'
    process.combinatoricRecoTausMuonCleaned.jetSrc = jetCollectionMuonCleaned
    # Adapt builders - MuonCleaned                                                                                                                 
    for builder in process.combinatoricRecoTausMuonCleaned.builders:
        for name,value in six.iteritems(builder.parameters_()):
            if name == 'qualityCuts':
                builder.qualityCuts.primaryVertexSrc = 'offlineSlimmedPrimaryVertices'
            elif name == 'pfCandSrc':
                builder.pfCandSrc =cms.InputTag('PackedCandsMuonCleaned','packedPFCandidatesMuonCleaned')

    # Adapt combinatoricRecoTau producer - LowPtElectronCleaned
    process.combinatoricRecoTausLowPtElectronCleaned.jetRegionSrc = 'recoTauAK4Jets08RegionPATLowPtElectronCleaned'
    process.combinatoricRecoTausLowPtElectronCleaned.jetSrc = jetCollectionLowPtElectronCleaned
    # Adapt builders - LowPtElectronCleaned                                                                                                                 
    for builder in process.combinatoricRecoTausLowPtElectronCleaned.builders:
        for name,value in six.iteritems(builder.parameters_()):
            if name == 'qualityCuts':
                builder.qualityCuts.primaryVertexSrc = 'offlineSlimmedPrimaryVertices'
            elif name == 'pfCandSrc':
                builder.pfCandSrc =cms.InputTag('PackedCandsLowPtElectronCleaned','packedPFCandidatesLowPtElectronCleaned')
    
    # Adapt supported modifiers and remove unsupported ones 
    modifiersToRemove_ = cms.VPSet()

    for mod in process.combinatoricRecoTaus.modifiers:
        if mod.name.value() == 'elec_rej':
            modifiersToRemove_.append(mod)
            continue
        elif mod.name.value() == 'TTIworkaround':
            modifiersToRemove_.append(mod)
            continue
        for name,value in six.iteritems(mod.parameters_()):
            if name == 'qualityCuts':
                mod.qualityCuts.primaryVertexSrc = 'offlineSlimmedPrimaryVertices'
    for mod in modifiersToRemove_:
        process.combinatoricRecoTaus.modifiers.remove(mod)

    modifiersToRemoveBoosted_ = cms.VPSet()

    for mod in process.combinatoricRecoTausBoosted.modifiers:
        if mod.name.value() == 'elec_rej':
            modifiersToRemoveBoosted_.append(mod)
            continue
        elif mod.name.value() == 'TTIworkaround':
            modifiersToRemoveBoosted_.append(mod)
            continue
        for name,value in six.iteritems(mod.parameters_()):
            if name == 'qualityCuts':
                mod.qualityCuts.primaryVertexSrc = 'offlineSlimmedPrimaryVertices'
    for mod in modifiersToRemoveBoosted_:
        process.combinatoricRecoTausBoosted.modifiers.remove(mod)
    
    modifiersToRemoveElectronCleaned_ = cms.VPSet()  
    
    for mod in process.combinatoricRecoTausElectronCleaned.modifiers:
        if mod.name.value() == 'elec_rej':
            modifiersToRemoveElectronCleaned_.append(mod)
            continue
        elif mod.name.value() == 'TTIworkaround':
            modifiersToRemoveElectronCleaned_.append(mod)
            continue
        for name,value in six.iteritems(mod.parameters_()):
            if name == 'qualityCuts':
                mod.qualityCuts.primaryVertexSrc = 'offlineSlimmedPrimaryVertices'
    for mod in modifiersToRemoveElectronCleaned_:
        process.combinatoricRecoTausElectronCleaned.modifiers.remove(mod)

    modifiersToRemoveMuonCleaned_ = cms.VPSet()  
    
    for mod in process.combinatoricRecoTausMuonCleaned.modifiers:
        if mod.name.value() == 'elec_rej':
            modifiersToRemoveMuonCleaned_.append(mod)
            continue
        elif mod.name.value() == 'TTIworkaround':
            modifiersToRemoveMuonCleaned_.append(mod)
            continue
        for name,value in six.iteritems(mod.parameters_()):
            if name == 'qualityCuts':
                mod.qualityCuts.primaryVertexSrc = 'offlineSlimmedPrimaryVertices'
    for mod in modifiersToRemoveMuonCleaned_:
        process.combinatoricRecoTausMuonCleaned.modifiers.remove(mod)

    modifiersToRemoveLowPtElectronCleaned_ = cms.VPSet()  
    
    for mod in process.combinatoricRecoTausLowPtElectronCleaned.modifiers:
        if mod.name.value() == 'elec_rej':
            modifiersToRemoveLowPtElectronCleaned_.append(mod)
            continue
        elif mod.name.value() == 'TTIworkaround':
            modifiersToRemoveLowPtElectronCleaned_.append(mod)
            continue
        for name,value in six.iteritems(mod.parameters_()):
            if name == 'qualityCuts':
                mod.qualityCuts.primaryVertexSrc = 'offlineSlimmedPrimaryVertices'
    for mod in modifiersToRemoveLowPtElectronCleaned_:
        process.combinatoricRecoTausLowPtElectronCleaned.modifiers.remove(mod)

    
    # Redefine tau PV producer
    process.hpsPFTauPrimaryVertexProducer.__dict__['_TypedParameterizable__type'] = 'PFTauMiniAODPrimaryVertexProducer'
    process.hpsPFTauPrimaryVertexProducer.PVTag = 'offlineSlimmedPrimaryVertices'
    process.hpsPFTauPrimaryVertexProducer.packedCandidatesTag = cms.InputTag("packedPFCandidates")
    process.hpsPFTauPrimaryVertexProducer.lostCandidatesTag = cms.InputTag("lostTracks")

    # Redefine tau PV producer-ElectronCleaned
    process.hpsPFTauPrimaryVertexProducerElectronCleaned.__dict__['_TypedParameterizable__type'] = 'PFTauMiniAODPrimaryVertexProducer'
    process.hpsPFTauPrimaryVertexProducerElectronCleaned.PVTag = 'offlineSlimmedPrimaryVertices'
    process.hpsPFTauPrimaryVertexProducerElectronCleaned.packedCandidatesTag = cms.InputTag('PackedCandsElectronCleaned','packedPFCandidatesElectronCleaned')
    process.hpsPFTauPrimaryVertexProducerElectronCleaned.lostCandidatesTag = cms.InputTag("lostTracks")
    
    # Redefine tau PV producer-MuonCleaned
    process.hpsPFTauPrimaryVertexProducerMuonCleaned.__dict__['_TypedParameterizable__type'] = 'PFTauMiniAODPrimaryVertexProducer'
    process.hpsPFTauPrimaryVertexProducerMuonCleaned.PVTag = 'offlineSlimmedPrimaryVertices'
    process.hpsPFTauPrimaryVertexProducerMuonCleaned.packedCandidatesTag = cms.InputTag('PackedCandsMuonCleaned','packedPFCandidatesMuonCleaned')
    process.hpsPFTauPrimaryVertexProducerMuonCleaned.lostCandidatesTag = cms.InputTag("lostTracks")

    # Redefine tau PV producer-LowPtElectronCleaned
    process.hpsPFTauPrimaryVertexProducerLowPtElectronCleaned.__dict__['_TypedParameterizable__type'] = 'PFTauMiniAODPrimaryVertexProducer'
    process.hpsPFTauPrimaryVertexProducerLowPtElectronCleaned.PVTag = 'offlineSlimmedPrimaryVertices'
    process.hpsPFTauPrimaryVertexProducerLowPtElectronCleaned.packedCandidatesTag = cms.InputTag('PackedCandsLowPtElectronCleaned','packedPFCandidatesLowPtElectronCleaned')
    process.hpsPFTauPrimaryVertexProducerLowPtElectronCleaned.lostCandidatesTag = cms.InputTag("lostTracks")
    
    
    # Redefine tau SV producer
    process.hpsPFTauSecondaryVertexProducer = cms.EDProducer("PFTauSecondaryVertexProducer",
                                                             PFTauTag = cms.InputTag("hpsPFTauProducer")
    )

    # Redefine tau SV producer-Boosted
    process.hpsPFTauSecondaryVertexProducerBoosted = cms.EDProducer("PFTauSecondaryVertexProducer",
                                                             PFTauTag = cms.InputTag("hpsPFTauProducerBoosted")
    )
    
    # Redefine tau SV producer-ElectronCleaned
    process.hpsPFTauSecondaryVertexProducerElectronCleaned = cms.EDProducer("PFTauSecondaryVertexProducer",
                                                             PFTauTag = cms.InputTag("hpsPFTauProducerElectronCleaned")
    )
    
    # Redefine tau SV producer-MuonCleaned
    process.hpsPFTauSecondaryVertexProducerMuonCleaned = cms.EDProducer("PFTauSecondaryVertexProducer",
                                                             PFTauTag = cms.InputTag("hpsPFTauProducerMuonCleaned")
    )

    # Redefine tau SV producer-LowPtElectronCleaned
    process.hpsPFTauSecondaryVertexProducerLowPtElectronCleaned = cms.EDProducer("PFTauSecondaryVertexProducer",
                                                             PFTauTag = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned")
    )
    
    # Remove RecoTau producers which are not supported (yet?), i.e. against-e/mu discriminats
    for moduleName in process.TauReco.moduleNames(): 
        if 'ElectronRejection' in moduleName or 'MuonRejection' in moduleName:
            if 'ByDeadECALElectronRejection' in moduleName: continue
            process.miniAODTausTask.remove(getattr(process, moduleName))

    # Remove RecoTau producers which are not supported (yet?), i.e. against-e/mu discriminats
    for moduleName in process.TauRecoBoosted.moduleNames(): 
        if 'ElectronRejection' in moduleName or 'MuonRejection' in moduleName:
            if 'ByDeadECALElectronRejection' in moduleName: continue
            process.miniAODTausTaskBoosted.remove(getattr(process, moduleName))
    
    
    # Remove RecoTau producers which are not supported (yet?), i.e. against-e/mu discriminats
    for moduleName in process.TauRecoElectronCleaned.moduleNames(): 
        if 'ElectronRejection' in moduleName or 'MuonRejection' in moduleName:
            if 'ByDeadECALElectronRejection' in moduleName: continue
            process.miniAODTausTaskElectronCleaned.remove(getattr(process, moduleName))
    

    # Remove RecoTau producers which are not supported (yet?), i.e. against-e/mu discriminats
    for moduleName in process.TauRecoMuonCleaned.moduleNames(): 
        if 'ElectronRejection' in moduleName or 'MuonRejection' in moduleName:
            if 'ByDeadECALElectronRejection' in moduleName: continue
            process.miniAODTausTaskMuonCleaned.remove(getattr(process, moduleName))

    # Remove RecoTau producers which are not supported (yet?), i.e. against-e/mu discriminats
    for moduleName in process.TauRecoLowPtElectronCleaned.moduleNames(): 
        if 'ElectronRejection' in moduleName or 'MuonRejection' in moduleName:
            if 'ByDeadECALElectronRejection' in moduleName: continue
            process.miniAODTausTaskLowPtElectronCleaned.remove(getattr(process, moduleName))
    
    # Instead add against-mu discriminants which are MiniAOD compatible
    from RecoTauTag.RecoTau.hpsPFTauDiscriminationByMuonRejectionSimple_cff import hpsPFTauDiscriminationByMuonRejectionSimple
    
    process.hpsPFTauDiscriminationByMuonRejectionSimple = hpsPFTauDiscriminationByMuonRejectionSimple
    process.miniAODTausTask.add(process.hpsPFTauDiscriminationByMuonRejectionSimple)

    process.hpsPFTauDiscriminationByMuonRejectionSimpleBoosted = hpsPFTauDiscriminationByMuonRejectionSimple.clone(PFTauProducer = cms.InputTag("hpsPFTauProducerBoosted"))
    process.miniAODTausTask.add(process.hpsPFTauDiscriminationByMuonRejectionSimpleBoosted)

    process.hpsPFTauDiscriminationByMuonRejectionSimpleElectronCleaned = process.hpsPFTauDiscriminationByMuonRejectionSimple.clone(PFTauProducer = cms.InputTag("hpsPFTauProducerElectronCleaned"))
    process.miniAODTausTaskElectronCleaned.add(process.hpsPFTauDiscriminationByMuonRejectionSimpleElectronCleaned)
    
    process.hpsPFTauDiscriminationByMuonRejectionSimpleMuonCleaned = process.hpsPFTauDiscriminationByMuonRejectionSimple.clone(PFTauProducer = cms.InputTag("hpsPFTauProducerMuonCleaned"))
    process.miniAODTausTaskMuonCleaned.add(process.hpsPFTauDiscriminationByMuonRejectionSimpleMuonCleaned)

    process.hpsPFTauDiscriminationByMuonRejectionSimpleLowPtElectronCleaned = process.hpsPFTauDiscriminationByMuonRejectionSimple.clone(PFTauProducer = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned"))
    process.miniAODTausTaskLowPtElectronCleaned.add(process.hpsPFTauDiscriminationByMuonRejectionSimpleLowPtElectronCleaned)    

    #####
    # PAT part in the following
    if runType=='signal' or runType=='background':
        print(runType,': Identified')
    
        process.tauGenJets.GenParticles = cms.InputTag("prunedGenParticles")
        process.tauMatch.matched = cms.InputTag("prunedGenParticles")

        process.tauGenJetsElectronCleaned.GenParticles = cms.InputTag("prunedGenParticles")
        process.tauMatchElectronCleaned.matched = cms.InputTag("prunedGenParticles")
   
        process.tauGenJetsMuonCleaned.GenParticles = cms.InputTag("prunedGenParticles")
        process.tauMatchMuonCleaned.matched = cms.InputTag("prunedGenParticles")

        process.tauGenJetsLowPtElectronCleaned.GenParticles = cms.InputTag("prunedGenParticles")
        process.tauMatchLowPtElectronCleaned.matched = cms.InputTag("prunedGenParticles")
    
    else:
        print (runType, ': Identified, No MC Matching')
        from PhysicsTools.PatAlgos.tools.coreTools import runOnData
        runOnData(process, names = ['Taus'], outputModules = [])
        runOnData(process, names = ['Taus'],outputModules = [],postfix='MuonCleaned')
        runOnData(process, names = ['Taus'],outputModules = [],postfix='ElectronCleaned')
        runOnData(process, names = ['Taus'],outputModules = [],postfix='LowPtElectronCleaned')
        
    # Remove unsupported tauIDs
    for name, src in six.iteritems(process.patTaus.tauIDSources.parameters_()):
        if name.find('againstElectron') > -1 or name.find('againstMuon') > -1:
            if name.find('againstElectronDeadECAL') > -1: continue
            delattr(process.patTaus.tauIDSources,name)
    # Add MiniAOD specific ones
        setattr(process.patTaus.tauIDSources,'againstMuonLooseSimple',
            cms.PSet(inputTag = cms.InputTag('hpsPFTauDiscriminationByMuonRejectionSimple'),
                     provenanceConfigLabel = cms.string('IDWPdefinitions'),
                     idLabel = cms.string('ByLooseMuonRejectionSimple')
                 ))
    
    setattr(process.patTaus.tauIDSources,'againstMuonTightSimple',
            cms.PSet(inputTag = cms.InputTag('hpsPFTauDiscriminationByMuonRejectionSimple'),
                     provenanceConfigLabel = cms.string('IDWPdefinitions'),
                     idLabel = cms.string('ByTightMuonRejectionSimple')
                 ))

    # Remove unsupported tauIDs-Boosted
    for name, src in six.iteritems(process.patTausBoosted.tauIDSources.parameters_()):
        if name.find('againstElectron') > -1 or name.find('againstMuon') > -1:
            if name.find('againstElectronDeadECAL') > -1 : continue #and name.find('Boosted') > -1: continue
            delattr(process.patTausBoosted.tauIDSources,name)
    # Add MiniAOD specific ones
    setattr(process.patTausBoosted.tauIDSources,'againstMuonLooseSimple',
            cms.PSet(inputTag = cms.InputTag('hpsPFTauDiscriminationByMuonRejectionSimpleBoosted'),
                     provenanceConfigLabel = cms.string('IDWPdefinitions'),
                     idLabel = cms.string('ByLooseMuonRejectionSimple')
                 ))
    
    setattr(process.patTausBoosted.tauIDSources,'againstMuonTightSimple',
            cms.PSet(inputTag = cms.InputTag('hpsPFTauDiscriminationByMuonRejectionSimpleBoosted'),
                     provenanceConfigLabel = cms.string('IDWPdefinitions'),
                     idLabel = cms.string('ByTightMuonRejectionSimple')
                 ))

    # Remove unsupported tauIDs-ElectronCleaned
    for name, src in six.iteritems(process.patTausElectronCleaned.tauIDSources.parameters_()):
        if name.find('againstElectron') > -1 or name.find('againstMuon') > -1:
            if name.find('againstElectronDeadECAL') > -1 : continue #and name.find('ElectronCleaned') > -1: continue
            delattr(process.patTausElectronCleaned.tauIDSources,name)
    # Add MiniAOD specific ones
    setattr(process.patTausElectronCleaned.tauIDSources,'againstMuonLooseSimple',
            cms.PSet(inputTag = cms.InputTag('hpsPFTauDiscriminationByMuonRejectionSimpleElectronCleaned'),
                     provenanceConfigLabel = cms.string('IDWPdefinitions'),
                     idLabel = cms.string('ByLooseMuonRejectionSimple')
                 ))
    
    setattr(process.patTausElectronCleaned.tauIDSources,'againstMuonTightSimple',
            cms.PSet(inputTag = cms.InputTag('hpsPFTauDiscriminationByMuonRejectionSimpleElectronCleaned'),
                     provenanceConfigLabel = cms.string('IDWPdefinitions'),
                     idLabel = cms.string('ByTightMuonRejectionSimple')
                 ))
    
    # Remove unsupported tauIDs-MuonCleaned
    for name, src in six.iteritems(process.patTausMuonCleaned.tauIDSources.parameters_()):
        if name.find('againstElectron') > -1 or name.find('againstMuon') > -1:
            if name.find('againstElectronDeadECAL') > -1 : continue #and name.find('MuonCleaned'): continue
            delattr(process.patTausMuonCleaned.tauIDSources,name)
    setattr(process.patTausMuonCleaned.tauIDSources,'againstMuonLooseSimple',
            cms.PSet(inputTag = cms.InputTag('hpsPFTauDiscriminationByMuonRejectionSimpleMuonCleaned'),
                     provenanceConfigLabel = cms.string('IDWPdefinitions'),
                     idLabel = cms.string('ByLooseMuonRejectionSimple')
                 ))
    
    setattr(process.patTausMuonCleaned.tauIDSources,'againstMuonTightSimple',
            cms.PSet(inputTag = cms.InputTag('hpsPFTauDiscriminationByMuonRejectionSimpleMuonCleaned'),
                     provenanceConfigLabel = cms.string('IDWPdefinitions'),
                     idLabel = cms.string('ByTightMuonRejectionSimple')
                 ))

    # Remove unsupported tauIDs-LowPtElectronCleaned
    for name, src in six.iteritems(process.patTausLowPtElectronCleaned.tauIDSources.parameters_()):
        if name.find('againstElectron') > -1 or name.find('againstMuon') > -1:
            if name.find('againstElectronDeadECAL') > -1 : continue #and name.find('LowPtElectronCleaned') > -1: continue
            delattr(process.patTausLowPtElectronCleaned.tauIDSources,name)
    # Add MiniAOD specific ones
    setattr(process.patTausLowPtElectronCleaned.tauIDSources,'againstMuonLooseSimple',
            cms.PSet(inputTag = cms.InputTag('hpsPFTauDiscriminationByMuonRejectionSimpleLowPtElectronCleaned'),
                     provenanceConfigLabel = cms.string('IDWPdefinitions'),
                     idLabel = cms.string('ByLooseMuonRejectionSimple')
                 ))
    
    setattr(process.patTausLowPtElectronCleaned.tauIDSources,'againstMuonTightSimple',
            cms.PSet(inputTag = cms.InputTag('hpsPFTauDiscriminationByMuonRejectionSimpleLowPtElectronCleaned'),
                     provenanceConfigLabel = cms.string('IDWPdefinitions'),
                     idLabel = cms.string('ByTightMuonRejectionSimple')
                 ))
    
    print('New ID')
    # Run TauIDs (anti-e && deepTau) on top of selectedPatTaus
    _updatedTauName = 'selectedPatTausNewIDs'
    _noUpdatedTauName = 'selectedPatTausNoNewIDs'
    import RecoTauTag.RecoTau.tools.runTauIdMVA as tauIdConfig
    tauIdEmbedder = tauIdConfig.TauIDEmbedder(
        process, debug = False,
        updatedTauName = _updatedTauName,
        toKeep = ['againstEle2018','deepTau2017v2p1','2017v2']
    )
    tauIdEmbedder.runTauID()
    setattr(process, _noUpdatedTauName, process.selectedPatTaus.clone(cut = cms.string('pt > 8.0 && abs(eta)<2.3 && tauID(\'decayModeFinding\')> 0.5')))
    process.miniAODTausTask.add(getattr(process,_noUpdatedTauName))
    delattr(process, 'selectedPatTaus')
    process.deepTau2017v2p1.taus = _noUpdatedTauName
    process.patTauDiscriminationByElectronRejectionMVA62018Raw.PATTauProducer = _noUpdatedTauName
    process.patTauDiscriminationByElectronRejectionMVA62018.PATTauProducer = _noUpdatedTauName
    process.rerunDiscriminationByIsolationOldDMMVArun2017v2raw.PATTauProducer = _noUpdatedTauName
    process.rerunDiscriminationByIsolationOldDMMVArun2017v2.PATTauProducer = _noUpdatedTauName
    process.selectedPatTaus = getattr(process, _updatedTauName).clone(
        src = _noUpdatedTauName
    )
    process.newTauIDsTask = cms.Task(
        process.rerunMvaIsolationTask,
        process.selectedPatTaus
    )
    process.miniAODTausTask.add(process.newTauIDsTask)
    print('New ID Done')
    
    print('New ID ElectronCleaned')
    # Run TauIDs (anti-e && deepTau) on top of selectedPatTaus-ElectronCleaned
    _updatedTauNameElectronCleaned = 'selectedPatTausNewIDsElectronCleaned'
    _noUpdatedTauNameElectronCleaned = 'selectedPatTausNoNewIDsElectronCleaned'
    
    import BoostedDiTau.MiniAODSkimmer.tools.runTauIdMVA_ElectronCleaned as tauIdConfigElectronCleaned
    tauIdEmbedderElectronCleaned = tauIdConfigElectronCleaned.TauIDEmbedder(
        process, debug = False,
        updatedTauName = _updatedTauNameElectronCleaned,
        postfix="ElectronCleaned",
        toKeep = ['againstEle2018','deepTau2017v2p1','2017v2']
    )
    tauIdEmbedderElectronCleaned.runTauID()
    setattr(process, _noUpdatedTauNameElectronCleaned, process.selectedPatTausElectronCleaned.clone(cut = cms.string('pt > 8.0 && abs(eta)<2.3 && tauID(\'decayModeFinding\')> 0.5')))
    process.miniAODTausTaskElectronCleaned.add(getattr(process,_noUpdatedTauNameElectronCleaned))
    delattr(process,'selectedPatTausElectronCleaned')
    process.deepTau2017v2p1ElectronCleaned.taus = _noUpdatedTauNameElectronCleaned
    process.patTauDiscriminationByElectronRejectionMVA62018RawElectronCleaned.PATTauProducer = _noUpdatedTauNameElectronCleaned
    process.patTauDiscriminationByElectronRejectionMVA62018ElectronCleaned.PATTauProducer = _noUpdatedTauNameElectronCleaned
    process.rerunDiscriminationByIsolationOldDMMVArun2017v2rawElectronCleaned.PATTauProducer = _noUpdatedTauNameElectronCleaned
    process.rerunDiscriminationByIsolationOldDMMVArun2017v2ElectronCleaned.PATTauProducer = _noUpdatedTauNameElectronCleaned
    process.selectedPatTausElectronCleaned = getattr(process, _updatedTauNameElectronCleaned).clone(
        src = _noUpdatedTauNameElectronCleaned
    )
    process.newTauIDsTaskElectronCleaned = cms.Task(
        process.rerunMvaIsolationTaskElectronCleaned,
        process.selectedPatTausElectronCleaned
    )
    process.miniAODTausTaskElectronCleaned.add(process.newTauIDsTaskElectronCleaned)
    print('New ID ElectronCleaned - Done ')
    
    print('New ID MuonCleaned')
    # Run TauIDs (anti-e && deepTau) on top of selectedPatTaus-MuonCleaned
    _updatedTauNameMuonCleaned = 'selectedPatTausNewIDsMuonCleaned'
    _noUpdatedTauNameMuonCleaned = 'selectedPatTausNoNewIDsMuonCleaned'
    
    import BoostedDiTau.MiniAODSkimmer.tools.runTauIdMVA_MuonCleaned as tauIdConfigMuonCleaned
    tauIdEmbedderMuonCleaned = tauIdConfigMuonCleaned.TauIDEmbedder(
        process, debug = False,
        updatedTauName = _updatedTauNameMuonCleaned,
        postfix="MuonCleaned",
        toKeep = ['againstEle2018','deepTau2017v2p1','2017v2']
    )
    tauIdEmbedderMuonCleaned.runTauID()
    setattr(process, _noUpdatedTauNameMuonCleaned, process.selectedPatTausMuonCleaned.clone(cut = cms.string('pt > 8.0 && abs(eta)<2.3 && tauID(\'decayModeFinding\')> 0.5')))
    process.miniAODTausTaskMuonCleaned.add(getattr(process,_noUpdatedTauNameMuonCleaned))
    delattr(process,'selectedPatTausMuonCleaned')
    process.deepTau2017v2p1MuonCleaned.taus = _noUpdatedTauNameMuonCleaned
    process.patTauDiscriminationByElectronRejectionMVA62018RawMuonCleaned.PATTauProducer = _noUpdatedTauNameMuonCleaned
    process.patTauDiscriminationByElectronRejectionMVA62018MuonCleaned.PATTauProducer = _noUpdatedTauNameMuonCleaned
    process.rerunDiscriminationByIsolationOldDMMVArun2017v2rawMuonCleaned.PATTauProducer = _noUpdatedTauNameMuonCleaned
    process.rerunDiscriminationByIsolationOldDMMVArun2017v2MuonCleaned.PATTauProducer = _noUpdatedTauNameMuonCleaned
    process.selectedPatTausMuonCleaned = getattr(process, _updatedTauNameMuonCleaned).clone(
        src = _noUpdatedTauNameMuonCleaned
    )
    process.newTauIDsTaskMuonCleaned = cms.Task(
        process.rerunMvaIsolationTaskMuonCleaned,
        process.selectedPatTausMuonCleaned
    )
    process.miniAODTausTaskMuonCleaned.add(process.newTauIDsTaskMuonCleaned)
    print('New ID MuonCleaned - Done ')

    print('New ID LowPtElectronCleaned')
    # Run TauIDs (anti-e && deepTau) on top of selectedPatTaus-LowPtElectronCleaned
    _updatedTauNameLowPtElectronCleaned = 'selectedPatTausNewIDsLowPtElectronCleaned'
    _noUpdatedTauNameLowPtElectronCleaned = 'selectedPatTausNoNewIDsLowPtElectronCleaned'
    
    import BoostedDiTau.MiniAODSkimmer.tools.runTauIdMVA_LowPtElectronCleaned as tauIdConfigLowPtElectronCleaned
    tauIdEmbedderLowPtElectronCleaned = tauIdConfigLowPtElectronCleaned.TauIDEmbedder(
        process, debug = False,
        updatedTauName = _updatedTauNameLowPtElectronCleaned,
        postfix="LowPtElectronCleaned",
        toKeep = ['againstEle2018','deepTau2017v2p1','2017v2']
    )
    tauIdEmbedderLowPtElectronCleaned.runTauID()
    setattr(process, _noUpdatedTauNameLowPtElectronCleaned, process.selectedPatTausLowPtElectronCleaned.clone(cut = cms.string('pt > 8.0 && abs(eta)<2.3 && tauID(\'decayModeFinding\')> 0.5')))
    process.miniAODTausTaskLowPtElectronCleaned.add(getattr(process,_noUpdatedTauNameLowPtElectronCleaned))
    delattr(process,'selectedPatTausLowPtElectronCleaned')
    process.deepTau2017v2p1LowPtElectronCleaned.taus = _noUpdatedTauNameLowPtElectronCleaned
    process.patTauDiscriminationByElectronRejectionMVA62018RawLowPtElectronCleaned.PATTauProducer = _noUpdatedTauNameLowPtElectronCleaned
    process.patTauDiscriminationByElectronRejectionMVA62018LowPtElectronCleaned.PATTauProducer = _noUpdatedTauNameLowPtElectronCleaned
    process.rerunDiscriminationByIsolationOldDMMVArun2017v2rawLowPtElectronCleaned.PATTauProducer = _noUpdatedTauNameLowPtElectronCleaned
    process.rerunDiscriminationByIsolationOldDMMVArun2017v2LowPtElectronCleaned.PATTauProducer = _noUpdatedTauNameLowPtElectronCleaned
    process.selectedPatTausLowPtElectronCleaned = getattr(process, _updatedTauNameLowPtElectronCleaned).clone(
        src = _noUpdatedTauNameLowPtElectronCleaned
    )
    process.newTauIDsTaskLowPtElectronCleaned = cms.Task(
        process.rerunMvaIsolationTaskLowPtElectronCleaned,
        process.selectedPatTausLowPtElectronCleaned
    )
    process.miniAODTausTaskLowPtElectronCleaned.add(process.newTauIDsTaskLowPtElectronCleaned)
    print('New ID LowPtElectronCleaned - Done ')
    
    print('New ID Boosted')
    # Run TauIDs (anti-e && deepTau) on top of selectedPatTaus-Boosted
    _updatedTauNameBoosted = 'selectedPatTausNewIDsBoosted'
    _noUpdatedTauNameBoosted = 'selectedPatTausNoNewIDsBoosted'
    
    import BoostedDiTau.MiniAODSkimmer.tools.runTauIdMVA_Boosted as tauIdConfigBoosted
    tauIdEmbedderBoosted = tauIdConfigBoosted.TauIDEmbedder(
        process, debug = False,
        updatedTauName = _updatedTauNameBoosted,
        postfix="Boosted",
        toKeep = ['againstEle2018','deepTau2017v2p1','2017v2']
    )
    tauIdEmbedderBoosted.runTauID()
    setattr(process, _noUpdatedTauNameBoosted, process.selectedPatTausBoosted.clone(cut = cms.string('pt > 8.0 && abs(eta)<2.3 && tauID(\'decayModeFinding\')> 0.5')))
    process.miniAODTausTaskBoosted.add(getattr(process,_noUpdatedTauNameBoosted))
    delattr(process,'selectedPatTausBoosted')
    process.deepTau2017v2p1Boosted.taus = _noUpdatedTauNameBoosted
    process.patTauDiscriminationByElectronRejectionMVA62018RawBoosted.PATTauProducer = _noUpdatedTauNameBoosted
    process.patTauDiscriminationByElectronRejectionMVA62018Boosted.PATTauProducer = _noUpdatedTauNameBoosted
    process.rerunDiscriminationByIsolationOldDMMVArun2017v2rawBoosted.PATTauProducer = _noUpdatedTauNameBoosted
    process.rerunDiscriminationByIsolationOldDMMVArun2017v2Boosted.PATTauProducer = _noUpdatedTauNameBoosted
    process.selectedPatTausBoosted = getattr(process, _updatedTauNameBoosted).clone(
        src = _noUpdatedTauNameBoosted
    )
    process.newTauIDsTaskBoosted = cms.Task(
        process.rerunMvaIsolationTaskBoosted,
        process.selectedPatTausBoosted
    )
    process.miniAODTausTaskBoosted.add(process.newTauIDsTaskBoosted)
    print('New ID Boosted - Done ')

    # print('Slimming the various Tau Collections')
    print('Slimming the various Tau Collections')
    process.slimpath = cms.Path()
    from PhysicsTools.PatAlgos.slimming.slimmedTaus_cfi import slimmedTaus
    process.slimmedTausUnCleaned = slimmedTaus.clone(src = cms.InputTag('selectedPatTaus'))
    process.slimmedTausBoosted = slimmedTaus.clone(src = cms.InputTag('selectedPatTausBoosted'))
    process.slimmedTausElectronCleaned = slimmedTaus.clone(src = cms.InputTag('selectedPatTausElectronCleaned'), packedPFCandidates = cms.InputTag('PackedCandsElectronCleaned','packedPFCandidatesElectronCleaned'))
    process.slimmedTausMuonCleaned = slimmedTaus.clone(src = cms.InputTag('selectedPatTausMuonCleaned'), packedPFCandidates = cms.InputTag('PackedCandsMuonCleaned','packedPFCandidatesMuonCleaned'))
    process.slimmedTausLowPtElectronCleaned = slimmedTaus.clone(src = cms.InputTag('selectedPatTausLowPtElectronCleaned'), packedPFCandidates = cms.InputTag('PackedCandsLowPtElectronCleaned','packedPFCandidatesLowPtElectronCleaned'))
    process.slimpath *=process.slimmedTausUnCleaned
    process.slimpath *=process.slimmedTausBoosted
    process.slimpath  *=process.slimmedTausElectronCleaned
    process.slimpath  *=process.slimmedTausMuonCleaned
    process.slimpath  *=process.slimmedTausLowPtElectronCleaned
    process.schedule.append(process.slimpath)
    print('Slimming Done')

    print('Adding PU ID for jets')
    ## implementation based on: https://twiki.cern.ch/twiki/bin/viewauth/CMS/PileupJetID
    from RecoJets.JetProducers.PileupJetID_cfi import pileupJetId, _chsalgos_106X_UL17
    process.pileupJetIdUpdated = pileupJetId.clone( 
        jets=cms.InputTag("slimmedJets"),
        inputIsCorrected=True,
        applyJec=False,
        vertexes=cms.InputTag("offlineSlimmedPrimaryVertices"),
        algos = cms.VPSet(_chsalgos_106X_UL17),
    )

    process.load("PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cff")
    process.patJetCorrFactorsReapplyJEC = process.updatedPatJetCorrFactors.clone(
        src = cms.InputTag("slimmedJets"),
        levels = ['L1FastJet', 'L2Relative', 'L3Absolute']
    )
    process.updatedJets = process.updatedPatJets.clone(
        jetSource = cms.InputTag("slimmedJets"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsReapplyJEC"))
    )
    process.updatedJets.userData.userInts.src += ['pileupJetIdUpdated:fullId']
    process.updatedJets.userData.userFloats.src += ['pileupJetIdUpdated:fullDiscriminant']

    process.pileupjetidpath = cms.Path( process.pileupJetIdUpdated + process.patJetCorrFactorsReapplyJEC + process.updatedJets )

    process.schedule.append(process.pileupjetidpath)
    
def addFurtherSkimming(process):
    
    #########################
    ### Skim Path MiniAOD ###
    #########################
    process.main_path = cms.Path()
    
    ## First store summed weights before skimming
    process.lumiSummary = cms.EDAnalyzer("LumiAnalyzer",
                                         genEventInfo = cms.InputTag("generator")
    )
    
    #process.main_path *= process.lumiSummary
     

    ###############
    ### Trigger ###
    ###############
    process.HLT =cms.EDFilter("HLTHighLevel",
                              TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
                              HLTPaths = cms.vstring("HLT_PFJet450_v*", "HLT_PFJet500_v*","HLT_PFHT1050_v*", "HLT_PFHT500_PFMET100_PFMHT100_IDTight_v*", "HLT_IsoMu27_v*", "HLT_Mu50_v", "HLT_Ele35_WPTight_Gsf_v", "HLT_Ele32_WPTight_Gsf_L1DoubleEG_v", "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1_v", "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v", "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v", "HLT_DoubleEle33_CaloIdL_MW_v", "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v", "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v", "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v", "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v", "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg_v", "HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_MET90_v","HLT_Ele115_CaloIdVT_GsfTrkIdT_v*","HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v*","HLT_Photon200_v*"), #2017
                              #HLTPaths = cms.vstring("HLT_IsoMu24_v*"), #2018  
                              eventSetupPathsKey = cms.string(''),
                              andOr = cms.bool(True), #----- True = OR, False = AND between the HLTPaths
                              throw = cms.bool(False) # throw exception on unknown path names
                    )
    #process.main_path *= process.HLT

    process.schedule.append(process.main_path)

    
    ### this is not needed unless you want to save EDM format files
##     process.lumiSummary = cms.EDProducer("LumiSummaryProducer",
##                                          genEventInfo = cms.InputTag("generator"),
##                                          lheEventProduct = cms.InputTag("externalLHEProducer"),
##     )
##     process.lumiSummary_step = cms.Path(process.lumiSummary)
##     process.schedule.append(process.lumiSummary_step)
    
    
def addTCPNtuples(process):
    process.tcpNtuples = cms.EDAnalyzer("TCPNtuples",
                                        METCollection = cms.InputTag("slimmedMETs"),
                                        JetCollection = cms.InputTag("updatedJets"),
                                        MuonCollection = cms.InputTag("slimmedMuons"),
                                        ElectronCollection = cms.InputTag("slimmedElectrons"),
                                        LowPtElectronCollection = cms.InputTag("slimmedLowPtElectrons"),
                                        LowPtEIdScoreCut = cms.string("4"),
                                        VertexCollection = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                        rhoTag = cms.InputTag("fixedGridRhoFastjetAll"),
                                        effAreasConfigFile = cms.FileInPath("BoostedDiTau/MiniAODSkimmer/data/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt"),
                                        UnCleanedTauCollection = cms.InputTag('slimmedTausUnCleaned'),
                                        ECleanedTauCollection = cms.InputTag('slimmedTausElectronCleaned'),
                                        LowPtECleanedTauCollection = cms.InputTag('slimmedTausLowPtElectronCleaned'),
                                        MCleanedTauCollection = cms.InputTag('slimmedTausMuonCleaned'),
                                        BoostedTauCollection = cms.InputTag('slimmedTausBoosted'),
                                        PhotonCollection = cms.InputTag('slimmedPhotons'),
                                        
    )
    process.tcpNtupleMaker = cms.Path(process.tcpNtuples)

    process.tcpGenNtuples = cms.EDAnalyzer("GenAnalyzer",
                                        GenParticleCollection = cms.InputTag("prunedGenParticles"),
                                        GenJetCollection = cms.InputTag("slimmedGenJets"),
                                        genEventInfo = cms.InputTag("generator"),
                                        pileupSummaryInfo = cms.InputTag("slimmedAddPileupInfo"),
                                        puDataFileName = cms.FileInPath("BoostedDiTau/MiniAODSkimmer/data/PileupHistogram-goldenJSON-13tev-2017-69200ub-99bins.root"),
                                        puDataFileNameUp = cms.FileInPath("BoostedDiTau/MiniAODSkimmer/data/PileupHistogram-goldenJSON-13tev-2017-72400ub-99bins.root"),
                                        puDataFileNameDown = cms.FileInPath("BoostedDiTau/MiniAODSkimmer/data/PileupHistogram-goldenJSON-13tev-2017-66000ub-99bins.root"),
                                        puMCFileName = cms.FileInPath("BoostedDiTau/MiniAODSkimmer/data/PileupMC2017.root")
    )
    process.tcpGenNtupleMaker = cms.Path(process.tcpGenNtuples)

    process.tcpTrigNtuples = cms.EDAnalyzer("TCPTrigNtuples",
                                            TriggerResults = cms.InputTag("TriggerResults", "", "HLT")
    )
    process.tcpTrigNtupleMaker = cms.Path(process.tcpTrigNtuples)

    process.testTrigObj = cms.EDAnalyzer("TCPTrigObjectAnalyzer",
                                         bits = cms.InputTag("TriggerResults","","HLT"),
                                         prescales = cms.InputTag("patTrigger"),
                                         objects = cms.InputTag("slimmedPatTrigger"),   
    )

    process.testTrigObjMaker = cms.Path(process.testTrigObj)

    process.tcpPrefiring = cms.EDAnalyzer("TCPPrefiring",
                                          PrefiringWeight = cms.InputTag("prefiringweight:nonPrefiringProb"),
                                          PrefiringWeightUp = cms.InputTag("prefiringweight:nonPrefiringProbUp"),
                                          PrefiringWeightDown = cms.InputTag("prefiringweight:nonPrefiringProbDown")
    )

    process.tcpPrefiringMaker = cms.Path(process.tcpPrefiring)

    process.tcpMetfilter = cms.EDAnalyzer("TCPMETFilter",
                                          metFilters = cms.InputTag("TriggerResults","","PAT"),
                                          primaryVertexFilterSel = cms.string("Flag_goodVertices"),
                                          beamHaloFilterSel = cms.string("Flag_globalSuperTightHalo2016Filter"),
                                          hbheFilterSel = cms.string("Flag_HBHENoiseFilter"),
                                          hbheIsoFilterSel = cms.string("Flag_HBHENoiseIsoFilter"),
                                          ecalTPFilterSel = cms.string("Flag_EcalDeadCellTriggerPrimitiveFilter"),
                                          badPFMuonFilterSel = cms.string("Flag_BadPFMuonFilter"),
                                          badChargedCandFilterSel = cms.string("Flag_BadChargedCandidateFilter"),
                                          eeBadScFilterSel = cms.string("Flag_eeBadScFilter"),
                                          ecalBadCalFilterSel = cms.string("Flag_ecalBadCalibFilter")
    )

    process.tcpMetfilterMaker = cms.Path(process.tcpMetfilter)

    process.schedule.append(process.tcpMetfilterMaker)
    process.schedule.append(process.tcpTrigNtupleMaker)
    process.schedule.append(process.tcpGenNtupleMaker)
    process.schedule.append(process.tcpNtupleMaker)
    process.schedule.append(process.tcpPrefiringMaker)
    process.schedule.append(process.testTrigObjMaker)

    process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('TCPNtuple.root'),
                                   closeFileFast = cms.untracked.bool(True)
    )

def addMTTNtuples(process):
    process.fast_mtt_ntuples = cms.EDAnalyzer("fastMTTNtuples",
                                  METCollection = cms.InputTag("slimmedMETs"),
                                  JetCollection = cms.InputTag("slimmedJets"),
                                  MuonCollection = cms.InputTag("slimmedMuons"),
                                  VertexCollection = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                  MCleanedTauCollection = cms.InputTag('slimmedTausMuonCleaned'),
                                  BoostedTauCollection = cms.InputTag('slimmedTausBoosted')
                                              )
    process.mttNtupleMaker = cms.Path(process.fast_mtt_ntuples)

    process.schedule.append(process.mttNtupleMaker)

    process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('mttNtuple.root'),
                                   closeFileFast = cms.untracked.bool(True)
    )


### this is not needed unless you want to save EDM format files
def setOutputModule(mode=0):
    #mode = 0: store original MiniAOD and new selectedPatTaus 
    #mode = 1: store original MiniAOD, new selectedPatTaus, and all PFTau products as in AOD (except of unsuported ones), plus a few additional collections (charged hadrons, pi zeros, combinatoric reco taus)
    
    import Configuration.EventContent.EventContent_cff as evtContent
    output = cms.OutputModule(
        'PoolOutputModule',
        fileName=cms.untracked.string('miniAOD_TauReco.root'),
        fastCloning=cms.untracked.bool(False),
        dataset=cms.untracked.PSet(
            dataTier=cms.untracked.string('MINIAODSIM'),
            filterName=cms.untracked.string('')
        ),
        outputCommands = evtContent.MINIAODSIMEventContent.outputCommands,
        SelectEvents=cms.untracked.PSet(
            SelectEvents=cms.vstring('main_path_et','main_path_mt')
        )
    )
    #output.outputCommands.append('keep *_selectedPatTaus_*_*')
    if mode==1:
        for prod in evtContent.RecoTauTagAOD.outputCommands:
            if prod.find('ElectronRejection') > -1:
                continue
            if prod.find('MuonRejection') > -1:
                    continue
                    output.outputCommands.append(prod)
        output.outputCommands.append('keep *_hpsPFTauDiscriminationByLooseMuonRejectionSimple_*_*')
        output.outputCommands.append('keep *_hpsPFTauDiscriminationByTightMuonRejectionSimple_*_*')
        output.outputCommands.append('keep *_combinatoricReco*_*_*')
        output.outputCommands.append('keep *_ak4PFJetsRecoTauChargedHadrons_*_*')
        output.outputCommands.append('keep *_ak4PFJetsLegacyHPSPiZeros_*_*')
        output.outputCommands.append('keep *_patJetsPAT_*_*')

    if mode==2:
        output = cms.OutputModule('PoolOutputModule',
                                  fileName=cms.untracked.string('miniAOD_TauReco.root'),
                                  fastCloning=cms.untracked.bool(False),
                                  dataset=cms.untracked.PSet(
                                      dataTier=cms.untracked.string('MINIAODSIM'),
                                      filterName=cms.untracked.string('')
                                  ),
                                  outputCommands = evtContent.MINIAODSIMEventContent.outputCommands
        )
    return output

#####
