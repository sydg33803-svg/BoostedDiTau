import FWCore.ParameterSet.Config as cms

process = cms.Process("TAURECO")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('root://eoshome-y.cern.ch//eos/user/y/yohay/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8-MINIAODSIM-106X_mcRun2_asymptotic_preVFP_v11-v2-230000-10CA3EDE-F47E-044F-9F6E-DBAA69C46BFD.root'),
    secondaryFileNames = cms.untracked.vstring()
)
process.CondDB = cms.PSet(
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    connect = cms.string('')
)

process.CondDBTauConnection = cms.PSet(
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS')
)

process.HFRecalParameterBlock = cms.PSet(
    HFdepthOneParameterA = cms.vdouble(
        0.004123, 0.00602, 0.008201, 0.010489, 0.013379,
        0.016997, 0.021464, 0.027371, 0.034195, 0.044807,
        0.058939, 0.125497
    ),
    HFdepthOneParameterB = cms.vdouble(
        -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05,
        2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107,
        0.000425, 0.000209
    ),
    HFdepthTwoParameterA = cms.vdouble(
        0.002861, 0.004168, 0.0064, 0.008388, 0.011601,
        0.014425, 0.018633, 0.023232, 0.028274, 0.035447,
        0.051579, 0.086593
    ),
    HFdepthTwoParameterB = cms.vdouble(
        -2e-06, -0.0, -7e-06, -6e-06, -2e-06,
        1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05,
        0.000157, -3e-06
    )
)

process.PFRecoTauPFJetInputs = cms.PSet(
    inputJetCollection = cms.InputTag("patJetsPAT"),
    isolationConeSize = cms.double(0.5),
    jetConeSize = cms.double(0.5),
    maxJetAbsEta = cms.double(2.5),
    minJetPt = cms.double(14.0)
)

process.PFTauQualityCuts = cms.PSet(
    isolationQualityCuts = cms.PSet(
        maxDeltaZ = cms.double(0.2),
        maxDeltaZToLeadTrack = cms.double(-1.0),
        maxTrackChi2 = cms.double(100.0),
        maxTransverseImpactParameter = cms.double(0.03),
        minGammaEt = cms.double(1.5),
        minTrackHits = cms.uint32(8),
        minTrackPixelHits = cms.uint32(0),
        minTrackPt = cms.double(1.0),
        minTrackVertexWeight = cms.double(-1.0)
    ),
    leadingTrkOrPFCandOption = cms.string('leadPFCand'),
    primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
    pvFindingAlgo = cms.string('closestInDeltaZ'),
    recoverLeadingTrk = cms.bool(False),
    signalQualityCuts = cms.PSet(
        maxDeltaZ = cms.double(0.4),
        maxDeltaZToLeadTrack = cms.double(-1.0),
        maxTrackChi2 = cms.double(100.0),
        maxTransverseImpactParameter = cms.double(0.1),
        minGammaEt = cms.double(1.0),
        minNeutralHadronEt = cms.double(30.0),
        minTrackHits = cms.uint32(3),
        minTrackPixelHits = cms.uint32(0),
        minTrackPt = cms.double(0.5),
        minTrackVertexWeight = cms.double(-1.0)
    ),
    vertexTrackFiltering = cms.bool(False),
    vxAssocQualityCuts = cms.PSet(
        maxTrackChi2 = cms.double(100.0),
        maxTransverseImpactParameter = cms.double(0.1),
        minGammaEt = cms.double(1.0),
        minTrackHits = cms.uint32(3),
        minTrackPixelHits = cms.uint32(0),
        minTrackPt = cms.double(0.5),
        minTrackVertexWeight = cms.double(-1.0)
    )
)

process.decayMode_1Prong0Pi0 = cms.PSet(
    applyBendCorrection = cms.PSet(
        eta = cms.bool(True),
        mass = cms.bool(True),
        phi = cms.bool(True)
    ),
    assumeStripMass = cms.double(-1.0),
    maxMass = cms.string('1.'),
    maxPi0Mass = cms.double(1000000000.0),
    minMass = cms.double(-1000.0),
    minPi0Mass = cms.double(-1000.0),
    nCharged = cms.uint32(1),
    nChargedPFCandsMin = cms.uint32(1),
    nPiZeros = cms.uint32(0),
    nTracksMin = cms.uint32(1)
)

process.decayMode_1Prong1Pi0 = cms.PSet(
    applyBendCorrection = cms.PSet(
        eta = cms.bool(True),
        mass = cms.bool(True),
        phi = cms.bool(True)
    ),
    assumeStripMass = cms.double(0.1349),
    maxMass = cms.string('max(1.3, min(1.3*sqrt(pt/100.), 4.2))'),
    maxPi0Mass = cms.double(1000000000.0),
    minMass = cms.double(0.3),
    minPi0Mass = cms.double(-1000.0),
    nCharged = cms.uint32(1),
    nChargedPFCandsMin = cms.uint32(1),
    nPiZeros = cms.uint32(1),
    nTracksMin = cms.uint32(1)
)

process.decayMode_1Prong2Pi0 = cms.PSet(
    applyBendCorrection = cms.PSet(
        eta = cms.bool(True),
        mass = cms.bool(True),
        phi = cms.bool(True)
    ),
    assumeStripMass = cms.double(0.0),
    maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
    maxPi0Mass = cms.double(0.2),
    minMass = cms.double(0.4),
    minPi0Mass = cms.double(0.05),
    nCharged = cms.uint32(1),
    nChargedPFCandsMin = cms.uint32(1),
    nPiZeros = cms.uint32(2),
    nTracksMin = cms.uint32(1)
)

process.decayMode_2Prong0Pi0 = cms.PSet(
    applyBendCorrection = cms.PSet(
        eta = cms.bool(False),
        mass = cms.bool(False),
        phi = cms.bool(False)
    ),
    assumeStripMass = cms.double(-1.0),
    maxMass = cms.string('1.2'),
    maxPi0Mass = cms.double(1000000000.0),
    minMass = cms.double(0.0),
    minPi0Mass = cms.double(-1000.0),
    nCharged = cms.uint32(2),
    nChargedPFCandsMin = cms.uint32(1),
    nPiZeros = cms.uint32(0),
    nTracksMin = cms.uint32(2)
)

process.decayMode_2Prong1Pi0 = cms.PSet(
    applyBendCorrection = cms.PSet(
        eta = cms.bool(False),
        mass = cms.bool(False),
        phi = cms.bool(False)
    ),
    assumeStripMass = cms.double(-1.0),
    maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
    maxPi0Mass = cms.double(1000000000.0),
    minMass = cms.double(0.0),
    minPi0Mass = cms.double(-1000.0),
    nCharged = cms.uint32(2),
    nChargedPFCandsMin = cms.uint32(1),
    nPiZeros = cms.uint32(1),
    nTracksMin = cms.uint32(2)
)

process.decayMode_3Prong0Pi0 = cms.PSet(
    applyBendCorrection = cms.PSet(
        eta = cms.bool(False),
        mass = cms.bool(False),
        phi = cms.bool(False)
    ),
    assumeStripMass = cms.double(-1.0),
    maxMass = cms.string('1.5'),
    maxPi0Mass = cms.double(1000000000.0),
    minMass = cms.double(0.8),
    minPi0Mass = cms.double(-1000.0),
    nCharged = cms.uint32(3),
    nChargedPFCandsMin = cms.uint32(1),
    nPiZeros = cms.uint32(0),
    nTracksMin = cms.uint32(2)
)

process.decayMode_3Prong1Pi0 = cms.PSet(
    applyBendCorrection = cms.PSet(
        eta = cms.bool(False),
        mass = cms.bool(False),
        phi = cms.bool(False)
    ),
    assumeStripMass = cms.double(-1.0),
    maxMass = cms.string('1.6'),
    maxPi0Mass = cms.double(1000000000.0),
    minMass = cms.double(0.9),
    minPi0Mass = cms.double(-1000.0),
    nCharged = cms.uint32(3),
    nChargedPFCandsMin = cms.uint32(1),
    nPiZeros = cms.uint32(1),
    nTracksMin = cms.uint32(2)
)

process.leadTrackFinding = cms.PSet(
    Producer = cms.InputTag("pfRecoTauDiscriminationByLeadingTrackFinding"),
    cut = cms.double(0.5)
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

process.maxLuminosityBlocks = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.noPrediscriminants = cms.PSet(
    BooleanOperator = cms.string('and')
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(True)
)

process.pset = cms.PSet(
    IDname = cms.string('ByTightCombinedIsolationDBSumPtCorr3HitsdR03'),
    maximumAbsoluteValues = cms.vdouble(0.8, 1000000000.0),
    maximumRelativeValues = cms.vdouble(-1.0, 0.1),
    referenceRawIDNames = cms.vstring(
        'ByRawCombinedIsolationDBSumPtCorr3HitsdR03',
        'PhotonPtSumOutsideSignalConedR03'
    )
)

process.requireDecayMode = cms.PSet(
    BooleanOperator = cms.string('and'),
    decayMode = cms.PSet(
        Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
        cut = cms.double(0.5)
    )
)

process.requireLeadPion = cms.PSet(
    BooleanOperator = cms.string('and'),
    leadPion = cms.PSet(
        Producer = cms.InputTag("pfRecoTauDiscriminationByLeadingTrackFinding"),
        cut = cms.double(0.5)
    )
)

process.requireLeadTrack = cms.PSet(
    BooleanOperator = cms.string('and'),
    leadTrack = cms.PSet(
        Producer = cms.InputTag("pfRecoTauDiscriminationByLeadingTrackFinding"),
        cut = cms.double(0.5)
    )
)

process.tautagInfoModifer = cms.PSet(
    name = cms.string('TTIworkaround'),
    pfTauTagInfoSrc = cms.InputTag("pfRecoTauTagInfoProducer"),
    plugin = cms.string('RecoTauTagInfoWorkaroundModifer')
)

process.PFTauPrimaryVertexProducer = cms.EDProducer("PFTauPrimaryVertexProducer",
    Algorithm = cms.int32(0),
    ElectronTag = cms.InputTag("MyElectrons"),
    MuonTag = cms.InputTag("MyMuons"),
    PFTauTag = cms.InputTag("hpsPFTauProducer"),
    PVTag = cms.InputTag("offlinePrimaryVertices"),
    RemoveElectronTracks = cms.bool(False),
    RemoveMuonTracks = cms.bool(False),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    cut = cms.string('pt > 18.0 & abs(eta)<2.3'),
    discriminators = cms.VPSet(cms.PSet(
        discriminator = cms.InputTag("hpsPFTauDiscriminationByDecayModeFinding"),
        selectionCut = cms.double(0.5)
    )),
    mightGet = cms.optional.untracked.vstring,
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(1.5),
            minTrackHits = cms.uint32(8),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(1.0),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    useBeamSpot = cms.bool(True),
    useSelectedTaus = cms.bool(False)
)


process.PFTauSecondaryVertexProducer = cms.EDProducer("PFTauSecondaryVertexProducer",
    PFTauTag = cms.InputTag("hpsPFTauProducer")
)


process.PFTauTransverseImpactParameters = cms.EDProducer("PFTauTransverseImpactParameters",
    PFTauPVATag = cms.InputTag("PFTauPrimaryVertexProducer"),
    PFTauSVATag = cms.InputTag("PFTauSecondaryVertexProducer"),
    PFTauTag = cms.InputTag("hpsPFTauProducer"),
    useFullCalculation = cms.bool(False)
)


process.PackedCandsElectronCleaned = cms.EDProducer("ElectronCleanedPackedCandidateProducer",
    electronSrc = cms.InputTag("LooseFilter","LooseElectronRef"),
    packedCandSrc = cms.InputTag("packedPFCandidates")
)


process.PackedCandsLowPtElectronCleaned = cms.EDProducer("LowPtElectronCleanedPackedCandidateProducer",
    electronSrc = cms.InputTag("LowPtFilter","LowPtElectronRef"),
    packedCandSrc = cms.InputTag("packedPFCandidates")
)


process.PackedCandsMuonCleaned = cms.EDProducer("MuonCleanedPackedCandidateProducer",
    muonSrc = cms.InputTag("LooseMuonFilter"),
    packedCandSrc = cms.InputTag("packedPFCandidates")
)


process.RecoTauCleaner = cms.EDProducer("RecoTauCleaner",
    cleaners = cms.VPSet(
        cms.PSet(
            name = cms.string('Charge'),
            nprongs = cms.vuint32(1, 3),
            passForCharge = cms.int32(1),
            plugin = cms.string('RecoTauChargeCleanerPlugin'),
            selectionFailValue = cms.double(0),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            name = cms.string('HPS_Select'),
            plugin = cms.string('RecoTauDiscriminantCleanerPlugin'),
            src = cms.InputTag("hpsSelectionDiscriminator"),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            minTrackPt = cms.double(5.0),
            name = cms.string('killSoftTwoProngTaus'),
            plugin = cms.string('RecoTauSoftTwoProngTausCleanerPlugin'),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            name = cms.string('ChargedHadronMultiplicity'),
            plugin = cms.string('RecoTauChargedHadronMultiplicityCleanerPlugin'),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            name = cms.string('Pt'),
            plugin = cms.string('RecoTauStringCleanerPlugin'),
            selection = cms.string('leadCand().isNonnull()'),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('-pt()'),
            tolerance = cms.double(0.01)
        ),
        cms.PSet(
            name = cms.string('StripMultiplicity'),
            plugin = cms.string('RecoTauStringCleanerPlugin'),
            selection = cms.string('leadCand().isNonnull()'),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('-signalPiZeroCandidates().size()'),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            name = cms.string('CombinedIsolation'),
            plugin = cms.string('RecoTauStringCleanerPlugin'),
            selection = cms.string('leadCand().isNonnull()'),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('isolationPFChargedHadrCandsPtSum() + isolationPFGammaCandsEtSum()'),
            tolerance = cms.double(0)
        )
    ),
    outputSelection = cms.string(''),
    src = cms.InputTag("combinatoricRecoTaus"),
    verbosity = cms.int32(0)
)


process.RecoTauJetRegionProducer = cms.EDProducer("RecoTauJetRegionProducer",
    deltaR = cms.double(0.8),
    maxJetAbsEta = cms.double(2.5),
    minJetPt = cms.double(14.0),
    pfCandAssocMapSrc = cms.InputTag(""),
    pfCandSrc = cms.InputTag("particleFlow"),
    src = cms.InputTag("patJetsPAT"),
    verbosity = cms.int32(0)
)


process.RecoTauPiZeroUnembedder = cms.EDProducer("RecoTauPiZeroUnembedder",
    src = cms.InputTag("hpsPFTauProducerSansRefs")
)


process.ak4JetTracksAssociatorAtVertexPF = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.4),
    jets = cms.InputTag("ak4PFJetsCHS"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("generalTracks"),
    useAssigned = cms.bool(False)
)


process.ak4PFJetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.4),
    jets = cms.InputTag("patJetsPAT"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("generalTracks"),
    useAssigned = cms.bool(False)
)


process.ak4PFJetTracksAssociatorAtVertexBoosted = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.4),
    jets = cms.InputTag("ak4PFJets"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("generalTracks"),
    useAssigned = cms.bool(False)
)


process.ak4PFJetTracksAssociatorAtVertexElectronCleaned = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.4),
    jets = cms.InputTag("ak4PFJets"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("generalTracks"),
    useAssigned = cms.bool(False)
)


process.ak4PFJetTracksAssociatorAtVertexLowPtElectronCleaned = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.4),
    jets = cms.InputTag("ak4PFJets"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("generalTracks"),
    useAssigned = cms.bool(False)
)


process.ak4PFJetTracksAssociatorAtVertexMuonCleaned = cms.EDProducer("JetTracksAssociatorAtVertex",
    coneSize = cms.double(0.4),
    jets = cms.InputTag("ak4PFJets"),
    pvSrc = cms.InputTag("offlinePrimaryVertices"),
    tracks = cms.InputTag("generalTracks"),
    useAssigned = cms.bool(False)
)


process.ak4PFJetsLegacyHPSPiZeros = cms.EDProducer("RecoTauPiZeroProducer",
    builders = cms.VPSet(cms.PSet(
        applyElecTrackQcuts = cms.bool(False),
        makeCombinatoricStrips = cms.bool(False),
        maxStripBuildIterations = cms.int32(-1),
        minGammaEtStripAdd = cms.double(1.0),
        minGammaEtStripSeed = cms.double(1.0),
        minStripEt = cms.double(1.0),
        name = cms.string('s'),
        plugin = cms.string('RecoTauPiZeroStripPlugin3'),
        qualityCuts = cms.PSet(
            isolationQualityCuts = cms.PSet(
                maxDeltaZ = cms.double(0.2),
                maxDeltaZToLeadTrack = cms.double(-1.0),
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.03),
                minGammaEt = cms.double(1.5),
                minTrackHits = cms.uint32(8),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(1.0),
                minTrackVertexWeight = cms.double(-1.0)
            ),
            leadingTrkOrPFCandOption = cms.string('leadPFCand'),
            primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
            pvFindingAlgo = cms.string('closestInDeltaZ'),
            recoverLeadingTrk = cms.bool(False),
            signalQualityCuts = cms.PSet(
                maxDeltaZ = cms.double(0.4),
                maxDeltaZToLeadTrack = cms.double(-1.0),
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.1),
                minGammaEt = cms.double(1.0),
                minNeutralHadronEt = cms.double(30.0),
                minTrackHits = cms.uint32(3),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(0.5),
                minTrackVertexWeight = cms.double(-1.0)
            ),
            vertexTrackFiltering = cms.bool(False),
            vxAssocQualityCuts = cms.PSet(
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.1),
                minGammaEt = cms.double(1.0),
                minTrackHits = cms.uint32(3),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(0.5),
                minTrackVertexWeight = cms.double(-1.0)
            )
        ),
        stripCandidatesParticleIds = cms.vint32(2, 4),
        stripEtaAssociationDistance = cms.double(0.05),
        stripEtaAssociationDistanceFunc = cms.PSet(
            function = cms.string('TMath::Min(0.15, TMath::Max(0.05, [0]*TMath::Power(pT, -[1])))'),
            par0 = cms.double(0.197077),
            par1 = cms.double(0.658701)
        ),
        stripPhiAssociationDistance = cms.double(0.2),
        stripPhiAssociationDistanceFunc = cms.PSet(
            function = cms.string('TMath::Min(0.3, TMath::Max(0.05, [0]*TMath::Power(pT, -[1])))'),
            par0 = cms.double(0.352476),
            par1 = cms.double(0.707716)
        ),
        updateStripAfterEachDaughter = cms.bool(False),
        verbosity = cms.int32(0)
    )),
    jetSrc = cms.InputTag("patJetsPAT"),
    massHypothesis = cms.double(0.136),
    maxJetAbsEta = cms.double(2.5),
    mightGet = cms.optional.untracked.vstring,
    minJetPt = cms.double(5),
    outputSelection = cms.string('pt > 0'),
    ranking = cms.VPSet(cms.PSet(
        name = cms.string('InStrip'),
        plugin = cms.string('RecoTauPiZeroStringQuality'),
        selection = cms.string('algoIs("kStrips")'),
        selectionFailValue = cms.double(1000),
        selectionPassFunction = cms.string('abs(mass() - 0.13579)')
    )),
    verbosity = cms.int32(0)
)


process.ak4PFJetsLegacyHPSPiZerosBoosted = cms.EDProducer("RecoTauPiZeroProducer",
    builders = cms.VPSet(cms.PSet(
        applyElecTrackQcuts = cms.bool(False),
        makeCombinatoricStrips = cms.bool(False),
        maxStripBuildIterations = cms.int32(-1),
        minGammaEtStripAdd = cms.double(1.0),
        minGammaEtStripSeed = cms.double(1.0),
        minStripEt = cms.double(1.0),
        name = cms.string('s'),
        plugin = cms.string('RecoTauPiZeroStripPlugin3'),
        qualityCuts = cms.PSet(
            isolationQualityCuts = cms.PSet(
                maxDeltaZ = cms.double(0.2),
                maxDeltaZToLeadTrack = cms.double(-1.0),
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.03),
                minGammaEt = cms.double(1.5),
                minTrackHits = cms.uint32(8),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(1.0),
                minTrackVertexWeight = cms.double(-1.0)
            ),
            leadingTrkOrPFCandOption = cms.string('leadPFCand'),
            primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
            pvFindingAlgo = cms.string('closestInDeltaZ'),
            recoverLeadingTrk = cms.bool(False),
            signalQualityCuts = cms.PSet(
                maxDeltaZ = cms.double(0.4),
                maxDeltaZToLeadTrack = cms.double(-1.0),
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.1),
                minGammaEt = cms.double(1.0),
                minNeutralHadronEt = cms.double(30.0),
                minTrackHits = cms.uint32(3),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(0.5),
                minTrackVertexWeight = cms.double(-1.0)
            ),
            vertexTrackFiltering = cms.bool(False),
            vxAssocQualityCuts = cms.PSet(
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.1),
                minGammaEt = cms.double(1.0),
                minTrackHits = cms.uint32(3),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(0.5),
                minTrackVertexWeight = cms.double(-1.0)
            )
        ),
        stripCandidatesParticleIds = cms.vint32(2, 4),
        stripEtaAssociationDistance = cms.double(0.05),
        stripEtaAssociationDistanceFunc = cms.PSet(
            function = cms.string('TMath::Min(0.15, TMath::Max(0.05, [0]*TMath::Power(pT, -[1])))'),
            par0 = cms.double(0.197077),
            par1 = cms.double(0.658701)
        ),
        stripPhiAssociationDistance = cms.double(0.2),
        stripPhiAssociationDistanceFunc = cms.PSet(
            function = cms.string('TMath::Min(0.3, TMath::Max(0.05, [0]*TMath::Power(pT, -[1])))'),
            par0 = cms.double(0.352476),
            par1 = cms.double(0.707716)
        ),
        updateStripAfterEachDaughter = cms.bool(False),
        verbosity = cms.int32(0)
    )),
    jetSrc = cms.InputTag("boostedTauSeedsPAT"),
    massHypothesis = cms.double(0.136),
    maxJetAbsEta = cms.double(2.5),
    mightGet = cms.optional.untracked.vstring,
    minJetPt = cms.double(5),
    outputSelection = cms.string('pt > 0'),
    ranking = cms.VPSet(cms.PSet(
        name = cms.string('InStrip'),
        plugin = cms.string('RecoTauPiZeroStringQuality'),
        selection = cms.string('algoIs("kStrips")'),
        selectionFailValue = cms.double(1000),
        selectionPassFunction = cms.string('abs(mass() - 0.13579)')
    )),
    verbosity = cms.int32(0)
)


process.ak4PFJetsLegacyHPSPiZerosElectronCleaned = cms.EDProducer("RecoTauPiZeroProducer",
    builders = cms.VPSet(cms.PSet(
        applyElecTrackQcuts = cms.bool(False),
        makeCombinatoricStrips = cms.bool(False),
        maxStripBuildIterations = cms.int32(-1),
        minGammaEtStripAdd = cms.double(1.0),
        minGammaEtStripSeed = cms.double(1.0),
        minStripEt = cms.double(1.0),
        name = cms.string('s'),
        plugin = cms.string('RecoTauPiZeroStripPlugin3'),
        qualityCuts = cms.PSet(
            isolationQualityCuts = cms.PSet(
                maxDeltaZ = cms.double(0.2),
                maxDeltaZToLeadTrack = cms.double(-1.0),
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.03),
                minGammaEt = cms.double(1.5),
                minTrackHits = cms.uint32(8),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(1.0),
                minTrackVertexWeight = cms.double(-1.0)
            ),
            leadingTrkOrPFCandOption = cms.string('leadPFCand'),
            primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
            pvFindingAlgo = cms.string('closestInDeltaZ'),
            recoverLeadingTrk = cms.bool(False),
            signalQualityCuts = cms.PSet(
                maxDeltaZ = cms.double(0.4),
                maxDeltaZToLeadTrack = cms.double(-1.0),
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.1),
                minGammaEt = cms.double(1.0),
                minNeutralHadronEt = cms.double(30.0),
                minTrackHits = cms.uint32(3),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(0.5),
                minTrackVertexWeight = cms.double(-1.0)
            ),
            vertexTrackFiltering = cms.bool(False),
            vxAssocQualityCuts = cms.PSet(
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.1),
                minGammaEt = cms.double(1.0),
                minTrackHits = cms.uint32(3),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(0.5),
                minTrackVertexWeight = cms.double(-1.0)
            )
        ),
        stripCandidatesParticleIds = cms.vint32(2, 4),
        stripEtaAssociationDistance = cms.double(0.05),
        stripEtaAssociationDistanceFunc = cms.PSet(
            function = cms.string('TMath::Min(0.15, TMath::Max(0.05, [0]*TMath::Power(pT, -[1])))'),
            par0 = cms.double(0.197077),
            par1 = cms.double(0.658701)
        ),
        stripPhiAssociationDistance = cms.double(0.2),
        stripPhiAssociationDistanceFunc = cms.PSet(
            function = cms.string('TMath::Min(0.3, TMath::Max(0.05, [0]*TMath::Power(pT, -[1])))'),
            par0 = cms.double(0.352476),
            par1 = cms.double(0.707716)
        ),
        updateStripAfterEachDaughter = cms.bool(False),
        verbosity = cms.int32(0)
    )),
    jetSrc = cms.InputTag("patJetsPATElectronCleaned"),
    massHypothesis = cms.double(0.136),
    maxJetAbsEta = cms.double(2.5),
    mightGet = cms.optional.untracked.vstring,
    minJetPt = cms.double(5),
    outputSelection = cms.string('pt > 0'),
    ranking = cms.VPSet(cms.PSet(
        name = cms.string('InStrip'),
        plugin = cms.string('RecoTauPiZeroStringQuality'),
        selection = cms.string('algoIs("kStrips")'),
        selectionFailValue = cms.double(1000),
        selectionPassFunction = cms.string('abs(mass() - 0.13579)')
    )),
    verbosity = cms.int32(0)
)


process.ak4PFJetsLegacyHPSPiZerosLowPtElectronCleaned = cms.EDProducer("RecoTauPiZeroProducer",
    builders = cms.VPSet(cms.PSet(
        applyElecTrackQcuts = cms.bool(False),
        makeCombinatoricStrips = cms.bool(False),
        maxStripBuildIterations = cms.int32(-1),
        minGammaEtStripAdd = cms.double(1.0),
        minGammaEtStripSeed = cms.double(1.0),
        minStripEt = cms.double(1.0),
        name = cms.string('s'),
        plugin = cms.string('RecoTauPiZeroStripPlugin3'),
        qualityCuts = cms.PSet(
            isolationQualityCuts = cms.PSet(
                maxDeltaZ = cms.double(0.2),
                maxDeltaZToLeadTrack = cms.double(-1.0),
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.03),
                minGammaEt = cms.double(1.5),
                minTrackHits = cms.uint32(8),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(1.0),
                minTrackVertexWeight = cms.double(-1.0)
            ),
            leadingTrkOrPFCandOption = cms.string('leadPFCand'),
            primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
            pvFindingAlgo = cms.string('closestInDeltaZ'),
            recoverLeadingTrk = cms.bool(False),
            signalQualityCuts = cms.PSet(
                maxDeltaZ = cms.double(0.4),
                maxDeltaZToLeadTrack = cms.double(-1.0),
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.1),
                minGammaEt = cms.double(1.0),
                minNeutralHadronEt = cms.double(30.0),
                minTrackHits = cms.uint32(3),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(0.5),
                minTrackVertexWeight = cms.double(-1.0)
            ),
            vertexTrackFiltering = cms.bool(False),
            vxAssocQualityCuts = cms.PSet(
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.1),
                minGammaEt = cms.double(1.0),
                minTrackHits = cms.uint32(3),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(0.5),
                minTrackVertexWeight = cms.double(-1.0)
            )
        ),
        stripCandidatesParticleIds = cms.vint32(2, 4),
        stripEtaAssociationDistance = cms.double(0.05),
        stripEtaAssociationDistanceFunc = cms.PSet(
            function = cms.string('TMath::Min(0.15, TMath::Max(0.05, [0]*TMath::Power(pT, -[1])))'),
            par0 = cms.double(0.197077),
            par1 = cms.double(0.658701)
        ),
        stripPhiAssociationDistance = cms.double(0.2),
        stripPhiAssociationDistanceFunc = cms.PSet(
            function = cms.string('TMath::Min(0.3, TMath::Max(0.05, [0]*TMath::Power(pT, -[1])))'),
            par0 = cms.double(0.352476),
            par1 = cms.double(0.707716)
        ),
        updateStripAfterEachDaughter = cms.bool(False),
        verbosity = cms.int32(0)
    )),
    jetSrc = cms.InputTag("patJetsPATLowPtElectronCleaned"),
    massHypothesis = cms.double(0.136),
    maxJetAbsEta = cms.double(2.5),
    mightGet = cms.optional.untracked.vstring,
    minJetPt = cms.double(14.0),
    outputSelection = cms.string('pt > 0'),
    ranking = cms.VPSet(cms.PSet(
        name = cms.string('InStrip'),
        plugin = cms.string('RecoTauPiZeroStringQuality'),
        selection = cms.string('algoIs("kStrips")'),
        selectionFailValue = cms.double(1000),
        selectionPassFunction = cms.string('abs(mass() - 0.13579)')
    )),
    verbosity = cms.int32(0)
)


process.ak4PFJetsLegacyHPSPiZerosMuonCleaned = cms.EDProducer("RecoTauPiZeroProducer",
    builders = cms.VPSet(cms.PSet(
        applyElecTrackQcuts = cms.bool(False),
        makeCombinatoricStrips = cms.bool(False),
        maxStripBuildIterations = cms.int32(-1),
        minGammaEtStripAdd = cms.double(1.0),
        minGammaEtStripSeed = cms.double(1.0),
        minStripEt = cms.double(1.0),
        name = cms.string('s'),
        plugin = cms.string('RecoTauPiZeroStripPlugin3'),
        qualityCuts = cms.PSet(
            isolationQualityCuts = cms.PSet(
                maxDeltaZ = cms.double(0.2),
                maxDeltaZToLeadTrack = cms.double(-1.0),
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.03),
                minGammaEt = cms.double(1.5),
                minTrackHits = cms.uint32(8),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(1.0),
                minTrackVertexWeight = cms.double(-1.0)
            ),
            leadingTrkOrPFCandOption = cms.string('leadPFCand'),
            primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
            pvFindingAlgo = cms.string('closestInDeltaZ'),
            recoverLeadingTrk = cms.bool(False),
            signalQualityCuts = cms.PSet(
                maxDeltaZ = cms.double(0.4),
                maxDeltaZToLeadTrack = cms.double(-1.0),
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.1),
                minGammaEt = cms.double(1.0),
                minNeutralHadronEt = cms.double(30.0),
                minTrackHits = cms.uint32(3),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(0.5),
                minTrackVertexWeight = cms.double(-1.0)
            ),
            vertexTrackFiltering = cms.bool(False),
            vxAssocQualityCuts = cms.PSet(
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.1),
                minGammaEt = cms.double(1.0),
                minTrackHits = cms.uint32(3),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(0.5),
                minTrackVertexWeight = cms.double(-1.0)
            )
        ),
        stripCandidatesParticleIds = cms.vint32(2, 4),
        stripEtaAssociationDistance = cms.double(0.05),
        stripEtaAssociationDistanceFunc = cms.PSet(
            function = cms.string('TMath::Min(0.15, TMath::Max(0.05, [0]*TMath::Power(pT, -[1])))'),
            par0 = cms.double(0.197077),
            par1 = cms.double(0.658701)
        ),
        stripPhiAssociationDistance = cms.double(0.2),
        stripPhiAssociationDistanceFunc = cms.PSet(
            function = cms.string('TMath::Min(0.3, TMath::Max(0.05, [0]*TMath::Power(pT, -[1])))'),
            par0 = cms.double(0.352476),
            par1 = cms.double(0.707716)
        ),
        updateStripAfterEachDaughter = cms.bool(False),
        verbosity = cms.int32(0)
    )),
    jetSrc = cms.InputTag("patJetsPATMuonCleaned"),
    massHypothesis = cms.double(0.136),
    maxJetAbsEta = cms.double(2.5),
    mightGet = cms.optional.untracked.vstring,
    minJetPt = cms.double(5),
    outputSelection = cms.string('pt > 0'),
    ranking = cms.VPSet(cms.PSet(
        name = cms.string('InStrip'),
        plugin = cms.string('RecoTauPiZeroStringQuality'),
        selection = cms.string('algoIs("kStrips")'),
        selectionFailValue = cms.double(1000),
        selectionPassFunction = cms.string('abs(mass() - 0.13579)')
    )),
    verbosity = cms.int32(0)
)


process.ak4PFJetsPAT = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    applyWeight = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(5.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("packedPFCandidates"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak4PFJetsPATElectronCleaned = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    applyWeight = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(5.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("PackedCandsElectronCleaned","packedPFCandidatesElectronCleaned"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak4PFJetsPATLowPtElectronCleaned = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    applyWeight = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(5.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("PackedCandsLowPtElectronCleaned","packedPFCandidatesLowPtElectronCleaned"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak4PFJetsPATMuonCleaned = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    applyWeight = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(5.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.4),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("PackedCandsMuonCleaned","packedPFCandidatesMuonCleaned"),
    srcPVs = cms.InputTag(""),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak4PFJetsRecoTauChargedHadrons = cms.EDProducer("PFRecoTauChargedHadronProducer",
    builders = cms.VPSet(
        cms.PSet(
            chargedHadronCandidatesParticleIds = cms.vint32(1, 2, 3),
            dRmergeNeutralHadronWrtChargedHadron = cms.double(0.005),
            dRmergeNeutralHadronWrtElectron = cms.double(0.05),
            dRmergeNeutralHadronWrtNeutralHadron = cms.double(0.01),
            dRmergeNeutralHadronWrtOther = cms.double(0.005),
            dRmergePhotonWrtChargedHadron = cms.double(0.005),
            dRmergePhotonWrtElectron = cms.double(0.005),
            dRmergePhotonWrtNeutralHadron = cms.double(0.01),
            dRmergePhotonWrtOther = cms.double(0.005),
            maxUnmatchedBlockElementsNeutralHadron = cms.int32(1),
            maxUnmatchedBlockElementsPhoton = cms.int32(1),
            minBlockElementMatchesNeutralHadron = cms.int32(2),
            minBlockElementMatchesPhoton = cms.int32(2),
            minMergeChargedHadronPt = cms.double(100.0),
            minMergeGammaEt = cms.double(1.0),
            minMergeNeutralHadronEt = cms.double(1.0),
            name = cms.string('chargedPFCandidates'),
            plugin = cms.string('PFRecoTauChargedHadronFromPFCandidatePlugin'),
            qualityCuts = cms.PSet(
                isolationQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.2),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.03),
                    minGammaEt = cms.double(1.5),
                    minTrackHits = cms.uint32(8),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(1.0),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                leadingTrkOrPFCandOption = cms.string('leadPFCand'),
                primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
                pvFindingAlgo = cms.string('closestInDeltaZ'),
                recoverLeadingTrk = cms.bool(False),
                signalQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.4),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minNeutralHadronEt = cms.double(30.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                vertexTrackFiltering = cms.bool(False),
                vxAssocQualityCuts = cms.PSet(
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                )
            ),
            verbosity = cms.int32(0)
        ),
        cms.PSet(
            dRcone = cms.double(0.5),
            dRconeLimitedToJetArea = cms.bool(False),
            dRmergeNeutralHadron = cms.double(0.1),
            dRmergePhoton = cms.double(0.05),
            minMergeChargedHadronPt = cms.double(100.0),
            minMergeGammaEt = cms.double(1.0),
            minMergeNeutralHadronEt = cms.double(1.0),
            name = cms.string('lostTracks'),
            plugin = cms.string('PFRecoTauChargedHadronFromLostTrackPlugin'),
            qualityCuts = cms.PSet(
                isolationQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.2),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.03),
                    minGammaEt = cms.double(1.5),
                    minTrackHits = cms.uint32(8),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(1.0),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                leadingTrkOrPFCandOption = cms.string('leadPFCand'),
                primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
                pvFindingAlgo = cms.string('closestInDeltaZ'),
                recoverLeadingTrk = cms.bool(False),
                signalQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.4),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minNeutralHadronEt = cms.double(30.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                vertexTrackFiltering = cms.bool(False),
                vxAssocQualityCuts = cms.PSet(
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                )
            ),
            srcTracks = cms.InputTag("lostTracks"),
            verbosity = cms.int32(0)
        ),
        cms.PSet(
            chargedHadronCandidatesParticleIds = cms.vint32(5),
            dRmergeNeutralHadronWrtChargedHadron = cms.double(0.005),
            dRmergeNeutralHadronWrtElectron = cms.double(0.05),
            dRmergeNeutralHadronWrtNeutralHadron = cms.double(0.01),
            dRmergeNeutralHadronWrtOther = cms.double(0.005),
            dRmergePhotonWrtChargedHadron = cms.double(0.005),
            dRmergePhotonWrtElectron = cms.double(0.005),
            dRmergePhotonWrtNeutralHadron = cms.double(0.01),
            dRmergePhotonWrtOther = cms.double(0.005),
            maxUnmatchedBlockElementsNeutralHadron = cms.int32(1),
            maxUnmatchedBlockElementsPhoton = cms.int32(1),
            minBlockElementMatchesNeutralHadron = cms.int32(2),
            minBlockElementMatchesPhoton = cms.int32(2),
            minMergeChargedHadronPt = cms.double(0.0),
            minMergeGammaEt = cms.double(1.0),
            minMergeNeutralHadronEt = cms.double(1.0),
            name = cms.string('PFNeutralHadrons'),
            plugin = cms.string('PFRecoTauChargedHadronFromPFCandidatePlugin'),
            qualityCuts = cms.PSet(
                isolationQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.2),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.03),
                    minGammaEt = cms.double(1.5),
                    minTrackHits = cms.uint32(8),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(1.0),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                leadingTrkOrPFCandOption = cms.string('leadPFCand'),
                primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
                pvFindingAlgo = cms.string('closestInDeltaZ'),
                recoverLeadingTrk = cms.bool(False),
                signalQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.4),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minNeutralHadronEt = cms.double(30.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                vertexTrackFiltering = cms.bool(False),
                vxAssocQualityCuts = cms.PSet(
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                )
            ),
            verbosity = cms.int32(0)
        )
    ),
    jetSrc = cms.InputTag("patJetsPAT"),
    maxJetAbsEta = cms.double(2.5),
    mightGet = cms.optional.untracked.vstring,
    minJetPt = cms.double(5),
    outputSelection = cms.string('pt > 0.5'),
    ranking = cms.VPSet(
        cms.PSet(
            name = cms.string('ChargedPFCandidate'),
            plugin = cms.string('PFRecoTauChargedHadronStringQuality'),
            selection = cms.string("algoIs(\'kChargedPFCandidate\')"),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('-pt')
        ),
        cms.PSet(
            name = cms.string('ChargedPFCandidate'),
            plugin = cms.string('PFRecoTauChargedHadronStringQuality'),
            selection = cms.string("algoIs(\'kTrack\')"),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('-pt')
        ),
        cms.PSet(
            name = cms.string('ChargedPFCandidate'),
            plugin = cms.string('PFRecoTauChargedHadronStringQuality'),
            selection = cms.string("algoIs(\'kPFNeutralHadron\')"),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('-pt')
        )
    ),
    verbosity = cms.int32(0)
)


process.ak4PFJetsRecoTauChargedHadronsBoosted = cms.EDProducer("PFRecoTauChargedHadronProducer",
    builders = cms.VPSet(
        cms.PSet(
            chargedHadronCandidatesParticleIds = cms.vint32(1, 2, 3),
            dRmergeNeutralHadronWrtChargedHadron = cms.double(0.005),
            dRmergeNeutralHadronWrtElectron = cms.double(0.05),
            dRmergeNeutralHadronWrtNeutralHadron = cms.double(0.01),
            dRmergeNeutralHadronWrtOther = cms.double(0.005),
            dRmergePhotonWrtChargedHadron = cms.double(0.005),
            dRmergePhotonWrtElectron = cms.double(0.005),
            dRmergePhotonWrtNeutralHadron = cms.double(0.01),
            dRmergePhotonWrtOther = cms.double(0.005),
            maxUnmatchedBlockElementsNeutralHadron = cms.int32(1),
            maxUnmatchedBlockElementsPhoton = cms.int32(1),
            minBlockElementMatchesNeutralHadron = cms.int32(2),
            minBlockElementMatchesPhoton = cms.int32(2),
            minMergeChargedHadronPt = cms.double(100.0),
            minMergeGammaEt = cms.double(1.0),
            minMergeNeutralHadronEt = cms.double(1.0),
            name = cms.string('chargedPFCandidates'),
            plugin = cms.string('PFRecoTauChargedHadronFromPFCandidatePlugin'),
            qualityCuts = cms.PSet(
                isolationQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.2),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.03),
                    minGammaEt = cms.double(1.5),
                    minTrackHits = cms.uint32(8),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(1.0),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                leadingTrkOrPFCandOption = cms.string('leadPFCand'),
                primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
                pvFindingAlgo = cms.string('closestInDeltaZ'),
                recoverLeadingTrk = cms.bool(False),
                signalQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.4),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minNeutralHadronEt = cms.double(30.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                vertexTrackFiltering = cms.bool(False),
                vxAssocQualityCuts = cms.PSet(
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                )
            ),
            verbosity = cms.int32(0)
        ),
        cms.PSet(
            dRcone = cms.double(0.5),
            dRconeLimitedToJetArea = cms.bool(False),
            dRmergeNeutralHadron = cms.double(0.1),
            dRmergePhoton = cms.double(0.05),
            minMergeChargedHadronPt = cms.double(100.0),
            minMergeGammaEt = cms.double(1.0),
            minMergeNeutralHadronEt = cms.double(1.0),
            name = cms.string('lostTracks'),
            plugin = cms.string('PFRecoTauChargedHadronFromLostTrackPlugin'),
            qualityCuts = cms.PSet(
                isolationQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.2),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.03),
                    minGammaEt = cms.double(1.5),
                    minTrackHits = cms.uint32(8),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(1.0),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                leadingTrkOrPFCandOption = cms.string('leadPFCand'),
                primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
                pvFindingAlgo = cms.string('closestInDeltaZ'),
                recoverLeadingTrk = cms.bool(False),
                signalQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.4),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minNeutralHadronEt = cms.double(30.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                vertexTrackFiltering = cms.bool(False),
                vxAssocQualityCuts = cms.PSet(
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                )
            ),
            srcTracks = cms.InputTag("lostTracks"),
            verbosity = cms.int32(0)
        ),
        cms.PSet(
            chargedHadronCandidatesParticleIds = cms.vint32(5),
            dRmergeNeutralHadronWrtChargedHadron = cms.double(0.005),
            dRmergeNeutralHadronWrtElectron = cms.double(0.05),
            dRmergeNeutralHadronWrtNeutralHadron = cms.double(0.01),
            dRmergeNeutralHadronWrtOther = cms.double(0.005),
            dRmergePhotonWrtChargedHadron = cms.double(0.005),
            dRmergePhotonWrtElectron = cms.double(0.005),
            dRmergePhotonWrtNeutralHadron = cms.double(0.01),
            dRmergePhotonWrtOther = cms.double(0.005),
            maxUnmatchedBlockElementsNeutralHadron = cms.int32(1),
            maxUnmatchedBlockElementsPhoton = cms.int32(1),
            minBlockElementMatchesNeutralHadron = cms.int32(2),
            minBlockElementMatchesPhoton = cms.int32(2),
            minMergeChargedHadronPt = cms.double(0.0),
            minMergeGammaEt = cms.double(1.0),
            minMergeNeutralHadronEt = cms.double(1.0),
            name = cms.string('PFNeutralHadrons'),
            plugin = cms.string('PFRecoTauChargedHadronFromPFCandidatePlugin'),
            qualityCuts = cms.PSet(
                isolationQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.2),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.03),
                    minGammaEt = cms.double(1.5),
                    minTrackHits = cms.uint32(8),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(1.0),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                leadingTrkOrPFCandOption = cms.string('leadPFCand'),
                primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
                pvFindingAlgo = cms.string('closestInDeltaZ'),
                recoverLeadingTrk = cms.bool(False),
                signalQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.4),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minNeutralHadronEt = cms.double(30.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                vertexTrackFiltering = cms.bool(False),
                vxAssocQualityCuts = cms.PSet(
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                )
            ),
            verbosity = cms.int32(0)
        )
    ),
    jetSrc = cms.InputTag("boostedTauSeedsPAT"),
    maxJetAbsEta = cms.double(2.5),
    mightGet = cms.optional.untracked.vstring,
    minJetPt = cms.double(5),
    outputSelection = cms.string('pt > 0.5'),
    ranking = cms.VPSet(
        cms.PSet(
            name = cms.string('ChargedPFCandidate'),
            plugin = cms.string('PFRecoTauChargedHadronStringQuality'),
            selection = cms.string("algoIs(\'kChargedPFCandidate\')"),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('-pt')
        ),
        cms.PSet(
            name = cms.string('ChargedPFCandidate'),
            plugin = cms.string('PFRecoTauChargedHadronStringQuality'),
            selection = cms.string("algoIs(\'kTrack\')"),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('-pt')
        ),
        cms.PSet(
            name = cms.string('ChargedPFCandidate'),
            plugin = cms.string('PFRecoTauChargedHadronStringQuality'),
            selection = cms.string("algoIs(\'kPFNeutralHadron\')"),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('-pt')
        )
    ),
    verbosity = cms.int32(0)
)


process.ak4PFJetsRecoTauChargedHadronsElectronCleaned = cms.EDProducer("PFRecoTauChargedHadronProducer",
    builders = cms.VPSet(
        cms.PSet(
            chargedHadronCandidatesParticleIds = cms.vint32(1, 2, 3),
            dRmergeNeutralHadronWrtChargedHadron = cms.double(0.005),
            dRmergeNeutralHadronWrtElectron = cms.double(0.05),
            dRmergeNeutralHadronWrtNeutralHadron = cms.double(0.01),
            dRmergeNeutralHadronWrtOther = cms.double(0.005),
            dRmergePhotonWrtChargedHadron = cms.double(0.005),
            dRmergePhotonWrtElectron = cms.double(0.005),
            dRmergePhotonWrtNeutralHadron = cms.double(0.01),
            dRmergePhotonWrtOther = cms.double(0.005),
            maxUnmatchedBlockElementsNeutralHadron = cms.int32(1),
            maxUnmatchedBlockElementsPhoton = cms.int32(1),
            minBlockElementMatchesNeutralHadron = cms.int32(2),
            minBlockElementMatchesPhoton = cms.int32(2),
            minMergeChargedHadronPt = cms.double(100.0),
            minMergeGammaEt = cms.double(1.0),
            minMergeNeutralHadronEt = cms.double(1.0),
            name = cms.string('chargedPFCandidates'),
            plugin = cms.string('PFRecoTauChargedHadronFromPFCandidatePlugin'),
            qualityCuts = cms.PSet(
                isolationQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.2),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.03),
                    minGammaEt = cms.double(1.5),
                    minTrackHits = cms.uint32(8),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(1.0),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                leadingTrkOrPFCandOption = cms.string('leadPFCand'),
                primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
                pvFindingAlgo = cms.string('closestInDeltaZ'),
                recoverLeadingTrk = cms.bool(False),
                signalQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.4),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minNeutralHadronEt = cms.double(30.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                vertexTrackFiltering = cms.bool(False),
                vxAssocQualityCuts = cms.PSet(
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                )
            ),
            verbosity = cms.int32(0)
        ),
        cms.PSet(
            dRcone = cms.double(0.5),
            dRconeLimitedToJetArea = cms.bool(False),
            dRmergeNeutralHadron = cms.double(0.1),
            dRmergePhoton = cms.double(0.05),
            minMergeChargedHadronPt = cms.double(100.0),
            minMergeGammaEt = cms.double(1.0),
            minMergeNeutralHadronEt = cms.double(1.0),
            name = cms.string('lostTracks'),
            plugin = cms.string('PFRecoTauChargedHadronFromLostTrackPlugin'),
            qualityCuts = cms.PSet(
                isolationQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.2),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.03),
                    minGammaEt = cms.double(1.5),
                    minTrackHits = cms.uint32(8),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(1.0),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                leadingTrkOrPFCandOption = cms.string('leadPFCand'),
                primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
                pvFindingAlgo = cms.string('closestInDeltaZ'),
                recoverLeadingTrk = cms.bool(False),
                signalQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.4),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minNeutralHadronEt = cms.double(30.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                vertexTrackFiltering = cms.bool(False),
                vxAssocQualityCuts = cms.PSet(
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                )
            ),
            srcTracks = cms.InputTag("lostTracks"),
            verbosity = cms.int32(0)
        ),
        cms.PSet(
            chargedHadronCandidatesParticleIds = cms.vint32(5),
            dRmergeNeutralHadronWrtChargedHadron = cms.double(0.005),
            dRmergeNeutralHadronWrtElectron = cms.double(0.05),
            dRmergeNeutralHadronWrtNeutralHadron = cms.double(0.01),
            dRmergeNeutralHadronWrtOther = cms.double(0.005),
            dRmergePhotonWrtChargedHadron = cms.double(0.005),
            dRmergePhotonWrtElectron = cms.double(0.005),
            dRmergePhotonWrtNeutralHadron = cms.double(0.01),
            dRmergePhotonWrtOther = cms.double(0.005),
            maxUnmatchedBlockElementsNeutralHadron = cms.int32(1),
            maxUnmatchedBlockElementsPhoton = cms.int32(1),
            minBlockElementMatchesNeutralHadron = cms.int32(2),
            minBlockElementMatchesPhoton = cms.int32(2),
            minMergeChargedHadronPt = cms.double(0.0),
            minMergeGammaEt = cms.double(1.0),
            minMergeNeutralHadronEt = cms.double(1.0),
            name = cms.string('PFNeutralHadrons'),
            plugin = cms.string('PFRecoTauChargedHadronFromPFCandidatePlugin'),
            qualityCuts = cms.PSet(
                isolationQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.2),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.03),
                    minGammaEt = cms.double(1.5),
                    minTrackHits = cms.uint32(8),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(1.0),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                leadingTrkOrPFCandOption = cms.string('leadPFCand'),
                primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
                pvFindingAlgo = cms.string('closestInDeltaZ'),
                recoverLeadingTrk = cms.bool(False),
                signalQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.4),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minNeutralHadronEt = cms.double(30.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                vertexTrackFiltering = cms.bool(False),
                vxAssocQualityCuts = cms.PSet(
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                )
            ),
            verbosity = cms.int32(0)
        )
    ),
    jetSrc = cms.InputTag("patJetsPATElectronCleaned"),
    maxJetAbsEta = cms.double(2.5),
    mightGet = cms.optional.untracked.vstring,
    minJetPt = cms.double(5),
    outputSelection = cms.string('pt > 0.5'),
    ranking = cms.VPSet(
        cms.PSet(
            name = cms.string('ChargedPFCandidate'),
            plugin = cms.string('PFRecoTauChargedHadronStringQuality'),
            selection = cms.string("algoIs(\'kChargedPFCandidate\')"),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('-pt')
        ),
        cms.PSet(
            name = cms.string('ChargedPFCandidate'),
            plugin = cms.string('PFRecoTauChargedHadronStringQuality'),
            selection = cms.string("algoIs(\'kTrack\')"),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('-pt')
        ),
        cms.PSet(
            name = cms.string('ChargedPFCandidate'),
            plugin = cms.string('PFRecoTauChargedHadronStringQuality'),
            selection = cms.string("algoIs(\'kPFNeutralHadron\')"),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('-pt')
        )
    ),
    verbosity = cms.int32(0)
)


process.ak4PFJetsRecoTauChargedHadronsLowPtElectronCleaned = cms.EDProducer("PFRecoTauChargedHadronProducer",
    builders = cms.VPSet(
        cms.PSet(
            chargedHadronCandidatesParticleIds = cms.vint32(1, 2, 3),
            dRmergeNeutralHadronWrtChargedHadron = cms.double(0.005),
            dRmergeNeutralHadronWrtElectron = cms.double(0.05),
            dRmergeNeutralHadronWrtNeutralHadron = cms.double(0.01),
            dRmergeNeutralHadronWrtOther = cms.double(0.005),
            dRmergePhotonWrtChargedHadron = cms.double(0.005),
            dRmergePhotonWrtElectron = cms.double(0.005),
            dRmergePhotonWrtNeutralHadron = cms.double(0.01),
            dRmergePhotonWrtOther = cms.double(0.005),
            maxUnmatchedBlockElementsNeutralHadron = cms.int32(1),
            maxUnmatchedBlockElementsPhoton = cms.int32(1),
            minBlockElementMatchesNeutralHadron = cms.int32(2),
            minBlockElementMatchesPhoton = cms.int32(2),
            minMergeChargedHadronPt = cms.double(100.0),
            minMergeGammaEt = cms.double(1.0),
            minMergeNeutralHadronEt = cms.double(1.0),
            name = cms.string('chargedPFCandidates'),
            plugin = cms.string('PFRecoTauChargedHadronFromPFCandidatePlugin'),
            qualityCuts = cms.PSet(
                isolationQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.2),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.03),
                    minGammaEt = cms.double(1.5),
                    minTrackHits = cms.uint32(8),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(1.0),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                leadingTrkOrPFCandOption = cms.string('leadPFCand'),
                primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
                pvFindingAlgo = cms.string('closestInDeltaZ'),
                recoverLeadingTrk = cms.bool(False),
                signalQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.4),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minNeutralHadronEt = cms.double(30.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                vertexTrackFiltering = cms.bool(False),
                vxAssocQualityCuts = cms.PSet(
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                )
            ),
            verbosity = cms.int32(0)
        ),
        cms.PSet(
            dRcone = cms.double(0.5),
            dRconeLimitedToJetArea = cms.bool(False),
            dRmergeNeutralHadron = cms.double(0.1),
            dRmergePhoton = cms.double(0.05),
            minMergeChargedHadronPt = cms.double(100.0),
            minMergeGammaEt = cms.double(1.0),
            minMergeNeutralHadronEt = cms.double(1.0),
            name = cms.string('lostTracks'),
            plugin = cms.string('PFRecoTauChargedHadronFromLostTrackPlugin'),
            qualityCuts = cms.PSet(
                isolationQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.2),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.03),
                    minGammaEt = cms.double(1.5),
                    minTrackHits = cms.uint32(8),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(1.0),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                leadingTrkOrPFCandOption = cms.string('leadPFCand'),
                primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
                pvFindingAlgo = cms.string('closestInDeltaZ'),
                recoverLeadingTrk = cms.bool(False),
                signalQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.4),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minNeutralHadronEt = cms.double(30.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                vertexTrackFiltering = cms.bool(False),
                vxAssocQualityCuts = cms.PSet(
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                )
            ),
            srcTracks = cms.InputTag("lostTracks"),
            verbosity = cms.int32(0)
        ),
        cms.PSet(
            chargedHadronCandidatesParticleIds = cms.vint32(5),
            dRmergeNeutralHadronWrtChargedHadron = cms.double(0.005),
            dRmergeNeutralHadronWrtElectron = cms.double(0.05),
            dRmergeNeutralHadronWrtNeutralHadron = cms.double(0.01),
            dRmergeNeutralHadronWrtOther = cms.double(0.005),
            dRmergePhotonWrtChargedHadron = cms.double(0.005),
            dRmergePhotonWrtElectron = cms.double(0.005),
            dRmergePhotonWrtNeutralHadron = cms.double(0.01),
            dRmergePhotonWrtOther = cms.double(0.005),
            maxUnmatchedBlockElementsNeutralHadron = cms.int32(1),
            maxUnmatchedBlockElementsPhoton = cms.int32(1),
            minBlockElementMatchesNeutralHadron = cms.int32(2),
            minBlockElementMatchesPhoton = cms.int32(2),
            minMergeChargedHadronPt = cms.double(0.0),
            minMergeGammaEt = cms.double(1.0),
            minMergeNeutralHadronEt = cms.double(1.0),
            name = cms.string('PFNeutralHadrons'),
            plugin = cms.string('PFRecoTauChargedHadronFromPFCandidatePlugin'),
            qualityCuts = cms.PSet(
                isolationQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.2),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.03),
                    minGammaEt = cms.double(1.5),
                    minTrackHits = cms.uint32(8),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(1.0),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                leadingTrkOrPFCandOption = cms.string('leadPFCand'),
                primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
                pvFindingAlgo = cms.string('closestInDeltaZ'),
                recoverLeadingTrk = cms.bool(False),
                signalQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.4),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minNeutralHadronEt = cms.double(30.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                vertexTrackFiltering = cms.bool(False),
                vxAssocQualityCuts = cms.PSet(
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                )
            ),
            verbosity = cms.int32(0)
        )
    ),
    jetSrc = cms.InputTag("patJetsPATLowPtElectronCleaned"),
    maxJetAbsEta = cms.double(2.5),
    mightGet = cms.optional.untracked.vstring,
    minJetPt = cms.double(14.0),
    outputSelection = cms.string('pt > 0.5'),
    ranking = cms.VPSet(
        cms.PSet(
            name = cms.string('ChargedPFCandidate'),
            plugin = cms.string('PFRecoTauChargedHadronStringQuality'),
            selection = cms.string("algoIs(\'kChargedPFCandidate\')"),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('-pt')
        ),
        cms.PSet(
            name = cms.string('ChargedPFCandidate'),
            plugin = cms.string('PFRecoTauChargedHadronStringQuality'),
            selection = cms.string("algoIs(\'kTrack\')"),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('-pt')
        ),
        cms.PSet(
            name = cms.string('ChargedPFCandidate'),
            plugin = cms.string('PFRecoTauChargedHadronStringQuality'),
            selection = cms.string("algoIs(\'kPFNeutralHadron\')"),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('-pt')
        )
    ),
    verbosity = cms.int32(0)
)


process.ak4PFJetsRecoTauChargedHadronsMuonCleaned = cms.EDProducer("PFRecoTauChargedHadronProducer",
    builders = cms.VPSet(
        cms.PSet(
            chargedHadronCandidatesParticleIds = cms.vint32(1, 2, 3),
            dRmergeNeutralHadronWrtChargedHadron = cms.double(0.005),
            dRmergeNeutralHadronWrtElectron = cms.double(0.05),
            dRmergeNeutralHadronWrtNeutralHadron = cms.double(0.01),
            dRmergeNeutralHadronWrtOther = cms.double(0.005),
            dRmergePhotonWrtChargedHadron = cms.double(0.005),
            dRmergePhotonWrtElectron = cms.double(0.005),
            dRmergePhotonWrtNeutralHadron = cms.double(0.01),
            dRmergePhotonWrtOther = cms.double(0.005),
            maxUnmatchedBlockElementsNeutralHadron = cms.int32(1),
            maxUnmatchedBlockElementsPhoton = cms.int32(1),
            minBlockElementMatchesNeutralHadron = cms.int32(2),
            minBlockElementMatchesPhoton = cms.int32(2),
            minMergeChargedHadronPt = cms.double(100.0),
            minMergeGammaEt = cms.double(1.0),
            minMergeNeutralHadronEt = cms.double(1.0),
            name = cms.string('chargedPFCandidates'),
            plugin = cms.string('PFRecoTauChargedHadronFromPFCandidatePlugin'),
            qualityCuts = cms.PSet(
                isolationQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.2),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.03),
                    minGammaEt = cms.double(1.5),
                    minTrackHits = cms.uint32(8),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(1.0),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                leadingTrkOrPFCandOption = cms.string('leadPFCand'),
                primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
                pvFindingAlgo = cms.string('closestInDeltaZ'),
                recoverLeadingTrk = cms.bool(False),
                signalQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.4),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minNeutralHadronEt = cms.double(30.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                vertexTrackFiltering = cms.bool(False),
                vxAssocQualityCuts = cms.PSet(
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                )
            ),
            verbosity = cms.int32(0)
        ),
        cms.PSet(
            dRcone = cms.double(0.5),
            dRconeLimitedToJetArea = cms.bool(False),
            dRmergeNeutralHadron = cms.double(0.1),
            dRmergePhoton = cms.double(0.05),
            minMergeChargedHadronPt = cms.double(100.0),
            minMergeGammaEt = cms.double(1.0),
            minMergeNeutralHadronEt = cms.double(1.0),
            name = cms.string('lostTracks'),
            plugin = cms.string('PFRecoTauChargedHadronFromLostTrackPlugin'),
            qualityCuts = cms.PSet(
                isolationQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.2),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.03),
                    minGammaEt = cms.double(1.5),
                    minTrackHits = cms.uint32(8),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(1.0),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                leadingTrkOrPFCandOption = cms.string('leadPFCand'),
                primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
                pvFindingAlgo = cms.string('closestInDeltaZ'),
                recoverLeadingTrk = cms.bool(False),
                signalQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.4),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minNeutralHadronEt = cms.double(30.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                vertexTrackFiltering = cms.bool(False),
                vxAssocQualityCuts = cms.PSet(
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                )
            ),
            srcTracks = cms.InputTag("lostTracks"),
            verbosity = cms.int32(0)
        ),
        cms.PSet(
            chargedHadronCandidatesParticleIds = cms.vint32(5),
            dRmergeNeutralHadronWrtChargedHadron = cms.double(0.005),
            dRmergeNeutralHadronWrtElectron = cms.double(0.05),
            dRmergeNeutralHadronWrtNeutralHadron = cms.double(0.01),
            dRmergeNeutralHadronWrtOther = cms.double(0.005),
            dRmergePhotonWrtChargedHadron = cms.double(0.005),
            dRmergePhotonWrtElectron = cms.double(0.005),
            dRmergePhotonWrtNeutralHadron = cms.double(0.01),
            dRmergePhotonWrtOther = cms.double(0.005),
            maxUnmatchedBlockElementsNeutralHadron = cms.int32(1),
            maxUnmatchedBlockElementsPhoton = cms.int32(1),
            minBlockElementMatchesNeutralHadron = cms.int32(2),
            minBlockElementMatchesPhoton = cms.int32(2),
            minMergeChargedHadronPt = cms.double(0.0),
            minMergeGammaEt = cms.double(1.0),
            minMergeNeutralHadronEt = cms.double(1.0),
            name = cms.string('PFNeutralHadrons'),
            plugin = cms.string('PFRecoTauChargedHadronFromPFCandidatePlugin'),
            qualityCuts = cms.PSet(
                isolationQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.2),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.03),
                    minGammaEt = cms.double(1.5),
                    minTrackHits = cms.uint32(8),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(1.0),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                leadingTrkOrPFCandOption = cms.string('leadPFCand'),
                primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
                pvFindingAlgo = cms.string('closestInDeltaZ'),
                recoverLeadingTrk = cms.bool(False),
                signalQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.4),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minNeutralHadronEt = cms.double(30.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                vertexTrackFiltering = cms.bool(False),
                vxAssocQualityCuts = cms.PSet(
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                )
            ),
            verbosity = cms.int32(0)
        )
    ),
    jetSrc = cms.InputTag("patJetsPATMuonCleaned"),
    maxJetAbsEta = cms.double(2.5),
    mightGet = cms.optional.untracked.vstring,
    minJetPt = cms.double(5),
    outputSelection = cms.string('pt > 0.5'),
    ranking = cms.VPSet(
        cms.PSet(
            name = cms.string('ChargedPFCandidate'),
            plugin = cms.string('PFRecoTauChargedHadronStringQuality'),
            selection = cms.string("algoIs(\'kChargedPFCandidate\')"),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('-pt')
        ),
        cms.PSet(
            name = cms.string('ChargedPFCandidate'),
            plugin = cms.string('PFRecoTauChargedHadronStringQuality'),
            selection = cms.string("algoIs(\'kTrack\')"),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('-pt')
        ),
        cms.PSet(
            name = cms.string('ChargedPFCandidate'),
            plugin = cms.string('PFRecoTauChargedHadronStringQuality'),
            selection = cms.string("algoIs(\'kPFNeutralHadron\')"),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('-pt')
        )
    ),
    verbosity = cms.int32(0)
)


process.boostedTauSeedsPAT = cms.EDProducer("PATBoostedTauSeedsProducer",
    pfCandidateSrc = cms.InputTag("packedPFCandidates"),
    subjetSrc = cms.InputTag("ca8PFJetsCHSprunedForBoostedTausPAT","subJetsForSeedingBoostedTausPAT"),
    verbosity = cms.int32(0)
)


process.ca8PFJetsCHSprunedForBoostedTausPAT = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    applyWeight = cms.bool(False),
    dRMax = cms.double(0.8),
    dRMin = cms.double(0.0),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('CambridgeAachen'),
    jetCollInstanceName = cms.string('subJetsForSeedingBoostedTausPAT'),
    jetPtMin = cms.double(10),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxDepth = cms.int32(100),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    muMax = cms.double(0.667),
    muMin = cms.double(0.0),
    nFilt = cms.int32(100),
    nSigmaPU = cms.double(1.0),
    rParam = cms.double(0.8),
    radiusPU = cms.double(0.5),
    src = cms.InputTag("packedPFCandidates"),
    srcPVs = cms.InputTag(""),
    subjetPtMin = cms.double(5),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(True),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9),
    writeCompound = cms.bool(True),
    yMax = cms.double(1000000.0),
    yMin = cms.double(-1000000.0)
)


process.combinatoricRecoTaus = cms.EDProducer("RecoTauProducer",
    buildNullTaus = cms.bool(False),
    builders = cms.VPSet(cms.PSet(
        decayModes = cms.VPSet(
            cms.PSet(
                maxPiZeros = cms.uint32(0),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(1),
                nPiZeros = cms.uint32(0)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(6),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(1),
                nPiZeros = cms.uint32(1)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(5),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(1),
                nPiZeros = cms.uint32(2)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(0),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(2),
                nPiZeros = cms.uint32(0)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(3),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(2),
                nPiZeros = cms.uint32(1)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(0),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(3),
                nPiZeros = cms.uint32(0)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(3),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(3),
                nPiZeros = cms.uint32(1)
            )
        ),
        isolationConeSize = cms.double(0.5),
        minAbsPhotonSumPt_insideSignalCone = cms.double(2.5),
        minAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
        minRelPhotonSumPt_insideSignalCone = cms.double(0.1),
        minRelPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
        name = cms.string('combinatoric'),
        pfCandSrc = cms.InputTag("packedPFCandidates"),
        plugin = cms.string('RecoTauBuilderCombinatoricPlugin'),
        qualityCuts = cms.PSet(
            isolationQualityCuts = cms.PSet(
                maxDeltaZ = cms.double(0.2),
                maxDeltaZToLeadTrack = cms.double(-1.0),
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.03),
                minGammaEt = cms.double(1.5),
                minTrackHits = cms.uint32(8),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(1.0),
                minTrackVertexWeight = cms.double(-1.0)
            ),
            leadingTrkOrPFCandOption = cms.string('leadPFCand'),
            primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
            pvFindingAlgo = cms.string('closestInDeltaZ'),
            recoverLeadingTrk = cms.bool(False),
            signalQualityCuts = cms.PSet(
                maxDeltaZ = cms.double(0.4),
                maxDeltaZToLeadTrack = cms.double(-1.0),
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.1),
                minGammaEt = cms.double(1.0),
                minNeutralHadronEt = cms.double(30.0),
                minTrackHits = cms.uint32(3),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(0.5),
                minTrackVertexWeight = cms.double(-1.0)
            ),
            vertexTrackFiltering = cms.bool(False),
            vxAssocQualityCuts = cms.PSet(
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.1),
                minGammaEt = cms.double(1.0),
                minTrackHits = cms.uint32(3),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(0.5),
                minTrackVertexWeight = cms.double(-1.0)
            )
        ),
        signalConeSize = cms.string('max(min(0.1, 3.0/pt()), 0.05)'),
        verbosity = cms.int32(0)
    )),
    chargedHadronSrc = cms.InputTag("ak4PFJetsRecoTauChargedHadrons"),
    jetRegionSrc = cms.InputTag("recoTauAK4Jets08RegionPAT"),
    jetSrc = cms.InputTag("patJetsPAT"),
    maxJetAbsEta = cms.double(2.5),
    minJetPt = cms.double(5),
    modifiers = cms.VPSet(
        cms.PSet(
            name = cms.string('sipt'),
            plugin = cms.string('RecoTauImpactParameterSignificancePlugin'),
            qualityCuts = cms.PSet(
                isolationQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.2),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.03),
                    minGammaEt = cms.double(1.5),
                    minTrackHits = cms.uint32(8),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(1.0),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                leadingTrkOrPFCandOption = cms.string('leadPFCand'),
                primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
                pvFindingAlgo = cms.string('closestInDeltaZ'),
                recoverLeadingTrk = cms.bool(False),
                signalQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.4),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minNeutralHadronEt = cms.double(30.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                vertexTrackFiltering = cms.bool(False),
                vxAssocQualityCuts = cms.PSet(
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                )
            )
        ),
        cms.PSet(
            dRaddNeutralHadron = cms.double(0.12),
            dRaddPhoton = cms.double(-1.0),
            minGammaEt = cms.double(10.0),
            minNeutralHadronEt = cms.double(50.0),
            name = cms.string('tau_en_reconstruction'),
            plugin = cms.string('PFRecoTauEnergyAlgorithmPlugin'),
            verbosity = cms.int32(0)
        ),
        cms.PSet(
            name = cms.string('tau_mass'),
            plugin = cms.string('PFRecoTauMassPlugin'),
            verbosity = cms.int32(0)
        )
    ),
    outputSelection = cms.string('leadChargedHadrCand().isNonnull()'),
    piZeroSrc = cms.InputTag("ak4PFJetsLegacyHPSPiZeros")
)


process.combinatoricRecoTausBoosted = cms.EDProducer("RecoTauProducer",
    buildNullTaus = cms.bool(False),
    builders = cms.VPSet(cms.PSet(
        decayModes = cms.VPSet(
            cms.PSet(
                maxPiZeros = cms.uint32(0),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(1),
                nPiZeros = cms.uint32(0)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(6),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(1),
                nPiZeros = cms.uint32(1)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(5),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(1),
                nPiZeros = cms.uint32(2)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(0),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(2),
                nPiZeros = cms.uint32(0)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(3),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(2),
                nPiZeros = cms.uint32(1)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(0),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(3),
                nPiZeros = cms.uint32(0)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(3),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(3),
                nPiZeros = cms.uint32(1)
            )
        ),
        isolationConeSize = cms.double(0.5),
        minAbsPhotonSumPt_insideSignalCone = cms.double(2.5),
        minAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
        minRelPhotonSumPt_insideSignalCone = cms.double(0.1),
        minRelPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
        name = cms.string('combinatoric'),
        pfCandSrc = cms.InputTag("packedPFCandidates"),
        plugin = cms.string('RecoTauBuilderCombinatoricPlugin'),
        qualityCuts = cms.PSet(
            isolationQualityCuts = cms.PSet(
                maxDeltaZ = cms.double(0.2),
                maxDeltaZToLeadTrack = cms.double(-1.0),
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.03),
                minGammaEt = cms.double(1.5),
                minTrackHits = cms.uint32(8),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(1.0),
                minTrackVertexWeight = cms.double(-1.0)
            ),
            leadingTrkOrPFCandOption = cms.string('leadPFCand'),
            primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
            pvFindingAlgo = cms.string('closestInDeltaZ'),
            recoverLeadingTrk = cms.bool(False),
            signalQualityCuts = cms.PSet(
                maxDeltaZ = cms.double(0.4),
                maxDeltaZToLeadTrack = cms.double(-1.0),
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.1),
                minGammaEt = cms.double(1.0),
                minNeutralHadronEt = cms.double(30.0),
                minTrackHits = cms.uint32(3),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(0.5),
                minTrackVertexWeight = cms.double(-1.0)
            ),
            vertexTrackFiltering = cms.bool(False),
            vxAssocQualityCuts = cms.PSet(
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.1),
                minGammaEt = cms.double(1.0),
                minTrackHits = cms.uint32(3),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(0.5),
                minTrackVertexWeight = cms.double(-1.0)
            )
        ),
        signalConeSize = cms.string('max(min(0.1, 3.0/pt()), 0.05)'),
        verbosity = cms.int32(0)
    )),
    chargedHadronSrc = cms.InputTag("ak4PFJetsRecoTauChargedHadronsBoosted"),
    jetRegionSrc = cms.InputTag("recoTauAK4Jets08RegionPATBoosted"),
    jetSrc = cms.InputTag("boostedTauSeedsPAT"),
    maxJetAbsEta = cms.double(2.5),
    minJetPt = cms.double(5),
    modifiers = cms.VPSet(
        cms.PSet(
            name = cms.string('sipt'),
            plugin = cms.string('RecoTauImpactParameterSignificancePlugin'),
            qualityCuts = cms.PSet(
                isolationQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.2),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.03),
                    minGammaEt = cms.double(1.5),
                    minTrackHits = cms.uint32(8),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(1.0),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                leadingTrkOrPFCandOption = cms.string('leadPFCand'),
                primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
                pvFindingAlgo = cms.string('closestInDeltaZ'),
                recoverLeadingTrk = cms.bool(False),
                signalQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.4),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minNeutralHadronEt = cms.double(30.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                vertexTrackFiltering = cms.bool(False),
                vxAssocQualityCuts = cms.PSet(
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                )
            )
        ),
        cms.PSet(
            dRaddNeutralHadron = cms.double(0.12),
            dRaddPhoton = cms.double(-1.0),
            minGammaEt = cms.double(10.0),
            minNeutralHadronEt = cms.double(50.0),
            name = cms.string('tau_en_reconstruction'),
            plugin = cms.string('PFRecoTauEnergyAlgorithmPlugin'),
            verbosity = cms.int32(0)
        ),
        cms.PSet(
            name = cms.string('tau_mass'),
            plugin = cms.string('PFRecoTauMassPlugin'),
            verbosity = cms.int32(0)
        )
    ),
    outputSelection = cms.string('leadChargedHadrCand().isNonnull()'),
    piZeroSrc = cms.InputTag("ak4PFJetsLegacyHPSPiZerosBoosted")
)


process.combinatoricRecoTausElectronCleaned = cms.EDProducer("RecoTauProducer",
    buildNullTaus = cms.bool(False),
    builders = cms.VPSet(cms.PSet(
        decayModes = cms.VPSet(
            cms.PSet(
                maxPiZeros = cms.uint32(0),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(1),
                nPiZeros = cms.uint32(0)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(6),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(1),
                nPiZeros = cms.uint32(1)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(5),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(1),
                nPiZeros = cms.uint32(2)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(0),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(2),
                nPiZeros = cms.uint32(0)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(3),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(2),
                nPiZeros = cms.uint32(1)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(0),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(3),
                nPiZeros = cms.uint32(0)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(3),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(3),
                nPiZeros = cms.uint32(1)
            )
        ),
        isolationConeSize = cms.double(0.5),
        minAbsPhotonSumPt_insideSignalCone = cms.double(2.5),
        minAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
        minRelPhotonSumPt_insideSignalCone = cms.double(0.1),
        minRelPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
        name = cms.string('combinatoric'),
        pfCandSrc = cms.InputTag("PackedCandsElectronCleaned","packedPFCandidatesElectronCleaned"),
        plugin = cms.string('RecoTauBuilderCombinatoricPlugin'),
        qualityCuts = cms.PSet(
            isolationQualityCuts = cms.PSet(
                maxDeltaZ = cms.double(0.2),
                maxDeltaZToLeadTrack = cms.double(-1.0),
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.03),
                minGammaEt = cms.double(1.5),
                minTrackHits = cms.uint32(8),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(1.0),
                minTrackVertexWeight = cms.double(-1.0)
            ),
            leadingTrkOrPFCandOption = cms.string('leadPFCand'),
            primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
            pvFindingAlgo = cms.string('closestInDeltaZ'),
            recoverLeadingTrk = cms.bool(False),
            signalQualityCuts = cms.PSet(
                maxDeltaZ = cms.double(0.4),
                maxDeltaZToLeadTrack = cms.double(-1.0),
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.1),
                minGammaEt = cms.double(1.0),
                minNeutralHadronEt = cms.double(30.0),
                minTrackHits = cms.uint32(3),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(0.5),
                minTrackVertexWeight = cms.double(-1.0)
            ),
            vertexTrackFiltering = cms.bool(False),
            vxAssocQualityCuts = cms.PSet(
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.1),
                minGammaEt = cms.double(1.0),
                minTrackHits = cms.uint32(3),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(0.5),
                minTrackVertexWeight = cms.double(-1.0)
            )
        ),
        signalConeSize = cms.string('max(min(0.1, 3.0/pt()), 0.05)'),
        verbosity = cms.int32(0)
    )),
    chargedHadronSrc = cms.InputTag("ak4PFJetsRecoTauChargedHadronsElectronCleaned"),
    jetRegionSrc = cms.InputTag("recoTauAK4Jets08RegionPATElectronCleaned"),
    jetSrc = cms.InputTag("patJetsPATElectronCleaned"),
    maxJetAbsEta = cms.double(2.5),
    minJetPt = cms.double(5),
    modifiers = cms.VPSet(
        cms.PSet(
            name = cms.string('sipt'),
            plugin = cms.string('RecoTauImpactParameterSignificancePlugin'),
            qualityCuts = cms.PSet(
                isolationQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.2),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.03),
                    minGammaEt = cms.double(1.5),
                    minTrackHits = cms.uint32(8),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(1.0),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                leadingTrkOrPFCandOption = cms.string('leadPFCand'),
                primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
                pvFindingAlgo = cms.string('closestInDeltaZ'),
                recoverLeadingTrk = cms.bool(False),
                signalQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.4),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minNeutralHadronEt = cms.double(30.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                vertexTrackFiltering = cms.bool(False),
                vxAssocQualityCuts = cms.PSet(
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                )
            )
        ),
        cms.PSet(
            dRaddNeutralHadron = cms.double(0.12),
            dRaddPhoton = cms.double(-1.0),
            minGammaEt = cms.double(10.0),
            minNeutralHadronEt = cms.double(50.0),
            name = cms.string('tau_en_reconstruction'),
            plugin = cms.string('PFRecoTauEnergyAlgorithmPlugin'),
            verbosity = cms.int32(0)
        ),
        cms.PSet(
            name = cms.string('tau_mass'),
            plugin = cms.string('PFRecoTauMassPlugin'),
            verbosity = cms.int32(0)
        )
    ),
    outputSelection = cms.string('leadChargedHadrCand().isNonnull()'),
    piZeroSrc = cms.InputTag("ak4PFJetsLegacyHPSPiZerosElectronCleaned")
)


process.combinatoricRecoTausLowPtElectronCleaned = cms.EDProducer("RecoTauProducer",
    buildNullTaus = cms.bool(False),
    builders = cms.VPSet(cms.PSet(
        decayModes = cms.VPSet(
            cms.PSet(
                maxPiZeros = cms.uint32(0),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(1),
                nPiZeros = cms.uint32(0)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(6),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(1),
                nPiZeros = cms.uint32(1)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(5),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(1),
                nPiZeros = cms.uint32(2)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(0),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(2),
                nPiZeros = cms.uint32(0)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(3),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(2),
                nPiZeros = cms.uint32(1)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(0),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(3),
                nPiZeros = cms.uint32(0)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(3),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(3),
                nPiZeros = cms.uint32(1)
            )
        ),
        isolationConeSize = cms.double(0.5),
        minAbsPhotonSumPt_insideSignalCone = cms.double(2.5),
        minAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
        minRelPhotonSumPt_insideSignalCone = cms.double(0.1),
        minRelPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
        name = cms.string('combinatoric'),
        pfCandSrc = cms.InputTag("PackedCandsLowPtElectronCleaned","packedPFCandidatesLowPtElectronCleaned"),
        plugin = cms.string('RecoTauBuilderCombinatoricPlugin'),
        qualityCuts = cms.PSet(
            isolationQualityCuts = cms.PSet(
                maxDeltaZ = cms.double(0.2),
                maxDeltaZToLeadTrack = cms.double(-1.0),
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.03),
                minGammaEt = cms.double(1.5),
                minTrackHits = cms.uint32(8),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(1.0),
                minTrackVertexWeight = cms.double(-1.0)
            ),
            leadingTrkOrPFCandOption = cms.string('leadPFCand'),
            primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
            pvFindingAlgo = cms.string('closestInDeltaZ'),
            recoverLeadingTrk = cms.bool(False),
            signalQualityCuts = cms.PSet(
                maxDeltaZ = cms.double(0.4),
                maxDeltaZToLeadTrack = cms.double(-1.0),
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.1),
                minGammaEt = cms.double(1.0),
                minNeutralHadronEt = cms.double(30.0),
                minTrackHits = cms.uint32(3),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(0.5),
                minTrackVertexWeight = cms.double(-1.0)
            ),
            vertexTrackFiltering = cms.bool(False),
            vxAssocQualityCuts = cms.PSet(
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.1),
                minGammaEt = cms.double(1.0),
                minTrackHits = cms.uint32(3),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(0.5),
                minTrackVertexWeight = cms.double(-1.0)
            )
        ),
        signalConeSize = cms.string('max(min(0.1, 3.0/pt()), 0.05)'),
        verbosity = cms.int32(0)
    )),
    chargedHadronSrc = cms.InputTag("ak4PFJetsRecoTauChargedHadronsLowPtElectronCleaned"),
    jetRegionSrc = cms.InputTag("recoTauAK4Jets08RegionPATLowPtElectronCleaned"),
    jetSrc = cms.InputTag("patJetsPATLowPtElectronCleaned"),
    maxJetAbsEta = cms.double(2.5),
    minJetPt = cms.double(14.0),
    modifiers = cms.VPSet(
        cms.PSet(
            name = cms.string('sipt'),
            plugin = cms.string('RecoTauImpactParameterSignificancePlugin'),
            qualityCuts = cms.PSet(
                isolationQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.2),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.03),
                    minGammaEt = cms.double(1.5),
                    minTrackHits = cms.uint32(8),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(1.0),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                leadingTrkOrPFCandOption = cms.string('leadPFCand'),
                primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
                pvFindingAlgo = cms.string('closestInDeltaZ'),
                recoverLeadingTrk = cms.bool(False),
                signalQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.4),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minNeutralHadronEt = cms.double(30.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                vertexTrackFiltering = cms.bool(False),
                vxAssocQualityCuts = cms.PSet(
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                )
            )
        ),
        cms.PSet(
            dRaddNeutralHadron = cms.double(0.12),
            dRaddPhoton = cms.double(-1.0),
            minGammaEt = cms.double(10.0),
            minNeutralHadronEt = cms.double(50.0),
            name = cms.string('tau_en_reconstruction'),
            plugin = cms.string('PFRecoTauEnergyAlgorithmPlugin'),
            verbosity = cms.int32(0)
        ),
        cms.PSet(
            name = cms.string('tau_mass'),
            plugin = cms.string('PFRecoTauMassPlugin'),
            verbosity = cms.int32(0)
        )
    ),
    outputSelection = cms.string('leadChargedHadrCand().isNonnull()'),
    piZeroSrc = cms.InputTag("ak4PFJetsLegacyHPSPiZerosLowPtElectronCleaned")
)


process.combinatoricRecoTausMuonCleaned = cms.EDProducer("RecoTauProducer",
    buildNullTaus = cms.bool(False),
    builders = cms.VPSet(cms.PSet(
        decayModes = cms.VPSet(
            cms.PSet(
                maxPiZeros = cms.uint32(0),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(1),
                nPiZeros = cms.uint32(0)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(6),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(1),
                nPiZeros = cms.uint32(1)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(5),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(1),
                nPiZeros = cms.uint32(2)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(0),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(2),
                nPiZeros = cms.uint32(0)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(3),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(2),
                nPiZeros = cms.uint32(1)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(0),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(3),
                nPiZeros = cms.uint32(0)
            ),
            cms.PSet(
                maxPiZeros = cms.uint32(3),
                maxTracks = cms.uint32(6),
                nCharged = cms.uint32(3),
                nPiZeros = cms.uint32(1)
            )
        ),
        isolationConeSize = cms.double(0.5),
        minAbsPhotonSumPt_insideSignalCone = cms.double(2.5),
        minAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
        minRelPhotonSumPt_insideSignalCone = cms.double(0.1),
        minRelPhotonSumPt_outsideSignalCone = cms.double(1000000000.0),
        name = cms.string('combinatoric'),
        pfCandSrc = cms.InputTag("PackedCandsMuonCleaned","packedPFCandidatesMuonCleaned"),
        plugin = cms.string('RecoTauBuilderCombinatoricPlugin'),
        qualityCuts = cms.PSet(
            isolationQualityCuts = cms.PSet(
                maxDeltaZ = cms.double(0.2),
                maxDeltaZToLeadTrack = cms.double(-1.0),
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.03),
                minGammaEt = cms.double(1.5),
                minTrackHits = cms.uint32(8),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(1.0),
                minTrackVertexWeight = cms.double(-1.0)
            ),
            leadingTrkOrPFCandOption = cms.string('leadPFCand'),
            primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
            pvFindingAlgo = cms.string('closestInDeltaZ'),
            recoverLeadingTrk = cms.bool(False),
            signalQualityCuts = cms.PSet(
                maxDeltaZ = cms.double(0.4),
                maxDeltaZToLeadTrack = cms.double(-1.0),
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.1),
                minGammaEt = cms.double(1.0),
                minNeutralHadronEt = cms.double(30.0),
                minTrackHits = cms.uint32(3),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(0.5),
                minTrackVertexWeight = cms.double(-1.0)
            ),
            vertexTrackFiltering = cms.bool(False),
            vxAssocQualityCuts = cms.PSet(
                maxTrackChi2 = cms.double(100.0),
                maxTransverseImpactParameter = cms.double(0.1),
                minGammaEt = cms.double(1.0),
                minTrackHits = cms.uint32(3),
                minTrackPixelHits = cms.uint32(0),
                minTrackPt = cms.double(0.5),
                minTrackVertexWeight = cms.double(-1.0)
            )
        ),
        signalConeSize = cms.string('max(min(0.1, 3.0/pt()), 0.05)'),
        verbosity = cms.int32(0)
    )),
    chargedHadronSrc = cms.InputTag("ak4PFJetsRecoTauChargedHadronsMuonCleaned"),
    jetRegionSrc = cms.InputTag("recoTauAK4Jets08RegionPATMuonCleaned"),
    jetSrc = cms.InputTag("patJetsPATMuonCleaned"),
    maxJetAbsEta = cms.double(2.5),
    minJetPt = cms.double(5),
    modifiers = cms.VPSet(
        cms.PSet(
            name = cms.string('sipt'),
            plugin = cms.string('RecoTauImpactParameterSignificancePlugin'),
            qualityCuts = cms.PSet(
                isolationQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.2),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.03),
                    minGammaEt = cms.double(1.5),
                    minTrackHits = cms.uint32(8),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(1.0),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                leadingTrkOrPFCandOption = cms.string('leadPFCand'),
                primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
                pvFindingAlgo = cms.string('closestInDeltaZ'),
                recoverLeadingTrk = cms.bool(False),
                signalQualityCuts = cms.PSet(
                    maxDeltaZ = cms.double(0.4),
                    maxDeltaZToLeadTrack = cms.double(-1.0),
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minNeutralHadronEt = cms.double(30.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                ),
                vertexTrackFiltering = cms.bool(False),
                vxAssocQualityCuts = cms.PSet(
                    maxTrackChi2 = cms.double(100.0),
                    maxTransverseImpactParameter = cms.double(0.1),
                    minGammaEt = cms.double(1.0),
                    minTrackHits = cms.uint32(3),
                    minTrackPixelHits = cms.uint32(0),
                    minTrackPt = cms.double(0.5),
                    minTrackVertexWeight = cms.double(-1.0)
                )
            )
        ),
        cms.PSet(
            dRaddNeutralHadron = cms.double(0.12),
            dRaddPhoton = cms.double(-1.0),
            minGammaEt = cms.double(10.0),
            minNeutralHadronEt = cms.double(50.0),
            name = cms.string('tau_en_reconstruction'),
            plugin = cms.string('PFRecoTauEnergyAlgorithmPlugin'),
            verbosity = cms.int32(0)
        ),
        cms.PSet(
            name = cms.string('tau_mass'),
            plugin = cms.string('PFRecoTauMassPlugin'),
            verbosity = cms.int32(0)
        )
    ),
    outputSelection = cms.string('leadChargedHadrCand().isNonnull()'),
    piZeroSrc = cms.InputTag("ak4PFJetsLegacyHPSPiZerosMuonCleaned")
)


process.deepTau2017v2p1 = cms.EDProducer("DeepTauId",
    VSeWP = cms.vstring(
        '0.0630386',
        '0.1686942',
        '0.362813',
        '0.6815435',
        '0.8847544',
        '0.9675541',
        '0.9859251',
        '0.9928449'
    ),
    VSjetWP = cms.vstring(
        '0.2599605',
        '0.4249705',
        '0.5983682',
        '0.7848675',
        '0.8834768',
        '0.9308689',
        '0.9573137',
        '0.9733927'
    ),
    VSmuWP = cms.vstring(
        '0.1058354',
        '0.2158633',
        '0.5551894',
        '0.8754835'
    ),
    debug_level = cms.int32(0),
    disable_dxy_pca = cms.bool(True),
    electrons = cms.InputTag("slimmedElectrons"),
    graph_file = cms.vstring(
        'core:RecoTauTag/TrainingFiles/data/DeepTauId/deepTau_2017v2p6_e6_core.pb',
        'inner:RecoTauTag/TrainingFiles/data/DeepTauId/deepTau_2017v2p6_e6_inner.pb',
        'outer:RecoTauTag/TrainingFiles/data/DeepTauId/deepTau_2017v2p6_e6_outer.pb'
    ),
    is_online = cms.bool(False),
    mem_mapped = cms.bool(False),
    muons = cms.InputTag("slimmedMuons"),
    pfcands = cms.InputTag("packedPFCandidates"),
    rho = cms.InputTag("fixedGridRhoAll"),
    taus = cms.InputTag("selectedPatTausNoNewIDs"),
    version = cms.uint32(2),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.deepTau2017v2p1Boosted = cms.EDProducer("DeepTauId",
    VSeWP = cms.vstring(
        '0.0630386',
        '0.1686942',
        '0.362813',
        '0.6815435',
        '0.8847544',
        '0.9675541',
        '0.9859251',
        '0.9928449'
    ),
    VSjetWP = cms.vstring(
        '0.2599605',
        '0.4249705',
        '0.5983682',
        '0.7848675',
        '0.8834768',
        '0.9308689',
        '0.9573137',
        '0.9733927'
    ),
    VSmuWP = cms.vstring(
        '0.1058354',
        '0.2158633',
        '0.5551894',
        '0.8754835'
    ),
    debug_level = cms.int32(0),
    disable_dxy_pca = cms.bool(True),
    electrons = cms.InputTag("slimmedElectrons"),
    graph_file = cms.vstring(
        'core:RecoTauTag/TrainingFiles/data/DeepTauId/deepTau_2017v2p6_e6_core.pb',
        'inner:RecoTauTag/TrainingFiles/data/DeepTauId/deepTau_2017v2p6_e6_inner.pb',
        'outer:RecoTauTag/TrainingFiles/data/DeepTauId/deepTau_2017v2p6_e6_outer.pb'
    ),
    is_online = cms.bool(False),
    mem_mapped = cms.bool(False),
    muons = cms.InputTag("slimmedMuons"),
    pfcands = cms.InputTag("packedPFCandidates"),
    rho = cms.InputTag("fixedGridRhoAll"),
    taus = cms.InputTag("selectedPatTausNoNewIDsBoosted"),
    version = cms.uint32(2),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.deepTau2017v2p1ElectronCleaned = cms.EDProducer("DeepTauId",
    VSeWP = cms.vstring(
        '0.0630386',
        '0.1686942',
        '0.362813',
        '0.6815435',
        '0.8847544',
        '0.9675541',
        '0.9859251',
        '0.9928449'
    ),
    VSjetWP = cms.vstring(
        '0.2599605',
        '0.4249705',
        '0.5983682',
        '0.7848675',
        '0.8834768',
        '0.9308689',
        '0.9573137',
        '0.9733927'
    ),
    VSmuWP = cms.vstring(
        '0.1058354',
        '0.2158633',
        '0.5551894',
        '0.8754835'
    ),
    debug_level = cms.int32(0),
    disable_dxy_pca = cms.bool(True),
    electrons = cms.InputTag("slimmedElectrons"),
    graph_file = cms.vstring(
        'core:RecoTauTag/TrainingFiles/data/DeepTauId/deepTau_2017v2p6_e6_core.pb',
        'inner:RecoTauTag/TrainingFiles/data/DeepTauId/deepTau_2017v2p6_e6_inner.pb',
        'outer:RecoTauTag/TrainingFiles/data/DeepTauId/deepTau_2017v2p6_e6_outer.pb'
    ),
    is_online = cms.bool(False),
    mem_mapped = cms.bool(False),
    muons = cms.InputTag("slimmedMuons"),
    pfcands = cms.InputTag("packedPFCandidates"),
    rho = cms.InputTag("fixedGridRhoAll"),
    taus = cms.InputTag("selectedPatTausNoNewIDsElectronCleaned"),
    version = cms.uint32(2),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.deepTau2017v2p1LowPtElectronCleaned = cms.EDProducer("DeepTauId",
    VSeWP = cms.vstring(
        '0.0630386',
        '0.1686942',
        '0.362813',
        '0.6815435',
        '0.8847544',
        '0.9675541',
        '0.9859251',
        '0.9928449'
    ),
    VSjetWP = cms.vstring(
        '0.2599605',
        '0.4249705',
        '0.5983682',
        '0.7848675',
        '0.8834768',
        '0.9308689',
        '0.9573137',
        '0.9733927'
    ),
    VSmuWP = cms.vstring(
        '0.1058354',
        '0.2158633',
        '0.5551894',
        '0.8754835'
    ),
    debug_level = cms.int32(0),
    disable_dxy_pca = cms.bool(True),
    electrons = cms.InputTag("slimmedElectrons"),
    graph_file = cms.vstring(
        'core:RecoTauTag/TrainingFiles/data/DeepTauId/deepTau_2017v2p6_e6_core.pb',
        'inner:RecoTauTag/TrainingFiles/data/DeepTauId/deepTau_2017v2p6_e6_inner.pb',
        'outer:RecoTauTag/TrainingFiles/data/DeepTauId/deepTau_2017v2p6_e6_outer.pb'
    ),
    is_online = cms.bool(False),
    mem_mapped = cms.bool(False),
    muons = cms.InputTag("slimmedMuons"),
    pfcands = cms.InputTag("packedPFCandidates"),
    rho = cms.InputTag("fixedGridRhoAll"),
    taus = cms.InputTag("selectedPatTausNoNewIDsLowPtElectronCleaned"),
    version = cms.uint32(2),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.deepTau2017v2p1MuonCleaned = cms.EDProducer("DeepTauId",
    VSeWP = cms.vstring(
        '0.0630386',
        '0.1686942',
        '0.362813',
        '0.6815435',
        '0.8847544',
        '0.9675541',
        '0.9859251',
        '0.9928449'
    ),
    VSjetWP = cms.vstring(
        '0.2599605',
        '0.4249705',
        '0.5983682',
        '0.7848675',
        '0.8834768',
        '0.9308689',
        '0.9573137',
        '0.9733927'
    ),
    VSmuWP = cms.vstring(
        '0.1058354',
        '0.2158633',
        '0.5551894',
        '0.8754835'
    ),
    debug_level = cms.int32(0),
    disable_dxy_pca = cms.bool(True),
    electrons = cms.InputTag("slimmedElectrons"),
    graph_file = cms.vstring(
        'core:RecoTauTag/TrainingFiles/data/DeepTauId/deepTau_2017v2p6_e6_core.pb',
        'inner:RecoTauTag/TrainingFiles/data/DeepTauId/deepTau_2017v2p6_e6_inner.pb',
        'outer:RecoTauTag/TrainingFiles/data/DeepTauId/deepTau_2017v2p6_e6_outer.pb'
    ),
    is_online = cms.bool(False),
    mem_mapped = cms.bool(False),
    muons = cms.InputTag("slimmedMuons"),
    pfcands = cms.InputTag("packedPFCandidates"),
    rho = cms.InputTag("fixedGridRhoAll"),
    taus = cms.InputTag("selectedPatTausNoNewIDsMuonCleaned"),
    version = cms.uint32(2),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.discriminationByIsolationMVArun2v1 = cms.EDProducer("RecoTauDiscriminantCutMultiplexer",
    PFTauProducer = cms.InputTag("pfTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            Producer = cms.InputTag("pfRecoTauDiscriminationByLeadingTrackFinding"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('newDMwLT'),
        variable = cms.string('pt')
    )),
    mightGet = cms.optional.untracked.vstring,
    mvaOutput_normalization = cms.string(''),
    rawValues = cms.vstring('discriminator'),
    toMultiplex = cms.InputTag("discriminationByIsolationMVArun2v1raw"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        'Eff80',
        'Eff70',
        'Eff60',
        'Eff50',
        'Eff40'
    )
)


process.discriminationByIsolationMVArun2v1raw = cms.EDProducer("PFRecoTauDiscriminationByMVAIsolationRun2",
    PFTauProducer = cms.InputTag("pfTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            Producer = cms.InputTag("pfRecoTauDiscriminationByLeadingTrackFinding"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.optional.FileInPath,
    inputIDNameSuffix = cms.string(''),
    loadMVAfromDB = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    mvaName = cms.string('tauIdMVAnewDMwLT'),
    mvaOpt = cms.string('newDMwLT'),
    srcBasicTauDiscriminators = cms.InputTag("hpsPFTauBasicDiscriminators"),
    srcTauTransverseImpactParameters = cms.InputTag(""),
    verbosity = cms.int32(0)
)


process.hpsPFTauBasicDiscriminators = cms.EDProducer("PFRecoTauDiscriminationByIsolationContainer",
    IDWPdefinitions = cms.VPSet(
        cms.PSet(
            IDname = cms.string('ByLooseCombinedIsolationDBSumPtCorr3Hits'),
            maximumAbsoluteValues = cms.vdouble(2.5, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3Hits',
                'PhotonPtSumOutsideSignalCone'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByMediumCombinedIsolationDBSumPtCorr3Hits'),
            maximumAbsoluteValues = cms.vdouble(1.5, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3Hits',
                'PhotonPtSumOutsideSignalCone'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByTightCombinedIsolationDBSumPtCorr3Hits'),
            maximumAbsoluteValues = cms.vdouble(0.8, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3Hits',
                'PhotonPtSumOutsideSignalCone'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByLooseChargedIsolation'),
            maximumAbsoluteValues = cms.vdouble(2.5),
            referenceRawIDNames = cms.vstring('ChargedIsoPtSum')
        ),
        cms.PSet(
            IDname = cms.string('ByPhotonPtSumOutsideSignalCone'),
            maximumRelativeValues = cms.vdouble(0.1),
            referenceRawIDNames = cms.vstring('PhotonPtSumOutsideSignalCone')
        )
    ),
    IDdefinitions = cms.VPSet(
        cms.PSet(
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            IDname = cms.string('ChargedIsoPtSum'),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByECALIsolation = cms.bool(True),
            IDname = cms.string('NeutralIsoPtSum'),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByWeightedECALIsolation = cms.bool(True),
            IDname = cms.string('NeutralIsoPtSumWeight'),
            UseAllPFCandsForWeights = cms.bool(True),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('TauFootprintCorrection'),
            storeRawFootprintCorrection = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('PhotonPtSumOutsideSignalCone'),
            storeRawPhotonSumPt_outsideSignalCone = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('PUcorrPtSum'),
            applyDeltaBetaCorrection = cms.bool(True),
            storeRawPUsumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByECALIsolation = cms.bool(True),
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            IDname = cms.string('ByRawCombinedIsolationDBSumPtCorr3Hits'),
            applyDeltaBetaCorrection = cms.bool(True),
            storeRawSumPt = cms.bool(True)
        )
    ),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    WeightECALIsolation = cms.double(1),
    applyFootprintCorrection = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    customOuterCone = cms.double(0.5),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.bool(True),
    deltaBetaPUTrackPtCutOverride_val = cms.double(0.5),
    footprintCorrections = cms.VPSet(
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 0')
        ),
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ),
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ),
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ),
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )
    ),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    mightGet = cms.optional.untracked.vstring,
    minTauPtForNoIso = cms.double(-99),
    particleFlowSrc = cms.InputTag("packedPFCandidates"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.hpsPFTauBasicDiscriminatorsBoosted = cms.EDProducer("PFRecoTauDiscriminationByIsolationContainer",
    IDWPdefinitions = cms.VPSet(
        cms.PSet(
            IDname = cms.string('ByLooseCombinedIsolationDBSumPtCorr3Hits'),
            maximumAbsoluteValues = cms.vdouble(2.5, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3Hits',
                'PhotonPtSumOutsideSignalCone'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByMediumCombinedIsolationDBSumPtCorr3Hits'),
            maximumAbsoluteValues = cms.vdouble(1.5, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3Hits',
                'PhotonPtSumOutsideSignalCone'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByTightCombinedIsolationDBSumPtCorr3Hits'),
            maximumAbsoluteValues = cms.vdouble(0.8, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3Hits',
                'PhotonPtSumOutsideSignalCone'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByLooseChargedIsolation'),
            maximumAbsoluteValues = cms.vdouble(2.5),
            referenceRawIDNames = cms.vstring('ChargedIsoPtSum')
        ),
        cms.PSet(
            IDname = cms.string('ByPhotonPtSumOutsideSignalCone'),
            maximumRelativeValues = cms.vdouble(0.1),
            referenceRawIDNames = cms.vstring('PhotonPtSumOutsideSignalCone')
        )
    ),
    IDdefinitions = cms.VPSet(
        cms.PSet(
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            IDname = cms.string('ChargedIsoPtSum'),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByECALIsolation = cms.bool(True),
            IDname = cms.string('NeutralIsoPtSum'),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByWeightedECALIsolation = cms.bool(True),
            IDname = cms.string('NeutralIsoPtSumWeight'),
            UseAllPFCandsForWeights = cms.bool(True),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('TauFootprintCorrection'),
            storeRawFootprintCorrection = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('PhotonPtSumOutsideSignalCone'),
            storeRawPhotonSumPt_outsideSignalCone = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('PUcorrPtSum'),
            applyDeltaBetaCorrection = cms.bool(True),
            storeRawPUsumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByECALIsolation = cms.bool(True),
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            IDname = cms.string('ByRawCombinedIsolationDBSumPtCorr3Hits'),
            applyDeltaBetaCorrection = cms.bool(True),
            storeRawSumPt = cms.bool(True)
        )
    ),
    PFTauProducer = cms.InputTag("hpsPFTauProducerBoosted"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsBoosted"),
            cut = cms.double(0.5)
        )
    ),
    WeightECALIsolation = cms.double(1),
    applyFootprintCorrection = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    customOuterCone = cms.double(0.5),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.bool(True),
    deltaBetaPUTrackPtCutOverride_val = cms.double(0.5),
    footprintCorrections = cms.VPSet(
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 0')
        ),
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ),
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ),
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ),
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )
    ),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    mightGet = cms.optional.untracked.vstring,
    minTauPtForNoIso = cms.double(-99),
    particleFlowSrc = cms.InputTag("packedPFCandidates"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.hpsPFTauBasicDiscriminatorsElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationByIsolationContainer",
    IDWPdefinitions = cms.VPSet(
        cms.PSet(
            IDname = cms.string('ByLooseCombinedIsolationDBSumPtCorr3Hits'),
            maximumAbsoluteValues = cms.vdouble(2.5, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3Hits',
                'PhotonPtSumOutsideSignalCone'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByMediumCombinedIsolationDBSumPtCorr3Hits'),
            maximumAbsoluteValues = cms.vdouble(1.5, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3Hits',
                'PhotonPtSumOutsideSignalCone'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByTightCombinedIsolationDBSumPtCorr3Hits'),
            maximumAbsoluteValues = cms.vdouble(0.8, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3Hits',
                'PhotonPtSumOutsideSignalCone'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByLooseChargedIsolation'),
            maximumAbsoluteValues = cms.vdouble(2.5),
            referenceRawIDNames = cms.vstring('ChargedIsoPtSum')
        ),
        cms.PSet(
            IDname = cms.string('ByPhotonPtSumOutsideSignalCone'),
            maximumRelativeValues = cms.vdouble(0.1),
            referenceRawIDNames = cms.vstring('PhotonPtSumOutsideSignalCone')
        )
    ),
    IDdefinitions = cms.VPSet(
        cms.PSet(
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            IDname = cms.string('ChargedIsoPtSum'),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByECALIsolation = cms.bool(True),
            IDname = cms.string('NeutralIsoPtSum'),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByWeightedECALIsolation = cms.bool(True),
            IDname = cms.string('NeutralIsoPtSumWeight'),
            UseAllPFCandsForWeights = cms.bool(True),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('TauFootprintCorrection'),
            storeRawFootprintCorrection = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('PhotonPtSumOutsideSignalCone'),
            storeRawPhotonSumPt_outsideSignalCone = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('PUcorrPtSum'),
            applyDeltaBetaCorrection = cms.bool(True),
            storeRawPUsumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByECALIsolation = cms.bool(True),
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            IDname = cms.string('ByRawCombinedIsolationDBSumPtCorr3Hits'),
            applyDeltaBetaCorrection = cms.bool(True),
            storeRawSumPt = cms.bool(True)
        )
    ),
    PFTauProducer = cms.InputTag("hpsPFTauProducerElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsElectronCleaned"),
            cut = cms.double(0.5)
        )
    ),
    WeightECALIsolation = cms.double(1),
    applyFootprintCorrection = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    customOuterCone = cms.double(0.5),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.bool(True),
    deltaBetaPUTrackPtCutOverride_val = cms.double(0.5),
    footprintCorrections = cms.VPSet(
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 0')
        ),
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ),
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ),
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ),
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )
    ),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    mightGet = cms.optional.untracked.vstring,
    minTauPtForNoIso = cms.double(-99),
    particleFlowSrc = cms.InputTag("PackedCandsElectronCleaned","packedPFCandidatesElectronCleaned"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.hpsPFTauBasicDiscriminatorsLowPtElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationByIsolationContainer",
    IDWPdefinitions = cms.VPSet(
        cms.PSet(
            IDname = cms.string('ByLooseCombinedIsolationDBSumPtCorr3Hits'),
            maximumAbsoluteValues = cms.vdouble(2.5, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3Hits',
                'PhotonPtSumOutsideSignalCone'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByMediumCombinedIsolationDBSumPtCorr3Hits'),
            maximumAbsoluteValues = cms.vdouble(1.5, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3Hits',
                'PhotonPtSumOutsideSignalCone'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByTightCombinedIsolationDBSumPtCorr3Hits'),
            maximumAbsoluteValues = cms.vdouble(0.8, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3Hits',
                'PhotonPtSumOutsideSignalCone'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByLooseChargedIsolation'),
            maximumAbsoluteValues = cms.vdouble(2.5),
            referenceRawIDNames = cms.vstring('ChargedIsoPtSum')
        ),
        cms.PSet(
            IDname = cms.string('ByPhotonPtSumOutsideSignalCone'),
            maximumRelativeValues = cms.vdouble(0.1),
            referenceRawIDNames = cms.vstring('PhotonPtSumOutsideSignalCone')
        )
    ),
    IDdefinitions = cms.VPSet(
        cms.PSet(
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            IDname = cms.string('ChargedIsoPtSum'),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByECALIsolation = cms.bool(True),
            IDname = cms.string('NeutralIsoPtSum'),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByWeightedECALIsolation = cms.bool(True),
            IDname = cms.string('NeutralIsoPtSumWeight'),
            UseAllPFCandsForWeights = cms.bool(True),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('TauFootprintCorrection'),
            storeRawFootprintCorrection = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('PhotonPtSumOutsideSignalCone'),
            storeRawPhotonSumPt_outsideSignalCone = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('PUcorrPtSum'),
            applyDeltaBetaCorrection = cms.bool(True),
            storeRawPUsumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByECALIsolation = cms.bool(True),
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            IDname = cms.string('ByRawCombinedIsolationDBSumPtCorr3Hits'),
            applyDeltaBetaCorrection = cms.bool(True),
            storeRawSumPt = cms.bool(True)
        )
    ),
    PFTauProducer = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsLowPtElectronCleaned"),
            cut = cms.double(0.5)
        )
    ),
    WeightECALIsolation = cms.double(1),
    applyFootprintCorrection = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    customOuterCone = cms.double(0.5),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.bool(True),
    deltaBetaPUTrackPtCutOverride_val = cms.double(0.5),
    footprintCorrections = cms.VPSet(
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 0')
        ),
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ),
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ),
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ),
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )
    ),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    mightGet = cms.optional.untracked.vstring,
    minTauPtForNoIso = cms.double(-99),
    particleFlowSrc = cms.InputTag("PackedCandsLowPtElectronCleaned","packedPFCandidatesLowPtElectronCleaned"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.hpsPFTauBasicDiscriminatorsMuonCleaned = cms.EDProducer("PFRecoTauDiscriminationByIsolationContainer",
    IDWPdefinitions = cms.VPSet(
        cms.PSet(
            IDname = cms.string('ByLooseCombinedIsolationDBSumPtCorr3Hits'),
            maximumAbsoluteValues = cms.vdouble(2.5, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3Hits',
                'PhotonPtSumOutsideSignalCone'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByMediumCombinedIsolationDBSumPtCorr3Hits'),
            maximumAbsoluteValues = cms.vdouble(1.5, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3Hits',
                'PhotonPtSumOutsideSignalCone'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByTightCombinedIsolationDBSumPtCorr3Hits'),
            maximumAbsoluteValues = cms.vdouble(0.8, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3Hits',
                'PhotonPtSumOutsideSignalCone'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByLooseChargedIsolation'),
            maximumAbsoluteValues = cms.vdouble(2.5),
            referenceRawIDNames = cms.vstring('ChargedIsoPtSum')
        ),
        cms.PSet(
            IDname = cms.string('ByPhotonPtSumOutsideSignalCone'),
            maximumRelativeValues = cms.vdouble(0.1),
            referenceRawIDNames = cms.vstring('PhotonPtSumOutsideSignalCone')
        )
    ),
    IDdefinitions = cms.VPSet(
        cms.PSet(
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            IDname = cms.string('ChargedIsoPtSum'),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByECALIsolation = cms.bool(True),
            IDname = cms.string('NeutralIsoPtSum'),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByWeightedECALIsolation = cms.bool(True),
            IDname = cms.string('NeutralIsoPtSumWeight'),
            UseAllPFCandsForWeights = cms.bool(True),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('TauFootprintCorrection'),
            storeRawFootprintCorrection = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('PhotonPtSumOutsideSignalCone'),
            storeRawPhotonSumPt_outsideSignalCone = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('PUcorrPtSum'),
            applyDeltaBetaCorrection = cms.bool(True),
            storeRawPUsumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByECALIsolation = cms.bool(True),
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            IDname = cms.string('ByRawCombinedIsolationDBSumPtCorr3Hits'),
            applyDeltaBetaCorrection = cms.bool(True),
            storeRawSumPt = cms.bool(True)
        )
    ),
    PFTauProducer = cms.InputTag("hpsPFTauProducerMuonCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsMuonCleaned"),
            cut = cms.double(0.5)
        )
    ),
    WeightECALIsolation = cms.double(1),
    applyFootprintCorrection = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    customOuterCone = cms.double(0.5),
    deltaBetaFactor = cms.string('0.2000'),
    deltaBetaPUTrackPtCutOverride = cms.bool(True),
    deltaBetaPUTrackPtCutOverride_val = cms.double(0.5),
    footprintCorrections = cms.VPSet(
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 0')
        ),
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ),
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ),
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ),
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )
    ),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    mightGet = cms.optional.untracked.vstring,
    minTauPtForNoIso = cms.double(-99),
    particleFlowSrc = cms.InputTag("PackedCandsMuonCleaned","packedPFCandidatesMuonCleaned"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.hpsPFTauBasicDiscriminatorsdR03 = cms.EDProducer("PFRecoTauDiscriminationByIsolationContainer",
    IDWPdefinitions = cms.VPSet(
        cms.PSet(
            IDname = cms.string('ByLooseCombinedIsolationDBSumPtCorr3HitsdR03'),
            maximumAbsoluteValues = cms.vdouble(2.5, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3HitsdR03',
                'PhotonPtSumOutsideSignalConedR03'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByMediumCombinedIsolationDBSumPtCorr3HitsdR03'),
            maximumAbsoluteValues = cms.vdouble(1.5, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3HitsdR03',
                'PhotonPtSumOutsideSignalConedR03'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByTightCombinedIsolationDBSumPtCorr3HitsdR03'),
            maximumAbsoluteValues = cms.vdouble(0.8, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3HitsdR03',
                'PhotonPtSumOutsideSignalConedR03'
            )
        )
    ),
    IDdefinitions = cms.VPSet(
        cms.PSet(
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            IDname = cms.string('ChargedIsoPtSumdR03'),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByECALIsolation = cms.bool(True),
            IDname = cms.string('NeutralIsoPtSumdR03'),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByWeightedECALIsolation = cms.bool(True),
            IDname = cms.string('NeutralIsoPtSumWeightdR03'),
            UseAllPFCandsForWeights = cms.bool(True),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('TauFootprintCorrectiondR03'),
            storeRawFootprintCorrection = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('PhotonPtSumOutsideSignalConedR03'),
            storeRawPhotonSumPt_outsideSignalCone = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('PUcorrPtSumdR03'),
            applyDeltaBetaCorrection = cms.bool(True),
            storeRawPUsumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByECALIsolation = cms.bool(True),
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            IDname = cms.string('ByRawCombinedIsolationDBSumPtCorr3HitsdR03'),
            applyDeltaBetaCorrection = cms.bool(True),
            storeRawSumPt = cms.bool(True)
        )
    ),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    WeightECALIsolation = cms.double(1),
    applyFootprintCorrection = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    customOuterCone = cms.double(0.3),
    deltaBetaFactor = cms.string('0.0720'),
    deltaBetaPUTrackPtCutOverride = cms.bool(True),
    deltaBetaPUTrackPtCutOverride_val = cms.double(0.5),
    footprintCorrections = cms.VPSet(
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 0')
        ),
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ),
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ),
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ),
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )
    ),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    mightGet = cms.optional.untracked.vstring,
    minTauPtForNoIso = cms.double(-99),
    particleFlowSrc = cms.InputTag("packedPFCandidates"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.hpsPFTauBasicDiscriminatorsdR03Boosted = cms.EDProducer("PFRecoTauDiscriminationByIsolationContainer",
    IDWPdefinitions = cms.VPSet(
        cms.PSet(
            IDname = cms.string('ByLooseCombinedIsolationDBSumPtCorr3HitsdR03'),
            maximumAbsoluteValues = cms.vdouble(2.5, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3HitsdR03',
                'PhotonPtSumOutsideSignalConedR03'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByMediumCombinedIsolationDBSumPtCorr3HitsdR03'),
            maximumAbsoluteValues = cms.vdouble(1.5, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3HitsdR03',
                'PhotonPtSumOutsideSignalConedR03'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByTightCombinedIsolationDBSumPtCorr3HitsdR03'),
            maximumAbsoluteValues = cms.vdouble(0.8, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3HitsdR03',
                'PhotonPtSumOutsideSignalConedR03'
            )
        )
    ),
    IDdefinitions = cms.VPSet(
        cms.PSet(
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            IDname = cms.string('ChargedIsoPtSumdR03'),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByECALIsolation = cms.bool(True),
            IDname = cms.string('NeutralIsoPtSumdR03'),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByWeightedECALIsolation = cms.bool(True),
            IDname = cms.string('NeutralIsoPtSumWeightdR03'),
            UseAllPFCandsForWeights = cms.bool(True),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('TauFootprintCorrectiondR03'),
            storeRawFootprintCorrection = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('PhotonPtSumOutsideSignalConedR03'),
            storeRawPhotonSumPt_outsideSignalCone = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('PUcorrPtSumdR03'),
            applyDeltaBetaCorrection = cms.bool(True),
            storeRawPUsumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByECALIsolation = cms.bool(True),
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            IDname = cms.string('ByRawCombinedIsolationDBSumPtCorr3HitsdR03'),
            applyDeltaBetaCorrection = cms.bool(True),
            storeRawSumPt = cms.bool(True)
        )
    ),
    PFTauProducer = cms.InputTag("hpsPFTauProducerBoosted"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsBoosted"),
            cut = cms.double(0.5)
        )
    ),
    WeightECALIsolation = cms.double(1),
    applyFootprintCorrection = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    customOuterCone = cms.double(0.3),
    deltaBetaFactor = cms.string('0.0720'),
    deltaBetaPUTrackPtCutOverride = cms.bool(True),
    deltaBetaPUTrackPtCutOverride_val = cms.double(0.5),
    footprintCorrections = cms.VPSet(
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 0')
        ),
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ),
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ),
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ),
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )
    ),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    mightGet = cms.optional.untracked.vstring,
    minTauPtForNoIso = cms.double(-99),
    particleFlowSrc = cms.InputTag("packedPFCandidates"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.hpsPFTauBasicDiscriminatorsdR03ElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationByIsolationContainer",
    IDWPdefinitions = cms.VPSet(
        cms.PSet(
            IDname = cms.string('ByLooseCombinedIsolationDBSumPtCorr3HitsdR03'),
            maximumAbsoluteValues = cms.vdouble(2.5, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3HitsdR03',
                'PhotonPtSumOutsideSignalConedR03'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByMediumCombinedIsolationDBSumPtCorr3HitsdR03'),
            maximumAbsoluteValues = cms.vdouble(1.5, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3HitsdR03',
                'PhotonPtSumOutsideSignalConedR03'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByTightCombinedIsolationDBSumPtCorr3HitsdR03'),
            maximumAbsoluteValues = cms.vdouble(0.8, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3HitsdR03',
                'PhotonPtSumOutsideSignalConedR03'
            )
        )
    ),
    IDdefinitions = cms.VPSet(
        cms.PSet(
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            IDname = cms.string('ChargedIsoPtSumdR03'),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByECALIsolation = cms.bool(True),
            IDname = cms.string('NeutralIsoPtSumdR03'),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByWeightedECALIsolation = cms.bool(True),
            IDname = cms.string('NeutralIsoPtSumWeightdR03'),
            UseAllPFCandsForWeights = cms.bool(True),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('TauFootprintCorrectiondR03'),
            storeRawFootprintCorrection = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('PhotonPtSumOutsideSignalConedR03'),
            storeRawPhotonSumPt_outsideSignalCone = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('PUcorrPtSumdR03'),
            applyDeltaBetaCorrection = cms.bool(True),
            storeRawPUsumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByECALIsolation = cms.bool(True),
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            IDname = cms.string('ByRawCombinedIsolationDBSumPtCorr3HitsdR03'),
            applyDeltaBetaCorrection = cms.bool(True),
            storeRawSumPt = cms.bool(True)
        )
    ),
    PFTauProducer = cms.InputTag("hpsPFTauProducerElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsElectronCleaned"),
            cut = cms.double(0.5)
        )
    ),
    WeightECALIsolation = cms.double(1),
    applyFootprintCorrection = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    customOuterCone = cms.double(0.3),
    deltaBetaFactor = cms.string('0.0720'),
    deltaBetaPUTrackPtCutOverride = cms.bool(True),
    deltaBetaPUTrackPtCutOverride_val = cms.double(0.5),
    footprintCorrections = cms.VPSet(
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 0')
        ),
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ),
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ),
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ),
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )
    ),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    mightGet = cms.optional.untracked.vstring,
    minTauPtForNoIso = cms.double(-99),
    particleFlowSrc = cms.InputTag("PackedCandsElectronCleaned","packedPFCandidatesElectronCleaned"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.hpsPFTauBasicDiscriminatorsdR03LowPtElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationByIsolationContainer",
    IDWPdefinitions = cms.VPSet(
        cms.PSet(
            IDname = cms.string('ByLooseCombinedIsolationDBSumPtCorr3HitsdR03'),
            maximumAbsoluteValues = cms.vdouble(2.5, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3HitsdR03',
                'PhotonPtSumOutsideSignalConedR03'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByMediumCombinedIsolationDBSumPtCorr3HitsdR03'),
            maximumAbsoluteValues = cms.vdouble(1.5, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3HitsdR03',
                'PhotonPtSumOutsideSignalConedR03'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByTightCombinedIsolationDBSumPtCorr3HitsdR03'),
            maximumAbsoluteValues = cms.vdouble(0.8, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3HitsdR03',
                'PhotonPtSumOutsideSignalConedR03'
            )
        )
    ),
    IDdefinitions = cms.VPSet(
        cms.PSet(
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            IDname = cms.string('ChargedIsoPtSumdR03'),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByECALIsolation = cms.bool(True),
            IDname = cms.string('NeutralIsoPtSumdR03'),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByWeightedECALIsolation = cms.bool(True),
            IDname = cms.string('NeutralIsoPtSumWeightdR03'),
            UseAllPFCandsForWeights = cms.bool(True),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('TauFootprintCorrectiondR03'),
            storeRawFootprintCorrection = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('PhotonPtSumOutsideSignalConedR03'),
            storeRawPhotonSumPt_outsideSignalCone = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('PUcorrPtSumdR03'),
            applyDeltaBetaCorrection = cms.bool(True),
            storeRawPUsumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByECALIsolation = cms.bool(True),
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            IDname = cms.string('ByRawCombinedIsolationDBSumPtCorr3HitsdR03'),
            applyDeltaBetaCorrection = cms.bool(True),
            storeRawSumPt = cms.bool(True)
        )
    ),
    PFTauProducer = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsLowPtElectronCleaned"),
            cut = cms.double(0.5)
        )
    ),
    WeightECALIsolation = cms.double(1),
    applyFootprintCorrection = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    customOuterCone = cms.double(0.3),
    deltaBetaFactor = cms.string('0.0720'),
    deltaBetaPUTrackPtCutOverride = cms.bool(True),
    deltaBetaPUTrackPtCutOverride_val = cms.double(0.5),
    footprintCorrections = cms.VPSet(
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 0')
        ),
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ),
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ),
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ),
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )
    ),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    mightGet = cms.optional.untracked.vstring,
    minTauPtForNoIso = cms.double(-99),
    particleFlowSrc = cms.InputTag("PackedCandsLowPtElectronCleaned","packedPFCandidatesLowPtElectronCleaned"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.hpsPFTauBasicDiscriminatorsdR03MuonCleaned = cms.EDProducer("PFRecoTauDiscriminationByIsolationContainer",
    IDWPdefinitions = cms.VPSet(
        cms.PSet(
            IDname = cms.string('ByLooseCombinedIsolationDBSumPtCorr3HitsdR03'),
            maximumAbsoluteValues = cms.vdouble(2.5, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3HitsdR03',
                'PhotonPtSumOutsideSignalConedR03'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByMediumCombinedIsolationDBSumPtCorr3HitsdR03'),
            maximumAbsoluteValues = cms.vdouble(1.5, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3HitsdR03',
                'PhotonPtSumOutsideSignalConedR03'
            )
        ),
        cms.PSet(
            IDname = cms.string('ByTightCombinedIsolationDBSumPtCorr3HitsdR03'),
            maximumAbsoluteValues = cms.vdouble(0.8, 1000000000.0),
            maximumRelativeValues = cms.vdouble(-1.0, 0.1),
            referenceRawIDNames = cms.vstring(
                'ByRawCombinedIsolationDBSumPtCorr3HitsdR03',
                'PhotonPtSumOutsideSignalConedR03'
            )
        )
    ),
    IDdefinitions = cms.VPSet(
        cms.PSet(
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            IDname = cms.string('ChargedIsoPtSumdR03'),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByECALIsolation = cms.bool(True),
            IDname = cms.string('NeutralIsoPtSumdR03'),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByWeightedECALIsolation = cms.bool(True),
            IDname = cms.string('NeutralIsoPtSumWeightdR03'),
            UseAllPFCandsForWeights = cms.bool(True),
            storeRawSumPt = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('TauFootprintCorrectiondR03'),
            storeRawFootprintCorrection = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('PhotonPtSumOutsideSignalConedR03'),
            storeRawPhotonSumPt_outsideSignalCone = cms.bool(True)
        ),
        cms.PSet(
            IDname = cms.string('PUcorrPtSumdR03'),
            applyDeltaBetaCorrection = cms.bool(True),
            storeRawPUsumPt = cms.bool(True)
        ),
        cms.PSet(
            ApplyDiscriminationByECALIsolation = cms.bool(True),
            ApplyDiscriminationByTrackerIsolation = cms.bool(True),
            IDname = cms.string('ByRawCombinedIsolationDBSumPtCorr3HitsdR03'),
            applyDeltaBetaCorrection = cms.bool(True),
            storeRawSumPt = cms.bool(True)
        )
    ),
    PFTauProducer = cms.InputTag("hpsPFTauProducerMuonCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsMuonCleaned"),
            cut = cms.double(0.5)
        )
    ),
    WeightECALIsolation = cms.double(1),
    applyFootprintCorrection = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    customOuterCone = cms.double(0.3),
    deltaBetaFactor = cms.string('0.0720'),
    deltaBetaPUTrackPtCutOverride = cms.bool(True),
    deltaBetaPUTrackPtCutOverride_val = cms.double(0.5),
    footprintCorrections = cms.VPSet(
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 0')
        ),
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ),
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ),
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ),
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )
    ),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    mightGet = cms.optional.untracked.vstring,
    minTauPtForNoIso = cms.double(-99),
    particleFlowSrc = cms.InputTag("PackedCandsMuonCleaned","packedPFCandidatesMuonCleaned"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.hpsPFTauDiscriminationByDeadECALElectronRejection = cms.EDProducer("PFRecoTauDiscriminationAgainstElectronDeadECAL",
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    dR = cms.double(0.08),
    extrapolateToECalEntrance = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    minStatus = cms.uint32(12),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByDeadECALElectronRejectionBoosted = cms.EDProducer("PFRecoTauDiscriminationAgainstElectronDeadECAL",
    PFTauProducer = cms.InputTag("hpsPFTauProducerBoosted"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsBoosted"),
            cut = cms.double(0.5)
        )
    ),
    dR = cms.double(0.08),
    extrapolateToECalEntrance = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    minStatus = cms.uint32(12),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByDeadECALElectronRejectionElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationAgainstElectronDeadECAL",
    PFTauProducer = cms.InputTag("hpsPFTauProducerElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsElectronCleaned"),
            cut = cms.double(0.5)
        )
    ),
    dR = cms.double(0.08),
    extrapolateToECalEntrance = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    minStatus = cms.uint32(12),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByDeadECALElectronRejectionLowPtElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationAgainstElectronDeadECAL",
    PFTauProducer = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsLowPtElectronCleaned"),
            cut = cms.double(0.5)
        )
    ),
    dR = cms.double(0.08),
    extrapolateToECalEntrance = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    minStatus = cms.uint32(12),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByDeadECALElectronRejectionMuonCleaned = cms.EDProducer("PFRecoTauDiscriminationAgainstElectronDeadECAL",
    PFTauProducer = cms.InputTag("hpsPFTauProducerMuonCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsMuonCleaned"),
            cut = cms.double(0.5)
        )
    ),
    dR = cms.double(0.08),
    extrapolateToECalEntrance = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    minStatus = cms.uint32(12),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByDecayModeFinding = cms.EDProducer("PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    decayModes = cms.VPSet(
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(-1000.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.1349),
            maxMass = cms.string('max(1.3, min(1.3*sqrt(pt/100.), 4.2))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.3),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(0.2),
            minMass = cms.double(0.4),
            minPi0Mass = cms.double(0.05),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(2),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.5'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.8),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        )
    ),
    matchingCone = cms.double(0.5),
    minPixelHits = cms.int32(1),
    minTauPt = cms.double(0.0),
    requireTauChargedHadronsToBeChargedPFCands = cms.bool(True),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByDecayModeFindingBoosted = cms.EDProducer("PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag("hpsPFTauProducerBoosted"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    decayModes = cms.VPSet(
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(-1000.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.1349),
            maxMass = cms.string('max(1.3, min(1.3*sqrt(pt/100.), 4.2))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.3),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(0.2),
            minMass = cms.double(0.4),
            minPi0Mass = cms.double(0.05),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(2),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.5'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.8),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        )
    ),
    matchingCone = cms.double(0.5),
    minPixelHits = cms.int32(1),
    minTauPt = cms.double(0.0),
    requireTauChargedHadronsToBeChargedPFCands = cms.bool(True),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByDecayModeFindingElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag("hpsPFTauProducerElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    decayModes = cms.VPSet(
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(-1000.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.1349),
            maxMass = cms.string('max(1.3, min(1.3*sqrt(pt/100.), 4.2))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.3),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(0.2),
            minMass = cms.double(0.4),
            minPi0Mass = cms.double(0.05),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(2),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.5'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.8),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        )
    ),
    matchingCone = cms.double(0.5),
    minPixelHits = cms.int32(1),
    minTauPt = cms.double(0.0),
    requireTauChargedHadronsToBeChargedPFCands = cms.bool(True),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByDecayModeFindingLowPtElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    decayModes = cms.VPSet(
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(-1000.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.1349),
            maxMass = cms.string('max(1.3, min(1.3*sqrt(pt/100.), 4.2))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.3),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(0.2),
            minMass = cms.double(0.4),
            minPi0Mass = cms.double(0.05),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(2),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.5'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.8),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        )
    ),
    matchingCone = cms.double(0.5),
    minPixelHits = cms.int32(1),
    minTauPt = cms.double(0.0),
    requireTauChargedHadronsToBeChargedPFCands = cms.bool(True),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByDecayModeFindingMuonCleaned = cms.EDProducer("PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag("hpsPFTauProducerMuonCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    decayModes = cms.VPSet(
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(-1000.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.1349),
            maxMass = cms.string('max(1.3, min(1.3*sqrt(pt/100.), 4.2))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.3),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(0.2),
            minMass = cms.double(0.4),
            minPi0Mass = cms.double(0.05),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(2),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.5'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.8),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        )
    ),
    matchingCone = cms.double(0.5),
    minPixelHits = cms.int32(1),
    minTauPt = cms.double(0.0),
    requireTauChargedHadronsToBeChargedPFCands = cms.bool(True),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByDecayModeFindingNewDMs = cms.EDProducer("PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    decayModes = cms.VPSet(
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(-1000.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.1349),
            maxMass = cms.string('max(1.3, min(1.3*sqrt(pt/100.), 4.2))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.3),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(0.2),
            minMass = cms.double(0.4),
            minPi0Mass = cms.double(0.05),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(2),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.2'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(2),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(2),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.5'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.8),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.6'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.9),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(2)
        )
    ),
    matchingCone = cms.double(0.5),
    minPixelHits = cms.int32(1),
    minTauPt = cms.double(0.0),
    requireTauChargedHadronsToBeChargedPFCands = cms.bool(False),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByDecayModeFindingNewDMsBoosted = cms.EDProducer("PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag("hpsPFTauProducerBoosted"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    decayModes = cms.VPSet(
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(-1000.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.1349),
            maxMass = cms.string('max(1.3, min(1.3*sqrt(pt/100.), 4.2))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.3),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(0.2),
            minMass = cms.double(0.4),
            minPi0Mass = cms.double(0.05),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(2),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.2'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(2),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(2),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.5'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.8),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.6'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.9),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(2)
        )
    ),
    matchingCone = cms.double(0.5),
    minPixelHits = cms.int32(1),
    minTauPt = cms.double(0.0),
    requireTauChargedHadronsToBeChargedPFCands = cms.bool(False),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByDecayModeFindingNewDMsElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag("hpsPFTauProducerElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    decayModes = cms.VPSet(
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(-1000.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.1349),
            maxMass = cms.string('max(1.3, min(1.3*sqrt(pt/100.), 4.2))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.3),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(0.2),
            minMass = cms.double(0.4),
            minPi0Mass = cms.double(0.05),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(2),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.2'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(2),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(2),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.5'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.8),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.6'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.9),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(2)
        )
    ),
    matchingCone = cms.double(0.5),
    minPixelHits = cms.int32(1),
    minTauPt = cms.double(0.0),
    requireTauChargedHadronsToBeChargedPFCands = cms.bool(False),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByDecayModeFindingNewDMsLowPtElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    decayModes = cms.VPSet(
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(-1000.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.1349),
            maxMass = cms.string('max(1.3, min(1.3*sqrt(pt/100.), 4.2))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.3),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(0.2),
            minMass = cms.double(0.4),
            minPi0Mass = cms.double(0.05),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(2),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.2'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(2),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(2),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.5'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.8),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.6'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.9),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(2)
        )
    ),
    matchingCone = cms.double(0.5),
    minPixelHits = cms.int32(1),
    minTauPt = cms.double(0.0),
    requireTauChargedHadronsToBeChargedPFCands = cms.bool(False),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByDecayModeFindingNewDMsMuonCleaned = cms.EDProducer("PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag("hpsPFTauProducerMuonCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    decayModes = cms.VPSet(
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(-1000.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.1349),
            maxMass = cms.string('max(1.3, min(1.3*sqrt(pt/100.), 4.2))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.3),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(0.2),
            minMass = cms.double(0.4),
            minPi0Mass = cms.double(0.05),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(2),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.2'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(2),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(2),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.5'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.8),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.6'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.9),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(2)
        )
    ),
    matchingCone = cms.double(0.5),
    minPixelHits = cms.int32(1),
    minTauPt = cms.double(0.0),
    requireTauChargedHadronsToBeChargedPFCands = cms.bool(False),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByDecayModeFindingOldDMs = cms.EDProducer("PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    decayModes = cms.VPSet(
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(-1000.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.1349),
            maxMass = cms.string('max(1.3, min(1.3*sqrt(pt/100.), 4.2))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.3),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(0.2),
            minMass = cms.double(0.4),
            minPi0Mass = cms.double(0.05),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(2),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.5'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.8),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        )
    ),
    matchingCone = cms.double(0.5),
    minPixelHits = cms.int32(1),
    minTauPt = cms.double(0.0),
    requireTauChargedHadronsToBeChargedPFCands = cms.bool(True),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByDecayModeFindingOldDMsBoosted = cms.EDProducer("PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag("hpsPFTauProducerBoosted"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    decayModes = cms.VPSet(
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(-1000.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.1349),
            maxMass = cms.string('max(1.3, min(1.3*sqrt(pt/100.), 4.2))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.3),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(0.2),
            minMass = cms.double(0.4),
            minPi0Mass = cms.double(0.05),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(2),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.5'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.8),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        )
    ),
    matchingCone = cms.double(0.5),
    minPixelHits = cms.int32(1),
    minTauPt = cms.double(0.0),
    requireTauChargedHadronsToBeChargedPFCands = cms.bool(True),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByDecayModeFindingOldDMsElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag("hpsPFTauProducerElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    decayModes = cms.VPSet(
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(-1000.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.1349),
            maxMass = cms.string('max(1.3, min(1.3*sqrt(pt/100.), 4.2))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.3),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(0.2),
            minMass = cms.double(0.4),
            minPi0Mass = cms.double(0.05),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(2),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.5'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.8),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        )
    ),
    matchingCone = cms.double(0.5),
    minPixelHits = cms.int32(1),
    minTauPt = cms.double(0.0),
    requireTauChargedHadronsToBeChargedPFCands = cms.bool(True),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByDecayModeFindingOldDMsLowPtElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    decayModes = cms.VPSet(
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(-1000.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.1349),
            maxMass = cms.string('max(1.3, min(1.3*sqrt(pt/100.), 4.2))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.3),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(0.2),
            minMass = cms.double(0.4),
            minPi0Mass = cms.double(0.05),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(2),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.5'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.8),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        )
    ),
    matchingCone = cms.double(0.5),
    minPixelHits = cms.int32(1),
    minTauPt = cms.double(0.0),
    requireTauChargedHadronsToBeChargedPFCands = cms.bool(True),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByDecayModeFindingOldDMsMuonCleaned = cms.EDProducer("PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag("hpsPFTauProducerMuonCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    decayModes = cms.VPSet(
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(-1000.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.1349),
            maxMass = cms.string('max(1.3, min(1.3*sqrt(pt/100.), 4.2))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.3),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(0.2),
            minMass = cms.double(0.4),
            minPi0Mass = cms.double(0.05),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(2),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.5'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.8),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        )
    ),
    matchingCone = cms.double(0.5),
    minPixelHits = cms.int32(1),
    minTauPt = cms.double(0.0),
    requireTauChargedHadronsToBeChargedPFCands = cms.bool(True),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT = cms.EDProducer("RecoTauDiscriminantCutMultiplexer",
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT'),
        variable = cms.string('pt')
    )),
    mightGet = cms.optional.untracked.vstring,
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT_mvaOutput_normalization'),
    rawValues = cms.vstring('discriminator'),
    toMultiplex = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_VVLoose',
        '_VLoose',
        '_Loose',
        '_Medium',
        '_Tight',
        '_VTight',
        '_VVTight'
    )
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTBoosted = cms.EDProducer("RecoTauDiscriminantCutMultiplexer",
    PFTauProducer = cms.InputTag("hpsPFTauProducerBoosted"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsBoosted"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT'),
        variable = cms.string('pt')
    )),
    mightGet = cms.optional.untracked.vstring,
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT_mvaOutput_normalization'),
    rawValues = cms.vstring('discriminator'),
    toMultiplex = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTrawBoosted"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_VVLoose',
        '_VLoose',
        '_Loose',
        '_Medium',
        '_Tight',
        '_VTight',
        '_VVTight'
    )
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTElectronCleaned = cms.EDProducer("RecoTauDiscriminantCutMultiplexer",
    PFTauProducer = cms.InputTag("hpsPFTauProducerElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsElectronCleaned"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT'),
        variable = cms.string('pt')
    )),
    mightGet = cms.optional.untracked.vstring,
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT_mvaOutput_normalization'),
    rawValues = cms.vstring('discriminator'),
    toMultiplex = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTrawElectronCleaned"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_VVLoose',
        '_VLoose',
        '_Loose',
        '_Medium',
        '_Tight',
        '_VTight',
        '_VVTight'
    )
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTLowPtElectronCleaned = cms.EDProducer("RecoTauDiscriminantCutMultiplexer",
    PFTauProducer = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsLowPtElectronCleaned"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT'),
        variable = cms.string('pt')
    )),
    mightGet = cms.optional.untracked.vstring,
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT_mvaOutput_normalization'),
    rawValues = cms.vstring('discriminator'),
    toMultiplex = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTrawLowPtElectronCleaned"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_VVLoose',
        '_VLoose',
        '_Loose',
        '_Medium',
        '_Tight',
        '_VTight',
        '_VVTight'
    )
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTMuonCleaned = cms.EDProducer("RecoTauDiscriminantCutMultiplexer",
    PFTauProducer = cms.InputTag("hpsPFTauProducerMuonCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsMuonCleaned"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT'),
        variable = cms.string('pt')
    )),
    mightGet = cms.optional.untracked.vstring,
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT_mvaOutput_normalization'),
    rawValues = cms.vstring('discriminator'),
    toMultiplex = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTrawMuonCleaned"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_VVLoose',
        '_VLoose',
        '_Loose',
        '_Medium',
        '_Tight',
        '_VTight',
        '_VVTight'
    )
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw = cms.EDProducer("PFRecoTauDiscriminationByMVAIsolationRun2",
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.optional.FileInPath,
    inputIDNameSuffix = cms.string('dR03'),
    loadMVAfromDB = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    mvaName = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT'),
    mvaOpt = cms.string('DBoldDMwLTwGJ'),
    srcBasicTauDiscriminators = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03"),
    srcTauTransverseImpactParameters = cms.InputTag("hpsPFTauTransverseImpactParameters"),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTrawBoosted = cms.EDProducer("PFRecoTauDiscriminationByMVAIsolationRun2",
    PFTauProducer = cms.InputTag("hpsPFTauProducerBoosted"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsBoosted"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.optional.FileInPath,
    inputIDNameSuffix = cms.string('dR03'),
    loadMVAfromDB = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    mvaName = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT'),
    mvaOpt = cms.string('DBoldDMwLTwGJ'),
    srcBasicTauDiscriminators = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03Boosted"),
    srcTauTransverseImpactParameters = cms.InputTag("hpsPFTauTransverseImpactParametersBoosted"),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTrawElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationByMVAIsolationRun2",
    PFTauProducer = cms.InputTag("hpsPFTauProducerElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsElectronCleaned"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.optional.FileInPath,
    inputIDNameSuffix = cms.string('dR03'),
    loadMVAfromDB = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    mvaName = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT'),
    mvaOpt = cms.string('DBoldDMwLTwGJ'),
    srcBasicTauDiscriminators = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03ElectronCleaned"),
    srcTauTransverseImpactParameters = cms.InputTag("hpsPFTauTransverseImpactParametersElectronCleaned"),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTrawLowPtElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationByMVAIsolationRun2",
    PFTauProducer = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsLowPtElectronCleaned"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.optional.FileInPath,
    inputIDNameSuffix = cms.string('dR03'),
    loadMVAfromDB = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    mvaName = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT'),
    mvaOpt = cms.string('DBoldDMwLTwGJ'),
    srcBasicTauDiscriminators = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03LowPtElectronCleaned"),
    srcTauTransverseImpactParameters = cms.InputTag("hpsPFTauTransverseImpactParametersLowPtElectronCleaned"),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTrawMuonCleaned = cms.EDProducer("PFRecoTauDiscriminationByMVAIsolationRun2",
    PFTauProducer = cms.InputTag("hpsPFTauProducerMuonCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsMuonCleaned"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.optional.FileInPath,
    inputIDNameSuffix = cms.string('dR03'),
    loadMVAfromDB = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    mvaName = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT'),
    mvaOpt = cms.string('DBoldDMwLTwGJ'),
    srcBasicTauDiscriminators = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03MuonCleaned"),
    srcTauTransverseImpactParameters = cms.InputTag("hpsPFTauTransverseImpactParametersMuonCleaned"),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT = cms.EDProducer("RecoTauDiscriminantCutMultiplexer",
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT'),
        variable = cms.string('pt')
    )),
    mightGet = cms.optional.untracked.vstring,
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT_mvaOutput_normalization'),
    rawValues = cms.vstring('discriminator'),
    toMultiplex = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_VVLoose',
        '_VLoose',
        '_Loose',
        '_Medium',
        '_Tight',
        '_VTight',
        '_VVTight'
    )
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTBoosted = cms.EDProducer("RecoTauDiscriminantCutMultiplexer",
    PFTauProducer = cms.InputTag("hpsPFTauProducerBoosted"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsBoosted"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT'),
        variable = cms.string('pt')
    )),
    mightGet = cms.optional.untracked.vstring,
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT_mvaOutput_normalization'),
    rawValues = cms.vstring('discriminator'),
    toMultiplex = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTrawBoosted"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_VVLoose',
        '_VLoose',
        '_Loose',
        '_Medium',
        '_Tight',
        '_VTight',
        '_VVTight'
    )
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTElectronCleaned = cms.EDProducer("RecoTauDiscriminantCutMultiplexer",
    PFTauProducer = cms.InputTag("hpsPFTauProducerElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsElectronCleaned"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT'),
        variable = cms.string('pt')
    )),
    mightGet = cms.optional.untracked.vstring,
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT_mvaOutput_normalization'),
    rawValues = cms.vstring('discriminator'),
    toMultiplex = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTrawElectronCleaned"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_VVLoose',
        '_VLoose',
        '_Loose',
        '_Medium',
        '_Tight',
        '_VTight',
        '_VVTight'
    )
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTLowPtElectronCleaned = cms.EDProducer("RecoTauDiscriminantCutMultiplexer",
    PFTauProducer = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsLowPtElectronCleaned"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT'),
        variable = cms.string('pt')
    )),
    mightGet = cms.optional.untracked.vstring,
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT_mvaOutput_normalization'),
    rawValues = cms.vstring('discriminator'),
    toMultiplex = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTrawLowPtElectronCleaned"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_VVLoose',
        '_VLoose',
        '_Loose',
        '_Medium',
        '_Tight',
        '_VTight',
        '_VVTight'
    )
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTMuonCleaned = cms.EDProducer("RecoTauDiscriminantCutMultiplexer",
    PFTauProducer = cms.InputTag("hpsPFTauProducerMuonCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsMuonCleaned"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT'),
        variable = cms.string('pt')
    )),
    mightGet = cms.optional.untracked.vstring,
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT_mvaOutput_normalization'),
    rawValues = cms.vstring('discriminator'),
    toMultiplex = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTrawMuonCleaned"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_VVLoose',
        '_VLoose',
        '_Loose',
        '_Medium',
        '_Tight',
        '_VTight',
        '_VVTight'
    )
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw = cms.EDProducer("PFRecoTauDiscriminationByMVAIsolationRun2",
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.optional.FileInPath,
    inputIDNameSuffix = cms.string(''),
    loadMVAfromDB = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    mvaName = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT'),
    mvaOpt = cms.string('DBnewDMwLTwGJ'),
    srcBasicTauDiscriminators = cms.InputTag("hpsPFTauBasicDiscriminators"),
    srcTauTransverseImpactParameters = cms.InputTag("hpsPFTauTransverseImpactParameters"),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTrawBoosted = cms.EDProducer("PFRecoTauDiscriminationByMVAIsolationRun2",
    PFTauProducer = cms.InputTag("hpsPFTauProducerBoosted"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsBoosted"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.optional.FileInPath,
    inputIDNameSuffix = cms.string(''),
    loadMVAfromDB = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    mvaName = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT'),
    mvaOpt = cms.string('DBnewDMwLTwGJ'),
    srcBasicTauDiscriminators = cms.InputTag("hpsPFTauBasicDiscriminatorsBoosted"),
    srcTauTransverseImpactParameters = cms.InputTag("hpsPFTauTransverseImpactParametersBoosted"),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTrawElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationByMVAIsolationRun2",
    PFTauProducer = cms.InputTag("hpsPFTauProducerElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsElectronCleaned"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.optional.FileInPath,
    inputIDNameSuffix = cms.string(''),
    loadMVAfromDB = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    mvaName = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT'),
    mvaOpt = cms.string('DBnewDMwLTwGJ'),
    srcBasicTauDiscriminators = cms.InputTag("hpsPFTauBasicDiscriminatorsElectronCleaned"),
    srcTauTransverseImpactParameters = cms.InputTag("hpsPFTauTransverseImpactParametersElectronCleaned"),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTrawLowPtElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationByMVAIsolationRun2",
    PFTauProducer = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsLowPtElectronCleaned"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.optional.FileInPath,
    inputIDNameSuffix = cms.string(''),
    loadMVAfromDB = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    mvaName = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT'),
    mvaOpt = cms.string('DBnewDMwLTwGJ'),
    srcBasicTauDiscriminators = cms.InputTag("hpsPFTauBasicDiscriminatorsLowPtElectronCleaned"),
    srcTauTransverseImpactParameters = cms.InputTag("hpsPFTauTransverseImpactParametersLowPtElectronCleaned"),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTrawMuonCleaned = cms.EDProducer("PFRecoTauDiscriminationByMVAIsolationRun2",
    PFTauProducer = cms.InputTag("hpsPFTauProducerMuonCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsMuonCleaned"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.optional.FileInPath,
    inputIDNameSuffix = cms.string(''),
    loadMVAfromDB = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    mvaName = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT'),
    mvaOpt = cms.string('DBnewDMwLTwGJ'),
    srcBasicTauDiscriminators = cms.InputTag("hpsPFTauBasicDiscriminatorsMuonCleaned"),
    srcTauTransverseImpactParameters = cms.InputTag("hpsPFTauTransverseImpactParametersMuonCleaned"),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT = cms.EDProducer("RecoTauDiscriminantCutMultiplexer",
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT'),
        variable = cms.string('pt')
    )),
    mightGet = cms.optional.untracked.vstring,
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT_mvaOutput_normalization'),
    rawValues = cms.vstring('discriminator'),
    toMultiplex = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_VVLoose',
        '_VLoose',
        '_Loose',
        '_Medium',
        '_Tight',
        '_VTight',
        '_VVTight'
    )
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTBoosted = cms.EDProducer("RecoTauDiscriminantCutMultiplexer",
    PFTauProducer = cms.InputTag("hpsPFTauProducerBoosted"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsBoosted"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT'),
        variable = cms.string('pt')
    )),
    mightGet = cms.optional.untracked.vstring,
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT_mvaOutput_normalization'),
    rawValues = cms.vstring('discriminator'),
    toMultiplex = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTrawBoosted"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_VVLoose',
        '_VLoose',
        '_Loose',
        '_Medium',
        '_Tight',
        '_VTight',
        '_VVTight'
    )
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTElectronCleaned = cms.EDProducer("RecoTauDiscriminantCutMultiplexer",
    PFTauProducer = cms.InputTag("hpsPFTauProducerElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsElectronCleaned"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT'),
        variable = cms.string('pt')
    )),
    mightGet = cms.optional.untracked.vstring,
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT_mvaOutput_normalization'),
    rawValues = cms.vstring('discriminator'),
    toMultiplex = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTrawElectronCleaned"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_VVLoose',
        '_VLoose',
        '_Loose',
        '_Medium',
        '_Tight',
        '_VTight',
        '_VVTight'
    )
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTLowPtElectronCleaned = cms.EDProducer("RecoTauDiscriminantCutMultiplexer",
    PFTauProducer = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsLowPtElectronCleaned"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT'),
        variable = cms.string('pt')
    )),
    mightGet = cms.optional.untracked.vstring,
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT_mvaOutput_normalization'),
    rawValues = cms.vstring('discriminator'),
    toMultiplex = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTrawLowPtElectronCleaned"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_VVLoose',
        '_VLoose',
        '_Loose',
        '_Medium',
        '_Tight',
        '_VTight',
        '_VVTight'
    )
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTMuonCleaned = cms.EDProducer("RecoTauDiscriminantCutMultiplexer",
    PFTauProducer = cms.InputTag("hpsPFTauProducerMuonCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsMuonCleaned"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT'),
        variable = cms.string('pt')
    )),
    mightGet = cms.optional.untracked.vstring,
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT_mvaOutput_normalization'),
    rawValues = cms.vstring('discriminator'),
    toMultiplex = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTrawMuonCleaned"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_VVLoose',
        '_VLoose',
        '_Loose',
        '_Medium',
        '_Tight',
        '_VTight',
        '_VVTight'
    )
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw = cms.EDProducer("PFRecoTauDiscriminationByMVAIsolationRun2",
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.optional.FileInPath,
    inputIDNameSuffix = cms.string(''),
    loadMVAfromDB = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    mvaName = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT'),
    mvaOpt = cms.string('DBoldDMwLTwGJ'),
    srcBasicTauDiscriminators = cms.InputTag("hpsPFTauBasicDiscriminators"),
    srcTauTransverseImpactParameters = cms.InputTag("hpsPFTauTransverseImpactParameters"),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTrawBoosted = cms.EDProducer("PFRecoTauDiscriminationByMVAIsolationRun2",
    PFTauProducer = cms.InputTag("hpsPFTauProducerBoosted"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsBoosted"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.optional.FileInPath,
    inputIDNameSuffix = cms.string(''),
    loadMVAfromDB = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    mvaName = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT'),
    mvaOpt = cms.string('DBoldDMwLTwGJ'),
    srcBasicTauDiscriminators = cms.InputTag("hpsPFTauBasicDiscriminatorsBoosted"),
    srcTauTransverseImpactParameters = cms.InputTag("hpsPFTauTransverseImpactParametersBoosted"),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTrawElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationByMVAIsolationRun2",
    PFTauProducer = cms.InputTag("hpsPFTauProducerElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsElectronCleaned"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.optional.FileInPath,
    inputIDNameSuffix = cms.string(''),
    loadMVAfromDB = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    mvaName = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT'),
    mvaOpt = cms.string('DBoldDMwLTwGJ'),
    srcBasicTauDiscriminators = cms.InputTag("hpsPFTauBasicDiscriminatorsElectronCleaned"),
    srcTauTransverseImpactParameters = cms.InputTag("hpsPFTauTransverseImpactParametersElectronCleaned"),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTrawLowPtElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationByMVAIsolationRun2",
    PFTauProducer = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsLowPtElectronCleaned"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.optional.FileInPath,
    inputIDNameSuffix = cms.string(''),
    loadMVAfromDB = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    mvaName = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT'),
    mvaOpt = cms.string('DBoldDMwLTwGJ'),
    srcBasicTauDiscriminators = cms.InputTag("hpsPFTauBasicDiscriminatorsLowPtElectronCleaned"),
    srcTauTransverseImpactParameters = cms.InputTag("hpsPFTauTransverseImpactParametersLowPtElectronCleaned"),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTrawMuonCleaned = cms.EDProducer("PFRecoTauDiscriminationByMVAIsolationRun2",
    PFTauProducer = cms.InputTag("hpsPFTauProducerMuonCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsMuonCleaned"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.optional.FileInPath,
    inputIDNameSuffix = cms.string(''),
    loadMVAfromDB = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    mvaName = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT'),
    mvaOpt = cms.string('DBoldDMwLTwGJ'),
    srcBasicTauDiscriminators = cms.InputTag("hpsPFTauBasicDiscriminatorsMuonCleaned"),
    srcTauTransverseImpactParameters = cms.InputTag("hpsPFTauTransverseImpactParametersMuonCleaned"),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByLooseElectronRejection = cms.EDProducer("PFRecoTauDiscriminationAgainstElectron",
    ApplyCut_BremCombined = cms.bool(False),
    ApplyCut_BremsRecoveryEOverPLead = cms.bool(False),
    ApplyCut_EOverPLead = cms.bool(False),
    ApplyCut_EcalCrackCut = cms.bool(False),
    ApplyCut_ElectronPreID = cms.bool(False),
    ApplyCut_ElectronPreID_2D = cms.bool(False),
    ApplyCut_EmFraction = cms.bool(False),
    ApplyCut_Hcal3x3OverPLead = cms.bool(False),
    ApplyCut_HcalMaxOverPLead = cms.bool(False),
    ApplyCut_HcalTotOverPLead = cms.bool(False),
    ApplyCut_PFElectronMVA = cms.bool(True),
    BremCombined_Fraction = cms.double(0.99),
    BremCombined_HOP = cms.double(0.1),
    BremCombined_Mass = cms.double(0.55),
    BremCombined_StripSize = cms.double(0.03),
    BremsRecoveryEOverPLead_maxValue = cms.double(1.8),
    BremsRecoveryEOverPLead_minValue = cms.double(0.8),
    EOverPLead_maxValue = cms.double(1.8),
    EOverPLead_minValue = cms.double(0.8),
    ElecPreID0_EOverPLead_maxValue = cms.double(0.95),
    ElecPreID0_HOverPLead_minValue = cms.double(0.05),
    ElecPreID1_EOverPLead_maxValue = cms.double(0.8),
    ElecPreID1_HOverPLead_minValue = cms.double(0.15),
    EmFraction_maxValue = cms.double(0.9),
    Hcal3x3OverPLead_minValue = cms.double(0.1),
    HcalMaxOverPLead_minValue = cms.double(0.1),
    HcalTotOverPLead_minValue = cms.double(0.1),
    PFElectronMVA_maxValue = cms.double(0.6),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    )
)


process.hpsPFTauDiscriminationByLooseElectronRejectionBoosted = cms.EDProducer("PFRecoTauDiscriminationAgainstElectron",
    ApplyCut_BremCombined = cms.bool(False),
    ApplyCut_BremsRecoveryEOverPLead = cms.bool(False),
    ApplyCut_EOverPLead = cms.bool(False),
    ApplyCut_EcalCrackCut = cms.bool(False),
    ApplyCut_ElectronPreID = cms.bool(False),
    ApplyCut_ElectronPreID_2D = cms.bool(False),
    ApplyCut_EmFraction = cms.bool(False),
    ApplyCut_Hcal3x3OverPLead = cms.bool(False),
    ApplyCut_HcalMaxOverPLead = cms.bool(False),
    ApplyCut_HcalTotOverPLead = cms.bool(False),
    ApplyCut_PFElectronMVA = cms.bool(True),
    BremCombined_Fraction = cms.double(0.99),
    BremCombined_HOP = cms.double(0.1),
    BremCombined_Mass = cms.double(0.55),
    BremCombined_StripSize = cms.double(0.03),
    BremsRecoveryEOverPLead_maxValue = cms.double(1.8),
    BremsRecoveryEOverPLead_minValue = cms.double(0.8),
    EOverPLead_maxValue = cms.double(1.8),
    EOverPLead_minValue = cms.double(0.8),
    ElecPreID0_EOverPLead_maxValue = cms.double(0.95),
    ElecPreID0_HOverPLead_minValue = cms.double(0.05),
    ElecPreID1_EOverPLead_maxValue = cms.double(0.8),
    ElecPreID1_HOverPLead_minValue = cms.double(0.15),
    EmFraction_maxValue = cms.double(0.9),
    Hcal3x3OverPLead_minValue = cms.double(0.1),
    HcalMaxOverPLead_minValue = cms.double(0.1),
    HcalTotOverPLead_minValue = cms.double(0.1),
    PFElectronMVA_maxValue = cms.double(0.6),
    PFTauProducer = cms.InputTag("hpsPFTauProducerBoosted"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    )
)


process.hpsPFTauDiscriminationByLooseElectronRejectionElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationAgainstElectron",
    ApplyCut_BremCombined = cms.bool(False),
    ApplyCut_BremsRecoveryEOverPLead = cms.bool(False),
    ApplyCut_EOverPLead = cms.bool(False),
    ApplyCut_EcalCrackCut = cms.bool(False),
    ApplyCut_ElectronPreID = cms.bool(False),
    ApplyCut_ElectronPreID_2D = cms.bool(False),
    ApplyCut_EmFraction = cms.bool(False),
    ApplyCut_Hcal3x3OverPLead = cms.bool(False),
    ApplyCut_HcalMaxOverPLead = cms.bool(False),
    ApplyCut_HcalTotOverPLead = cms.bool(False),
    ApplyCut_PFElectronMVA = cms.bool(True),
    BremCombined_Fraction = cms.double(0.99),
    BremCombined_HOP = cms.double(0.1),
    BremCombined_Mass = cms.double(0.55),
    BremCombined_StripSize = cms.double(0.03),
    BremsRecoveryEOverPLead_maxValue = cms.double(1.8),
    BremsRecoveryEOverPLead_minValue = cms.double(0.8),
    EOverPLead_maxValue = cms.double(1.8),
    EOverPLead_minValue = cms.double(0.8),
    ElecPreID0_EOverPLead_maxValue = cms.double(0.95),
    ElecPreID0_HOverPLead_minValue = cms.double(0.05),
    ElecPreID1_EOverPLead_maxValue = cms.double(0.8),
    ElecPreID1_HOverPLead_minValue = cms.double(0.15),
    EmFraction_maxValue = cms.double(0.9),
    Hcal3x3OverPLead_minValue = cms.double(0.1),
    HcalMaxOverPLead_minValue = cms.double(0.1),
    HcalTotOverPLead_minValue = cms.double(0.1),
    PFElectronMVA_maxValue = cms.double(0.6),
    PFTauProducer = cms.InputTag("hpsPFTauProducerElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    )
)


process.hpsPFTauDiscriminationByLooseElectronRejectionLowPtElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationAgainstElectron",
    ApplyCut_BremCombined = cms.bool(False),
    ApplyCut_BremsRecoveryEOverPLead = cms.bool(False),
    ApplyCut_EOverPLead = cms.bool(False),
    ApplyCut_EcalCrackCut = cms.bool(False),
    ApplyCut_ElectronPreID = cms.bool(False),
    ApplyCut_ElectronPreID_2D = cms.bool(False),
    ApplyCut_EmFraction = cms.bool(False),
    ApplyCut_Hcal3x3OverPLead = cms.bool(False),
    ApplyCut_HcalMaxOverPLead = cms.bool(False),
    ApplyCut_HcalTotOverPLead = cms.bool(False),
    ApplyCut_PFElectronMVA = cms.bool(True),
    BremCombined_Fraction = cms.double(0.99),
    BremCombined_HOP = cms.double(0.1),
    BremCombined_Mass = cms.double(0.55),
    BremCombined_StripSize = cms.double(0.03),
    BremsRecoveryEOverPLead_maxValue = cms.double(1.8),
    BremsRecoveryEOverPLead_minValue = cms.double(0.8),
    EOverPLead_maxValue = cms.double(1.8),
    EOverPLead_minValue = cms.double(0.8),
    ElecPreID0_EOverPLead_maxValue = cms.double(0.95),
    ElecPreID0_HOverPLead_minValue = cms.double(0.05),
    ElecPreID1_EOverPLead_maxValue = cms.double(0.8),
    ElecPreID1_HOverPLead_minValue = cms.double(0.15),
    EmFraction_maxValue = cms.double(0.9),
    Hcal3x3OverPLead_minValue = cms.double(0.1),
    HcalMaxOverPLead_minValue = cms.double(0.1),
    HcalTotOverPLead_minValue = cms.double(0.1),
    PFElectronMVA_maxValue = cms.double(0.6),
    PFTauProducer = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    )
)


process.hpsPFTauDiscriminationByLooseElectronRejectionMuonCleaned = cms.EDProducer("PFRecoTauDiscriminationAgainstElectron",
    ApplyCut_BremCombined = cms.bool(False),
    ApplyCut_BremsRecoveryEOverPLead = cms.bool(False),
    ApplyCut_EOverPLead = cms.bool(False),
    ApplyCut_EcalCrackCut = cms.bool(False),
    ApplyCut_ElectronPreID = cms.bool(False),
    ApplyCut_ElectronPreID_2D = cms.bool(False),
    ApplyCut_EmFraction = cms.bool(False),
    ApplyCut_Hcal3x3OverPLead = cms.bool(False),
    ApplyCut_HcalMaxOverPLead = cms.bool(False),
    ApplyCut_HcalTotOverPLead = cms.bool(False),
    ApplyCut_PFElectronMVA = cms.bool(True),
    BremCombined_Fraction = cms.double(0.99),
    BremCombined_HOP = cms.double(0.1),
    BremCombined_Mass = cms.double(0.55),
    BremCombined_StripSize = cms.double(0.03),
    BremsRecoveryEOverPLead_maxValue = cms.double(1.8),
    BremsRecoveryEOverPLead_minValue = cms.double(0.8),
    EOverPLead_maxValue = cms.double(1.8),
    EOverPLead_minValue = cms.double(0.8),
    ElecPreID0_EOverPLead_maxValue = cms.double(0.95),
    ElecPreID0_HOverPLead_minValue = cms.double(0.05),
    ElecPreID1_EOverPLead_maxValue = cms.double(0.8),
    ElecPreID1_HOverPLead_minValue = cms.double(0.15),
    EmFraction_maxValue = cms.double(0.9),
    Hcal3x3OverPLead_minValue = cms.double(0.1),
    HcalMaxOverPLead_minValue = cms.double(0.1),
    HcalTotOverPLead_minValue = cms.double(0.1),
    PFElectronMVA_maxValue = cms.double(0.6),
    PFTauProducer = cms.InputTag("hpsPFTauProducerMuonCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    )
)


process.hpsPFTauDiscriminationByMVA6ElectronRejection = cms.EDProducer("RecoTauDiscriminantCutMultiplexer",
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(
        cms.PSet(
            category = cms.uint32(0),
            cut = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_woGwoGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(2),
            cut = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_wGwoGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(5),
            cut = cms.string('RecoTauTag_antiElectronMVA_woGwGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(7),
            cut = cms.string('RecoTauTag_antiElectronMVA_wGwGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(8),
            cut = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_woGwoGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(10),
            cut = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_wGwoGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(13),
            cut = cms.string('RecoTauTag_antiElectronMVA_woGwGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(15),
            cut = cms.string('RecoTauTag_antiElectronMVA_wGwGSF_EC'),
            variable = cms.string('pt')
        )
    ),
    mightGet = cms.optional.untracked.vstring,
    mvaOutput_normalization = cms.string(''),
    rawValues = cms.vstring(
        'discriminator',
        'category'
    ),
    toMultiplex = cms.InputTag("hpsPFTauDiscriminationByMVA6rawElectronRejection"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_VLoose',
        '_Loose',
        '_Medium',
        '_Tight',
        '_VTight'
    )
)


process.hpsPFTauDiscriminationByMVA6ElectronRejectionBoosted = cms.EDProducer("RecoTauDiscriminantCutMultiplexer",
    PFTauProducer = cms.InputTag("hpsPFTauProducerBoosted"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsBoosted"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(
        cms.PSet(
            category = cms.uint32(0),
            cut = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_woGwoGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(2),
            cut = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_wGwoGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(5),
            cut = cms.string('RecoTauTag_antiElectronMVA_woGwGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(7),
            cut = cms.string('RecoTauTag_antiElectronMVA_wGwGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(8),
            cut = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_woGwoGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(10),
            cut = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_wGwoGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(13),
            cut = cms.string('RecoTauTag_antiElectronMVA_woGwGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(15),
            cut = cms.string('RecoTauTag_antiElectronMVA_wGwGSF_EC'),
            variable = cms.string('pt')
        )
    ),
    mightGet = cms.optional.untracked.vstring,
    mvaOutput_normalization = cms.string(''),
    rawValues = cms.vstring(
        'discriminator',
        'category'
    ),
    toMultiplex = cms.InputTag("hpsPFTauDiscriminationByMVA6rawElectronRejectionBoosted"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_VLoose',
        '_Loose',
        '_Medium',
        '_Tight',
        '_VTight'
    )
)


process.hpsPFTauDiscriminationByMVA6ElectronRejectionElectronCleaned = cms.EDProducer("RecoTauDiscriminantCutMultiplexer",
    PFTauProducer = cms.InputTag("hpsPFTauProducerElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsElectronCleaned"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(
        cms.PSet(
            category = cms.uint32(0),
            cut = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_woGwoGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(2),
            cut = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_wGwoGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(5),
            cut = cms.string('RecoTauTag_antiElectronMVA_woGwGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(7),
            cut = cms.string('RecoTauTag_antiElectronMVA_wGwGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(8),
            cut = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_woGwoGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(10),
            cut = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_wGwoGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(13),
            cut = cms.string('RecoTauTag_antiElectronMVA_woGwGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(15),
            cut = cms.string('RecoTauTag_antiElectronMVA_wGwGSF_EC'),
            variable = cms.string('pt')
        )
    ),
    mightGet = cms.optional.untracked.vstring,
    mvaOutput_normalization = cms.string(''),
    rawValues = cms.vstring(
        'discriminator',
        'category'
    ),
    toMultiplex = cms.InputTag("hpsPFTauDiscriminationByMVA6rawElectronRejectionElectronCleaned"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_VLoose',
        '_Loose',
        '_Medium',
        '_Tight',
        '_VTight'
    )
)


process.hpsPFTauDiscriminationByMVA6ElectronRejectionLowPtElectronCleaned = cms.EDProducer("RecoTauDiscriminantCutMultiplexer",
    PFTauProducer = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsLowPtElectronCleaned"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(
        cms.PSet(
            category = cms.uint32(0),
            cut = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_woGwoGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(2),
            cut = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_wGwoGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(5),
            cut = cms.string('RecoTauTag_antiElectronMVA_woGwGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(7),
            cut = cms.string('RecoTauTag_antiElectronMVA_wGwGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(8),
            cut = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_woGwoGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(10),
            cut = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_wGwoGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(13),
            cut = cms.string('RecoTauTag_antiElectronMVA_woGwGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(15),
            cut = cms.string('RecoTauTag_antiElectronMVA_wGwGSF_EC'),
            variable = cms.string('pt')
        )
    ),
    mightGet = cms.optional.untracked.vstring,
    mvaOutput_normalization = cms.string(''),
    rawValues = cms.vstring(
        'discriminator',
        'category'
    ),
    toMultiplex = cms.InputTag("hpsPFTauDiscriminationByMVA6rawElectronRejectionLowPtElectronCleaned"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_VLoose',
        '_Loose',
        '_Medium',
        '_Tight',
        '_VTight'
    )
)


process.hpsPFTauDiscriminationByMVA6ElectronRejectionMuonCleaned = cms.EDProducer("RecoTauDiscriminantCutMultiplexer",
    PFTauProducer = cms.InputTag("hpsPFTauProducerMuonCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsMuonCleaned"),
            cut = cms.double(0.5)
        )
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(
        cms.PSet(
            category = cms.uint32(0),
            cut = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_woGwoGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(2),
            cut = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_wGwoGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(5),
            cut = cms.string('RecoTauTag_antiElectronMVA_woGwGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(7),
            cut = cms.string('RecoTauTag_antiElectronMVA_wGwGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(8),
            cut = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_woGwoGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(10),
            cut = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_wGwoGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(13),
            cut = cms.string('RecoTauTag_antiElectronMVA_woGwGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(15),
            cut = cms.string('RecoTauTag_antiElectronMVA_wGwGSF_EC'),
            variable = cms.string('pt')
        )
    ),
    mightGet = cms.optional.untracked.vstring,
    mvaOutput_normalization = cms.string(''),
    rawValues = cms.vstring(
        'discriminator',
        'category'
    ),
    toMultiplex = cms.InputTag("hpsPFTauDiscriminationByMVA6rawElectronRejectionMuonCleaned"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_VLoose',
        '_Loose',
        '_Medium',
        '_Tight',
        '_VTight'
    )
)


process.hpsPFTauDiscriminationByMVA6rawElectronRejection = cms.EDProducer("PFRecoTauDiscriminationAgainstElectronMVA6",
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        )
    ),
    hgcalElectronIDs = cms.VInputTag(),
    isPhase2 = cms.bool(False),
    loadMVAfromDB = cms.bool(True),
    method = cms.string('BDTG'),
    mightGet = cms.optional.untracked.vstring,
    minMVANoEleMatchWOgWOgsfBL = cms.double(0),
    minMVANoEleMatchWOgWOgsfEC = cms.double(0),
    minMVANoEleMatchWgWOgsfBL = cms.double(0),
    minMVANoEleMatchWgWOgsfEC = cms.double(0),
    minMVAWOgWgsfBL = cms.double(0),
    minMVAWOgWgsfEC = cms.double(0),
    minMVAWgWgsfBL = cms.double(0),
    minMVAWgWgsfEC = cms.double(0),
    mvaName_NoEleMatch_wGwoGSF_BL = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_wGwoGSF_BL'),
    mvaName_NoEleMatch_wGwoGSF_EC = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_wGwoGSF_EC'),
    mvaName_NoEleMatch_woGwoGSF_BL = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_woGwoGSF_BL'),
    mvaName_NoEleMatch_woGwoGSF_EC = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_woGwoGSF_EC'),
    mvaName_wGwGSF_BL = cms.string('RecoTauTag_antiElectronMVA_wGwGSF_BL'),
    mvaName_wGwGSF_EC = cms.string('RecoTauTag_antiElectronMVA_wGwGSF_EC'),
    mvaName_woGwGSF_BL = cms.string('RecoTauTag_antiElectronMVA_woGwGSF_BL'),
    mvaName_woGwGSF_EC = cms.string('RecoTauTag_antiElectronMVA_woGwGSF_EC'),
    returnMVA = cms.bool(True),
    srcElectrons = cms.InputTag("gedGsfElectrons"),
    usePhiAtEcalEntranceExtrapolation = cms.bool(False),
    verbosity = cms.int32(0),
    vetoEcalCracks = cms.bool(False)
)


process.hpsPFTauDiscriminationByMVA6rawElectronRejectionBoosted = cms.EDProducer("PFRecoTauDiscriminationAgainstElectronMVA6",
    PFTauProducer = cms.InputTag("hpsPFTauProducerBoosted"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsBoosted"),
            cut = cms.double(0.5)
        )
    ),
    hgcalElectronIDs = cms.VInputTag(),
    isPhase2 = cms.bool(False),
    loadMVAfromDB = cms.bool(True),
    method = cms.string('BDTG'),
    mightGet = cms.optional.untracked.vstring,
    minMVANoEleMatchWOgWOgsfBL = cms.double(0),
    minMVANoEleMatchWOgWOgsfEC = cms.double(0),
    minMVANoEleMatchWgWOgsfBL = cms.double(0),
    minMVANoEleMatchWgWOgsfEC = cms.double(0),
    minMVAWOgWgsfBL = cms.double(0),
    minMVAWOgWgsfEC = cms.double(0),
    minMVAWgWgsfBL = cms.double(0),
    minMVAWgWgsfEC = cms.double(0),
    mvaName_NoEleMatch_wGwoGSF_BL = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_wGwoGSF_BL'),
    mvaName_NoEleMatch_wGwoGSF_EC = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_wGwoGSF_EC'),
    mvaName_NoEleMatch_woGwoGSF_BL = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_woGwoGSF_BL'),
    mvaName_NoEleMatch_woGwoGSF_EC = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_woGwoGSF_EC'),
    mvaName_wGwGSF_BL = cms.string('RecoTauTag_antiElectronMVA_wGwGSF_BL'),
    mvaName_wGwGSF_EC = cms.string('RecoTauTag_antiElectronMVA_wGwGSF_EC'),
    mvaName_woGwGSF_BL = cms.string('RecoTauTag_antiElectronMVA_woGwGSF_BL'),
    mvaName_woGwGSF_EC = cms.string('RecoTauTag_antiElectronMVA_woGwGSF_EC'),
    returnMVA = cms.bool(True),
    srcElectrons = cms.InputTag("gedGsfElectrons"),
    usePhiAtEcalEntranceExtrapolation = cms.bool(False),
    verbosity = cms.int32(0),
    vetoEcalCracks = cms.bool(False)
)


process.hpsPFTauDiscriminationByMVA6rawElectronRejectionElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationAgainstElectronMVA6",
    PFTauProducer = cms.InputTag("hpsPFTauProducerElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsElectronCleaned"),
            cut = cms.double(0.5)
        )
    ),
    hgcalElectronIDs = cms.VInputTag(),
    isPhase2 = cms.bool(False),
    loadMVAfromDB = cms.bool(True),
    method = cms.string('BDTG'),
    mightGet = cms.optional.untracked.vstring,
    minMVANoEleMatchWOgWOgsfBL = cms.double(0),
    minMVANoEleMatchWOgWOgsfEC = cms.double(0),
    minMVANoEleMatchWgWOgsfBL = cms.double(0),
    minMVANoEleMatchWgWOgsfEC = cms.double(0),
    minMVAWOgWgsfBL = cms.double(0),
    minMVAWOgWgsfEC = cms.double(0),
    minMVAWgWgsfBL = cms.double(0),
    minMVAWgWgsfEC = cms.double(0),
    mvaName_NoEleMatch_wGwoGSF_BL = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_wGwoGSF_BL'),
    mvaName_NoEleMatch_wGwoGSF_EC = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_wGwoGSF_EC'),
    mvaName_NoEleMatch_woGwoGSF_BL = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_woGwoGSF_BL'),
    mvaName_NoEleMatch_woGwoGSF_EC = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_woGwoGSF_EC'),
    mvaName_wGwGSF_BL = cms.string('RecoTauTag_antiElectronMVA_wGwGSF_BL'),
    mvaName_wGwGSF_EC = cms.string('RecoTauTag_antiElectronMVA_wGwGSF_EC'),
    mvaName_woGwGSF_BL = cms.string('RecoTauTag_antiElectronMVA_woGwGSF_BL'),
    mvaName_woGwGSF_EC = cms.string('RecoTauTag_antiElectronMVA_woGwGSF_EC'),
    returnMVA = cms.bool(True),
    srcElectrons = cms.InputTag("gedGsfElectrons"),
    usePhiAtEcalEntranceExtrapolation = cms.bool(False),
    verbosity = cms.int32(0),
    vetoEcalCracks = cms.bool(False)
)


process.hpsPFTauDiscriminationByMVA6rawElectronRejectionLowPtElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationAgainstElectronMVA6",
    PFTauProducer = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsLowPtElectronCleaned"),
            cut = cms.double(0.5)
        )
    ),
    hgcalElectronIDs = cms.VInputTag(),
    isPhase2 = cms.bool(False),
    loadMVAfromDB = cms.bool(True),
    method = cms.string('BDTG'),
    mightGet = cms.optional.untracked.vstring,
    minMVANoEleMatchWOgWOgsfBL = cms.double(0),
    minMVANoEleMatchWOgWOgsfEC = cms.double(0),
    minMVANoEleMatchWgWOgsfBL = cms.double(0),
    minMVANoEleMatchWgWOgsfEC = cms.double(0),
    minMVAWOgWgsfBL = cms.double(0),
    minMVAWOgWgsfEC = cms.double(0),
    minMVAWgWgsfBL = cms.double(0),
    minMVAWgWgsfEC = cms.double(0),
    mvaName_NoEleMatch_wGwoGSF_BL = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_wGwoGSF_BL'),
    mvaName_NoEleMatch_wGwoGSF_EC = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_wGwoGSF_EC'),
    mvaName_NoEleMatch_woGwoGSF_BL = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_woGwoGSF_BL'),
    mvaName_NoEleMatch_woGwoGSF_EC = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_woGwoGSF_EC'),
    mvaName_wGwGSF_BL = cms.string('RecoTauTag_antiElectronMVA_wGwGSF_BL'),
    mvaName_wGwGSF_EC = cms.string('RecoTauTag_antiElectronMVA_wGwGSF_EC'),
    mvaName_woGwGSF_BL = cms.string('RecoTauTag_antiElectronMVA_woGwGSF_BL'),
    mvaName_woGwGSF_EC = cms.string('RecoTauTag_antiElectronMVA_woGwGSF_EC'),
    returnMVA = cms.bool(True),
    srcElectrons = cms.InputTag("gedGsfElectrons"),
    usePhiAtEcalEntranceExtrapolation = cms.bool(False),
    verbosity = cms.int32(0),
    vetoEcalCracks = cms.bool(False)
)


process.hpsPFTauDiscriminationByMVA6rawElectronRejectionMuonCleaned = cms.EDProducer("PFRecoTauDiscriminationAgainstElectronMVA6",
    PFTauProducer = cms.InputTag("hpsPFTauProducerMuonCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsMuonCleaned"),
            cut = cms.double(0.5)
        )
    ),
    hgcalElectronIDs = cms.VInputTag(),
    isPhase2 = cms.bool(False),
    loadMVAfromDB = cms.bool(True),
    method = cms.string('BDTG'),
    mightGet = cms.optional.untracked.vstring,
    minMVANoEleMatchWOgWOgsfBL = cms.double(0),
    minMVANoEleMatchWOgWOgsfEC = cms.double(0),
    minMVANoEleMatchWgWOgsfBL = cms.double(0),
    minMVANoEleMatchWgWOgsfEC = cms.double(0),
    minMVAWOgWgsfBL = cms.double(0),
    minMVAWOgWgsfEC = cms.double(0),
    minMVAWgWgsfBL = cms.double(0),
    minMVAWgWgsfEC = cms.double(0),
    mvaName_NoEleMatch_wGwoGSF_BL = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_wGwoGSF_BL'),
    mvaName_NoEleMatch_wGwoGSF_EC = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_wGwoGSF_EC'),
    mvaName_NoEleMatch_woGwoGSF_BL = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_woGwoGSF_BL'),
    mvaName_NoEleMatch_woGwoGSF_EC = cms.string('RecoTauTag_antiElectronMVA_NoEleMatch_woGwoGSF_EC'),
    mvaName_wGwGSF_BL = cms.string('RecoTauTag_antiElectronMVA_wGwGSF_BL'),
    mvaName_wGwGSF_EC = cms.string('RecoTauTag_antiElectronMVA_wGwGSF_EC'),
    mvaName_woGwGSF_BL = cms.string('RecoTauTag_antiElectronMVA_woGwGSF_BL'),
    mvaName_woGwGSF_EC = cms.string('RecoTauTag_antiElectronMVA_woGwGSF_EC'),
    returnMVA = cms.bool(True),
    srcElectrons = cms.InputTag("gedGsfElectrons"),
    usePhiAtEcalEntranceExtrapolation = cms.bool(False),
    verbosity = cms.int32(0),
    vetoEcalCracks = cms.bool(False)
)


process.hpsPFTauDiscriminationByMediumElectronRejection = cms.EDProducer("PFRecoTauDiscriminationAgainstElectron",
    ApplyCut_BremCombined = cms.bool(False),
    ApplyCut_BremsRecoveryEOverPLead = cms.bool(False),
    ApplyCut_EOverPLead = cms.bool(False),
    ApplyCut_EcalCrackCut = cms.bool(True),
    ApplyCut_ElectronPreID = cms.bool(False),
    ApplyCut_ElectronPreID_2D = cms.bool(False),
    ApplyCut_EmFraction = cms.bool(False),
    ApplyCut_Hcal3x3OverPLead = cms.bool(False),
    ApplyCut_HcalMaxOverPLead = cms.bool(False),
    ApplyCut_HcalTotOverPLead = cms.bool(False),
    ApplyCut_PFElectronMVA = cms.bool(True),
    BremCombined_Fraction = cms.double(0.99),
    BremCombined_HOP = cms.double(0.1),
    BremCombined_Mass = cms.double(0.55),
    BremCombined_StripSize = cms.double(0.03),
    BremsRecoveryEOverPLead_maxValue = cms.double(1.8),
    BremsRecoveryEOverPLead_minValue = cms.double(0.8),
    EOverPLead_maxValue = cms.double(1.8),
    EOverPLead_minValue = cms.double(0.8),
    ElecPreID0_EOverPLead_maxValue = cms.double(0.95),
    ElecPreID0_HOverPLead_minValue = cms.double(0.05),
    ElecPreID1_EOverPLead_maxValue = cms.double(0.8),
    ElecPreID1_HOverPLead_minValue = cms.double(0.15),
    EmFraction_maxValue = cms.double(0.9),
    Hcal3x3OverPLead_minValue = cms.double(0.1),
    HcalMaxOverPLead_minValue = cms.double(0.1),
    HcalTotOverPLead_minValue = cms.double(0.1),
    PFElectronMVA_maxValue = cms.double(-0.1),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    )
)


process.hpsPFTauDiscriminationByMediumElectronRejectionBoosted = cms.EDProducer("PFRecoTauDiscriminationAgainstElectron",
    ApplyCut_BremCombined = cms.bool(False),
    ApplyCut_BremsRecoveryEOverPLead = cms.bool(False),
    ApplyCut_EOverPLead = cms.bool(False),
    ApplyCut_EcalCrackCut = cms.bool(True),
    ApplyCut_ElectronPreID = cms.bool(False),
    ApplyCut_ElectronPreID_2D = cms.bool(False),
    ApplyCut_EmFraction = cms.bool(False),
    ApplyCut_Hcal3x3OverPLead = cms.bool(False),
    ApplyCut_HcalMaxOverPLead = cms.bool(False),
    ApplyCut_HcalTotOverPLead = cms.bool(False),
    ApplyCut_PFElectronMVA = cms.bool(True),
    BremCombined_Fraction = cms.double(0.99),
    BremCombined_HOP = cms.double(0.1),
    BremCombined_Mass = cms.double(0.55),
    BremCombined_StripSize = cms.double(0.03),
    BremsRecoveryEOverPLead_maxValue = cms.double(1.8),
    BremsRecoveryEOverPLead_minValue = cms.double(0.8),
    EOverPLead_maxValue = cms.double(1.8),
    EOverPLead_minValue = cms.double(0.8),
    ElecPreID0_EOverPLead_maxValue = cms.double(0.95),
    ElecPreID0_HOverPLead_minValue = cms.double(0.05),
    ElecPreID1_EOverPLead_maxValue = cms.double(0.8),
    ElecPreID1_HOverPLead_minValue = cms.double(0.15),
    EmFraction_maxValue = cms.double(0.9),
    Hcal3x3OverPLead_minValue = cms.double(0.1),
    HcalMaxOverPLead_minValue = cms.double(0.1),
    HcalTotOverPLead_minValue = cms.double(0.1),
    PFElectronMVA_maxValue = cms.double(-0.1),
    PFTauProducer = cms.InputTag("hpsPFTauProducerBoosted"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    )
)


process.hpsPFTauDiscriminationByMediumElectronRejectionElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationAgainstElectron",
    ApplyCut_BremCombined = cms.bool(False),
    ApplyCut_BremsRecoveryEOverPLead = cms.bool(False),
    ApplyCut_EOverPLead = cms.bool(False),
    ApplyCut_EcalCrackCut = cms.bool(True),
    ApplyCut_ElectronPreID = cms.bool(False),
    ApplyCut_ElectronPreID_2D = cms.bool(False),
    ApplyCut_EmFraction = cms.bool(False),
    ApplyCut_Hcal3x3OverPLead = cms.bool(False),
    ApplyCut_HcalMaxOverPLead = cms.bool(False),
    ApplyCut_HcalTotOverPLead = cms.bool(False),
    ApplyCut_PFElectronMVA = cms.bool(True),
    BremCombined_Fraction = cms.double(0.99),
    BremCombined_HOP = cms.double(0.1),
    BremCombined_Mass = cms.double(0.55),
    BremCombined_StripSize = cms.double(0.03),
    BremsRecoveryEOverPLead_maxValue = cms.double(1.8),
    BremsRecoveryEOverPLead_minValue = cms.double(0.8),
    EOverPLead_maxValue = cms.double(1.8),
    EOverPLead_minValue = cms.double(0.8),
    ElecPreID0_EOverPLead_maxValue = cms.double(0.95),
    ElecPreID0_HOverPLead_minValue = cms.double(0.05),
    ElecPreID1_EOverPLead_maxValue = cms.double(0.8),
    ElecPreID1_HOverPLead_minValue = cms.double(0.15),
    EmFraction_maxValue = cms.double(0.9),
    Hcal3x3OverPLead_minValue = cms.double(0.1),
    HcalMaxOverPLead_minValue = cms.double(0.1),
    HcalTotOverPLead_minValue = cms.double(0.1),
    PFElectronMVA_maxValue = cms.double(-0.1),
    PFTauProducer = cms.InputTag("hpsPFTauProducerElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    )
)


process.hpsPFTauDiscriminationByMediumElectronRejectionLowPtElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationAgainstElectron",
    ApplyCut_BremCombined = cms.bool(False),
    ApplyCut_BremsRecoveryEOverPLead = cms.bool(False),
    ApplyCut_EOverPLead = cms.bool(False),
    ApplyCut_EcalCrackCut = cms.bool(True),
    ApplyCut_ElectronPreID = cms.bool(False),
    ApplyCut_ElectronPreID_2D = cms.bool(False),
    ApplyCut_EmFraction = cms.bool(False),
    ApplyCut_Hcal3x3OverPLead = cms.bool(False),
    ApplyCut_HcalMaxOverPLead = cms.bool(False),
    ApplyCut_HcalTotOverPLead = cms.bool(False),
    ApplyCut_PFElectronMVA = cms.bool(True),
    BremCombined_Fraction = cms.double(0.99),
    BremCombined_HOP = cms.double(0.1),
    BremCombined_Mass = cms.double(0.55),
    BremCombined_StripSize = cms.double(0.03),
    BremsRecoveryEOverPLead_maxValue = cms.double(1.8),
    BremsRecoveryEOverPLead_minValue = cms.double(0.8),
    EOverPLead_maxValue = cms.double(1.8),
    EOverPLead_minValue = cms.double(0.8),
    ElecPreID0_EOverPLead_maxValue = cms.double(0.95),
    ElecPreID0_HOverPLead_minValue = cms.double(0.05),
    ElecPreID1_EOverPLead_maxValue = cms.double(0.8),
    ElecPreID1_HOverPLead_minValue = cms.double(0.15),
    EmFraction_maxValue = cms.double(0.9),
    Hcal3x3OverPLead_minValue = cms.double(0.1),
    HcalMaxOverPLead_minValue = cms.double(0.1),
    HcalTotOverPLead_minValue = cms.double(0.1),
    PFElectronMVA_maxValue = cms.double(-0.1),
    PFTauProducer = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    )
)


process.hpsPFTauDiscriminationByMediumElectronRejectionMuonCleaned = cms.EDProducer("PFRecoTauDiscriminationAgainstElectron",
    ApplyCut_BremCombined = cms.bool(False),
    ApplyCut_BremsRecoveryEOverPLead = cms.bool(False),
    ApplyCut_EOverPLead = cms.bool(False),
    ApplyCut_EcalCrackCut = cms.bool(True),
    ApplyCut_ElectronPreID = cms.bool(False),
    ApplyCut_ElectronPreID_2D = cms.bool(False),
    ApplyCut_EmFraction = cms.bool(False),
    ApplyCut_Hcal3x3OverPLead = cms.bool(False),
    ApplyCut_HcalMaxOverPLead = cms.bool(False),
    ApplyCut_HcalTotOverPLead = cms.bool(False),
    ApplyCut_PFElectronMVA = cms.bool(True),
    BremCombined_Fraction = cms.double(0.99),
    BremCombined_HOP = cms.double(0.1),
    BremCombined_Mass = cms.double(0.55),
    BremCombined_StripSize = cms.double(0.03),
    BremsRecoveryEOverPLead_maxValue = cms.double(1.8),
    BremsRecoveryEOverPLead_minValue = cms.double(0.8),
    EOverPLead_maxValue = cms.double(1.8),
    EOverPLead_minValue = cms.double(0.8),
    ElecPreID0_EOverPLead_maxValue = cms.double(0.95),
    ElecPreID0_HOverPLead_minValue = cms.double(0.05),
    ElecPreID1_EOverPLead_maxValue = cms.double(0.8),
    ElecPreID1_HOverPLead_minValue = cms.double(0.15),
    EmFraction_maxValue = cms.double(0.9),
    Hcal3x3OverPLead_minValue = cms.double(0.1),
    HcalMaxOverPLead_minValue = cms.double(0.1),
    HcalTotOverPLead_minValue = cms.double(0.1),
    PFElectronMVA_maxValue = cms.double(-0.1),
    PFTauProducer = cms.InputTag("hpsPFTauProducerMuonCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    )
)


process.hpsPFTauDiscriminationByMuonRejection3 = cms.EDProducer("PFRecoTauDiscriminationAgainstMuon2Container",
    IDWPdefinitions = cms.VPSet(
        cms.PSet(
            HoPMin = cms.double(0.2),
            IDname = cms.string('ByLooseMuonRejection3'),
            discriminatorOption = cms.string('custom'),
            doCaloMuonVeto = cms.bool(True),
            maxNumberOfHitsLast2Stations = cms.int32(-1),
            maxNumberOfMatches = cms.int32(1)
        ),
        cms.PSet(
            HoPMin = cms.double(0.2),
            IDname = cms.string('ByTightMuonRejection3'),
            discriminatorOption = cms.string('custom'),
            doCaloMuonVeto = cms.bool(True),
            maxNumberOfHitsLast2Stations = cms.int32(0),
            maxNumberOfMatches = cms.int32(1)
        )
    ),
    IDdefinitions = cms.VPSet(),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    dRmuonMatch = cms.double(0.3),
    dRmuonMatchLimitedToJetArea = cms.bool(False),
    maskHitsCSC = cms.vint32(0, 0, 0, 0),
    maskHitsDT = cms.vint32(0, 0, 0, 0),
    maskHitsRPC = cms.vint32(0, 0, 0, 0),
    maskMatchesCSC = cms.vint32(1, 0, 0, 0),
    maskMatchesDT = cms.vint32(0, 0, 0, 0),
    maskMatchesRPC = cms.vint32(0, 0, 0, 0),
    mightGet = cms.optional.untracked.vstring,
    minPtMatchedMuon = cms.double(5),
    srcMuons = cms.InputTag("muons"),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByMuonRejection3Boosted = cms.EDProducer("PFRecoTauDiscriminationAgainstMuon2Container",
    IDWPdefinitions = cms.VPSet(
        cms.PSet(
            HoPMin = cms.double(0.2),
            IDname = cms.string('ByLooseMuonRejection3'),
            discriminatorOption = cms.string('custom'),
            doCaloMuonVeto = cms.bool(True),
            maxNumberOfHitsLast2Stations = cms.int32(-1),
            maxNumberOfMatches = cms.int32(1)
        ),
        cms.PSet(
            HoPMin = cms.double(0.2),
            IDname = cms.string('ByTightMuonRejection3'),
            discriminatorOption = cms.string('custom'),
            doCaloMuonVeto = cms.bool(True),
            maxNumberOfHitsLast2Stations = cms.int32(0),
            maxNumberOfMatches = cms.int32(1)
        )
    ),
    IDdefinitions = cms.VPSet(),
    PFTauProducer = cms.InputTag("hpsPFTauProducerBoosted"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    dRmuonMatch = cms.double(0.3),
    dRmuonMatchLimitedToJetArea = cms.bool(False),
    maskHitsCSC = cms.vint32(0, 0, 0, 0),
    maskHitsDT = cms.vint32(0, 0, 0, 0),
    maskHitsRPC = cms.vint32(0, 0, 0, 0),
    maskMatchesCSC = cms.vint32(1, 0, 0, 0),
    maskMatchesDT = cms.vint32(0, 0, 0, 0),
    maskMatchesRPC = cms.vint32(0, 0, 0, 0),
    mightGet = cms.optional.untracked.vstring,
    minPtMatchedMuon = cms.double(5),
    srcMuons = cms.InputTag("muons"),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByMuonRejection3ElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationAgainstMuon2Container",
    IDWPdefinitions = cms.VPSet(
        cms.PSet(
            HoPMin = cms.double(0.2),
            IDname = cms.string('ByLooseMuonRejection3'),
            discriminatorOption = cms.string('custom'),
            doCaloMuonVeto = cms.bool(True),
            maxNumberOfHitsLast2Stations = cms.int32(-1),
            maxNumberOfMatches = cms.int32(1)
        ),
        cms.PSet(
            HoPMin = cms.double(0.2),
            IDname = cms.string('ByTightMuonRejection3'),
            discriminatorOption = cms.string('custom'),
            doCaloMuonVeto = cms.bool(True),
            maxNumberOfHitsLast2Stations = cms.int32(0),
            maxNumberOfMatches = cms.int32(1)
        )
    ),
    IDdefinitions = cms.VPSet(),
    PFTauProducer = cms.InputTag("hpsPFTauProducerElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    dRmuonMatch = cms.double(0.3),
    dRmuonMatchLimitedToJetArea = cms.bool(False),
    maskHitsCSC = cms.vint32(0, 0, 0, 0),
    maskHitsDT = cms.vint32(0, 0, 0, 0),
    maskHitsRPC = cms.vint32(0, 0, 0, 0),
    maskMatchesCSC = cms.vint32(1, 0, 0, 0),
    maskMatchesDT = cms.vint32(0, 0, 0, 0),
    maskMatchesRPC = cms.vint32(0, 0, 0, 0),
    mightGet = cms.optional.untracked.vstring,
    minPtMatchedMuon = cms.double(5),
    srcMuons = cms.InputTag("muons"),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByMuonRejection3LowPtElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationAgainstMuon2Container",
    IDWPdefinitions = cms.VPSet(
        cms.PSet(
            HoPMin = cms.double(0.2),
            IDname = cms.string('ByLooseMuonRejection3'),
            discriminatorOption = cms.string('custom'),
            doCaloMuonVeto = cms.bool(True),
            maxNumberOfHitsLast2Stations = cms.int32(-1),
            maxNumberOfMatches = cms.int32(1)
        ),
        cms.PSet(
            HoPMin = cms.double(0.2),
            IDname = cms.string('ByTightMuonRejection3'),
            discriminatorOption = cms.string('custom'),
            doCaloMuonVeto = cms.bool(True),
            maxNumberOfHitsLast2Stations = cms.int32(0),
            maxNumberOfMatches = cms.int32(1)
        )
    ),
    IDdefinitions = cms.VPSet(),
    PFTauProducer = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    dRmuonMatch = cms.double(0.3),
    dRmuonMatchLimitedToJetArea = cms.bool(False),
    maskHitsCSC = cms.vint32(0, 0, 0, 0),
    maskHitsDT = cms.vint32(0, 0, 0, 0),
    maskHitsRPC = cms.vint32(0, 0, 0, 0),
    maskMatchesCSC = cms.vint32(1, 0, 0, 0),
    maskMatchesDT = cms.vint32(0, 0, 0, 0),
    maskMatchesRPC = cms.vint32(0, 0, 0, 0),
    mightGet = cms.optional.untracked.vstring,
    minPtMatchedMuon = cms.double(5),
    srcMuons = cms.InputTag("muons"),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByMuonRejection3MuonCleaned = cms.EDProducer("PFRecoTauDiscriminationAgainstMuon2Container",
    IDWPdefinitions = cms.VPSet(
        cms.PSet(
            HoPMin = cms.double(0.2),
            IDname = cms.string('ByLooseMuonRejection3'),
            discriminatorOption = cms.string('custom'),
            doCaloMuonVeto = cms.bool(True),
            maxNumberOfHitsLast2Stations = cms.int32(-1),
            maxNumberOfMatches = cms.int32(1)
        ),
        cms.PSet(
            HoPMin = cms.double(0.2),
            IDname = cms.string('ByTightMuonRejection3'),
            discriminatorOption = cms.string('custom'),
            doCaloMuonVeto = cms.bool(True),
            maxNumberOfHitsLast2Stations = cms.int32(0),
            maxNumberOfMatches = cms.int32(1)
        )
    ),
    IDdefinitions = cms.VPSet(),
    PFTauProducer = cms.InputTag("hpsPFTauProducerMuonCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    dRmuonMatch = cms.double(0.3),
    dRmuonMatchLimitedToJetArea = cms.bool(False),
    maskHitsCSC = cms.vint32(0, 0, 0, 0),
    maskHitsDT = cms.vint32(0, 0, 0, 0),
    maskHitsRPC = cms.vint32(0, 0, 0, 0),
    maskMatchesCSC = cms.vint32(1, 0, 0, 0),
    maskMatchesDT = cms.vint32(0, 0, 0, 0),
    maskMatchesRPC = cms.vint32(0, 0, 0, 0),
    mightGet = cms.optional.untracked.vstring,
    minPtMatchedMuon = cms.double(5),
    srcMuons = cms.InputTag("muons"),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByMuonRejectionSimple = cms.EDProducer("PFRecoTauDiscriminationAgainstMuonSimple",
    IDWPdefinitions = cms.VPSet(
        cms.PSet(
            HoPMin = cms.double(0.2),
            IDname = cms.string('ByLooseMuonRejectionSimple'),
            doCaloMuonVeto = cms.bool(True),
            maxNumberOfHitsLast2Stations = cms.int32(-1),
            maxNumberOfMatches = cms.int32(1),
            maxNumberOfRPCMuons = cms.int32(-1),
            maxNumberOfSTAMuons = cms.int32(-1)
        ),
        cms.PSet(
            HoPMin = cms.double(0.2),
            IDname = cms.string('ByTightMuonRejectionSimple'),
            doCaloMuonVeto = cms.bool(True),
            maxNumberOfHitsLast2Stations = cms.int32(0),
            maxNumberOfMatches = cms.int32(1),
            maxNumberOfRPCMuons = cms.int32(-1),
            maxNumberOfSTAMuons = cms.int32(-1)
        )
    ),
    IDdefinitions = cms.VPSet(),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    dRmuonMatch = cms.double(0.3),
    dRmuonMatchLimitedToJetArea = cms.bool(False),
    maskHitsCSC = cms.vint32(0, 0, 0, 0),
    maskHitsDT = cms.vint32(0, 0, 0, 0),
    maskHitsRPC = cms.vint32(0, 0, 0, 0),
    maskMatchesCSC = cms.vint32(1, 0, 0, 0),
    maskMatchesDT = cms.vint32(0, 0, 0, 0),
    maskMatchesRPC = cms.vint32(0, 0, 0, 0),
    mightGet = cms.optional.untracked.vstring,
    minPtMatchedMuon = cms.double(5),
    srcPatMuons = cms.InputTag("slimmedMuons"),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByMuonRejectionSimpleBoosted = cms.EDProducer("PFRecoTauDiscriminationAgainstMuonSimple",
    IDWPdefinitions = cms.VPSet(
        cms.PSet(
            HoPMin = cms.double(0.2),
            IDname = cms.string('ByLooseMuonRejectionSimple'),
            doCaloMuonVeto = cms.bool(True),
            maxNumberOfHitsLast2Stations = cms.int32(-1),
            maxNumberOfMatches = cms.int32(1),
            maxNumberOfRPCMuons = cms.int32(-1),
            maxNumberOfSTAMuons = cms.int32(-1)
        ),
        cms.PSet(
            HoPMin = cms.double(0.2),
            IDname = cms.string('ByTightMuonRejectionSimple'),
            doCaloMuonVeto = cms.bool(True),
            maxNumberOfHitsLast2Stations = cms.int32(0),
            maxNumberOfMatches = cms.int32(1),
            maxNumberOfRPCMuons = cms.int32(-1),
            maxNumberOfSTAMuons = cms.int32(-1)
        )
    ),
    IDdefinitions = cms.VPSet(),
    PFTauProducer = cms.InputTag("hpsPFTauProducerBoosted"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    dRmuonMatch = cms.double(0.3),
    dRmuonMatchLimitedToJetArea = cms.bool(False),
    maskHitsCSC = cms.vint32(0, 0, 0, 0),
    maskHitsDT = cms.vint32(0, 0, 0, 0),
    maskHitsRPC = cms.vint32(0, 0, 0, 0),
    maskMatchesCSC = cms.vint32(1, 0, 0, 0),
    maskMatchesDT = cms.vint32(0, 0, 0, 0),
    maskMatchesRPC = cms.vint32(0, 0, 0, 0),
    mightGet = cms.optional.untracked.vstring,
    minPtMatchedMuon = cms.double(5),
    srcPatMuons = cms.InputTag("slimmedMuons"),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByMuonRejectionSimpleElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationAgainstMuonSimple",
    IDWPdefinitions = cms.VPSet(
        cms.PSet(
            HoPMin = cms.double(0.2),
            IDname = cms.string('ByLooseMuonRejectionSimple'),
            doCaloMuonVeto = cms.bool(True),
            maxNumberOfHitsLast2Stations = cms.int32(-1),
            maxNumberOfMatches = cms.int32(1),
            maxNumberOfRPCMuons = cms.int32(-1),
            maxNumberOfSTAMuons = cms.int32(-1)
        ),
        cms.PSet(
            HoPMin = cms.double(0.2),
            IDname = cms.string('ByTightMuonRejectionSimple'),
            doCaloMuonVeto = cms.bool(True),
            maxNumberOfHitsLast2Stations = cms.int32(0),
            maxNumberOfMatches = cms.int32(1),
            maxNumberOfRPCMuons = cms.int32(-1),
            maxNumberOfSTAMuons = cms.int32(-1)
        )
    ),
    IDdefinitions = cms.VPSet(),
    PFTauProducer = cms.InputTag("hpsPFTauProducerElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    dRmuonMatch = cms.double(0.3),
    dRmuonMatchLimitedToJetArea = cms.bool(False),
    maskHitsCSC = cms.vint32(0, 0, 0, 0),
    maskHitsDT = cms.vint32(0, 0, 0, 0),
    maskHitsRPC = cms.vint32(0, 0, 0, 0),
    maskMatchesCSC = cms.vint32(1, 0, 0, 0),
    maskMatchesDT = cms.vint32(0, 0, 0, 0),
    maskMatchesRPC = cms.vint32(0, 0, 0, 0),
    mightGet = cms.optional.untracked.vstring,
    minPtMatchedMuon = cms.double(5),
    srcPatMuons = cms.InputTag("slimmedMuons"),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByMuonRejectionSimpleLowPtElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationAgainstMuonSimple",
    IDWPdefinitions = cms.VPSet(
        cms.PSet(
            HoPMin = cms.double(0.2),
            IDname = cms.string('ByLooseMuonRejectionSimple'),
            doCaloMuonVeto = cms.bool(True),
            maxNumberOfHitsLast2Stations = cms.int32(-1),
            maxNumberOfMatches = cms.int32(1),
            maxNumberOfRPCMuons = cms.int32(-1),
            maxNumberOfSTAMuons = cms.int32(-1)
        ),
        cms.PSet(
            HoPMin = cms.double(0.2),
            IDname = cms.string('ByTightMuonRejectionSimple'),
            doCaloMuonVeto = cms.bool(True),
            maxNumberOfHitsLast2Stations = cms.int32(0),
            maxNumberOfMatches = cms.int32(1),
            maxNumberOfRPCMuons = cms.int32(-1),
            maxNumberOfSTAMuons = cms.int32(-1)
        )
    ),
    IDdefinitions = cms.VPSet(),
    PFTauProducer = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    dRmuonMatch = cms.double(0.3),
    dRmuonMatchLimitedToJetArea = cms.bool(False),
    maskHitsCSC = cms.vint32(0, 0, 0, 0),
    maskHitsDT = cms.vint32(0, 0, 0, 0),
    maskHitsRPC = cms.vint32(0, 0, 0, 0),
    maskMatchesCSC = cms.vint32(1, 0, 0, 0),
    maskMatchesDT = cms.vint32(0, 0, 0, 0),
    maskMatchesRPC = cms.vint32(0, 0, 0, 0),
    mightGet = cms.optional.untracked.vstring,
    minPtMatchedMuon = cms.double(5),
    srcPatMuons = cms.InputTag("slimmedMuons"),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByMuonRejectionSimpleMuonCleaned = cms.EDProducer("PFRecoTauDiscriminationAgainstMuonSimple",
    IDWPdefinitions = cms.VPSet(
        cms.PSet(
            HoPMin = cms.double(0.2),
            IDname = cms.string('ByLooseMuonRejectionSimple'),
            doCaloMuonVeto = cms.bool(True),
            maxNumberOfHitsLast2Stations = cms.int32(-1),
            maxNumberOfMatches = cms.int32(1),
            maxNumberOfRPCMuons = cms.int32(-1),
            maxNumberOfSTAMuons = cms.int32(-1)
        ),
        cms.PSet(
            HoPMin = cms.double(0.2),
            IDname = cms.string('ByTightMuonRejectionSimple'),
            doCaloMuonVeto = cms.bool(True),
            maxNumberOfHitsLast2Stations = cms.int32(0),
            maxNumberOfMatches = cms.int32(1),
            maxNumberOfRPCMuons = cms.int32(-1),
            maxNumberOfSTAMuons = cms.int32(-1)
        )
    ),
    IDdefinitions = cms.VPSet(),
    PFTauProducer = cms.InputTag("hpsPFTauProducerMuonCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    dRmuonMatch = cms.double(0.3),
    dRmuonMatchLimitedToJetArea = cms.bool(False),
    maskHitsCSC = cms.vint32(0, 0, 0, 0),
    maskHitsDT = cms.vint32(0, 0, 0, 0),
    maskHitsRPC = cms.vint32(0, 0, 0, 0),
    maskMatchesCSC = cms.vint32(1, 0, 0, 0),
    maskMatchesDT = cms.vint32(0, 0, 0, 0),
    maskMatchesRPC = cms.vint32(0, 0, 0, 0),
    mightGet = cms.optional.untracked.vstring,
    minPtMatchedMuon = cms.double(5),
    srcPatMuons = cms.InputTag("slimmedMuons"),
    verbosity = cms.int32(0)
)


process.hpsPFTauDiscriminationByTightElectronRejection = cms.EDProducer("PFRecoTauDiscriminationAgainstElectron",
    ApplyCut_BremCombined = cms.bool(True),
    ApplyCut_BremsRecoveryEOverPLead = cms.bool(False),
    ApplyCut_EOverPLead = cms.bool(False),
    ApplyCut_EcalCrackCut = cms.bool(True),
    ApplyCut_ElectronPreID = cms.bool(False),
    ApplyCut_ElectronPreID_2D = cms.bool(False),
    ApplyCut_EmFraction = cms.bool(False),
    ApplyCut_Hcal3x3OverPLead = cms.bool(False),
    ApplyCut_HcalMaxOverPLead = cms.bool(False),
    ApplyCut_HcalTotOverPLead = cms.bool(False),
    ApplyCut_PFElectronMVA = cms.bool(True),
    BremCombined_Fraction = cms.double(0.99),
    BremCombined_HOP = cms.double(0.1),
    BremCombined_Mass = cms.double(0.55),
    BremCombined_StripSize = cms.double(0.03),
    BremsRecoveryEOverPLead_maxValue = cms.double(1.8),
    BremsRecoveryEOverPLead_minValue = cms.double(0.8),
    EOverPLead_maxValue = cms.double(1.8),
    EOverPLead_minValue = cms.double(0.8),
    ElecPreID0_EOverPLead_maxValue = cms.double(0.95),
    ElecPreID0_HOverPLead_minValue = cms.double(0.05),
    ElecPreID1_EOverPLead_maxValue = cms.double(0.8),
    ElecPreID1_HOverPLead_minValue = cms.double(0.15),
    EmFraction_maxValue = cms.double(0.9),
    Hcal3x3OverPLead_minValue = cms.double(0.1),
    HcalMaxOverPLead_minValue = cms.double(0.1),
    HcalTotOverPLead_minValue = cms.double(0.1),
    PFElectronMVA_maxValue = cms.double(-0.1),
    PFTauProducer = cms.InputTag("hpsPFTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    )
)


process.hpsPFTauDiscriminationByTightElectronRejectionBoosted = cms.EDProducer("PFRecoTauDiscriminationAgainstElectron",
    ApplyCut_BremCombined = cms.bool(True),
    ApplyCut_BremsRecoveryEOverPLead = cms.bool(False),
    ApplyCut_EOverPLead = cms.bool(False),
    ApplyCut_EcalCrackCut = cms.bool(True),
    ApplyCut_ElectronPreID = cms.bool(False),
    ApplyCut_ElectronPreID_2D = cms.bool(False),
    ApplyCut_EmFraction = cms.bool(False),
    ApplyCut_Hcal3x3OverPLead = cms.bool(False),
    ApplyCut_HcalMaxOverPLead = cms.bool(False),
    ApplyCut_HcalTotOverPLead = cms.bool(False),
    ApplyCut_PFElectronMVA = cms.bool(True),
    BremCombined_Fraction = cms.double(0.99),
    BremCombined_HOP = cms.double(0.1),
    BremCombined_Mass = cms.double(0.55),
    BremCombined_StripSize = cms.double(0.03),
    BremsRecoveryEOverPLead_maxValue = cms.double(1.8),
    BremsRecoveryEOverPLead_minValue = cms.double(0.8),
    EOverPLead_maxValue = cms.double(1.8),
    EOverPLead_minValue = cms.double(0.8),
    ElecPreID0_EOverPLead_maxValue = cms.double(0.95),
    ElecPreID0_HOverPLead_minValue = cms.double(0.05),
    ElecPreID1_EOverPLead_maxValue = cms.double(0.8),
    ElecPreID1_HOverPLead_minValue = cms.double(0.15),
    EmFraction_maxValue = cms.double(0.9),
    Hcal3x3OverPLead_minValue = cms.double(0.1),
    HcalMaxOverPLead_minValue = cms.double(0.1),
    HcalTotOverPLead_minValue = cms.double(0.1),
    PFElectronMVA_maxValue = cms.double(-0.1),
    PFTauProducer = cms.InputTag("hpsPFTauProducerBoosted"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    )
)


process.hpsPFTauDiscriminationByTightElectronRejectionElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationAgainstElectron",
    ApplyCut_BremCombined = cms.bool(True),
    ApplyCut_BremsRecoveryEOverPLead = cms.bool(False),
    ApplyCut_EOverPLead = cms.bool(False),
    ApplyCut_EcalCrackCut = cms.bool(True),
    ApplyCut_ElectronPreID = cms.bool(False),
    ApplyCut_ElectronPreID_2D = cms.bool(False),
    ApplyCut_EmFraction = cms.bool(False),
    ApplyCut_Hcal3x3OverPLead = cms.bool(False),
    ApplyCut_HcalMaxOverPLead = cms.bool(False),
    ApplyCut_HcalTotOverPLead = cms.bool(False),
    ApplyCut_PFElectronMVA = cms.bool(True),
    BremCombined_Fraction = cms.double(0.99),
    BremCombined_HOP = cms.double(0.1),
    BremCombined_Mass = cms.double(0.55),
    BremCombined_StripSize = cms.double(0.03),
    BremsRecoveryEOverPLead_maxValue = cms.double(1.8),
    BremsRecoveryEOverPLead_minValue = cms.double(0.8),
    EOverPLead_maxValue = cms.double(1.8),
    EOverPLead_minValue = cms.double(0.8),
    ElecPreID0_EOverPLead_maxValue = cms.double(0.95),
    ElecPreID0_HOverPLead_minValue = cms.double(0.05),
    ElecPreID1_EOverPLead_maxValue = cms.double(0.8),
    ElecPreID1_HOverPLead_minValue = cms.double(0.15),
    EmFraction_maxValue = cms.double(0.9),
    Hcal3x3OverPLead_minValue = cms.double(0.1),
    HcalMaxOverPLead_minValue = cms.double(0.1),
    HcalTotOverPLead_minValue = cms.double(0.1),
    PFElectronMVA_maxValue = cms.double(-0.1),
    PFTauProducer = cms.InputTag("hpsPFTauProducerElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    )
)


process.hpsPFTauDiscriminationByTightElectronRejectionLowPtElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationAgainstElectron",
    ApplyCut_BremCombined = cms.bool(True),
    ApplyCut_BremsRecoveryEOverPLead = cms.bool(False),
    ApplyCut_EOverPLead = cms.bool(False),
    ApplyCut_EcalCrackCut = cms.bool(True),
    ApplyCut_ElectronPreID = cms.bool(False),
    ApplyCut_ElectronPreID_2D = cms.bool(False),
    ApplyCut_EmFraction = cms.bool(False),
    ApplyCut_Hcal3x3OverPLead = cms.bool(False),
    ApplyCut_HcalMaxOverPLead = cms.bool(False),
    ApplyCut_HcalTotOverPLead = cms.bool(False),
    ApplyCut_PFElectronMVA = cms.bool(True),
    BremCombined_Fraction = cms.double(0.99),
    BremCombined_HOP = cms.double(0.1),
    BremCombined_Mass = cms.double(0.55),
    BremCombined_StripSize = cms.double(0.03),
    BremsRecoveryEOverPLead_maxValue = cms.double(1.8),
    BremsRecoveryEOverPLead_minValue = cms.double(0.8),
    EOverPLead_maxValue = cms.double(1.8),
    EOverPLead_minValue = cms.double(0.8),
    ElecPreID0_EOverPLead_maxValue = cms.double(0.95),
    ElecPreID0_HOverPLead_minValue = cms.double(0.05),
    ElecPreID1_EOverPLead_maxValue = cms.double(0.8),
    ElecPreID1_HOverPLead_minValue = cms.double(0.15),
    EmFraction_maxValue = cms.double(0.9),
    Hcal3x3OverPLead_minValue = cms.double(0.1),
    HcalMaxOverPLead_minValue = cms.double(0.1),
    HcalTotOverPLead_minValue = cms.double(0.1),
    PFElectronMVA_maxValue = cms.double(-0.1),
    PFTauProducer = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    )
)


process.hpsPFTauDiscriminationByTightElectronRejectionMuonCleaned = cms.EDProducer("PFRecoTauDiscriminationAgainstElectron",
    ApplyCut_BremCombined = cms.bool(True),
    ApplyCut_BremsRecoveryEOverPLead = cms.bool(False),
    ApplyCut_EOverPLead = cms.bool(False),
    ApplyCut_EcalCrackCut = cms.bool(True),
    ApplyCut_ElectronPreID = cms.bool(False),
    ApplyCut_ElectronPreID_2D = cms.bool(False),
    ApplyCut_EmFraction = cms.bool(False),
    ApplyCut_Hcal3x3OverPLead = cms.bool(False),
    ApplyCut_HcalMaxOverPLead = cms.bool(False),
    ApplyCut_HcalTotOverPLead = cms.bool(False),
    ApplyCut_PFElectronMVA = cms.bool(True),
    BremCombined_Fraction = cms.double(0.99),
    BremCombined_HOP = cms.double(0.1),
    BremCombined_Mass = cms.double(0.55),
    BremCombined_StripSize = cms.double(0.03),
    BremsRecoveryEOverPLead_maxValue = cms.double(1.8),
    BremsRecoveryEOverPLead_minValue = cms.double(0.8),
    EOverPLead_maxValue = cms.double(1.8),
    EOverPLead_minValue = cms.double(0.8),
    ElecPreID0_EOverPLead_maxValue = cms.double(0.95),
    ElecPreID0_HOverPLead_minValue = cms.double(0.05),
    ElecPreID1_EOverPLead_maxValue = cms.double(0.8),
    ElecPreID1_HOverPLead_minValue = cms.double(0.15),
    EmFraction_maxValue = cms.double(0.9),
    Hcal3x3OverPLead_minValue = cms.double(0.1),
    HcalMaxOverPLead_minValue = cms.double(0.1),
    HcalTotOverPLead_minValue = cms.double(0.1),
    PFElectronMVA_maxValue = cms.double(-0.1),
    PFTauProducer = cms.InputTag("hpsPFTauProducerMuonCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    )
)


process.hpsPFTauPrimaryVertexProducer = cms.EDProducer("PFTauMiniAODPrimaryVertexProducer",
    Algorithm = cms.int32(0),
    ElectronTag = cms.InputTag(""),
    MuonTag = cms.InputTag(""),
    PFTauTag = cms.InputTag("hpsPFTauProducer"),
    PVTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    RemoveElectronTracks = cms.bool(False),
    RemoveMuonTracks = cms.bool(False),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    cut = cms.string('pt > 18.0 & abs(eta) < 2.4'),
    discriminators = cms.VPSet(cms.PSet(
        discriminator = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
        selectionCut = cms.double(0.5)
    )),
    lostCandidatesTag = cms.InputTag("lostTracks"),
    mightGet = cms.optional.untracked.vstring,
    packedCandidatesTag = cms.InputTag("packedPFCandidates"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(1.5),
            minTrackHits = cms.uint32(8),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(1.0),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    useBeamSpot = cms.bool(True),
    useSelectedTaus = cms.bool(False)
)


process.hpsPFTauPrimaryVertexProducerBoosted = cms.EDProducer("PFTauPrimaryVertexProducer",
    Algorithm = cms.int32(0),
    ElectronTag = cms.InputTag(""),
    MuonTag = cms.InputTag(""),
    PFTauTag = cms.InputTag("hpsPFTauProducerBoosted"),
    PVTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    RemoveElectronTracks = cms.bool(False),
    RemoveMuonTracks = cms.bool(False),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    cut = cms.string('pt > 18.0 & abs(eta) < 2.4'),
    discriminators = cms.VPSet(cms.PSet(
        discriminator = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsBoosted"),
        selectionCut = cms.double(0.5)
    )),
    mightGet = cms.optional.untracked.vstring,
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(1.5),
            minTrackHits = cms.uint32(8),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(1.0),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    useBeamSpot = cms.bool(True),
    useSelectedTaus = cms.bool(False)
)


process.hpsPFTauPrimaryVertexProducerElectronCleaned = cms.EDProducer("PFTauMiniAODPrimaryVertexProducer",
    Algorithm = cms.int32(0),
    ElectronTag = cms.InputTag(""),
    MuonTag = cms.InputTag(""),
    PFTauTag = cms.InputTag("hpsPFTauProducerElectronCleaned"),
    PVTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    RemoveElectronTracks = cms.bool(False),
    RemoveMuonTracks = cms.bool(False),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    cut = cms.string('pt > 18.0 & abs(eta) < 2.4'),
    discriminators = cms.VPSet(cms.PSet(
        discriminator = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsElectronCleaned"),
        selectionCut = cms.double(0.5)
    )),
    lostCandidatesTag = cms.InputTag("lostTracks"),
    mightGet = cms.optional.untracked.vstring,
    packedCandidatesTag = cms.InputTag("PackedCandsElectronCleaned","packedPFCandidatesElectronCleaned"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(1.5),
            minTrackHits = cms.uint32(8),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(1.0),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    useBeamSpot = cms.bool(True),
    useSelectedTaus = cms.bool(False)
)


process.hpsPFTauPrimaryVertexProducerLowPtElectronCleaned = cms.EDProducer("PFTauMiniAODPrimaryVertexProducer",
    Algorithm = cms.int32(0),
    ElectronTag = cms.InputTag(""),
    MuonTag = cms.InputTag(""),
    PFTauTag = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned"),
    PVTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    RemoveElectronTracks = cms.bool(False),
    RemoveMuonTracks = cms.bool(False),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    cut = cms.string('pt > 18.0 & abs(eta) < 2.4'),
    discriminators = cms.VPSet(cms.PSet(
        discriminator = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsLowPtElectronCleaned"),
        selectionCut = cms.double(0.5)
    )),
    lostCandidatesTag = cms.InputTag("lostTracks"),
    mightGet = cms.optional.untracked.vstring,
    packedCandidatesTag = cms.InputTag("PackedCandsLowPtElectronCleaned","packedPFCandidatesLowPtElectronCleaned"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(1.5),
            minTrackHits = cms.uint32(8),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(1.0),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    useBeamSpot = cms.bool(True),
    useSelectedTaus = cms.bool(False)
)


process.hpsPFTauPrimaryVertexProducerMuonCleaned = cms.EDProducer("PFTauMiniAODPrimaryVertexProducer",
    Algorithm = cms.int32(0),
    ElectronTag = cms.InputTag(""),
    MuonTag = cms.InputTag(""),
    PFTauTag = cms.InputTag("hpsPFTauProducerMuonCleaned"),
    PVTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    RemoveElectronTracks = cms.bool(False),
    RemoveMuonTracks = cms.bool(False),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    cut = cms.string('pt > 18.0 & abs(eta) < 2.4'),
    discriminators = cms.VPSet(cms.PSet(
        discriminator = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsMuonCleaned"),
        selectionCut = cms.double(0.5)
    )),
    lostCandidatesTag = cms.InputTag("lostTracks"),
    mightGet = cms.optional.untracked.vstring,
    packedCandidatesTag = cms.InputTag("PackedCandsMuonCleaned","packedPFCandidatesMuonCleaned"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(1.5),
            minTrackHits = cms.uint32(8),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(1.0),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    useBeamSpot = cms.bool(True),
    useSelectedTaus = cms.bool(False)
)


process.hpsPFTauProducer = cms.EDProducer("RecoTauPiZeroUnembedder",
    src = cms.InputTag("hpsPFTauProducerSansRefs")
)


process.hpsPFTauProducerBoosted = cms.EDProducer("RecoTauPiZeroUnembedder",
    src = cms.InputTag("hpsPFTauProducerSansRefsBoosted")
)


process.hpsPFTauProducerElectronCleaned = cms.EDProducer("RecoTauPiZeroUnembedder",
    src = cms.InputTag("hpsPFTauProducerSansRefsElectronCleaned")
)


process.hpsPFTauProducerLowPtElectronCleaned = cms.EDProducer("RecoTauPiZeroUnembedder",
    src = cms.InputTag("hpsPFTauProducerSansRefsLowPtElectronCleaned")
)


process.hpsPFTauProducerMuonCleaned = cms.EDProducer("RecoTauPiZeroUnembedder",
    src = cms.InputTag("hpsPFTauProducerSansRefsMuonCleaned")
)


process.hpsPFTauProducerSansRefs = cms.EDProducer("RecoTauCleaner",
    cleaners = cms.VPSet(
        cms.PSet(
            name = cms.string('Charge'),
            nprongs = cms.vuint32(1, 3),
            passForCharge = cms.int32(1),
            plugin = cms.string('RecoTauChargeCleanerPlugin'),
            selectionFailValue = cms.double(0),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            name = cms.string('HPS_Select'),
            plugin = cms.string('RecoTauDiscriminantCleanerPlugin'),
            src = cms.InputTag("hpsSelectionDiscriminator"),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            minTrackPt = cms.double(5.0),
            name = cms.string('killSoftTwoProngTaus'),
            plugin = cms.string('RecoTauSoftTwoProngTausCleanerPlugin'),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            name = cms.string('ChargedHadronMultiplicity'),
            plugin = cms.string('RecoTauChargedHadronMultiplicityCleanerPlugin'),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            name = cms.string('Pt'),
            plugin = cms.string('RecoTauStringCleanerPlugin'),
            selection = cms.string('leadCand().isNonnull()'),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('-pt()'),
            tolerance = cms.double(0.01)
        ),
        cms.PSet(
            name = cms.string('StripMultiplicity'),
            plugin = cms.string('RecoTauStringCleanerPlugin'),
            selection = cms.string('leadCand().isNonnull()'),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('-signalPiZeroCandidates().size()'),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            name = cms.string('CombinedIsolation'),
            plugin = cms.string('RecoTauStringCleanerPlugin'),
            selection = cms.string('leadCand().isNonnull()'),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('isolationPFChargedHadrCandsPtSum() + isolationPFGammaCandsEtSum()'),
            tolerance = cms.double(0)
        )
    ),
    outputSelection = cms.string(''),
    src = cms.InputTag("combinatoricRecoTaus"),
    verbosity = cms.int32(0)
)


process.hpsPFTauProducerSansRefsBoosted = cms.EDProducer("RecoTauCleaner",
    cleaners = cms.VPSet(
        cms.PSet(
            name = cms.string('Charge'),
            nprongs = cms.vuint32(1, 3),
            passForCharge = cms.int32(1),
            plugin = cms.string('RecoTauChargeCleanerPlugin'),
            selectionFailValue = cms.double(0),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            name = cms.string('HPS_Select'),
            plugin = cms.string('RecoTauDiscriminantCleanerPlugin'),
            src = cms.InputTag("hpsSelectionDiscriminatorBoosted"),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            minTrackPt = cms.double(5.0),
            name = cms.string('killSoftTwoProngTaus'),
            plugin = cms.string('RecoTauSoftTwoProngTausCleanerPlugin'),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            name = cms.string('ChargedHadronMultiplicity'),
            plugin = cms.string('RecoTauChargedHadronMultiplicityCleanerPlugin'),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            name = cms.string('Pt'),
            plugin = cms.string('RecoTauStringCleanerPlugin'),
            selection = cms.string('leadCand().isNonnull()'),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('-pt()'),
            tolerance = cms.double(0.01)
        ),
        cms.PSet(
            name = cms.string('StripMultiplicity'),
            plugin = cms.string('RecoTauStringCleanerPlugin'),
            selection = cms.string('leadCand().isNonnull()'),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('-signalPiZeroCandidates().size()'),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            name = cms.string('CombinedIsolation'),
            plugin = cms.string('RecoTauStringCleanerPlugin'),
            selection = cms.string('leadCand().isNonnull()'),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('isolationPFChargedHadrCandsPtSum() + isolationPFGammaCandsEtSum()'),
            tolerance = cms.double(0)
        )
    ),
    outputSelection = cms.string(''),
    src = cms.InputTag("combinatoricRecoTausBoosted"),
    verbosity = cms.int32(0)
)


process.hpsPFTauProducerSansRefsElectronCleaned = cms.EDProducer("RecoTauCleaner",
    cleaners = cms.VPSet(
        cms.PSet(
            name = cms.string('Charge'),
            nprongs = cms.vuint32(1, 3),
            passForCharge = cms.int32(1),
            plugin = cms.string('RecoTauChargeCleanerPlugin'),
            selectionFailValue = cms.double(0),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            name = cms.string('HPS_Select'),
            plugin = cms.string('RecoTauDiscriminantCleanerPlugin'),
            src = cms.InputTag("hpsSelectionDiscriminatorElectronCleaned"),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            minTrackPt = cms.double(5.0),
            name = cms.string('killSoftTwoProngTaus'),
            plugin = cms.string('RecoTauSoftTwoProngTausCleanerPlugin'),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            name = cms.string('ChargedHadronMultiplicity'),
            plugin = cms.string('RecoTauChargedHadronMultiplicityCleanerPlugin'),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            name = cms.string('Pt'),
            plugin = cms.string('RecoTauStringCleanerPlugin'),
            selection = cms.string('leadCand().isNonnull()'),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('-pt()'),
            tolerance = cms.double(0.01)
        ),
        cms.PSet(
            name = cms.string('StripMultiplicity'),
            plugin = cms.string('RecoTauStringCleanerPlugin'),
            selection = cms.string('leadCand().isNonnull()'),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('-signalPiZeroCandidates().size()'),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            name = cms.string('CombinedIsolation'),
            plugin = cms.string('RecoTauStringCleanerPlugin'),
            selection = cms.string('leadCand().isNonnull()'),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('isolationPFChargedHadrCandsPtSum() + isolationPFGammaCandsEtSum()'),
            tolerance = cms.double(0)
        )
    ),
    outputSelection = cms.string(''),
    src = cms.InputTag("combinatoricRecoTausElectronCleaned"),
    verbosity = cms.int32(0)
)


process.hpsPFTauProducerSansRefsLowPtElectronCleaned = cms.EDProducer("RecoTauCleaner",
    cleaners = cms.VPSet(
        cms.PSet(
            name = cms.string('Charge'),
            nprongs = cms.vuint32(1, 3),
            passForCharge = cms.int32(1),
            plugin = cms.string('RecoTauChargeCleanerPlugin'),
            selectionFailValue = cms.double(0),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            name = cms.string('HPS_Select'),
            plugin = cms.string('RecoTauDiscriminantCleanerPlugin'),
            src = cms.InputTag("hpsSelectionDiscriminatorLowPtElectronCleaned"),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            minTrackPt = cms.double(5.0),
            name = cms.string('killSoftTwoProngTaus'),
            plugin = cms.string('RecoTauSoftTwoProngTausCleanerPlugin'),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            name = cms.string('ChargedHadronMultiplicity'),
            plugin = cms.string('RecoTauChargedHadronMultiplicityCleanerPlugin'),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            name = cms.string('Pt'),
            plugin = cms.string('RecoTauStringCleanerPlugin'),
            selection = cms.string('leadCand().isNonnull()'),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('-pt()'),
            tolerance = cms.double(0.01)
        ),
        cms.PSet(
            name = cms.string('StripMultiplicity'),
            plugin = cms.string('RecoTauStringCleanerPlugin'),
            selection = cms.string('leadCand().isNonnull()'),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('-signalPiZeroCandidates().size()'),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            name = cms.string('CombinedIsolation'),
            plugin = cms.string('RecoTauStringCleanerPlugin'),
            selection = cms.string('leadCand().isNonnull()'),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('isolationPFChargedHadrCandsPtSum() + isolationPFGammaCandsEtSum()'),
            tolerance = cms.double(0)
        )
    ),
    outputSelection = cms.string(''),
    src = cms.InputTag("combinatoricRecoTausLowPtElectronCleaned"),
    verbosity = cms.int32(0)
)


process.hpsPFTauProducerSansRefsMuonCleaned = cms.EDProducer("RecoTauCleaner",
    cleaners = cms.VPSet(
        cms.PSet(
            name = cms.string('Charge'),
            nprongs = cms.vuint32(1, 3),
            passForCharge = cms.int32(1),
            plugin = cms.string('RecoTauChargeCleanerPlugin'),
            selectionFailValue = cms.double(0),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            name = cms.string('HPS_Select'),
            plugin = cms.string('RecoTauDiscriminantCleanerPlugin'),
            src = cms.InputTag("hpsSelectionDiscriminatorMuonCleaned"),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            minTrackPt = cms.double(5.0),
            name = cms.string('killSoftTwoProngTaus'),
            plugin = cms.string('RecoTauSoftTwoProngTausCleanerPlugin'),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            name = cms.string('ChargedHadronMultiplicity'),
            plugin = cms.string('RecoTauChargedHadronMultiplicityCleanerPlugin'),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            name = cms.string('Pt'),
            plugin = cms.string('RecoTauStringCleanerPlugin'),
            selection = cms.string('leadCand().isNonnull()'),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('-pt()'),
            tolerance = cms.double(0.01)
        ),
        cms.PSet(
            name = cms.string('StripMultiplicity'),
            plugin = cms.string('RecoTauStringCleanerPlugin'),
            selection = cms.string('leadCand().isNonnull()'),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('-signalPiZeroCandidates().size()'),
            tolerance = cms.double(0)
        ),
        cms.PSet(
            name = cms.string('CombinedIsolation'),
            plugin = cms.string('RecoTauStringCleanerPlugin'),
            selection = cms.string('leadCand().isNonnull()'),
            selectionFailValue = cms.double(1000.0),
            selectionPassFunction = cms.string('isolationPFChargedHadrCandsPtSum() + isolationPFGammaCandsEtSum()'),
            tolerance = cms.double(0)
        )
    ),
    outputSelection = cms.string(''),
    src = cms.InputTag("combinatoricRecoTausMuonCleaned"),
    verbosity = cms.int32(0)
)


process.hpsPFTauSecondaryVertexProducer = cms.EDProducer("PFTauSecondaryVertexProducer",
    PFTauTag = cms.InputTag("hpsPFTauProducer")
)


process.hpsPFTauSecondaryVertexProducerBoosted = cms.EDProducer("PFTauSecondaryVertexProducer",
    PFTauTag = cms.InputTag("hpsPFTauProducerBoosted")
)


process.hpsPFTauSecondaryVertexProducerElectronCleaned = cms.EDProducer("PFTauSecondaryVertexProducer",
    PFTauTag = cms.InputTag("hpsPFTauProducerElectronCleaned")
)


process.hpsPFTauSecondaryVertexProducerLowPtElectronCleaned = cms.EDProducer("PFTauSecondaryVertexProducer",
    PFTauTag = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned")
)


process.hpsPFTauSecondaryVertexProducerMuonCleaned = cms.EDProducer("PFTauSecondaryVertexProducer",
    PFTauTag = cms.InputTag("hpsPFTauProducerMuonCleaned")
)


process.hpsPFTauTransverseImpactParameters = cms.EDProducer("PFTauTransverseImpactParameters",
    PFTauPVATag = cms.InputTag("hpsPFTauPrimaryVertexProducer"),
    PFTauSVATag = cms.InputTag("hpsPFTauSecondaryVertexProducer"),
    PFTauTag = cms.InputTag("hpsPFTauProducer"),
    useFullCalculation = cms.bool(True)
)


process.hpsPFTauTransverseImpactParametersBoosted = cms.EDProducer("PFTauTransverseImpactParameters",
    PFTauPVATag = cms.InputTag("hpsPFTauPrimaryVertexProducerBoosted"),
    PFTauSVATag = cms.InputTag("hpsPFTauSecondaryVertexProducerBoosted"),
    PFTauTag = cms.InputTag("hpsPFTauProducerBoosted"),
    useFullCalculation = cms.bool(True)
)


process.hpsPFTauTransverseImpactParametersElectronCleaned = cms.EDProducer("PFTauTransverseImpactParameters",
    PFTauPVATag = cms.InputTag("hpsPFTauPrimaryVertexProducerElectronCleaned"),
    PFTauSVATag = cms.InputTag("hpsPFTauSecondaryVertexProducerElectronCleaned"),
    PFTauTag = cms.InputTag("hpsPFTauProducerElectronCleaned"),
    useFullCalculation = cms.bool(True)
)


process.hpsPFTauTransverseImpactParametersLowPtElectronCleaned = cms.EDProducer("PFTauTransverseImpactParameters",
    PFTauPVATag = cms.InputTag("hpsPFTauPrimaryVertexProducerLowPtElectronCleaned"),
    PFTauSVATag = cms.InputTag("hpsPFTauSecondaryVertexProducerLowPtElectronCleaned"),
    PFTauTag = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned"),
    useFullCalculation = cms.bool(True)
)


process.hpsPFTauTransverseImpactParametersMuonCleaned = cms.EDProducer("PFTauTransverseImpactParameters",
    PFTauPVATag = cms.InputTag("hpsPFTauPrimaryVertexProducerMuonCleaned"),
    PFTauSVATag = cms.InputTag("hpsPFTauSecondaryVertexProducerMuonCleaned"),
    PFTauTag = cms.InputTag("hpsPFTauProducerMuonCleaned"),
    useFullCalculation = cms.bool(True)
)


process.hpsSelectionDiscriminator = cms.EDProducer("PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag("combinatoricRecoTaus"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    decayModes = cms.VPSet(
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(-1000.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.1349),
            maxMass = cms.string('max(1.3, min(1.3*sqrt(pt/100.), 4.2))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.3),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(0.2),
            minMass = cms.double(0.4),
            minPi0Mass = cms.double(0.05),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(2),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.2'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(2),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(2),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.5'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.8),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.6'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.9),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(2)
        )
    ),
    matchingCone = cms.double(0.5),
    minPixelHits = cms.int32(1),
    minTauPt = cms.double(0.0),
    requireTauChargedHadronsToBeChargedPFCands = cms.bool(False),
    verbosity = cms.int32(0)
)


process.hpsSelectionDiscriminatorBoosted = cms.EDProducer("PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag("combinatoricRecoTausBoosted"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    decayModes = cms.VPSet(
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(-1000.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.1349),
            maxMass = cms.string('max(1.3, min(1.3*sqrt(pt/100.), 4.2))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.3),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(0.2),
            minMass = cms.double(0.4),
            minPi0Mass = cms.double(0.05),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(2),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.2'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(2),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(2),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.5'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.8),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.6'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.9),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(2)
        )
    ),
    matchingCone = cms.double(0.5),
    minPixelHits = cms.int32(1),
    minTauPt = cms.double(0.0),
    requireTauChargedHadronsToBeChargedPFCands = cms.bool(False),
    verbosity = cms.int32(0)
)


process.hpsSelectionDiscriminatorElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag("combinatoricRecoTausElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    decayModes = cms.VPSet(
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(-1000.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.1349),
            maxMass = cms.string('max(1.3, min(1.3*sqrt(pt/100.), 4.2))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.3),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(0.2),
            minMass = cms.double(0.4),
            minPi0Mass = cms.double(0.05),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(2),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.2'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(2),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(2),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.5'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.8),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.6'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.9),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(2)
        )
    ),
    matchingCone = cms.double(0.5),
    minPixelHits = cms.int32(1),
    minTauPt = cms.double(0.0),
    requireTauChargedHadronsToBeChargedPFCands = cms.bool(False),
    verbosity = cms.int32(0)
)


process.hpsSelectionDiscriminatorLowPtElectronCleaned = cms.EDProducer("PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag("combinatoricRecoTausLowPtElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    decayModes = cms.VPSet(
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(-1000.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.1349),
            maxMass = cms.string('max(1.3, min(1.3*sqrt(pt/100.), 4.2))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.3),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(0.2),
            minMass = cms.double(0.4),
            minPi0Mass = cms.double(0.05),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(2),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.2'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(2),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(2),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.5'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.8),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.6'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.9),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(2)
        )
    ),
    matchingCone = cms.double(0.5),
    minPixelHits = cms.int32(1),
    minTauPt = cms.double(0.0),
    requireTauChargedHadronsToBeChargedPFCands = cms.bool(False),
    verbosity = cms.int32(0)
)


process.hpsSelectionDiscriminatorMuonCleaned = cms.EDProducer("PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag("combinatoricRecoTausMuonCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    decayModes = cms.VPSet(
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(-1000.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.1349),
            maxMass = cms.string('max(1.3, min(1.3*sqrt(pt/100.), 4.2))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.3),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(True),
                mass = cms.bool(True),
                phi = cms.bool(True)
            ),
            assumeStripMass = cms.double(0.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(0.2),
            minMass = cms.double(0.4),
            minPi0Mass = cms.double(0.05),
            nCharged = cms.uint32(1),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(2),
            nTracksMin = cms.uint32(1)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.2'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(2),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('max(1.2, min(1.2*sqrt(pt/100.), 4.0))'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.0),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(2),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.5'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.8),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(0),
            nTracksMin = cms.uint32(2)
        ),
        cms.PSet(
            applyBendCorrection = cms.PSet(
                eta = cms.bool(False),
                mass = cms.bool(False),
                phi = cms.bool(False)
            ),
            assumeStripMass = cms.double(-1.0),
            maxMass = cms.string('1.6'),
            maxPi0Mass = cms.double(1000000000.0),
            minMass = cms.double(0.9),
            minPi0Mass = cms.double(-1000.0),
            nCharged = cms.uint32(3),
            nChargedPFCandsMin = cms.uint32(1),
            nPiZeros = cms.uint32(1),
            nTracksMin = cms.uint32(2)
        )
    ),
    matchingCone = cms.double(0.5),
    minPixelHits = cms.int32(1),
    minTauPt = cms.double(0.0),
    requireTauChargedHadronsToBeChargedPFCands = cms.bool(False),
    verbosity = cms.int32(0)
)


process.patJetCorrFactors = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L1FastJet',
        'L2Relative',
        'L3Absolute'
    ),
    mightGet = cms.optional.untracked.vstring,
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("ak4PFJetsCHS"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsReapplyJEC = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L1FastJet',
        'L2Relative',
        'L3Absolute'
    ),
    mightGet = cms.optional.untracked.vstring,
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("slimmedJets"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetsPAT = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("patJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("patJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(False),
    addBTagInfo = cms.bool(False),
    addDiscriminators = cms.bool(False),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(False),
    addJetFlavourInfo = cms.bool(False),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(),
    efficiencies = cms.PSet(

    ),
    embedCaloTowers = cms.bool(False),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("patJetGenJetMatch"),
    genPartonMatch = cms.InputTag("patJetPartonMatch"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("ak4PFJetsPAT"),
    mightGet = cms.optional.untracked.vstring,
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("ak4JetTracksAssociatorAtVertexPF"),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patJetsPATElectronCleaned = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("patJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("patJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(False),
    addBTagInfo = cms.bool(False),
    addDiscriminators = cms.bool(False),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(False),
    addJetFlavourInfo = cms.bool(False),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(),
    efficiencies = cms.PSet(

    ),
    embedCaloTowers = cms.bool(False),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("patJetGenJetMatch"),
    genPartonMatch = cms.InputTag("patJetPartonMatch"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("ak4PFJetsPATElectronCleaned"),
    mightGet = cms.optional.untracked.vstring,
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("ak4JetTracksAssociatorAtVertexPF"),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patJetsPATLowPtElectronCleaned = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("patJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("patJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(False),
    addBTagInfo = cms.bool(False),
    addDiscriminators = cms.bool(False),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(False),
    addJetFlavourInfo = cms.bool(False),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(),
    efficiencies = cms.PSet(

    ),
    embedCaloTowers = cms.bool(False),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("patJetGenJetMatch"),
    genPartonMatch = cms.InputTag("patJetPartonMatch"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("ak4PFJetsPATLowPtElectronCleaned"),
    mightGet = cms.optional.untracked.vstring,
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("ak4JetTracksAssociatorAtVertexPF"),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patJetsPATMuonCleaned = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("patJetFlavourAssociation"),
    JetPartonMapSource = cms.InputTag("patJetFlavourAssociationLegacy"),
    addAssociatedTracks = cms.bool(False),
    addBTagInfo = cms.bool(False),
    addDiscriminators = cms.bool(False),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(False),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(False),
    addJetFlavourInfo = cms.bool(False),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(),
    efficiencies = cms.PSet(

    ),
    embedCaloTowers = cms.bool(False),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(False),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("patJetGenJetMatch"),
    genPartonMatch = cms.InputTag("patJetPartonMatch"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag("patJetCharge"),
    jetCorrFactorsSource = cms.VInputTag(),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("ak4PFJetsPATMuonCleaned"),
    mightGet = cms.optional.untracked.vstring,
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag("ak4JetTracksAssociatorAtVertexPF"),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patTauDiscriminationByElectronRejectionMVA62018 = cms.EDProducer("PATTauDiscriminantCutMultiplexer",
    PATTauProducer = cms.InputTag("selectedPatTausNoNewIDs"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(
        cms.PSet(
            category = cms.uint32(0),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(2),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(5),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(7),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(8),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(10),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(13),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(15),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_EC'),
            variable = cms.string('pt')
        )
    ),
    mvaOutput_normalization = cms.string(''),
    toMultiplex = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018Raw"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_WPeff98',
        '_WPeff90',
        '_WPeff80',
        '_WPeff70',
        '_WPeff60'
    )
)


process.patTauDiscriminationByElectronRejectionMVA62018Boosted = cms.EDProducer("PATTauDiscriminantCutMultiplexer",
    PATTauProducer = cms.InputTag("selectedPatTausNoNewIDsBoosted"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(
        cms.PSet(
            category = cms.uint32(0),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(2),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(5),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(7),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(8),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(10),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(13),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(15),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_EC'),
            variable = cms.string('pt')
        )
    ),
    mvaOutput_normalization = cms.string(''),
    toMultiplex = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018RawBoosted"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_WPeff98',
        '_WPeff90',
        '_WPeff80',
        '_WPeff70',
        '_WPeff60'
    )
)


process.patTauDiscriminationByElectronRejectionMVA62018ElectronCleaned = cms.EDProducer("PATTauDiscriminantCutMultiplexer",
    PATTauProducer = cms.InputTag("selectedPatTausNoNewIDsElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(
        cms.PSet(
            category = cms.uint32(0),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(2),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(5),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(7),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(8),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(10),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(13),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(15),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_EC'),
            variable = cms.string('pt')
        )
    ),
    mvaOutput_normalization = cms.string(''),
    toMultiplex = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018RawElectronCleaned"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_WPeff98',
        '_WPeff90',
        '_WPeff80',
        '_WPeff70',
        '_WPeff60'
    )
)


process.patTauDiscriminationByElectronRejectionMVA62018LowPtElectronCleaned = cms.EDProducer("PATTauDiscriminantCutMultiplexer",
    PATTauProducer = cms.InputTag("selectedPatTausNoNewIDsLowPtElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(
        cms.PSet(
            category = cms.uint32(0),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(2),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(5),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(7),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(8),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(10),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(13),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(15),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_EC'),
            variable = cms.string('pt')
        )
    ),
    mvaOutput_normalization = cms.string(''),
    toMultiplex = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018RawLowPtElectronCleaned"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_WPeff98',
        '_WPeff90',
        '_WPeff80',
        '_WPeff70',
        '_WPeff60'
    )
)


process.patTauDiscriminationByElectronRejectionMVA62018MuonCleaned = cms.EDProducer("PATTauDiscriminantCutMultiplexer",
    PATTauProducer = cms.InputTag("selectedPatTausNoNewIDsMuonCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(
        cms.PSet(
            category = cms.uint32(0),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(2),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(5),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(7),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_BL'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(8),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(10),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(13),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_EC'),
            variable = cms.string('pt')
        ),
        cms.PSet(
            category = cms.uint32(15),
            cut = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_EC'),
            variable = cms.string('pt')
        )
    ),
    mvaOutput_normalization = cms.string(''),
    toMultiplex = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018RawMuonCleaned"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_WPeff98',
        '_WPeff90',
        '_WPeff80',
        '_WPeff70',
        '_WPeff60'
    )
)


process.patTauDiscriminationByElectronRejectionMVA62018Raw = cms.EDProducer("PATTauDiscriminationAgainstElectronMVA6",
    PATTauProducer = cms.InputTag("selectedPatTausNoNewIDs"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    isPhase2 = cms.bool(False),
    loadMVAfromDB = cms.bool(True),
    method = cms.string('BDTG'),
    mightGet = cms.optional.untracked.vstring,
    minMVANoEleMatchWOgWOgsfBL = cms.double(0),
    minMVANoEleMatchWOgWOgsfEC = cms.double(0),
    minMVANoEleMatchWgWOgsfBL = cms.double(0),
    minMVANoEleMatchWgWOgsfEC = cms.double(0),
    minMVAWOgWgsfBL = cms.double(0),
    minMVAWOgWgsfEC = cms.double(0),
    minMVAWgWgsfBL = cms.double(0),
    minMVAWgWgsfEC = cms.double(0),
    mvaName_NoEleMatch_wGwoGSF_BL = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_BL'),
    mvaName_NoEleMatch_wGwoGSF_EC = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_EC'),
    mvaName_NoEleMatch_woGwoGSF_BL = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_BL'),
    mvaName_NoEleMatch_woGwoGSF_EC = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_EC'),
    mvaName_wGwGSF_BL = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_BL'),
    mvaName_wGwGSF_EC = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_EC'),
    mvaName_woGwGSF_BL = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_BL'),
    mvaName_woGwGSF_EC = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_EC'),
    returnMVA = cms.bool(True),
    srcElectrons = cms.InputTag("slimmedElectrons"),
    usePhiAtEcalEntranceExtrapolation = cms.bool(False),
    verbosity = cms.int32(0),
    vetoEcalCracks = cms.bool(False)
)


process.patTauDiscriminationByElectronRejectionMVA62018RawBoosted = cms.EDProducer("PATTauDiscriminationAgainstElectronMVA6",
    PATTauProducer = cms.InputTag("selectedPatTausNoNewIDsBoosted"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    isPhase2 = cms.bool(False),
    loadMVAfromDB = cms.bool(True),
    method = cms.string('BDTG'),
    mightGet = cms.optional.untracked.vstring,
    minMVANoEleMatchWOgWOgsfBL = cms.double(0),
    minMVANoEleMatchWOgWOgsfEC = cms.double(0),
    minMVANoEleMatchWgWOgsfBL = cms.double(0),
    minMVANoEleMatchWgWOgsfEC = cms.double(0),
    minMVAWOgWgsfBL = cms.double(0),
    minMVAWOgWgsfEC = cms.double(0),
    minMVAWgWgsfBL = cms.double(0),
    minMVAWgWgsfEC = cms.double(0),
    mvaName_NoEleMatch_wGwoGSF_BL = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_BL'),
    mvaName_NoEleMatch_wGwoGSF_EC = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_EC'),
    mvaName_NoEleMatch_woGwoGSF_BL = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_BL'),
    mvaName_NoEleMatch_woGwoGSF_EC = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_EC'),
    mvaName_wGwGSF_BL = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_BL'),
    mvaName_wGwGSF_EC = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_EC'),
    mvaName_woGwGSF_BL = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_BL'),
    mvaName_woGwGSF_EC = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_EC'),
    returnMVA = cms.bool(True),
    srcElectrons = cms.InputTag("slimmedElectrons"),
    usePhiAtEcalEntranceExtrapolation = cms.bool(False),
    verbosity = cms.int32(0),
    vetoEcalCracks = cms.bool(False)
)


process.patTauDiscriminationByElectronRejectionMVA62018RawElectronCleaned = cms.EDProducer("PATTauDiscriminationAgainstElectronMVA6",
    PATTauProducer = cms.InputTag("selectedPatTausNoNewIDsElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    isPhase2 = cms.bool(False),
    loadMVAfromDB = cms.bool(True),
    method = cms.string('BDTG'),
    mightGet = cms.optional.untracked.vstring,
    minMVANoEleMatchWOgWOgsfBL = cms.double(0),
    minMVANoEleMatchWOgWOgsfEC = cms.double(0),
    minMVANoEleMatchWgWOgsfBL = cms.double(0),
    minMVANoEleMatchWgWOgsfEC = cms.double(0),
    minMVAWOgWgsfBL = cms.double(0),
    minMVAWOgWgsfEC = cms.double(0),
    minMVAWgWgsfBL = cms.double(0),
    minMVAWgWgsfEC = cms.double(0),
    mvaName_NoEleMatch_wGwoGSF_BL = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_BL'),
    mvaName_NoEleMatch_wGwoGSF_EC = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_EC'),
    mvaName_NoEleMatch_woGwoGSF_BL = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_BL'),
    mvaName_NoEleMatch_woGwoGSF_EC = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_EC'),
    mvaName_wGwGSF_BL = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_BL'),
    mvaName_wGwGSF_EC = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_EC'),
    mvaName_woGwGSF_BL = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_BL'),
    mvaName_woGwGSF_EC = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_EC'),
    returnMVA = cms.bool(True),
    srcElectrons = cms.InputTag("slimmedElectrons"),
    usePhiAtEcalEntranceExtrapolation = cms.bool(False),
    verbosity = cms.int32(0),
    vetoEcalCracks = cms.bool(False)
)


process.patTauDiscriminationByElectronRejectionMVA62018RawLowPtElectronCleaned = cms.EDProducer("PATTauDiscriminationAgainstElectronMVA6",
    PATTauProducer = cms.InputTag("selectedPatTausNoNewIDsLowPtElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    isPhase2 = cms.bool(False),
    loadMVAfromDB = cms.bool(True),
    method = cms.string('BDTG'),
    mightGet = cms.optional.untracked.vstring,
    minMVANoEleMatchWOgWOgsfBL = cms.double(0),
    minMVANoEleMatchWOgWOgsfEC = cms.double(0),
    minMVANoEleMatchWgWOgsfBL = cms.double(0),
    minMVANoEleMatchWgWOgsfEC = cms.double(0),
    minMVAWOgWgsfBL = cms.double(0),
    minMVAWOgWgsfEC = cms.double(0),
    minMVAWgWgsfBL = cms.double(0),
    minMVAWgWgsfEC = cms.double(0),
    mvaName_NoEleMatch_wGwoGSF_BL = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_BL'),
    mvaName_NoEleMatch_wGwoGSF_EC = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_EC'),
    mvaName_NoEleMatch_woGwoGSF_BL = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_BL'),
    mvaName_NoEleMatch_woGwoGSF_EC = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_EC'),
    mvaName_wGwGSF_BL = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_BL'),
    mvaName_wGwGSF_EC = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_EC'),
    mvaName_woGwGSF_BL = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_BL'),
    mvaName_woGwGSF_EC = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_EC'),
    returnMVA = cms.bool(True),
    srcElectrons = cms.InputTag("slimmedElectrons"),
    usePhiAtEcalEntranceExtrapolation = cms.bool(False),
    verbosity = cms.int32(0),
    vetoEcalCracks = cms.bool(False)
)


process.patTauDiscriminationByElectronRejectionMVA62018RawMuonCleaned = cms.EDProducer("PATTauDiscriminationAgainstElectronMVA6",
    PATTauProducer = cms.InputTag("selectedPatTausNoNewIDsMuonCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    isPhase2 = cms.bool(False),
    loadMVAfromDB = cms.bool(True),
    method = cms.string('BDTG'),
    mightGet = cms.optional.untracked.vstring,
    minMVANoEleMatchWOgWOgsfBL = cms.double(0),
    minMVANoEleMatchWOgWOgsfEC = cms.double(0),
    minMVANoEleMatchWgWOgsfBL = cms.double(0),
    minMVANoEleMatchWgWOgsfEC = cms.double(0),
    minMVAWOgWgsfBL = cms.double(0),
    minMVAWOgWgsfEC = cms.double(0),
    minMVAWgWgsfBL = cms.double(0),
    minMVAWgWgsfEC = cms.double(0),
    mvaName_NoEleMatch_wGwoGSF_BL = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_BL'),
    mvaName_NoEleMatch_wGwoGSF_EC = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_EC'),
    mvaName_NoEleMatch_woGwoGSF_BL = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_BL'),
    mvaName_NoEleMatch_woGwoGSF_EC = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_EC'),
    mvaName_wGwGSF_BL = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_BL'),
    mvaName_wGwGSF_EC = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_EC'),
    mvaName_woGwGSF_BL = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_BL'),
    mvaName_woGwGSF_EC = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_EC'),
    returnMVA = cms.bool(True),
    srcElectrons = cms.InputTag("slimmedElectrons"),
    usePhiAtEcalEntranceExtrapolation = cms.bool(False),
    verbosity = cms.int32(0),
    vetoEcalCracks = cms.bool(False)
)


process.patTaus = cms.EDProducer("PATTauProducer",
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(True),
    addGenMatch = cms.bool(True),
    addResolutions = cms.bool(False),
    addTauID = cms.bool(True),
    addTauJetCorrFactors = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedIsolationPFCands = cms.bool(False),
    embedIsolationPFChargedHadrCands = cms.bool(False),
    embedIsolationPFGammaCands = cms.bool(False),
    embedIsolationPFNeutralHadrCands = cms.bool(False),
    embedIsolationTracks = cms.bool(False),
    embedLeadPFCand = cms.bool(False),
    embedLeadPFChargedHadrCand = cms.bool(False),
    embedLeadPFNeutralCand = cms.bool(False),
    embedLeadTrack = cms.bool(False),
    embedSignalPFCands = cms.bool(False),
    embedSignalPFChargedHadrCands = cms.bool(False),
    embedSignalPFGammaCands = cms.bool(False),
    embedSignalPFNeutralHadrCands = cms.bool(False),
    embedSignalTracks = cms.bool(False),
    genJetMatch = cms.InputTag("tauGenJetMatch"),
    genParticleMatch = cms.InputTag("tauMatch"),
    isoDeposits = cms.PSet(

    ),
    resolutions = cms.PSet(

    ),
    skipMissingTauID = cms.bool(False),
    tauIDSources = cms.PSet(
        againstElectronDeadECAL = cms.PSet(
            idLabel = cms.string(''),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByDeadECALElectronRejection"),
            provenanceConfigLabel = cms.string('')
        ),
        againstMuonLooseSimple = cms.PSet(
            idLabel = cms.string('ByLooseMuonRejectionSimple'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByMuonRejectionSimple"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        againstMuonTightSimple = cms.PSet(
            idLabel = cms.string('ByTightMuonRejectionSimple'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByMuonRejectionSimple"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byCombinedIsolationDeltaBetaCorrRaw3Hits = cms.PSet(
            idLabel = cms.string('ByRawCombinedIsolationDBSumPtCorr3Hits'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        byIsolationMVArun2v1DBdR03oldDMwLTraw = cms.PSet(
            idLabel = cms.string('discriminator'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT"),
            provenanceConfigLabel = cms.string('rawValues')
        ),
        byIsolationMVArun2v1DBnewDMwLTraw = cms.PSet(
            idLabel = cms.string('discriminator'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT"),
            provenanceConfigLabel = cms.string('rawValues')
        ),
        byIsolationMVArun2v1DBoldDMwLTraw = cms.PSet(
            idLabel = cms.string('discriminator'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT"),
            provenanceConfigLabel = cms.string('rawValues')
        ),
        byLooseCombinedIsolationDeltaBetaCorr3Hits = cms.PSet(
            idLabel = cms.string('ByLooseCombinedIsolationDBSumPtCorr3Hits'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byLooseIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_Loose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byLooseIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_Loose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byLooseIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_Loose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byMediumCombinedIsolationDeltaBetaCorr3Hits = cms.PSet(
            idLabel = cms.string('ByMediumCombinedIsolationDBSumPtCorr3Hits'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byMediumIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_Medium'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byMediumIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_Medium'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byMediumIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_Medium'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byPhotonPtSumOutsideSignalCone = cms.PSet(
            idLabel = cms.string('ByPhotonPtSumOutsideSignalCone'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byTightCombinedIsolationDeltaBetaCorr3Hits = cms.PSet(
            idLabel = cms.string('ByTightCombinedIsolationDBSumPtCorr3Hits'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byTightIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_Tight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byTightIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_Tight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byTightIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_Tight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVLooseIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_VLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVLooseIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_VLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVLooseIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_VLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVTightIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_VTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVTightIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_VTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVTightIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_VTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVLooseIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_VVLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVLooseIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_VVLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVLooseIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_VVLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVTightIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_VVTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVTightIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_VVTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVTightIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_VVTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        chargedIsoPtSum = cms.PSet(
            idLabel = cms.string('ChargedIsoPtSum'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        chargedIsoPtSumdR03 = cms.PSet(
            idLabel = cms.string('ChargedIsoPtSumdR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        decayModeFinding = cms.PSet(
            idLabel = cms.string(''),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByDecayModeFinding"),
            provenanceConfigLabel = cms.string('')
        ),
        decayModeFindingNewDMs = cms.PSet(
            idLabel = cms.string(''),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            provenanceConfigLabel = cms.string('')
        ),
        footprintCorrection = cms.PSet(
            idLabel = cms.string('TauFootprintCorrection'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        footprintCorrectiondR03 = cms.PSet(
            idLabel = cms.string('TauFootprintCorrectiondR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        neutralIsoPtSum = cms.PSet(
            idLabel = cms.string('NeutralIsoPtSum'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        neutralIsoPtSumWeight = cms.PSet(
            idLabel = cms.string('NeutralIsoPtSumWeight'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        neutralIsoPtSumWeightdR03 = cms.PSet(
            idLabel = cms.string('NeutralIsoPtSumWeightdR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        neutralIsoPtSumdR03 = cms.PSet(
            idLabel = cms.string('NeutralIsoPtSumdR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        photonPtSumOutsideSignalCone = cms.PSet(
            idLabel = cms.string('PhotonPtSumOutsideSignalCone'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        photonPtSumOutsideSignalConedR03 = cms.PSet(
            idLabel = cms.string('PhotonPtSumOutsideSignalConedR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        puCorrPtSum = cms.PSet(
            idLabel = cms.string('PUcorrPtSum'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminators"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        )
    ),
    tauJetCorrFactorsSource = cms.VInputTag(cms.InputTag("patTauJetCorrFactors")),
    tauSource = cms.InputTag("hpsPFTauProducer"),
    tauTransverseImpactParameterSource = cms.InputTag("hpsPFTauTransverseImpactParameters"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patTausBoosted = cms.EDProducer("PATTauProducer",
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(True),
    addGenMatch = cms.bool(True),
    addResolutions = cms.bool(False),
    addTauID = cms.bool(True),
    addTauJetCorrFactors = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedIsolationPFCands = cms.bool(False),
    embedIsolationPFChargedHadrCands = cms.bool(False),
    embedIsolationPFGammaCands = cms.bool(False),
    embedIsolationPFNeutralHadrCands = cms.bool(False),
    embedIsolationTracks = cms.bool(False),
    embedLeadPFCand = cms.bool(False),
    embedLeadPFChargedHadrCand = cms.bool(False),
    embedLeadPFNeutralCand = cms.bool(False),
    embedLeadTrack = cms.bool(False),
    embedSignalPFCands = cms.bool(False),
    embedSignalPFChargedHadrCands = cms.bool(False),
    embedSignalPFGammaCands = cms.bool(False),
    embedSignalPFNeutralHadrCands = cms.bool(False),
    embedSignalTracks = cms.bool(False),
    genJetMatch = cms.InputTag("tauGenJetMatchBoosted"),
    genParticleMatch = cms.InputTag("tauMatchBoosted"),
    isoDeposits = cms.PSet(

    ),
    resolutions = cms.PSet(

    ),
    skipMissingTauID = cms.bool(False),
    tauIDSources = cms.PSet(
        againstElectronDeadECAL = cms.PSet(
            idLabel = cms.string(''),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByDeadECALElectronRejectionBoosted"),
            provenanceConfigLabel = cms.string('')
        ),
        againstMuonLooseSimple = cms.PSet(
            idLabel = cms.string('ByLooseMuonRejectionSimple'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByMuonRejectionSimpleBoosted"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        againstMuonTightSimple = cms.PSet(
            idLabel = cms.string('ByTightMuonRejectionSimple'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByMuonRejectionSimpleBoosted"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byCombinedIsolationDeltaBetaCorrRaw3Hits = cms.PSet(
            idLabel = cms.string('ByRawCombinedIsolationDBSumPtCorr3Hits'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsBoosted"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        byIsolationMVArun2v1DBdR03oldDMwLTraw = cms.PSet(
            idLabel = cms.string('discriminator'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTBoosted"),
            provenanceConfigLabel = cms.string('rawValues')
        ),
        byIsolationMVArun2v1DBnewDMwLTraw = cms.PSet(
            idLabel = cms.string('discriminator'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTBoosted"),
            provenanceConfigLabel = cms.string('rawValues')
        ),
        byIsolationMVArun2v1DBoldDMwLTraw = cms.PSet(
            idLabel = cms.string('discriminator'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTBoosted"),
            provenanceConfigLabel = cms.string('rawValues')
        ),
        byLooseCombinedIsolationDeltaBetaCorr3Hits = cms.PSet(
            idLabel = cms.string('ByLooseCombinedIsolationDBSumPtCorr3Hits'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsBoosted"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byLooseIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_Loose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTBoosted"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byLooseIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_Loose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTBoosted"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byLooseIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_Loose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTBoosted"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byMediumCombinedIsolationDeltaBetaCorr3Hits = cms.PSet(
            idLabel = cms.string('ByMediumCombinedIsolationDBSumPtCorr3Hits'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsBoosted"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byMediumIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_Medium'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTBoosted"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byMediumIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_Medium'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTBoosted"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byMediumIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_Medium'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTBoosted"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byPhotonPtSumOutsideSignalCone = cms.PSet(
            idLabel = cms.string('ByPhotonPtSumOutsideSignalCone'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsBoosted"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byTightCombinedIsolationDeltaBetaCorr3Hits = cms.PSet(
            idLabel = cms.string('ByTightCombinedIsolationDBSumPtCorr3Hits'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsBoosted"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byTightIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_Tight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTBoosted"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byTightIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_Tight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTBoosted"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byTightIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_Tight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTBoosted"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVLooseIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_VLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTBoosted"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVLooseIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_VLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTBoosted"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVLooseIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_VLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTBoosted"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVTightIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_VTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTBoosted"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVTightIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_VTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTBoosted"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVTightIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_VTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTBoosted"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVLooseIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_VVLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTBoosted"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVLooseIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_VVLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTBoosted"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVLooseIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_VVLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTBoosted"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVTightIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_VVTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTBoosted"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVTightIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_VVTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTBoosted"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVTightIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_VVTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTBoosted"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        chargedIsoPtSum = cms.PSet(
            idLabel = cms.string('ChargedIsoPtSum'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsBoosted"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        chargedIsoPtSumdR03 = cms.PSet(
            idLabel = cms.string('ChargedIsoPtSumdR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03Boosted"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        decayModeFinding = cms.PSet(
            idLabel = cms.string(''),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingBoosted"),
            provenanceConfigLabel = cms.string('')
        ),
        decayModeFindingNewDMs = cms.PSet(
            idLabel = cms.string(''),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsBoosted"),
            provenanceConfigLabel = cms.string('')
        ),
        footprintCorrection = cms.PSet(
            idLabel = cms.string('TauFootprintCorrection'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsBoosted"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        footprintCorrectiondR03 = cms.PSet(
            idLabel = cms.string('TauFootprintCorrectiondR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03Boosted"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        neutralIsoPtSum = cms.PSet(
            idLabel = cms.string('NeutralIsoPtSum'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsBoosted"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        neutralIsoPtSumWeight = cms.PSet(
            idLabel = cms.string('NeutralIsoPtSumWeight'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsBoosted"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        neutralIsoPtSumWeightdR03 = cms.PSet(
            idLabel = cms.string('NeutralIsoPtSumWeightdR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03Boosted"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        neutralIsoPtSumdR03 = cms.PSet(
            idLabel = cms.string('NeutralIsoPtSumdR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03Boosted"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        photonPtSumOutsideSignalCone = cms.PSet(
            idLabel = cms.string('PhotonPtSumOutsideSignalCone'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsBoosted"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        photonPtSumOutsideSignalConedR03 = cms.PSet(
            idLabel = cms.string('PhotonPtSumOutsideSignalConedR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03Boosted"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        puCorrPtSum = cms.PSet(
            idLabel = cms.string('PUcorrPtSum'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsBoosted"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        )
    ),
    tauJetCorrFactorsSource = cms.VInputTag(cms.InputTag("patTauJetCorrFactors")),
    tauSource = cms.InputTag("hpsPFTauProducerBoosted"),
    tauTransverseImpactParameterSource = cms.InputTag("hpsPFTauTransverseImpactParametersBoosted"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patTausElectronCleaned = cms.EDProducer("PATTauProducer",
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(True),
    addGenMatch = cms.bool(True),
    addResolutions = cms.bool(False),
    addTauID = cms.bool(True),
    addTauJetCorrFactors = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedIsolationPFCands = cms.bool(False),
    embedIsolationPFChargedHadrCands = cms.bool(False),
    embedIsolationPFGammaCands = cms.bool(False),
    embedIsolationPFNeutralHadrCands = cms.bool(False),
    embedIsolationTracks = cms.bool(False),
    embedLeadPFCand = cms.bool(False),
    embedLeadPFChargedHadrCand = cms.bool(False),
    embedLeadPFNeutralCand = cms.bool(False),
    embedLeadTrack = cms.bool(False),
    embedSignalPFCands = cms.bool(False),
    embedSignalPFChargedHadrCands = cms.bool(False),
    embedSignalPFGammaCands = cms.bool(False),
    embedSignalPFNeutralHadrCands = cms.bool(False),
    embedSignalTracks = cms.bool(False),
    genJetMatch = cms.InputTag("tauGenJetMatchElectronCleaned"),
    genParticleMatch = cms.InputTag("tauMatchElectronCleaned"),
    isoDeposits = cms.PSet(

    ),
    resolutions = cms.PSet(

    ),
    skipMissingTauID = cms.bool(False),
    tauIDSources = cms.PSet(
        againstElectronDeadECAL = cms.PSet(
            idLabel = cms.string(''),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByDeadECALElectronRejectionElectronCleaned"),
            provenanceConfigLabel = cms.string('')
        ),
        againstMuonLooseSimple = cms.PSet(
            idLabel = cms.string('ByLooseMuonRejectionSimple'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByMuonRejectionSimpleElectronCleaned"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        againstMuonTightSimple = cms.PSet(
            idLabel = cms.string('ByTightMuonRejectionSimple'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByMuonRejectionSimpleElectronCleaned"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byCombinedIsolationDeltaBetaCorrRaw3Hits = cms.PSet(
            idLabel = cms.string('ByRawCombinedIsolationDBSumPtCorr3Hits'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsElectronCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        byIsolationMVArun2v1DBdR03oldDMwLTraw = cms.PSet(
            idLabel = cms.string('discriminator'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTElectronCleaned"),
            provenanceConfigLabel = cms.string('rawValues')
        ),
        byIsolationMVArun2v1DBnewDMwLTraw = cms.PSet(
            idLabel = cms.string('discriminator'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTElectronCleaned"),
            provenanceConfigLabel = cms.string('rawValues')
        ),
        byIsolationMVArun2v1DBoldDMwLTraw = cms.PSet(
            idLabel = cms.string('discriminator'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTElectronCleaned"),
            provenanceConfigLabel = cms.string('rawValues')
        ),
        byLooseCombinedIsolationDeltaBetaCorr3Hits = cms.PSet(
            idLabel = cms.string('ByLooseCombinedIsolationDBSumPtCorr3Hits'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsElectronCleaned"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byLooseIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_Loose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byLooseIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_Loose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byLooseIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_Loose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byMediumCombinedIsolationDeltaBetaCorr3Hits = cms.PSet(
            idLabel = cms.string('ByMediumCombinedIsolationDBSumPtCorr3Hits'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsElectronCleaned"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byMediumIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_Medium'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byMediumIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_Medium'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byMediumIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_Medium'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byPhotonPtSumOutsideSignalCone = cms.PSet(
            idLabel = cms.string('ByPhotonPtSumOutsideSignalCone'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsElectronCleaned"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byTightCombinedIsolationDeltaBetaCorr3Hits = cms.PSet(
            idLabel = cms.string('ByTightCombinedIsolationDBSumPtCorr3Hits'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsElectronCleaned"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byTightIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_Tight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byTightIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_Tight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byTightIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_Tight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVLooseIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_VLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVLooseIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_VLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVLooseIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_VLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVTightIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_VTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVTightIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_VTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVTightIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_VTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVLooseIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_VVLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVLooseIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_VVLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVLooseIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_VVLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVTightIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_VVTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVTightIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_VVTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVTightIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_VVTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        chargedIsoPtSum = cms.PSet(
            idLabel = cms.string('ChargedIsoPtSum'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsElectronCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        chargedIsoPtSumdR03 = cms.PSet(
            idLabel = cms.string('ChargedIsoPtSumdR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03ElectronCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        decayModeFinding = cms.PSet(
            idLabel = cms.string(''),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingElectronCleaned"),
            provenanceConfigLabel = cms.string('')
        ),
        decayModeFindingNewDMs = cms.PSet(
            idLabel = cms.string(''),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsElectronCleaned"),
            provenanceConfigLabel = cms.string('')
        ),
        footprintCorrection = cms.PSet(
            idLabel = cms.string('TauFootprintCorrection'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsElectronCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        footprintCorrectiondR03 = cms.PSet(
            idLabel = cms.string('TauFootprintCorrectiondR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03ElectronCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        neutralIsoPtSum = cms.PSet(
            idLabel = cms.string('NeutralIsoPtSum'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsElectronCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        neutralIsoPtSumWeight = cms.PSet(
            idLabel = cms.string('NeutralIsoPtSumWeight'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsElectronCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        neutralIsoPtSumWeightdR03 = cms.PSet(
            idLabel = cms.string('NeutralIsoPtSumWeightdR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03ElectronCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        neutralIsoPtSumdR03 = cms.PSet(
            idLabel = cms.string('NeutralIsoPtSumdR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03ElectronCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        photonPtSumOutsideSignalCone = cms.PSet(
            idLabel = cms.string('PhotonPtSumOutsideSignalCone'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsElectronCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        photonPtSumOutsideSignalConedR03 = cms.PSet(
            idLabel = cms.string('PhotonPtSumOutsideSignalConedR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03ElectronCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        puCorrPtSum = cms.PSet(
            idLabel = cms.string('PUcorrPtSum'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsElectronCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        )
    ),
    tauJetCorrFactorsSource = cms.VInputTag(cms.InputTag("patTauJetCorrFactors")),
    tauSource = cms.InputTag("hpsPFTauProducerElectronCleaned"),
    tauTransverseImpactParameterSource = cms.InputTag("hpsPFTauTransverseImpactParametersElectronCleaned"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patTausLowPtElectronCleaned = cms.EDProducer("PATTauProducer",
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(True),
    addGenMatch = cms.bool(True),
    addResolutions = cms.bool(False),
    addTauID = cms.bool(True),
    addTauJetCorrFactors = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedIsolationPFCands = cms.bool(False),
    embedIsolationPFChargedHadrCands = cms.bool(False),
    embedIsolationPFGammaCands = cms.bool(False),
    embedIsolationPFNeutralHadrCands = cms.bool(False),
    embedIsolationTracks = cms.bool(False),
    embedLeadPFCand = cms.bool(False),
    embedLeadPFChargedHadrCand = cms.bool(False),
    embedLeadPFNeutralCand = cms.bool(False),
    embedLeadTrack = cms.bool(False),
    embedSignalPFCands = cms.bool(False),
    embedSignalPFChargedHadrCands = cms.bool(False),
    embedSignalPFGammaCands = cms.bool(False),
    embedSignalPFNeutralHadrCands = cms.bool(False),
    embedSignalTracks = cms.bool(False),
    genJetMatch = cms.InputTag("tauGenJetMatchLowPtElectronCleaned"),
    genParticleMatch = cms.InputTag("tauMatchLowPtElectronCleaned"),
    isoDeposits = cms.PSet(

    ),
    resolutions = cms.PSet(

    ),
    skipMissingTauID = cms.bool(False),
    tauIDSources = cms.PSet(
        againstElectronDeadECAL = cms.PSet(
            idLabel = cms.string(''),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByDeadECALElectronRejectionLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('')
        ),
        againstMuonLooseSimple = cms.PSet(
            idLabel = cms.string('ByLooseMuonRejectionSimple'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByMuonRejectionSimpleLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        againstMuonTightSimple = cms.PSet(
            idLabel = cms.string('ByTightMuonRejectionSimple'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByMuonRejectionSimpleLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byCombinedIsolationDeltaBetaCorrRaw3Hits = cms.PSet(
            idLabel = cms.string('ByRawCombinedIsolationDBSumPtCorr3Hits'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        byIsolationMVArun2v1DBdR03oldDMwLTraw = cms.PSet(
            idLabel = cms.string('discriminator'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('rawValues')
        ),
        byIsolationMVArun2v1DBnewDMwLTraw = cms.PSet(
            idLabel = cms.string('discriminator'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('rawValues')
        ),
        byIsolationMVArun2v1DBoldDMwLTraw = cms.PSet(
            idLabel = cms.string('discriminator'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('rawValues')
        ),
        byLooseCombinedIsolationDeltaBetaCorr3Hits = cms.PSet(
            idLabel = cms.string('ByLooseCombinedIsolationDBSumPtCorr3Hits'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byLooseIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_Loose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byLooseIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_Loose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byLooseIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_Loose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byMediumCombinedIsolationDeltaBetaCorr3Hits = cms.PSet(
            idLabel = cms.string('ByMediumCombinedIsolationDBSumPtCorr3Hits'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byMediumIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_Medium'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byMediumIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_Medium'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byMediumIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_Medium'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byPhotonPtSumOutsideSignalCone = cms.PSet(
            idLabel = cms.string('ByPhotonPtSumOutsideSignalCone'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byTightCombinedIsolationDeltaBetaCorr3Hits = cms.PSet(
            idLabel = cms.string('ByTightCombinedIsolationDBSumPtCorr3Hits'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byTightIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_Tight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byTightIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_Tight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byTightIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_Tight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVLooseIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_VLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVLooseIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_VLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVLooseIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_VLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVTightIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_VTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVTightIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_VTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVTightIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_VTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVLooseIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_VVLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVLooseIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_VVLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVLooseIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_VVLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVTightIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_VVTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVTightIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_VVTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVTightIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_VVTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        chargedIsoPtSum = cms.PSet(
            idLabel = cms.string('ChargedIsoPtSum'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        chargedIsoPtSumdR03 = cms.PSet(
            idLabel = cms.string('ChargedIsoPtSumdR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03LowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        decayModeFinding = cms.PSet(
            idLabel = cms.string(''),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('')
        ),
        decayModeFindingNewDMs = cms.PSet(
            idLabel = cms.string(''),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('')
        ),
        footprintCorrection = cms.PSet(
            idLabel = cms.string('TauFootprintCorrection'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        footprintCorrectiondR03 = cms.PSet(
            idLabel = cms.string('TauFootprintCorrectiondR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03LowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        neutralIsoPtSum = cms.PSet(
            idLabel = cms.string('NeutralIsoPtSum'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        neutralIsoPtSumWeight = cms.PSet(
            idLabel = cms.string('NeutralIsoPtSumWeight'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        neutralIsoPtSumWeightdR03 = cms.PSet(
            idLabel = cms.string('NeutralIsoPtSumWeightdR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03LowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        neutralIsoPtSumdR03 = cms.PSet(
            idLabel = cms.string('NeutralIsoPtSumdR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03LowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        photonPtSumOutsideSignalCone = cms.PSet(
            idLabel = cms.string('PhotonPtSumOutsideSignalCone'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        photonPtSumOutsideSignalConedR03 = cms.PSet(
            idLabel = cms.string('PhotonPtSumOutsideSignalConedR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03LowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        puCorrPtSum = cms.PSet(
            idLabel = cms.string('PUcorrPtSum'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsLowPtElectronCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        )
    ),
    tauJetCorrFactorsSource = cms.VInputTag(cms.InputTag("patTauJetCorrFactors")),
    tauSource = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned"),
    tauTransverseImpactParameterSource = cms.InputTag("hpsPFTauTransverseImpactParametersLowPtElectronCleaned"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.patTausMuonCleaned = cms.EDProducer("PATTauProducer",
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(True),
    addGenMatch = cms.bool(True),
    addResolutions = cms.bool(False),
    addTauID = cms.bool(True),
    addTauJetCorrFactors = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenMatch = cms.bool(True),
    embedIsolationPFCands = cms.bool(False),
    embedIsolationPFChargedHadrCands = cms.bool(False),
    embedIsolationPFGammaCands = cms.bool(False),
    embedIsolationPFNeutralHadrCands = cms.bool(False),
    embedIsolationTracks = cms.bool(False),
    embedLeadPFCand = cms.bool(False),
    embedLeadPFChargedHadrCand = cms.bool(False),
    embedLeadPFNeutralCand = cms.bool(False),
    embedLeadTrack = cms.bool(False),
    embedSignalPFCands = cms.bool(False),
    embedSignalPFChargedHadrCands = cms.bool(False),
    embedSignalPFGammaCands = cms.bool(False),
    embedSignalPFNeutralHadrCands = cms.bool(False),
    embedSignalTracks = cms.bool(False),
    genJetMatch = cms.InputTag("tauGenJetMatchMuonCleaned"),
    genParticleMatch = cms.InputTag("tauMatchMuonCleaned"),
    isoDeposits = cms.PSet(

    ),
    resolutions = cms.PSet(

    ),
    skipMissingTauID = cms.bool(False),
    tauIDSources = cms.PSet(
        againstElectronDeadECAL = cms.PSet(
            idLabel = cms.string(''),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByDeadECALElectronRejectionMuonCleaned"),
            provenanceConfigLabel = cms.string('')
        ),
        againstMuonLooseSimple = cms.PSet(
            idLabel = cms.string('ByLooseMuonRejectionSimple'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByMuonRejectionSimpleMuonCleaned"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        againstMuonTightSimple = cms.PSet(
            idLabel = cms.string('ByTightMuonRejectionSimple'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByMuonRejectionSimpleMuonCleaned"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byCombinedIsolationDeltaBetaCorrRaw3Hits = cms.PSet(
            idLabel = cms.string('ByRawCombinedIsolationDBSumPtCorr3Hits'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsMuonCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        byIsolationMVArun2v1DBdR03oldDMwLTraw = cms.PSet(
            idLabel = cms.string('discriminator'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTMuonCleaned"),
            provenanceConfigLabel = cms.string('rawValues')
        ),
        byIsolationMVArun2v1DBnewDMwLTraw = cms.PSet(
            idLabel = cms.string('discriminator'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTMuonCleaned"),
            provenanceConfigLabel = cms.string('rawValues')
        ),
        byIsolationMVArun2v1DBoldDMwLTraw = cms.PSet(
            idLabel = cms.string('discriminator'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTMuonCleaned"),
            provenanceConfigLabel = cms.string('rawValues')
        ),
        byLooseCombinedIsolationDeltaBetaCorr3Hits = cms.PSet(
            idLabel = cms.string('ByLooseCombinedIsolationDBSumPtCorr3Hits'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsMuonCleaned"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byLooseIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_Loose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTMuonCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byLooseIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_Loose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTMuonCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byLooseIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_Loose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTMuonCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byMediumCombinedIsolationDeltaBetaCorr3Hits = cms.PSet(
            idLabel = cms.string('ByMediumCombinedIsolationDBSumPtCorr3Hits'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsMuonCleaned"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byMediumIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_Medium'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTMuonCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byMediumIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_Medium'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTMuonCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byMediumIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_Medium'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTMuonCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byPhotonPtSumOutsideSignalCone = cms.PSet(
            idLabel = cms.string('ByPhotonPtSumOutsideSignalCone'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsMuonCleaned"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byTightCombinedIsolationDeltaBetaCorr3Hits = cms.PSet(
            idLabel = cms.string('ByTightCombinedIsolationDBSumPtCorr3Hits'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsMuonCleaned"),
            provenanceConfigLabel = cms.string('IDWPdefinitions')
        ),
        byTightIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_Tight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTMuonCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byTightIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_Tight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTMuonCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byTightIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_Tight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTMuonCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVLooseIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_VLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTMuonCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVLooseIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_VLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTMuonCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVLooseIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_VLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTMuonCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVTightIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_VTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTMuonCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVTightIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_VTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTMuonCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVTightIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_VTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTMuonCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVLooseIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_VVLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTMuonCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVLooseIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_VVLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTMuonCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVLooseIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_VVLoose'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTMuonCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVTightIsolationMVArun2v1DBdR03oldDMwLT = cms.PSet(
            idLabel = cms.string('_VVTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTMuonCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVTightIsolationMVArun2v1DBnewDMwLT = cms.PSet(
            idLabel = cms.string('_VVTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTMuonCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        byVVTightIsolationMVArun2v1DBoldDMwLT = cms.PSet(
            idLabel = cms.string('_VVTight'),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTMuonCleaned"),
            provenanceConfigLabel = cms.string('workingPoints')
        ),
        chargedIsoPtSum = cms.PSet(
            idLabel = cms.string('ChargedIsoPtSum'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsMuonCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        chargedIsoPtSumdR03 = cms.PSet(
            idLabel = cms.string('ChargedIsoPtSumdR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03MuonCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        decayModeFinding = cms.PSet(
            idLabel = cms.string(''),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingMuonCleaned"),
            provenanceConfigLabel = cms.string('')
        ),
        decayModeFindingNewDMs = cms.PSet(
            idLabel = cms.string(''),
            inputTag = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMsMuonCleaned"),
            provenanceConfigLabel = cms.string('')
        ),
        footprintCorrection = cms.PSet(
            idLabel = cms.string('TauFootprintCorrection'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsMuonCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        footprintCorrectiondR03 = cms.PSet(
            idLabel = cms.string('TauFootprintCorrectiondR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03MuonCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        neutralIsoPtSum = cms.PSet(
            idLabel = cms.string('NeutralIsoPtSum'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsMuonCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        neutralIsoPtSumWeight = cms.PSet(
            idLabel = cms.string('NeutralIsoPtSumWeight'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsMuonCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        neutralIsoPtSumWeightdR03 = cms.PSet(
            idLabel = cms.string('NeutralIsoPtSumWeightdR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03MuonCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        neutralIsoPtSumdR03 = cms.PSet(
            idLabel = cms.string('NeutralIsoPtSumdR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03MuonCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        photonPtSumOutsideSignalCone = cms.PSet(
            idLabel = cms.string('PhotonPtSumOutsideSignalCone'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsMuonCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        photonPtSumOutsideSignalConedR03 = cms.PSet(
            idLabel = cms.string('PhotonPtSumOutsideSignalConedR03'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsdR03MuonCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        ),
        puCorrPtSum = cms.PSet(
            idLabel = cms.string('PUcorrPtSum'),
            inputTag = cms.InputTag("hpsPFTauBasicDiscriminatorsMuonCleaned"),
            provenanceConfigLabel = cms.string('IDdefinitions')
        )
    ),
    tauJetCorrFactorsSource = cms.VInputTag(cms.InputTag("patTauJetCorrFactors")),
    tauSource = cms.InputTag("hpsPFTauProducerMuonCleaned"),
    tauTransverseImpactParameterSource = cms.InputTag("hpsPFTauTransverseImpactParametersMuonCleaned"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    ),
    userIsolation = cms.PSet(

    )
)


process.pfNoPileUpIsoPFBRECO = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrs"),
    enable = cms.bool(True),
    matchByPtrDirect = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    name = cms.untracked.string('pileUpOnPFCandidates'),
    topCollection = cms.InputTag("pfPileUpIsoPFBRECO")
)


process.pfNoPileUpIsoPFBRECOBoosted = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrs"),
    enable = cms.bool(True),
    matchByPtrDirect = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    name = cms.untracked.string('pileUpOnPFCandidates'),
    topCollection = cms.InputTag("pfPileUpIsoPFBRECOBoosted")
)


process.pfNoPileUpIsoPFBRECOElectronCleaned = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrs"),
    enable = cms.bool(True),
    matchByPtrDirect = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    name = cms.untracked.string('pileUpOnPFCandidates'),
    topCollection = cms.InputTag("pfPileUpIsoPFBRECOElectronCleaned")
)


process.pfNoPileUpIsoPFBRECOLowPtElectronCleaned = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrs"),
    enable = cms.bool(True),
    matchByPtrDirect = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    name = cms.untracked.string('pileUpOnPFCandidates'),
    topCollection = cms.InputTag("pfPileUpIsoPFBRECOLowPtElectronCleaned")
)


process.pfNoPileUpIsoPFBRECOMuonCleaned = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrs"),
    enable = cms.bool(True),
    matchByPtrDirect = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    name = cms.untracked.string('pileUpOnPFCandidates'),
    topCollection = cms.InputTag("pfPileUpIsoPFBRECOMuonCleaned")
)


process.pfPileUpIsoPFBRECO = cms.EDProducer("PFPileUp",
    Enable = cms.bool(True),
    PFCandidates = cms.InputTag("particleFlowPtrs"),
    Vertices = cms.InputTag("offlinePrimaryVertices"),
    checkClosestZVertex = cms.bool(True),
    useVertexAssociation = cms.bool(False),
    verbose = cms.untracked.bool(False),
    vertexAssociation = cms.InputTag(""),
    vertexAssociationQuality = cms.int32(0)
)


process.pfPileUpIsoPFBRECOBoosted = cms.EDProducer("PFPileUp",
    Enable = cms.bool(True),
    PFCandidates = cms.InputTag("particleFlowPtrs"),
    Vertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    checkClosestZVertex = cms.bool(True),
    useVertexAssociation = cms.bool(False),
    verbose = cms.untracked.bool(False),
    vertexAssociation = cms.InputTag(""),
    vertexAssociationQuality = cms.int32(0)
)


process.pfPileUpIsoPFBRECOElectronCleaned = cms.EDProducer("PFPileUp",
    Enable = cms.bool(True),
    PFCandidates = cms.InputTag("particleFlowPtrs"),
    Vertices = cms.InputTag("offlinePrimaryVertices"),
    checkClosestZVertex = cms.bool(True),
    useVertexAssociation = cms.bool(False),
    verbose = cms.untracked.bool(False),
    vertexAssociation = cms.InputTag(""),
    vertexAssociationQuality = cms.int32(0)
)


process.pfPileUpIsoPFBRECOLowPtElectronCleaned = cms.EDProducer("PFPileUp",
    Enable = cms.bool(True),
    PFCandidates = cms.InputTag("particleFlowPtrs"),
    Vertices = cms.InputTag("offlinePrimaryVertices"),
    checkClosestZVertex = cms.bool(True),
    useVertexAssociation = cms.bool(False),
    verbose = cms.untracked.bool(False),
    vertexAssociation = cms.InputTag(""),
    vertexAssociationQuality = cms.int32(0)
)


process.pfPileUpIsoPFBRECOMuonCleaned = cms.EDProducer("PFPileUp",
    Enable = cms.bool(True),
    PFCandidates = cms.InputTag("particleFlowPtrs"),
    Vertices = cms.InputTag("offlinePrimaryVertices"),
    checkClosestZVertex = cms.bool(True),
    useVertexAssociation = cms.bool(False),
    verbose = cms.untracked.bool(False),
    vertexAssociation = cms.InputTag(""),
    vertexAssociationQuality = cms.int32(0)
)


process.pfRecoTauDiscriminationAgainstElectron = cms.EDProducer("PFRecoTauDiscriminationAgainstElectron",
    ApplyCut_BremCombined = cms.bool(False),
    ApplyCut_BremsRecoveryEOverPLead = cms.bool(False),
    ApplyCut_EOverPLead = cms.bool(False),
    ApplyCut_EcalCrackCut = cms.bool(False),
    ApplyCut_ElectronPreID = cms.bool(False),
    ApplyCut_ElectronPreID_2D = cms.bool(False),
    ApplyCut_EmFraction = cms.bool(False),
    ApplyCut_Hcal3x3OverPLead = cms.bool(False),
    ApplyCut_HcalMaxOverPLead = cms.bool(False),
    ApplyCut_HcalTotOverPLead = cms.bool(False),
    ApplyCut_PFElectronMVA = cms.bool(True),
    BremCombined_Fraction = cms.double(0.99),
    BremCombined_HOP = cms.double(0.1),
    BremCombined_Mass = cms.double(0.55),
    BremCombined_StripSize = cms.double(0.03),
    BremsRecoveryEOverPLead_maxValue = cms.double(1.8),
    BremsRecoveryEOverPLead_minValue = cms.double(0.8),
    EOverPLead_maxValue = cms.double(1.8),
    EOverPLead_minValue = cms.double(0.8),
    ElecPreID0_EOverPLead_maxValue = cms.double(0.95),
    ElecPreID0_HOverPLead_minValue = cms.double(0.05),
    ElecPreID1_EOverPLead_maxValue = cms.double(0.8),
    ElecPreID1_HOverPLead_minValue = cms.double(0.15),
    EmFraction_maxValue = cms.double(0.9),
    Hcal3x3OverPLead_minValue = cms.double(0.1),
    HcalMaxOverPLead_minValue = cms.double(0.1),
    HcalTotOverPLead_minValue = cms.double(0.1),
    PFElectronMVA_maxValue = cms.double(-0.1),
    PFTauProducer = cms.InputTag("pfRecoTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            Producer = cms.InputTag("pfRecoTauDiscriminationByLeadingTrackFinding"),
            cut = cms.double(0.5)
        )
    )
)


process.pfRecoTauDiscriminationAgainstElectronDeadECAL = cms.EDProducer("PFRecoTauDiscriminationAgainstElectronDeadECAL",
    PFTauProducer = cms.InputTag("fixme"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('AND'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("fixme"),
            cut = cms.double(0)
        ),
        leadTrack = cms.PSet(
            Producer = cms.InputTag("fixme"),
            cut = cms.double(0)
        )
    ),
    dR = cms.double(0.08),
    extrapolateToECalEntrance = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    minStatus = cms.uint32(12),
    verbosity = cms.int32(0)
)


process.pfRecoTauDiscriminationAgainstElectronMVA6 = cms.EDProducer("PFRecoTauDiscriminationAgainstElectronMVA6",
    PFTauProducer = cms.InputTag("fixme"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('AND'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("fixme"),
            cut = cms.double(0)
        ),
        leadTrack = cms.PSet(
            Producer = cms.InputTag("fixme"),
            cut = cms.double(0)
        )
    ),
    hgcalElectronIDs = cms.VInputTag(),
    isPhase2 = cms.bool(False),
    loadMVAfromDB = cms.bool(True),
    method = cms.string('BDTG'),
    mightGet = cms.optional.untracked.vstring,
    minMVANoEleMatchWOgWOgsfBL = cms.double(0),
    minMVANoEleMatchWOgWOgsfEC = cms.double(0),
    minMVANoEleMatchWgWOgsfBL = cms.double(0),
    minMVANoEleMatchWgWOgsfEC = cms.double(0),
    minMVAWOgWgsfBL = cms.double(0),
    minMVAWOgWgsfEC = cms.double(0),
    minMVAWgWgsfBL = cms.double(0),
    minMVAWgWgsfEC = cms.double(0),
    mvaName_NoEleMatch_wGwoGSF_BL = cms.string('gbr_NoEleMatch_wGwoGSF_BL'),
    mvaName_NoEleMatch_wGwoGSF_EC = cms.string('gbr_NoEleMatch_wGwoGSF_EC'),
    mvaName_NoEleMatch_woGwoGSF_BL = cms.string('gbr_NoEleMatch_woGwoGSF_BL'),
    mvaName_NoEleMatch_woGwoGSF_EC = cms.string('gbr_NoEleMatch_woGwoGSF_EC'),
    mvaName_wGwGSF_BL = cms.string('gbr_wGwGSF_BL'),
    mvaName_wGwGSF_EC = cms.string('gbr_wGwGSF_EC'),
    mvaName_woGwGSF_BL = cms.string('gbr_woGwGSF_BL'),
    mvaName_woGwGSF_EC = cms.string('gbr_woGwGSF_EC'),
    returnMVA = cms.bool(True),
    srcElectrons = cms.InputTag("fixme"),
    usePhiAtEcalEntranceExtrapolation = cms.bool(False),
    verbosity = cms.int32(0),
    vetoEcalCracks = cms.bool(True)
)


process.pfRecoTauDiscriminationAgainstMuon = cms.EDProducer("PFRecoTauDiscriminationAgainstMuon",
    HoPMin = cms.double(0.2),
    PFTauProducer = cms.InputTag("pfRecoTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            Producer = cms.InputTag("pfRecoTauDiscriminationByLeadingTrackFinding"),
            cut = cms.double(0.5)
        )
    ),
    a = cms.double(0.5),
    b = cms.double(0.5),
    c = cms.double(0.0),
    checkNumMatches = cms.bool(False),
    discriminatorOption = cms.string('noSegMatch'),
    maxNumberOfMatches = cms.int32(0)
)


process.pfRecoTauDiscriminationAgainstMuon2Container = cms.EDProducer("PFRecoTauDiscriminationAgainstMuon2Container",
    IDWPdefinitions = cms.VPSet(cms.PSet(
        HoPMin = cms.double(0.2),
        IDname = cms.string('pfRecoTauDiscriminationAgainstMuon2Container'),
        discriminatorOption = cms.string('loose'),
        doCaloMuonVeto = cms.bool(False),
        maxNumberOfHitsLast2Stations = cms.int32(0),
        maxNumberOfMatches = cms.int32(0)
    )),
    IDdefinitions = cms.VPSet(),
    PFTauProducer = cms.InputTag("pfRecoTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            Producer = cms.InputTag("pfRecoTauDiscriminationByLeadingTrackFinding"),
            cut = cms.double(0.5)
        )
    ),
    dRmuonMatch = cms.double(0.3),
    dRmuonMatchLimitedToJetArea = cms.bool(False),
    maskHitsCSC = cms.vint32(0, 0, 0, 0),
    maskHitsDT = cms.vint32(0, 0, 0, 0),
    maskHitsRPC = cms.vint32(0, 0, 0, 0),
    maskMatchesCSC = cms.vint32(1, 0, 0, 0),
    maskMatchesDT = cms.vint32(0, 0, 0, 0),
    maskMatchesRPC = cms.vint32(0, 0, 0, 0),
    mightGet = cms.optional.untracked.vstring,
    minPtMatchedMuon = cms.double(5),
    srcMuons = cms.InputTag("muons"),
    verbosity = cms.int32(0)
)


process.pfRecoTauDiscriminationAgainstMuonMVA = cms.EDProducer("PFRecoTauDiscriminationAgainstMuonMVA",
    PFTauProducer = cms.InputTag("pfTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            Producer = cms.InputTag("pfRecoTauDiscriminationByLeadingTrackFinding"),
            cut = cms.double(0.5)
        )
    ),
    dRmuonMatch = cms.double(0.3),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mvaMin = cms.double(0.0),
    mvaName = cms.string('againstMuonMVA'),
    returnMVA = cms.bool(True),
    srcMuons = cms.InputTag("muons"),
    verbosity = cms.int32(0)
)


process.pfRecoTauDiscriminationByIsolation = cms.EDProducer("PFRecoTauDiscriminationByIsolationContainer",
    IDWPdefinitions = cms.VPSet(),
    IDdefinitions = cms.VPSet(),
    PFTauProducer = cms.InputTag("pfRecoTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        leadTrack = cms.PSet(
            Producer = cms.InputTag("pfRecoTauDiscriminationByLeadingTrackFinding"),
            cut = cms.double(0.5)
        )
    ),
    WeightECALIsolation = cms.double(1),
    applyFootprintCorrection = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    customOuterCone = cms.double(-1),
    deltaBetaFactor = cms.string('0.38'),
    deltaBetaPUTrackPtCutOverride = cms.bool(False),
    deltaBetaPUTrackPtCutOverride_val = cms.double(-1.5),
    footprintCorrections = cms.VPSet(
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 0')
        ),
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 1 || decayMode() = 2')
        ),
        cms.PSet(
            offset = cms.string('2.7'),
            selection = cms.string('decayMode() = 5')
        ),
        cms.PSet(
            offset = cms.string('0.0'),
            selection = cms.string('decayMode() = 6')
        ),
        cms.PSet(
            offset = cms.string('max(2.0, 0.22*pt() - 2.0)'),
            selection = cms.string('decayMode() = 10')
        )
    ),
    isoConeSizeForDeltaBeta = cms.double(0.5),
    mightGet = cms.optional.untracked.vstring,
    minTauPtForNoIso = cms.double(-99),
    particleFlowSrc = cms.InputTag("particleFlow"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(1.5),
            minTrackHits = cms.uint32(8),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(1.0),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxDeltaZToLeadTrack = cms.double(-1.0),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    ),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.pfRecoTauDiscriminationByIsolationContainer = cms.EDProducer("PFRecoTauDiscriminationByIsolationContainer",
    IDWPdefinitions = cms.VPSet(),
    IDdefinitions = cms.VPSet(),
    PFTauProducer = cms.InputTag("pfRecoTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByDecayModeFindingNewDMs"),
            cut = cms.double(0.5)
        ),
        leadTrack = cms.PSet(
            Producer = cms.InputTag("pfRecoTauDiscriminationByLeadingTrackFinding"),
            cut = cms.double(0.5)
        ),
        preIso = cms.PSet(
            Producer = cms.InputTag("hpsPFTauDiscriminationByLooseChargedIsolation"),
            cut = cms.double(0.5)
        )
    ),
    WeightECALIsolation = cms.double(1),
    applyFootprintCorrection = cms.bool(False),
    applyRhoCorrection = cms.bool(False),
    customOuterCone = cms.double(-1),
    deltaBetaFactor = cms.string('0.38'),
    deltaBetaPUTrackPtCutOverride = cms.bool(False),
    deltaBetaPUTrackPtCutOverride_val = cms.double(-1.5),
    footprintCorrections = cms.VPSet(),
    isoConeSizeForDeltaBeta = cms.double(0.5),
    mightGet = cms.optional.untracked.vstring,
    minTauPtForNoIso = cms.double(-99),
    particleFlowSrc = cms.InputTag("particleFlow"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxDeltaZToLeadTrack = cms.double(-1),
            maxTrackChi2 = cms.double(100),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(1.5),
            minTrackHits = cms.uint32(8),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(1),
            minTrackVertexWeight = cms.double(-1),
            useTracksInsteadOfPFHadrons = cms.optional.bool
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("offlinePrimaryVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxDeltaZToLeadTrack = cms.double(-1),
            maxTrackChi2 = cms.double(100),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1),
            minNeutralHadronEt = cms.double(30),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1),
            useTracksInsteadOfPFHadrons = cms.optional.bool
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1),
            useTracksInsteadOfPFHadrons = cms.optional.bool
        )
    ),
    rhoConeSize = cms.double(0.5),
    rhoProducer = cms.InputTag("fixedGridRhoFastjetAll"),
    rhoUEOffsetCorrection = cms.double(1),
    verbosity = cms.int32(0),
    vertexSrc = cms.InputTag("offlinePrimaryVertices")
)


process.pfRecoTauDiscriminationByLeadingObjectPtCut = cms.EDProducer("PFRecoTauDiscriminationByLeadingObjectPtCut",
    MinPtLeadingObject = cms.double(5.0),
    PFTauProducer = cms.InputTag("pfRecoTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    UseOnlyChargedHadrons = cms.bool(False)
)


process.pfRecoTauDiscriminationByLeadingTrackFinding = cms.EDProducer("PFRecoTauDiscriminationByLeadingObjectPtCut",
    MinPtLeadingObject = cms.double(0.0),
    PFTauProducer = cms.InputTag("pfRecoTauProducer"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    UseOnlyChargedHadrons = cms.bool(True)
)


process.pfRecoTauDiscriminationByMVAIsolationRun2 = cms.EDProducer("PFRecoTauDiscriminationByMVAIsolationRun2",
    PFTauProducer = cms.InputTag("fixme"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('AND'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("fixme"),
            cut = cms.double(0)
        ),
        leadTrack = cms.PSet(
            Producer = cms.InputTag("fixme"),
            cut = cms.double(0)
        )
    ),
    inputFileName = cms.optional.FileInPath,
    inputIDNameSuffix = cms.string(''),
    loadMVAfromDB = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    mvaName = cms.string('tauIdMVAnewDMwLT'),
    mvaOpt = cms.string('newDMwLT'),
    srcBasicTauDiscriminators = cms.InputTag("hpsPFTauBasicDiscriminators"),
    srcTauTransverseImpactParameters = cms.InputTag(""),
    verbosity = cms.int32(0)
)


process.pfRecoTauTagInfoProducer = cms.EDProducer("PFRecoTauTagInfoProducer",
    ChargedHadrCand_AssociationCone = cms.double(0.8),
    ChargedHadrCand_tkPVmaxDZ = cms.double(0.2),
    ChargedHadrCand_tkmaxChi2 = cms.double(100),
    ChargedHadrCand_tkmaxipt = cms.double(0.03),
    ChargedHadrCand_tkminPixelHitsn = cms.int32(0),
    ChargedHadrCand_tkminPt = cms.double(0.5),
    ChargedHadrCand_tkminTrackerHitsn = cms.int32(3),
    GammaCand_EcalclusMinEt = cms.double(1),
    NeutrHadrCand_HcalclusMinEt = cms.double(1),
    PFCandidateProducer = cms.InputTag("particleFlow"),
    PFJetTracksAssociatorProducer = cms.InputTag("ak4PFJetTracksAssociatorAtVertex"),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    UsePVconstraint = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    smearedPVsigmaX = cms.double(0.0015),
    smearedPVsigmaY = cms.double(0.0015),
    smearedPVsigmaZ = cms.double(0.005),
    tkPVmaxDZ = cms.double(0.2),
    tkmaxChi2 = cms.double(100),
    tkmaxipt = cms.double(0.03),
    tkminPixelHitsn = cms.int32(0),
    tkminPt = cms.double(0.5),
    tkminTrackerHitsn = cms.int32(3)
)


process.pfRecoTauTagInfoProducerBoosted = cms.EDProducer("PFRecoTauTagInfoProducer",
    ChargedHadrCand_AssociationCone = cms.double(0.8),
    ChargedHadrCand_tkPVmaxDZ = cms.double(0.2),
    ChargedHadrCand_tkmaxChi2 = cms.double(100),
    ChargedHadrCand_tkmaxipt = cms.double(0.03),
    ChargedHadrCand_tkminPixelHitsn = cms.int32(0),
    ChargedHadrCand_tkminPt = cms.double(0.5),
    ChargedHadrCand_tkminTrackerHitsn = cms.int32(3),
    GammaCand_EcalclusMinEt = cms.double(1),
    NeutrHadrCand_HcalclusMinEt = cms.double(1),
    PFCandidateProducer = cms.InputTag("particleFlow"),
    PFJetTracksAssociatorProducer = cms.InputTag("ak4PFJetTracksAssociatorAtVertex"),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    UsePVconstraint = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    smearedPVsigmaX = cms.double(0.0015),
    smearedPVsigmaY = cms.double(0.0015),
    smearedPVsigmaZ = cms.double(0.005),
    tkPVmaxDZ = cms.double(0.2),
    tkmaxChi2 = cms.double(100),
    tkmaxipt = cms.double(0.03),
    tkminPixelHitsn = cms.int32(0),
    tkminPt = cms.double(0.5),
    tkminTrackerHitsn = cms.int32(3)
)


process.pfRecoTauTagInfoProducerElectronCleaned = cms.EDProducer("PFRecoTauTagInfoProducer",
    ChargedHadrCand_AssociationCone = cms.double(0.8),
    ChargedHadrCand_tkPVmaxDZ = cms.double(0.2),
    ChargedHadrCand_tkmaxChi2 = cms.double(100),
    ChargedHadrCand_tkmaxipt = cms.double(0.03),
    ChargedHadrCand_tkminPixelHitsn = cms.int32(0),
    ChargedHadrCand_tkminPt = cms.double(0.5),
    ChargedHadrCand_tkminTrackerHitsn = cms.int32(3),
    GammaCand_EcalclusMinEt = cms.double(1),
    NeutrHadrCand_HcalclusMinEt = cms.double(1),
    PFCandidateProducer = cms.InputTag("particleFlow"),
    PFJetTracksAssociatorProducer = cms.InputTag("ak4PFJetTracksAssociatorAtVertex"),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    UsePVconstraint = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    smearedPVsigmaX = cms.double(0.0015),
    smearedPVsigmaY = cms.double(0.0015),
    smearedPVsigmaZ = cms.double(0.005),
    tkPVmaxDZ = cms.double(0.2),
    tkmaxChi2 = cms.double(100),
    tkmaxipt = cms.double(0.03),
    tkminPixelHitsn = cms.int32(0),
    tkminPt = cms.double(0.5),
    tkminTrackerHitsn = cms.int32(3)
)


process.pfRecoTauTagInfoProducerLowPtElectronCleaned = cms.EDProducer("PFRecoTauTagInfoProducer",
    ChargedHadrCand_AssociationCone = cms.double(0.8),
    ChargedHadrCand_tkPVmaxDZ = cms.double(0.2),
    ChargedHadrCand_tkmaxChi2 = cms.double(100),
    ChargedHadrCand_tkmaxipt = cms.double(0.03),
    ChargedHadrCand_tkminPixelHitsn = cms.int32(0),
    ChargedHadrCand_tkminPt = cms.double(0.5),
    ChargedHadrCand_tkminTrackerHitsn = cms.int32(3),
    GammaCand_EcalclusMinEt = cms.double(1),
    NeutrHadrCand_HcalclusMinEt = cms.double(1),
    PFCandidateProducer = cms.InputTag("particleFlow"),
    PFJetTracksAssociatorProducer = cms.InputTag("ak4PFJetTracksAssociatorAtVertex"),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    UsePVconstraint = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    smearedPVsigmaX = cms.double(0.0015),
    smearedPVsigmaY = cms.double(0.0015),
    smearedPVsigmaZ = cms.double(0.005),
    tkPVmaxDZ = cms.double(0.2),
    tkmaxChi2 = cms.double(100),
    tkmaxipt = cms.double(0.03),
    tkminPixelHitsn = cms.int32(0),
    tkminPt = cms.double(0.5),
    tkminTrackerHitsn = cms.int32(3)
)


process.pfRecoTauTagInfoProducerMuonCleaned = cms.EDProducer("PFRecoTauTagInfoProducer",
    ChargedHadrCand_AssociationCone = cms.double(0.8),
    ChargedHadrCand_tkPVmaxDZ = cms.double(0.2),
    ChargedHadrCand_tkmaxChi2 = cms.double(100),
    ChargedHadrCand_tkmaxipt = cms.double(0.03),
    ChargedHadrCand_tkminPixelHitsn = cms.int32(0),
    ChargedHadrCand_tkminPt = cms.double(0.5),
    ChargedHadrCand_tkminTrackerHitsn = cms.int32(3),
    GammaCand_EcalclusMinEt = cms.double(1),
    NeutrHadrCand_HcalclusMinEt = cms.double(1),
    PFCandidateProducer = cms.InputTag("particleFlow"),
    PFJetTracksAssociatorProducer = cms.InputTag("ak4PFJetTracksAssociatorAtVertex"),
    PVProducer = cms.InputTag("offlinePrimaryVertices"),
    UsePVconstraint = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    smearedPVsigmaX = cms.double(0.0015),
    smearedPVsigmaY = cms.double(0.0015),
    smearedPVsigmaZ = cms.double(0.005),
    tkPVmaxDZ = cms.double(0.2),
    tkmaxChi2 = cms.double(100),
    tkmaxipt = cms.double(0.03),
    tkminPixelHitsn = cms.int32(0),
    tkminPt = cms.double(0.5),
    tkminTrackerHitsn = cms.int32(3)
)


process.pileupJetIdUpdated = cms.EDProducer("PileupJetIdProducer",
    algos = cms.VPSet(
        cms.PSet(
            JetIdParams = cms.PSet(
                Pt010_Loose = cms.vdouble(-0.95, -0.72, -0.68, -0.47),
                Pt010_Medium = cms.vdouble(0.26, -0.33, -0.54, -0.37),
                Pt010_Tight = cms.vdouble(0.77, 0.38, -0.31, -0.21),
                Pt1020_Loose = cms.vdouble(-0.95, -0.72, -0.68, -0.47),
                Pt1020_Medium = cms.vdouble(0.26, -0.33, -0.54, -0.37),
                Pt1020_Tight = cms.vdouble(0.77, 0.38, -0.31, -0.21),
                Pt2030_Loose = cms.vdouble(-0.88, -0.55, -0.6, -0.43),
                Pt2030_Medium = cms.vdouble(0.68, -0.04, -0.43, -0.3),
                Pt2030_Tight = cms.vdouble(0.9, 0.6, -0.12, -0.13),
                Pt3040_Loose = cms.vdouble(-0.63, -0.18, -0.43, -0.24),
                Pt3040_Medium = cms.vdouble(0.9, 0.36, -0.16, -0.09),
                Pt3040_Tight = cms.vdouble(0.96, 0.82, 0.2, 0.09),
                Pt4050_Loose = cms.vdouble(-0.19, 0.22, -0.13, -0.03),
                Pt4050_Medium = cms.vdouble(0.96, 0.61, 0.14, 0.12),
                Pt4050_Tight = cms.vdouble(0.98, 0.92, 0.47, 0.29)
            ),
            cutBased = cms.bool(False),
            etaBinnedWeights = cms.bool(True),
            impactParTkThreshold = cms.double(1.0),
            label = cms.string('full'),
            nEtaBins = cms.int32(4),
            tmvaMethod = cms.string('JetIDMVAHighPt'),
            tmvaSpectators = cms.vstring(
                'jetPt',
                'jetEta'
            ),
            trainings = cms.VPSet(
                cms.PSet(
                    jEtaMax = cms.double(2.5),
                    jEtaMin = cms.double(0.0),
                    tmvaVariables = cms.vstring(
                        'nvtx',
                        'beta',
                        'dR2Mean',
                        'frac01',
                        'frac02',
                        'frac03',
                        'frac04',
                        'majW',
                        'minW',
                        'jetR',
                        'jetRchg',
                        'nParticles',
                        'nCharged',
                        'ptD',
                        'pull'
                    ),
                    tmvaWeights = cms.FileInPath('RecoJets/JetProducers/data/pileupJetId_UL17_Eta0p0To2p5_chs_BDT.weights.xml.gz')
                ),
                cms.PSet(
                    jEtaMax = cms.double(2.75),
                    jEtaMin = cms.double(2.5),
                    tmvaVariables = cms.vstring(
                        'nvtx',
                        'beta',
                        'dR2Mean',
                        'frac01',
                        'frac02',
                        'frac03',
                        'frac04',
                        'majW',
                        'minW',
                        'jetR',
                        'jetRchg',
                        'nParticles',
                        'nCharged',
                        'ptD',
                        'pull'
                    ),
                    tmvaWeights = cms.FileInPath('RecoJets/JetProducers/data/pileupJetId_UL17_Eta2p5To2p75_chs_BDT.weights.xml.gz')
                ),
                cms.PSet(
                    jEtaMax = cms.double(3.0),
                    jEtaMin = cms.double(2.75),
                    tmvaVariables = cms.vstring(
                        'nvtx',
                        'beta',
                        'dR2Mean',
                        'frac01',
                        'frac02',
                        'frac03',
                        'frac04',
                        'majW',
                        'minW',
                        'jetR',
                        'jetRchg',
                        'nParticles',
                        'nCharged',
                        'ptD',
                        'pull'
                    ),
                    tmvaWeights = cms.FileInPath('RecoJets/JetProducers/data/pileupJetId_UL17_Eta2p75To3p0_chs_BDT.weights.xml.gz')
                ),
                cms.PSet(
                    jEtaMax = cms.double(5.0),
                    jEtaMin = cms.double(3.0),
                    tmvaVariables = cms.vstring(
                        'nvtx',
                        'dR2Mean',
                        'frac01',
                        'frac02',
                        'frac03',
                        'frac04',
                        'majW',
                        'minW',
                        'jetR',
                        'nParticles',
                        'ptD',
                        'pull'
                    ),
                    tmvaWeights = cms.FileInPath('RecoJets/JetProducers/data/pileupJetId_UL17_Eta3p0To5p0_chs_BDT.weights.xml.gz')
                )
            ),
            version = cms.int32(-1)
        ),
        cms.PSet(
            JetIdParams = cms.PSet(
                Pt010_BetaStarLoose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt010_BetaStarMedium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt010_BetaStarTight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt010_RMSLoose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt010_RMSMedium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt010_RMSTight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt1020_BetaStarLoose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt1020_BetaStarMedium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt1020_BetaStarTight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt1020_RMSLoose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt1020_RMSMedium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt1020_RMSTight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt2030_BetaStarLoose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt2030_BetaStarMedium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt2030_BetaStarTight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt2030_RMSLoose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt2030_RMSMedium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt2030_RMSTight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt3040_BetaStarLoose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt3040_BetaStarMedium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt3040_BetaStarTight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt3040_RMSLoose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt3040_RMSMedium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt3040_RMSTight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt4050_BetaStarLoose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt4050_BetaStarMedium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt4050_BetaStarTight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt4050_RMSLoose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt4050_RMSMedium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
                Pt4050_RMSTight = cms.vdouble(-999.0, -999.0, -999.0, -999.0)
            ),
            cutBased = cms.bool(True),
            impactParTkThreshold = cms.double(1.0),
            label = cms.string('cutbased')
        )
    ),
    applyJec = cms.bool(False),
    inputIsCorrected = cms.bool(True),
    jec = cms.string('AK4PFchs'),
    jetids = cms.InputTag(""),
    jets = cms.InputTag("slimmedJets"),
    produceJetIds = cms.bool(True),
    residualsFromTxt = cms.bool(False),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    runMvas = cms.bool(True),
    usePuppi = cms.bool(False),
    vertexes = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.prefiringweight = cms.EDProducer("L1PrefiringWeightProducer",
    DataEraECAL = cms.string('UL2017BtoF'),
    DataEraMuon = cms.string('20172018'),
    JetMaxMuonFraction = cms.double(0.5),
    L1Maps = cms.string('L1PrefiringMaps.root'),
    L1MuonParametrizations = cms.string('L1MuonPrefiringParametriations.root'),
    PrefiringRateSystematicUnctyECAL = cms.double(0.2),
    PrefiringRateSystematicUnctyMuon = cms.double(0.2),
    TheJets = cms.InputTag("updatedJets"),
    TheMuons = cms.InputTag("slimmedMuons"),
    ThePhotons = cms.InputTag("slimmedPhotons"),
    UseJetEMPt = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
)


process.recoTauAK4Jets08RegionPAT = cms.EDProducer("RecoTauPatJetRegionProducer",
    deltaR = cms.double(0.8),
    maxJetAbsEta = cms.double(2.5),
    minJetPt = cms.double(5),
    pfCandAssocMapSrc = cms.InputTag(""),
    pfCandSrc = cms.InputTag("packedPFCandidates"),
    src = cms.InputTag("patJetsPAT")
)


process.recoTauAK4Jets08RegionPATBoosted = cms.EDProducer("RecoTauPatJetRegionProducer",
    deltaR = cms.double(0.8),
    maxJetAbsEta = cms.double(2.5),
    minJetPt = cms.double(5),
    pfCandAssocMapSrc = cms.InputTag(""),
    pfCandSrc = cms.InputTag("packedPFCandidates"),
    src = cms.InputTag("boostedTauSeedsPAT")
)


process.recoTauAK4Jets08RegionPATElectronCleaned = cms.EDProducer("RecoTauPatJetRegionProducer",
    deltaR = cms.double(0.8),
    maxJetAbsEta = cms.double(2.5),
    minJetPt = cms.double(5),
    pfCandAssocMapSrc = cms.InputTag(""),
    pfCandSrc = cms.InputTag("PackedCandsElectronCleaned","packedPFCandidatesElectronCleaned"),
    src = cms.InputTag("patJetsPATElectronCleaned")
)


process.recoTauAK4Jets08RegionPATLowPtElectronCleaned = cms.EDProducer("RecoTauPatJetRegionProducer",
    deltaR = cms.double(0.8),
    maxJetAbsEta = cms.double(2.5),
    minJetPt = cms.double(14.0),
    pfCandAssocMapSrc = cms.InputTag(""),
    pfCandSrc = cms.InputTag("PackedCandsLowPtElectronCleaned","packedPFCandidatesLowPtElectronCleaned"),
    src = cms.InputTag("patJetsPATLowPtElectronCleaned")
)


process.recoTauAK4Jets08RegionPATMuonCleaned = cms.EDProducer("RecoTauPatJetRegionProducer",
    deltaR = cms.double(0.8),
    maxJetAbsEta = cms.double(2.5),
    minJetPt = cms.double(5),
    pfCandAssocMapSrc = cms.InputTag(""),
    pfCandSrc = cms.InputTag("PackedCandsMuonCleaned","packedPFCandidatesMuonCleaned"),
    src = cms.InputTag("patJetsPATMuonCleaned")
)


process.recoTauAK4PFJets08Region = cms.EDProducer("RecoTauJetRegionProducer",
    deltaR = cms.double(0.8),
    maxJetAbsEta = cms.double(2.5),
    minJetPt = cms.double(5),
    pfCandAssocMapSrc = cms.InputTag(""),
    pfCandSrc = cms.InputTag("particleFlow"),
    src = cms.InputTag("patJetsPAT"),
    verbosity = cms.int32(0)
)


process.recoTauAK4PFJets08RegionBoosted = cms.EDProducer("RecoTauJetRegionProducer",
    deltaR = cms.double(0.8),
    maxJetAbsEta = cms.double(2.5),
    minJetPt = cms.double(14.0),
    pfCandAssocMapSrc = cms.InputTag(""),
    pfCandSrc = cms.InputTag("particleFlow"),
    src = cms.InputTag("ak4PFJets"),
    verbosity = cms.int32(0)
)


process.recoTauAK4PFJets08RegionElectronCleaned = cms.EDProducer("RecoTauJetRegionProducer",
    deltaR = cms.double(0.8),
    maxJetAbsEta = cms.double(2.5),
    minJetPt = cms.double(5),
    pfCandAssocMapSrc = cms.InputTag(""),
    pfCandSrc = cms.InputTag("particleFlow"),
    src = cms.InputTag("ak4PFJets"),
    verbosity = cms.int32(0)
)


process.recoTauAK4PFJets08RegionLowPtElectronCleaned = cms.EDProducer("RecoTauJetRegionProducer",
    deltaR = cms.double(0.8),
    maxJetAbsEta = cms.double(2.5),
    minJetPt = cms.double(14.0),
    pfCandAssocMapSrc = cms.InputTag(""),
    pfCandSrc = cms.InputTag("particleFlow"),
    src = cms.InputTag("ak4PFJets"),
    verbosity = cms.int32(0)
)


process.recoTauAK4PFJets08RegionMuonCleaned = cms.EDProducer("RecoTauJetRegionProducer",
    deltaR = cms.double(0.8),
    maxJetAbsEta = cms.double(2.5),
    minJetPt = cms.double(5),
    pfCandAssocMapSrc = cms.InputTag(""),
    pfCandSrc = cms.InputTag("particleFlow"),
    src = cms.InputTag("ak4PFJets"),
    verbosity = cms.int32(0)
)


process.recoTauDiscriminantCutMultiplexerDefault = cms.EDProducer("RecoTauDiscriminantCutMultiplexer",
    PFTauProducer = cms.InputTag("fixme"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('AND'),
        decayMode = cms.PSet(
            Producer = cms.InputTag("fixme"),
            cut = cms.double(0)
        ),
        leadTrack = cms.PSet(
            Producer = cms.InputTag("fixme"),
            cut = cms.double(0)
        )
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('fixme')
    )),
    mightGet = cms.optional.untracked.vstring,
    mvaOutput_normalization = cms.string(''),
    rawValues = cms.vstring('discriminator'),
    toMultiplex = cms.InputTag("fixme"),
    verbosity = cms.int32(0),
    workingPoints = cms.vdouble(0)
)


process.rerunDiscriminationByIsolationOldDMMVArun2017v2 = cms.EDProducer("PATTauDiscriminantCutMultiplexer",
    PATTauProducer = cms.InputTag("selectedPatTausNoNewIDs"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2'),
        variable = cms.string('pt')
    )),
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_mvaOutput_normalization'),
    toMultiplex = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2raw"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_WPEff95',
        '_WPEff90',
        '_WPEff80',
        '_WPEff70',
        '_WPEff60',
        '_WPEff50',
        '_WPEff40'
    )
)


process.rerunDiscriminationByIsolationOldDMMVArun2017v2Boosted = cms.EDProducer("PATTauDiscriminantCutMultiplexer",
    PATTauProducer = cms.InputTag("selectedPatTausNoNewIDsBoosted"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2'),
        variable = cms.string('pt')
    )),
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_mvaOutput_normalization'),
    toMultiplex = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2rawBoosted"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_WPEff95',
        '_WPEff90',
        '_WPEff80',
        '_WPEff70',
        '_WPEff60',
        '_WPEff50',
        '_WPEff40'
    )
)


process.rerunDiscriminationByIsolationOldDMMVArun2017v2ElectronCleaned = cms.EDProducer("PATTauDiscriminantCutMultiplexer",
    PATTauProducer = cms.InputTag("selectedPatTausNoNewIDsElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2'),
        variable = cms.string('pt')
    )),
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_mvaOutput_normalization'),
    toMultiplex = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2rawElectronCleaned"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_WPEff95',
        '_WPEff90',
        '_WPEff80',
        '_WPEff70',
        '_WPEff60',
        '_WPEff50',
        '_WPEff40'
    )
)


process.rerunDiscriminationByIsolationOldDMMVArun2017v2LowPtElectronCleaned = cms.EDProducer("PATTauDiscriminantCutMultiplexer",
    PATTauProducer = cms.InputTag("selectedPatTausNoNewIDsLowPtElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2'),
        variable = cms.string('pt')
    )),
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_mvaOutput_normalization'),
    toMultiplex = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2rawLowPtElectronCleaned"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_WPEff95',
        '_WPEff90',
        '_WPEff80',
        '_WPEff70',
        '_WPEff60',
        '_WPEff50',
        '_WPEff40'
    )
)


process.rerunDiscriminationByIsolationOldDMMVArun2017v2MuonCleaned = cms.EDProducer("PATTauDiscriminantCutMultiplexer",
    PATTauProducer = cms.InputTag("selectedPatTausNoNewIDsMuonCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2'),
        variable = cms.string('pt')
    )),
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_mvaOutput_normalization'),
    toMultiplex = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2rawMuonCleaned"),
    verbosity = cms.int32(0),
    workingPoints = cms.vstring(
        '_WPEff95',
        '_WPEff90',
        '_WPEff80',
        '_WPEff70',
        '_WPEff60',
        '_WPEff50',
        '_WPEff40'
    )
)


process.rerunDiscriminationByIsolationOldDMMVArun2017v2raw = cms.EDProducer("PATTauDiscriminationByMVAIsolationRun2",
    PATTauProducer = cms.InputTag("selectedPatTausNoNewIDs"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    mvaName = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2'),
    mvaOpt = cms.string('DBoldDMwLTwGJ'),
    srcChargedIsoPtSum = cms.string('chargedIsoPtSum'),
    srcFootprintCorrection = cms.string('footprintCorrection'),
    srcNeutralIsoPtSum = cms.string('neutralIsoPtSum'),
    srcPUcorrPtSum = cms.string('puCorrPtSum'),
    srcPhotonPtSumOutsideSignalCone = cms.string('photonPtSumOutsideSignalCone'),
    verbosity = cms.int32(0)
)


process.rerunDiscriminationByIsolationOldDMMVArun2017v2rawBoosted = cms.EDProducer("PATTauDiscriminationByMVAIsolationRun2",
    PATTauProducer = cms.InputTag("selectedPatTausNoNewIDsBoosted"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    mvaName = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2'),
    mvaOpt = cms.string('DBoldDMwLTwGJ'),
    srcChargedIsoPtSum = cms.string('chargedIsoPtSum'),
    srcFootprintCorrection = cms.string('footprintCorrection'),
    srcNeutralIsoPtSum = cms.string('neutralIsoPtSum'),
    srcPUcorrPtSum = cms.string('puCorrPtSum'),
    srcPhotonPtSumOutsideSignalCone = cms.string('photonPtSumOutsideSignalCone'),
    verbosity = cms.int32(0)
)


process.rerunDiscriminationByIsolationOldDMMVArun2017v2rawElectronCleaned = cms.EDProducer("PATTauDiscriminationByMVAIsolationRun2",
    PATTauProducer = cms.InputTag("selectedPatTausNoNewIDsElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    mvaName = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2'),
    mvaOpt = cms.string('DBoldDMwLTwGJ'),
    srcChargedIsoPtSum = cms.string('chargedIsoPtSum'),
    srcFootprintCorrection = cms.string('footprintCorrection'),
    srcNeutralIsoPtSum = cms.string('neutralIsoPtSum'),
    srcPUcorrPtSum = cms.string('puCorrPtSum'),
    srcPhotonPtSumOutsideSignalCone = cms.string('photonPtSumOutsideSignalCone'),
    verbosity = cms.int32(0)
)


process.rerunDiscriminationByIsolationOldDMMVArun2017v2rawLowPtElectronCleaned = cms.EDProducer("PATTauDiscriminationByMVAIsolationRun2",
    PATTauProducer = cms.InputTag("selectedPatTausNoNewIDsLowPtElectronCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    mvaName = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2'),
    mvaOpt = cms.string('DBoldDMwLTwGJ'),
    srcChargedIsoPtSum = cms.string('chargedIsoPtSum'),
    srcFootprintCorrection = cms.string('footprintCorrection'),
    srcNeutralIsoPtSum = cms.string('neutralIsoPtSum'),
    srcPUcorrPtSum = cms.string('puCorrPtSum'),
    srcPhotonPtSumOutsideSignalCone = cms.string('photonPtSumOutsideSignalCone'),
    verbosity = cms.int32(0)
)


process.rerunDiscriminationByIsolationOldDMMVArun2017v2rawMuonCleaned = cms.EDProducer("PATTauDiscriminationByMVAIsolationRun2",
    PATTauProducer = cms.InputTag("selectedPatTausNoNewIDsMuonCleaned"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
    loadMVAfromDB = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    mvaName = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2'),
    mvaOpt = cms.string('DBoldDMwLTwGJ'),
    srcChargedIsoPtSum = cms.string('chargedIsoPtSum'),
    srcFootprintCorrection = cms.string('footprintCorrection'),
    srcNeutralIsoPtSum = cms.string('neutralIsoPtSum'),
    srcPUcorrPtSum = cms.string('puCorrPtSum'),
    srcPhotonPtSumOutsideSignalCone = cms.string('photonPtSumOutsideSignalCone'),
    verbosity = cms.int32(0)
)


process.selectedPatTaus = cms.EDProducer("PATTauIDEmbedder",
    cut = cms.string("pt > 8.0 && abs(eta)<2.3 && tauID(\'decayModeFinding\')> 0.5"),
    src = cms.InputTag("selectedPatTausNoNewIDs"),
    tauIDSources = cms.PSet(
        againstElectronLooseMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018"),
            workingPointIndex = cms.int32(1)
        ),
        againstElectronMVA6Raw2018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018"),
            workingPointIndex = cms.int32(-1)
        ),
        againstElectronMVA6category2018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018"),
            workingPointIndex = cms.int32(-2)
        ),
        againstElectronMediumMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018"),
            workingPointIndex = cms.int32(2)
        ),
        againstElectronTightMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018"),
            workingPointIndex = cms.int32(3)
        ),
        againstElectronVLooseMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018"),
            workingPointIndex = cms.int32(0)
        ),
        againstElectronVTightMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018"),
            workingPointIndex = cms.int32(4)
        ),
        byDeepTau2017v2p1VSeraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSe"),
            workingPointIndex = cms.int32(-1)
        ),
        byDeepTau2017v2p1VSjetraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSjet"),
            workingPointIndex = cms.int32(-1)
        ),
        byDeepTau2017v2p1VSmuraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSmu"),
            workingPointIndex = cms.int32(-1)
        ),
        byIsolationMVArun2017v2DBoldDMwLTraw2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2"),
            workingPointIndex = cms.int32(-1)
        ),
        byLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSe"),
            workingPointIndex = cms.int32(3)
        ),
        byLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSjet"),
            workingPointIndex = cms.int32(3)
        ),
        byLooseDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSmu"),
            workingPointIndex = cms.int32(1)
        ),
        byLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2"),
            workingPointIndex = cms.int32(2)
        ),
        byMediumDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSe"),
            workingPointIndex = cms.int32(4)
        ),
        byMediumDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSjet"),
            workingPointIndex = cms.int32(4)
        ),
        byMediumDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSmu"),
            workingPointIndex = cms.int32(2)
        ),
        byMediumIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2"),
            workingPointIndex = cms.int32(3)
        ),
        byTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSe"),
            workingPointIndex = cms.int32(5)
        ),
        byTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSjet"),
            workingPointIndex = cms.int32(5)
        ),
        byTightDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSmu"),
            workingPointIndex = cms.int32(3)
        ),
        byTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2"),
            workingPointIndex = cms.int32(4)
        ),
        byVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSe"),
            workingPointIndex = cms.int32(2)
        ),
        byVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSjet"),
            workingPointIndex = cms.int32(2)
        ),
        byVLooseDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSmu"),
            workingPointIndex = cms.int32(0)
        ),
        byVLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2"),
            workingPointIndex = cms.int32(1)
        ),
        byVTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSe"),
            workingPointIndex = cms.int32(6)
        ),
        byVTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSjet"),
            workingPointIndex = cms.int32(6)
        ),
        byVTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2"),
            workingPointIndex = cms.int32(5)
        ),
        byVVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSe"),
            workingPointIndex = cms.int32(1)
        ),
        byVVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSjet"),
            workingPointIndex = cms.int32(1)
        ),
        byVVLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2"),
            workingPointIndex = cms.int32(0)
        ),
        byVVTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSe"),
            workingPointIndex = cms.int32(7)
        ),
        byVVTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSjet"),
            workingPointIndex = cms.int32(7)
        ),
        byVVTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2"),
            workingPointIndex = cms.int32(6)
        ),
        byVVVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSe"),
            workingPointIndex = cms.int32(0)
        ),
        byVVVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSjet"),
            workingPointIndex = cms.int32(0)
        )
    )
)


process.selectedPatTausBoosted = cms.EDProducer("PATTauIDEmbedder",
    cut = cms.string("pt > 8 && abs(eta) < 2.3 && tauID(\'decayModeFinding\')> 0.5"),
    src = cms.InputTag("selectedPatTausNoNewIDsBoosted"),
    tauIDSources = cms.PSet(
        againstElectronLooseMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018Boosted"),
            workingPointIndex = cms.int32(1)
        ),
        againstElectronMVA6Raw2018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018Boosted"),
            workingPointIndex = cms.int32(-1)
        ),
        againstElectronMVA6category2018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018Boosted"),
            workingPointIndex = cms.int32(-2)
        ),
        againstElectronMediumMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018Boosted"),
            workingPointIndex = cms.int32(2)
        ),
        againstElectronTightMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018Boosted"),
            workingPointIndex = cms.int32(3)
        ),
        againstElectronVLooseMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018Boosted"),
            workingPointIndex = cms.int32(0)
        ),
        againstElectronVTightMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018Boosted"),
            workingPointIndex = cms.int32(4)
        ),
        byDeepTau2017v2p1VSeraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSe"),
            workingPointIndex = cms.int32(-1)
        ),
        byDeepTau2017v2p1VSjetraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSjet"),
            workingPointIndex = cms.int32(-1)
        ),
        byDeepTau2017v2p1VSmuraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSmu"),
            workingPointIndex = cms.int32(-1)
        ),
        byIsolationMVArun2017v2DBoldDMwLTraw2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2Boosted"),
            workingPointIndex = cms.int32(-1)
        ),
        byLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSe"),
            workingPointIndex = cms.int32(3)
        ),
        byLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSjet"),
            workingPointIndex = cms.int32(3)
        ),
        byLooseDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSmu"),
            workingPointIndex = cms.int32(1)
        ),
        byLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2Boosted"),
            workingPointIndex = cms.int32(2)
        ),
        byMediumDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSe"),
            workingPointIndex = cms.int32(4)
        ),
        byMediumDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSjet"),
            workingPointIndex = cms.int32(4)
        ),
        byMediumDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSmu"),
            workingPointIndex = cms.int32(2)
        ),
        byMediumIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2Boosted"),
            workingPointIndex = cms.int32(3)
        ),
        byTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSe"),
            workingPointIndex = cms.int32(5)
        ),
        byTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSjet"),
            workingPointIndex = cms.int32(5)
        ),
        byTightDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSmu"),
            workingPointIndex = cms.int32(3)
        ),
        byTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2Boosted"),
            workingPointIndex = cms.int32(4)
        ),
        byVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSe"),
            workingPointIndex = cms.int32(2)
        ),
        byVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSjet"),
            workingPointIndex = cms.int32(2)
        ),
        byVLooseDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSmu"),
            workingPointIndex = cms.int32(0)
        ),
        byVLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2Boosted"),
            workingPointIndex = cms.int32(1)
        ),
        byVTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSe"),
            workingPointIndex = cms.int32(6)
        ),
        byVTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSjet"),
            workingPointIndex = cms.int32(6)
        ),
        byVTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2Boosted"),
            workingPointIndex = cms.int32(5)
        ),
        byVVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSe"),
            workingPointIndex = cms.int32(1)
        ),
        byVVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSjet"),
            workingPointIndex = cms.int32(1)
        ),
        byVVLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2Boosted"),
            workingPointIndex = cms.int32(0)
        ),
        byVVTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSe"),
            workingPointIndex = cms.int32(7)
        ),
        byVVTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSjet"),
            workingPointIndex = cms.int32(7)
        ),
        byVVTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2Boosted"),
            workingPointIndex = cms.int32(6)
        ),
        byVVVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSe"),
            workingPointIndex = cms.int32(0)
        ),
        byVVVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSjet"),
            workingPointIndex = cms.int32(0)
        )
    )
)


process.selectedPatTausElectronCleaned = cms.EDProducer("PATTauIDEmbedder",
    cut = cms.string("pt > 8 && abs(eta) < 2.3 && tauID(\'decayModeFinding\')> 0.5"),
    src = cms.InputTag("selectedPatTausNoNewIDsElectronCleaned"),
    tauIDSources = cms.PSet(
        againstElectronLooseMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018ElectronCleaned"),
            workingPointIndex = cms.int32(1)
        ),
        againstElectronMVA6Raw2018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018ElectronCleaned"),
            workingPointIndex = cms.int32(-1)
        ),
        againstElectronMVA6category2018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018ElectronCleaned"),
            workingPointIndex = cms.int32(-2)
        ),
        againstElectronMediumMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018ElectronCleaned"),
            workingPointIndex = cms.int32(2)
        ),
        againstElectronTightMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018ElectronCleaned"),
            workingPointIndex = cms.int32(3)
        ),
        againstElectronVLooseMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018ElectronCleaned"),
            workingPointIndex = cms.int32(0)
        ),
        againstElectronVTightMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018ElectronCleaned"),
            workingPointIndex = cms.int32(4)
        ),
        byDeepTau2017v2p1VSeraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSe"),
            workingPointIndex = cms.int32(-1)
        ),
        byDeepTau2017v2p1VSjetraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(-1)
        ),
        byDeepTau2017v2p1VSmuraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSmu"),
            workingPointIndex = cms.int32(-1)
        ),
        byIsolationMVArun2017v2DBoldDMwLTraw2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2ElectronCleaned"),
            workingPointIndex = cms.int32(-1)
        ),
        byLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSe"),
            workingPointIndex = cms.int32(3)
        ),
        byLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(3)
        ),
        byLooseDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSmu"),
            workingPointIndex = cms.int32(1)
        ),
        byLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2ElectronCleaned"),
            workingPointIndex = cms.int32(2)
        ),
        byMediumDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSe"),
            workingPointIndex = cms.int32(4)
        ),
        byMediumDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(4)
        ),
        byMediumDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSmu"),
            workingPointIndex = cms.int32(2)
        ),
        byMediumIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2ElectronCleaned"),
            workingPointIndex = cms.int32(3)
        ),
        byTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSe"),
            workingPointIndex = cms.int32(5)
        ),
        byTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(5)
        ),
        byTightDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSmu"),
            workingPointIndex = cms.int32(3)
        ),
        byTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2ElectronCleaned"),
            workingPointIndex = cms.int32(4)
        ),
        byVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSe"),
            workingPointIndex = cms.int32(2)
        ),
        byVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(2)
        ),
        byVLooseDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSmu"),
            workingPointIndex = cms.int32(0)
        ),
        byVLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2ElectronCleaned"),
            workingPointIndex = cms.int32(1)
        ),
        byVTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSe"),
            workingPointIndex = cms.int32(6)
        ),
        byVTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(6)
        ),
        byVTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2ElectronCleaned"),
            workingPointIndex = cms.int32(5)
        ),
        byVVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSe"),
            workingPointIndex = cms.int32(1)
        ),
        byVVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(1)
        ),
        byVVLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2ElectronCleaned"),
            workingPointIndex = cms.int32(0)
        ),
        byVVTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSe"),
            workingPointIndex = cms.int32(7)
        ),
        byVVTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(7)
        ),
        byVVTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2ElectronCleaned"),
            workingPointIndex = cms.int32(6)
        ),
        byVVVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSe"),
            workingPointIndex = cms.int32(0)
        ),
        byVVVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(0)
        )
    )
)


process.selectedPatTausLowPtElectronCleaned = cms.EDProducer("PATTauIDEmbedder",
    src = cms.InputTag("selectedPatTausNoNewIDsLowPtElectronCleaned"),
    tauIDSources = cms.PSet(
        againstElectronLooseMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018LowPtElectronCleaned"),
            workingPointIndex = cms.int32(1)
        ),
        againstElectronMVA6Raw2018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018LowPtElectronCleaned"),
            workingPointIndex = cms.int32(-1)
        ),
        againstElectronMVA6category2018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018LowPtElectronCleaned"),
            workingPointIndex = cms.int32(-2)
        ),
        againstElectronMediumMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018LowPtElectronCleaned"),
            workingPointIndex = cms.int32(2)
        ),
        againstElectronTightMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018LowPtElectronCleaned"),
            workingPointIndex = cms.int32(3)
        ),
        againstElectronVLooseMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018LowPtElectronCleaned"),
            workingPointIndex = cms.int32(0)
        ),
        againstElectronVTightMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018LowPtElectronCleaned"),
            workingPointIndex = cms.int32(4)
        ),
        byDeepTau2017v2p1VSeraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSe"),
            workingPointIndex = cms.int32(-1)
        ),
        byDeepTau2017v2p1VSjetraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(-1)
        ),
        byDeepTau2017v2p1VSmuraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSmu"),
            workingPointIndex = cms.int32(-1)
        ),
        byIsolationMVArun2017v2DBoldDMwLTraw2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2LowPtElectronCleaned"),
            workingPointIndex = cms.int32(-1)
        ),
        byLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSe"),
            workingPointIndex = cms.int32(3)
        ),
        byLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(3)
        ),
        byLooseDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSmu"),
            workingPointIndex = cms.int32(1)
        ),
        byLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2LowPtElectronCleaned"),
            workingPointIndex = cms.int32(2)
        ),
        byMediumDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSe"),
            workingPointIndex = cms.int32(4)
        ),
        byMediumDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(4)
        ),
        byMediumDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSmu"),
            workingPointIndex = cms.int32(2)
        ),
        byMediumIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2LowPtElectronCleaned"),
            workingPointIndex = cms.int32(3)
        ),
        byTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSe"),
            workingPointIndex = cms.int32(5)
        ),
        byTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(5)
        ),
        byTightDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSmu"),
            workingPointIndex = cms.int32(3)
        ),
        byTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2LowPtElectronCleaned"),
            workingPointIndex = cms.int32(4)
        ),
        byVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSe"),
            workingPointIndex = cms.int32(2)
        ),
        byVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(2)
        ),
        byVLooseDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSmu"),
            workingPointIndex = cms.int32(0)
        ),
        byVLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2LowPtElectronCleaned"),
            workingPointIndex = cms.int32(1)
        ),
        byVTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSe"),
            workingPointIndex = cms.int32(6)
        ),
        byVTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(6)
        ),
        byVTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2LowPtElectronCleaned"),
            workingPointIndex = cms.int32(5)
        ),
        byVVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSe"),
            workingPointIndex = cms.int32(1)
        ),
        byVVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(1)
        ),
        byVVLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2LowPtElectronCleaned"),
            workingPointIndex = cms.int32(0)
        ),
        byVVTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSe"),
            workingPointIndex = cms.int32(7)
        ),
        byVVTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(7)
        ),
        byVVTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2LowPtElectronCleaned"),
            workingPointIndex = cms.int32(6)
        ),
        byVVVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSe"),
            workingPointIndex = cms.int32(0)
        ),
        byVVVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(0)
        )
    )
)


process.selectedPatTausMuonCleaned = cms.EDProducer("PATTauIDEmbedder",
    cut = cms.string("pt > 8 && abs(eta) < 2.3 && tauID(\'decayModeFinding\')> 0.5"),
    src = cms.InputTag("selectedPatTausNoNewIDsMuonCleaned"),
    tauIDSources = cms.PSet(
        againstElectronLooseMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018MuonCleaned"),
            workingPointIndex = cms.int32(1)
        ),
        againstElectronMVA6Raw2018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018MuonCleaned"),
            workingPointIndex = cms.int32(-1)
        ),
        againstElectronMVA6category2018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018MuonCleaned"),
            workingPointIndex = cms.int32(-2)
        ),
        againstElectronMediumMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018MuonCleaned"),
            workingPointIndex = cms.int32(2)
        ),
        againstElectronTightMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018MuonCleaned"),
            workingPointIndex = cms.int32(3)
        ),
        againstElectronVLooseMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018MuonCleaned"),
            workingPointIndex = cms.int32(0)
        ),
        againstElectronVTightMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018MuonCleaned"),
            workingPointIndex = cms.int32(4)
        ),
        byDeepTau2017v2p1VSeraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSe"),
            workingPointIndex = cms.int32(-1)
        ),
        byDeepTau2017v2p1VSjetraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSjet"),
            workingPointIndex = cms.int32(-1)
        ),
        byDeepTau2017v2p1VSmuraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSmu"),
            workingPointIndex = cms.int32(-1)
        ),
        byIsolationMVArun2017v2DBoldDMwLTraw2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2MuonCleaned"),
            workingPointIndex = cms.int32(-1)
        ),
        byLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSe"),
            workingPointIndex = cms.int32(3)
        ),
        byLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSjet"),
            workingPointIndex = cms.int32(3)
        ),
        byLooseDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSmu"),
            workingPointIndex = cms.int32(1)
        ),
        byLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2MuonCleaned"),
            workingPointIndex = cms.int32(2)
        ),
        byMediumDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSe"),
            workingPointIndex = cms.int32(4)
        ),
        byMediumDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSjet"),
            workingPointIndex = cms.int32(4)
        ),
        byMediumDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSmu"),
            workingPointIndex = cms.int32(2)
        ),
        byMediumIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2MuonCleaned"),
            workingPointIndex = cms.int32(3)
        ),
        byTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSe"),
            workingPointIndex = cms.int32(5)
        ),
        byTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSjet"),
            workingPointIndex = cms.int32(5)
        ),
        byTightDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSmu"),
            workingPointIndex = cms.int32(3)
        ),
        byTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2MuonCleaned"),
            workingPointIndex = cms.int32(4)
        ),
        byVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSe"),
            workingPointIndex = cms.int32(2)
        ),
        byVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSjet"),
            workingPointIndex = cms.int32(2)
        ),
        byVLooseDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSmu"),
            workingPointIndex = cms.int32(0)
        ),
        byVLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2MuonCleaned"),
            workingPointIndex = cms.int32(1)
        ),
        byVTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSe"),
            workingPointIndex = cms.int32(6)
        ),
        byVTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSjet"),
            workingPointIndex = cms.int32(6)
        ),
        byVTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2MuonCleaned"),
            workingPointIndex = cms.int32(5)
        ),
        byVVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSe"),
            workingPointIndex = cms.int32(1)
        ),
        byVVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSjet"),
            workingPointIndex = cms.int32(1)
        ),
        byVVLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2MuonCleaned"),
            workingPointIndex = cms.int32(0)
        ),
        byVVTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSe"),
            workingPointIndex = cms.int32(7)
        ),
        byVVTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSjet"),
            workingPointIndex = cms.int32(7)
        ),
        byVVTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2MuonCleaned"),
            workingPointIndex = cms.int32(6)
        ),
        byVVVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSe"),
            workingPointIndex = cms.int32(0)
        ),
        byVVVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSjet"),
            workingPointIndex = cms.int32(0)
        )
    )
)


process.selectedPatTausNewIDs = cms.EDProducer("PATTauIDEmbedder",
    src = cms.InputTag("slimmedTaus"),
    tauIDSources = cms.PSet(
        againstElectronLooseMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018"),
            workingPointIndex = cms.int32(1)
        ),
        againstElectronMVA6Raw2018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018"),
            workingPointIndex = cms.int32(-1)
        ),
        againstElectronMVA6category2018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018"),
            workingPointIndex = cms.int32(-2)
        ),
        againstElectronMediumMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018"),
            workingPointIndex = cms.int32(2)
        ),
        againstElectronTightMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018"),
            workingPointIndex = cms.int32(3)
        ),
        againstElectronVLooseMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018"),
            workingPointIndex = cms.int32(0)
        ),
        againstElectronVTightMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018"),
            workingPointIndex = cms.int32(4)
        ),
        byDeepTau2017v2p1VSeraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSe"),
            workingPointIndex = cms.int32(-1)
        ),
        byDeepTau2017v2p1VSjetraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSjet"),
            workingPointIndex = cms.int32(-1)
        ),
        byDeepTau2017v2p1VSmuraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSmu"),
            workingPointIndex = cms.int32(-1)
        ),
        byIsolationMVArun2017v2DBoldDMwLTraw2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2"),
            workingPointIndex = cms.int32(-1)
        ),
        byLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSe"),
            workingPointIndex = cms.int32(3)
        ),
        byLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSjet"),
            workingPointIndex = cms.int32(3)
        ),
        byLooseDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSmu"),
            workingPointIndex = cms.int32(1)
        ),
        byLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2"),
            workingPointIndex = cms.int32(2)
        ),
        byMediumDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSe"),
            workingPointIndex = cms.int32(4)
        ),
        byMediumDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSjet"),
            workingPointIndex = cms.int32(4)
        ),
        byMediumDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSmu"),
            workingPointIndex = cms.int32(2)
        ),
        byMediumIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2"),
            workingPointIndex = cms.int32(3)
        ),
        byTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSe"),
            workingPointIndex = cms.int32(5)
        ),
        byTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSjet"),
            workingPointIndex = cms.int32(5)
        ),
        byTightDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSmu"),
            workingPointIndex = cms.int32(3)
        ),
        byTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2"),
            workingPointIndex = cms.int32(4)
        ),
        byVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSe"),
            workingPointIndex = cms.int32(2)
        ),
        byVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSjet"),
            workingPointIndex = cms.int32(2)
        ),
        byVLooseDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSmu"),
            workingPointIndex = cms.int32(0)
        ),
        byVLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2"),
            workingPointIndex = cms.int32(1)
        ),
        byVTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSe"),
            workingPointIndex = cms.int32(6)
        ),
        byVTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSjet"),
            workingPointIndex = cms.int32(6)
        ),
        byVTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2"),
            workingPointIndex = cms.int32(5)
        ),
        byVVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSe"),
            workingPointIndex = cms.int32(1)
        ),
        byVVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSjet"),
            workingPointIndex = cms.int32(1)
        ),
        byVVLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2"),
            workingPointIndex = cms.int32(0)
        ),
        byVVTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSe"),
            workingPointIndex = cms.int32(7)
        ),
        byVVTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSjet"),
            workingPointIndex = cms.int32(7)
        ),
        byVVTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2"),
            workingPointIndex = cms.int32(6)
        ),
        byVVVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSe"),
            workingPointIndex = cms.int32(0)
        ),
        byVVVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1","VSjet"),
            workingPointIndex = cms.int32(0)
        )
    )
)


process.selectedPatTausNewIDsBoosted = cms.EDProducer("PATTauIDEmbedder",
    src = cms.InputTag("slimmedTaus"),
    tauIDSources = cms.PSet(
        againstElectronLooseMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018Boosted"),
            workingPointIndex = cms.int32(1)
        ),
        againstElectronMVA6Raw2018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018Boosted"),
            workingPointIndex = cms.int32(-1)
        ),
        againstElectronMVA6category2018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018Boosted"),
            workingPointIndex = cms.int32(-2)
        ),
        againstElectronMediumMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018Boosted"),
            workingPointIndex = cms.int32(2)
        ),
        againstElectronTightMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018Boosted"),
            workingPointIndex = cms.int32(3)
        ),
        againstElectronVLooseMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018Boosted"),
            workingPointIndex = cms.int32(0)
        ),
        againstElectronVTightMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018Boosted"),
            workingPointIndex = cms.int32(4)
        ),
        byDeepTau2017v2p1VSeraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSe"),
            workingPointIndex = cms.int32(-1)
        ),
        byDeepTau2017v2p1VSjetraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSjet"),
            workingPointIndex = cms.int32(-1)
        ),
        byDeepTau2017v2p1VSmuraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSmu"),
            workingPointIndex = cms.int32(-1)
        ),
        byIsolationMVArun2017v2DBoldDMwLTraw2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2Boosted"),
            workingPointIndex = cms.int32(-1)
        ),
        byLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSe"),
            workingPointIndex = cms.int32(3)
        ),
        byLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSjet"),
            workingPointIndex = cms.int32(3)
        ),
        byLooseDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSmu"),
            workingPointIndex = cms.int32(1)
        ),
        byLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2Boosted"),
            workingPointIndex = cms.int32(2)
        ),
        byMediumDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSe"),
            workingPointIndex = cms.int32(4)
        ),
        byMediumDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSjet"),
            workingPointIndex = cms.int32(4)
        ),
        byMediumDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSmu"),
            workingPointIndex = cms.int32(2)
        ),
        byMediumIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2Boosted"),
            workingPointIndex = cms.int32(3)
        ),
        byTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSe"),
            workingPointIndex = cms.int32(5)
        ),
        byTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSjet"),
            workingPointIndex = cms.int32(5)
        ),
        byTightDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSmu"),
            workingPointIndex = cms.int32(3)
        ),
        byTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2Boosted"),
            workingPointIndex = cms.int32(4)
        ),
        byVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSe"),
            workingPointIndex = cms.int32(2)
        ),
        byVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSjet"),
            workingPointIndex = cms.int32(2)
        ),
        byVLooseDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSmu"),
            workingPointIndex = cms.int32(0)
        ),
        byVLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2Boosted"),
            workingPointIndex = cms.int32(1)
        ),
        byVTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSe"),
            workingPointIndex = cms.int32(6)
        ),
        byVTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSjet"),
            workingPointIndex = cms.int32(6)
        ),
        byVTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2Boosted"),
            workingPointIndex = cms.int32(5)
        ),
        byVVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSe"),
            workingPointIndex = cms.int32(1)
        ),
        byVVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSjet"),
            workingPointIndex = cms.int32(1)
        ),
        byVVLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2Boosted"),
            workingPointIndex = cms.int32(0)
        ),
        byVVTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSe"),
            workingPointIndex = cms.int32(7)
        ),
        byVVTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSjet"),
            workingPointIndex = cms.int32(7)
        ),
        byVVTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2Boosted"),
            workingPointIndex = cms.int32(6)
        ),
        byVVVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSe"),
            workingPointIndex = cms.int32(0)
        ),
        byVVVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1Boosted","VSjet"),
            workingPointIndex = cms.int32(0)
        )
    )
)


process.selectedPatTausNewIDsElectronCleaned = cms.EDProducer("PATTauIDEmbedder",
    src = cms.InputTag("slimmedTaus"),
    tauIDSources = cms.PSet(
        againstElectronLooseMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018ElectronCleaned"),
            workingPointIndex = cms.int32(1)
        ),
        againstElectronMVA6Raw2018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018ElectronCleaned"),
            workingPointIndex = cms.int32(-1)
        ),
        againstElectronMVA6category2018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018ElectronCleaned"),
            workingPointIndex = cms.int32(-2)
        ),
        againstElectronMediumMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018ElectronCleaned"),
            workingPointIndex = cms.int32(2)
        ),
        againstElectronTightMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018ElectronCleaned"),
            workingPointIndex = cms.int32(3)
        ),
        againstElectronVLooseMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018ElectronCleaned"),
            workingPointIndex = cms.int32(0)
        ),
        againstElectronVTightMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018ElectronCleaned"),
            workingPointIndex = cms.int32(4)
        ),
        byDeepTau2017v2p1VSeraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSe"),
            workingPointIndex = cms.int32(-1)
        ),
        byDeepTau2017v2p1VSjetraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(-1)
        ),
        byDeepTau2017v2p1VSmuraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSmu"),
            workingPointIndex = cms.int32(-1)
        ),
        byIsolationMVArun2017v2DBoldDMwLTraw2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2ElectronCleaned"),
            workingPointIndex = cms.int32(-1)
        ),
        byLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSe"),
            workingPointIndex = cms.int32(3)
        ),
        byLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(3)
        ),
        byLooseDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSmu"),
            workingPointIndex = cms.int32(1)
        ),
        byLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2ElectronCleaned"),
            workingPointIndex = cms.int32(2)
        ),
        byMediumDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSe"),
            workingPointIndex = cms.int32(4)
        ),
        byMediumDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(4)
        ),
        byMediumDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSmu"),
            workingPointIndex = cms.int32(2)
        ),
        byMediumIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2ElectronCleaned"),
            workingPointIndex = cms.int32(3)
        ),
        byTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSe"),
            workingPointIndex = cms.int32(5)
        ),
        byTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(5)
        ),
        byTightDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSmu"),
            workingPointIndex = cms.int32(3)
        ),
        byTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2ElectronCleaned"),
            workingPointIndex = cms.int32(4)
        ),
        byVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSe"),
            workingPointIndex = cms.int32(2)
        ),
        byVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(2)
        ),
        byVLooseDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSmu"),
            workingPointIndex = cms.int32(0)
        ),
        byVLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2ElectronCleaned"),
            workingPointIndex = cms.int32(1)
        ),
        byVTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSe"),
            workingPointIndex = cms.int32(6)
        ),
        byVTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(6)
        ),
        byVTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2ElectronCleaned"),
            workingPointIndex = cms.int32(5)
        ),
        byVVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSe"),
            workingPointIndex = cms.int32(1)
        ),
        byVVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(1)
        ),
        byVVLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2ElectronCleaned"),
            workingPointIndex = cms.int32(0)
        ),
        byVVTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSe"),
            workingPointIndex = cms.int32(7)
        ),
        byVVTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(7)
        ),
        byVVTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2ElectronCleaned"),
            workingPointIndex = cms.int32(6)
        ),
        byVVVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSe"),
            workingPointIndex = cms.int32(0)
        ),
        byVVVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1ElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(0)
        )
    )
)


process.selectedPatTausNewIDsLowPtElectronCleaned = cms.EDProducer("PATTauIDEmbedder",
    src = cms.InputTag("slimmedTaus"),
    tauIDSources = cms.PSet(
        againstElectronLooseMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018LowPtElectronCleaned"),
            workingPointIndex = cms.int32(1)
        ),
        againstElectronMVA6Raw2018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018LowPtElectronCleaned"),
            workingPointIndex = cms.int32(-1)
        ),
        againstElectronMVA6category2018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018LowPtElectronCleaned"),
            workingPointIndex = cms.int32(-2)
        ),
        againstElectronMediumMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018LowPtElectronCleaned"),
            workingPointIndex = cms.int32(2)
        ),
        againstElectronTightMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018LowPtElectronCleaned"),
            workingPointIndex = cms.int32(3)
        ),
        againstElectronVLooseMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018LowPtElectronCleaned"),
            workingPointIndex = cms.int32(0)
        ),
        againstElectronVTightMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018LowPtElectronCleaned"),
            workingPointIndex = cms.int32(4)
        ),
        byDeepTau2017v2p1VSeraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSe"),
            workingPointIndex = cms.int32(-1)
        ),
        byDeepTau2017v2p1VSjetraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(-1)
        ),
        byDeepTau2017v2p1VSmuraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSmu"),
            workingPointIndex = cms.int32(-1)
        ),
        byIsolationMVArun2017v2DBoldDMwLTraw2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2LowPtElectronCleaned"),
            workingPointIndex = cms.int32(-1)
        ),
        byLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSe"),
            workingPointIndex = cms.int32(3)
        ),
        byLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(3)
        ),
        byLooseDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSmu"),
            workingPointIndex = cms.int32(1)
        ),
        byLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2LowPtElectronCleaned"),
            workingPointIndex = cms.int32(2)
        ),
        byMediumDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSe"),
            workingPointIndex = cms.int32(4)
        ),
        byMediumDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(4)
        ),
        byMediumDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSmu"),
            workingPointIndex = cms.int32(2)
        ),
        byMediumIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2LowPtElectronCleaned"),
            workingPointIndex = cms.int32(3)
        ),
        byTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSe"),
            workingPointIndex = cms.int32(5)
        ),
        byTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(5)
        ),
        byTightDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSmu"),
            workingPointIndex = cms.int32(3)
        ),
        byTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2LowPtElectronCleaned"),
            workingPointIndex = cms.int32(4)
        ),
        byVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSe"),
            workingPointIndex = cms.int32(2)
        ),
        byVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(2)
        ),
        byVLooseDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSmu"),
            workingPointIndex = cms.int32(0)
        ),
        byVLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2LowPtElectronCleaned"),
            workingPointIndex = cms.int32(1)
        ),
        byVTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSe"),
            workingPointIndex = cms.int32(6)
        ),
        byVTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(6)
        ),
        byVTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2LowPtElectronCleaned"),
            workingPointIndex = cms.int32(5)
        ),
        byVVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSe"),
            workingPointIndex = cms.int32(1)
        ),
        byVVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(1)
        ),
        byVVLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2LowPtElectronCleaned"),
            workingPointIndex = cms.int32(0)
        ),
        byVVTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSe"),
            workingPointIndex = cms.int32(7)
        ),
        byVVTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(7)
        ),
        byVVTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2LowPtElectronCleaned"),
            workingPointIndex = cms.int32(6)
        ),
        byVVVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSe"),
            workingPointIndex = cms.int32(0)
        ),
        byVVVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1LowPtElectronCleaned","VSjet"),
            workingPointIndex = cms.int32(0)
        )
    )
)


process.selectedPatTausNewIDsMuonCleaned = cms.EDProducer("PATTauIDEmbedder",
    src = cms.InputTag("slimmedTaus"),
    tauIDSources = cms.PSet(
        againstElectronLooseMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018MuonCleaned"),
            workingPointIndex = cms.int32(1)
        ),
        againstElectronMVA6Raw2018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018MuonCleaned"),
            workingPointIndex = cms.int32(-1)
        ),
        againstElectronMVA6category2018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018MuonCleaned"),
            workingPointIndex = cms.int32(-2)
        ),
        againstElectronMediumMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018MuonCleaned"),
            workingPointIndex = cms.int32(2)
        ),
        againstElectronTightMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018MuonCleaned"),
            workingPointIndex = cms.int32(3)
        ),
        againstElectronVLooseMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018MuonCleaned"),
            workingPointIndex = cms.int32(0)
        ),
        againstElectronVTightMVA62018 = cms.PSet(
            inputTag = cms.InputTag("patTauDiscriminationByElectronRejectionMVA62018MuonCleaned"),
            workingPointIndex = cms.int32(4)
        ),
        byDeepTau2017v2p1VSeraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSe"),
            workingPointIndex = cms.int32(-1)
        ),
        byDeepTau2017v2p1VSjetraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSjet"),
            workingPointIndex = cms.int32(-1)
        ),
        byDeepTau2017v2p1VSmuraw = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSmu"),
            workingPointIndex = cms.int32(-1)
        ),
        byIsolationMVArun2017v2DBoldDMwLTraw2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2MuonCleaned"),
            workingPointIndex = cms.int32(-1)
        ),
        byLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSe"),
            workingPointIndex = cms.int32(3)
        ),
        byLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSjet"),
            workingPointIndex = cms.int32(3)
        ),
        byLooseDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSmu"),
            workingPointIndex = cms.int32(1)
        ),
        byLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2MuonCleaned"),
            workingPointIndex = cms.int32(2)
        ),
        byMediumDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSe"),
            workingPointIndex = cms.int32(4)
        ),
        byMediumDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSjet"),
            workingPointIndex = cms.int32(4)
        ),
        byMediumDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSmu"),
            workingPointIndex = cms.int32(2)
        ),
        byMediumIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2MuonCleaned"),
            workingPointIndex = cms.int32(3)
        ),
        byTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSe"),
            workingPointIndex = cms.int32(5)
        ),
        byTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSjet"),
            workingPointIndex = cms.int32(5)
        ),
        byTightDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSmu"),
            workingPointIndex = cms.int32(3)
        ),
        byTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2MuonCleaned"),
            workingPointIndex = cms.int32(4)
        ),
        byVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSe"),
            workingPointIndex = cms.int32(2)
        ),
        byVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSjet"),
            workingPointIndex = cms.int32(2)
        ),
        byVLooseDeepTau2017v2p1VSmu = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSmu"),
            workingPointIndex = cms.int32(0)
        ),
        byVLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2MuonCleaned"),
            workingPointIndex = cms.int32(1)
        ),
        byVTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSe"),
            workingPointIndex = cms.int32(6)
        ),
        byVTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSjet"),
            workingPointIndex = cms.int32(6)
        ),
        byVTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2MuonCleaned"),
            workingPointIndex = cms.int32(5)
        ),
        byVVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSe"),
            workingPointIndex = cms.int32(1)
        ),
        byVVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSjet"),
            workingPointIndex = cms.int32(1)
        ),
        byVVLooseIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2MuonCleaned"),
            workingPointIndex = cms.int32(0)
        ),
        byVVTightDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSe"),
            workingPointIndex = cms.int32(7)
        ),
        byVVTightDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSjet"),
            workingPointIndex = cms.int32(7)
        ),
        byVVTightIsolationMVArun2017v2DBoldDMwLT2017 = cms.PSet(
            inputTag = cms.InputTag("rerunDiscriminationByIsolationOldDMMVArun2017v2MuonCleaned"),
            workingPointIndex = cms.int32(6)
        ),
        byVVVLooseDeepTau2017v2p1VSe = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSe"),
            workingPointIndex = cms.int32(0)
        ),
        byVVVLooseDeepTau2017v2p1VSjet = cms.PSet(
            inputTag = cms.InputTag("deepTau2017v2p1MuonCleaned","VSjet"),
            workingPointIndex = cms.int32(0)
        )
    )
)


process.slimmedTausBoosted = cms.EDProducer("PATTauSlimmer",
    dropPFSpecific = cms.bool(True),
    dropPiZeroRefs = cms.bool(True),
    dropTauChargedHadronRefs = cms.bool(True),
    linkToPackedPFCandidates = cms.bool(True),
    modifierConfig = cms.PSet(
        modifications = cms.VPSet()
    ),
    modifyTaus = cms.bool(True),
    packedPFCandidates = cms.InputTag("packedPFCandidates"),
    src = cms.InputTag("selectedPatTausBoosted")
)


process.slimmedTausElectronCleaned = cms.EDProducer("PATTauSlimmer",
    dropPFSpecific = cms.bool(True),
    dropPiZeroRefs = cms.bool(True),
    dropTauChargedHadronRefs = cms.bool(True),
    linkToPackedPFCandidates = cms.bool(True),
    modifierConfig = cms.PSet(
        modifications = cms.VPSet()
    ),
    modifyTaus = cms.bool(True),
    packedPFCandidates = cms.InputTag("PackedCandsElectronCleaned","packedPFCandidatesElectronCleaned"),
    src = cms.InputTag("selectedPatTausElectronCleaned")
)


process.slimmedTausLowPtElectronCleaned = cms.EDProducer("PATTauSlimmer",
    dropPFSpecific = cms.bool(True),
    dropPiZeroRefs = cms.bool(True),
    dropTauChargedHadronRefs = cms.bool(True),
    linkToPackedPFCandidates = cms.bool(True),
    modifierConfig = cms.PSet(
        modifications = cms.VPSet()
    ),
    modifyTaus = cms.bool(True),
    packedPFCandidates = cms.InputTag("PackedCandsLowPtElectronCleaned","packedPFCandidatesLowPtElectronCleaned"),
    src = cms.InputTag("selectedPatTausLowPtElectronCleaned")
)


process.slimmedTausMuonCleaned = cms.EDProducer("PATTauSlimmer",
    dropPFSpecific = cms.bool(True),
    dropPiZeroRefs = cms.bool(True),
    dropTauChargedHadronRefs = cms.bool(True),
    linkToPackedPFCandidates = cms.bool(True),
    modifierConfig = cms.PSet(
        modifications = cms.VPSet()
    ),
    modifyTaus = cms.bool(True),
    packedPFCandidates = cms.InputTag("PackedCandsMuonCleaned","packedPFCandidatesMuonCleaned"),
    src = cms.InputTag("selectedPatTausMuonCleaned")
)


process.slimmedTausUnCleaned = cms.EDProducer("PATTauSlimmer",
    dropPFSpecific = cms.bool(True),
    dropPiZeroRefs = cms.bool(True),
    dropTauChargedHadronRefs = cms.bool(True),
    linkToPackedPFCandidates = cms.bool(True),
    modifierConfig = cms.PSet(
        modifications = cms.VPSet()
    ),
    modifyTaus = cms.bool(True),
    packedPFCandidates = cms.InputTag("packedPFCandidates"),
    src = cms.InputTag("selectedPatTaus")
)


process.tauGenJetMatch = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("tauGenJetsSelectorAllHadrons"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.1),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer")
)


process.tauGenJetMatchBoosted = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("tauGenJetsSelectorAllHadronsBoosted"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.1),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducerBoosted")
)


process.tauGenJetMatchElectronCleaned = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("tauGenJetsSelectorAllHadronsElectronCleaned"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.1),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducerElectronCleaned")
)


process.tauGenJetMatchLowPtElectronCleaned = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("tauGenJetsSelectorAllHadronsLowPtElectronCleaned"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.1),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned")
)


process.tauGenJetMatchMuonCleaned = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("tauGenJetsSelectorAllHadronsMuonCleaned"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.1),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducerMuonCleaned")
)


process.tauGenJets = cms.EDProducer("TauGenJetProducer",
    GenParticles = cms.InputTag("prunedGenParticles"),
    includeNeutrinos = cms.bool(False),
    verbose = cms.untracked.bool(False)
)


process.tauGenJetsBoosted = cms.EDProducer("TauGenJetProducer",
    GenParticles = cms.InputTag("prunedGenParticles"),
    includeNeutrinos = cms.bool(False),
    verbose = cms.untracked.bool(False)
)


process.tauGenJetsElectronCleaned = cms.EDProducer("TauGenJetProducer",
    GenParticles = cms.InputTag("prunedGenParticles"),
    includeNeutrinos = cms.bool(False),
    verbose = cms.untracked.bool(False)
)


process.tauGenJetsLowPtElectronCleaned = cms.EDProducer("TauGenJetProducer",
    GenParticles = cms.InputTag("prunedGenParticles"),
    includeNeutrinos = cms.bool(False),
    verbose = cms.untracked.bool(False)
)


process.tauGenJetsMuonCleaned = cms.EDProducer("TauGenJetProducer",
    GenParticles = cms.InputTag("prunedGenParticles"),
    includeNeutrinos = cms.bool(False),
    verbose = cms.untracked.bool(False)
)


process.tauIsoDepositPFCandidates = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(10000.0),
        Diff_z = cms.double(10000.0),
        candidateSource = cms.InputTag("particleFlow"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducer")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFCandidatesBoosted = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(10000.0),
        Diff_z = cms.double(10000.0),
        candidateSource = cms.InputTag("packedPFCandidates"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducerBoosted")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducerBoosted"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFCandidatesElectronCleaned = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(10000.0),
        Diff_z = cms.double(10000.0),
        candidateSource = cms.InputTag("particleFlow"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducerElectronCleaned")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducerElectronCleaned"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFCandidatesLowPtElectronCleaned = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(10000.0),
        Diff_z = cms.double(10000.0),
        candidateSource = cms.InputTag("particleFlow"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFCandidatesMuonCleaned = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(10000.0),
        Diff_z = cms.double(10000.0),
        candidateSource = cms.InputTag("particleFlow"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducerMuonCleaned")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducerMuonCleaned"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFChargedHadrons = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(0.1),
        Diff_z = cms.double(0.2),
        candidateSource = cms.InputTag("pfAllChargedHadronsPFBRECO"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducer")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFChargedHadronsBoosted = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(0.1),
        Diff_z = cms.double(0.2),
        candidateSource = cms.InputTag("pfAllChargedHadronsPFBRECOBoosted"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducerBoosted")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducerBoosted"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFChargedHadronsElectronCleaned = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(0.1),
        Diff_z = cms.double(0.2),
        candidateSource = cms.InputTag("pfAllChargedHadronsPFBRECOElectronCleaned"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducerElectronCleaned")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducerElectronCleaned"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFChargedHadronsLowPtElectronCleaned = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(0.1),
        Diff_z = cms.double(0.2),
        candidateSource = cms.InputTag("pfAllChargedHadronsPFBRECOLowPtElectronCleaned"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFChargedHadronsMuonCleaned = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(0.1),
        Diff_z = cms.double(0.2),
        candidateSource = cms.InputTag("pfAllChargedHadronsPFBRECOMuonCleaned"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducerMuonCleaned")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducerMuonCleaned"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFGammas = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(10000.0),
        Diff_z = cms.double(10000.0),
        candidateSource = cms.InputTag("pfAllPhotonsPFBRECO"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducer")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFGammasBoosted = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(10000.0),
        Diff_z = cms.double(10000.0),
        candidateSource = cms.InputTag("pfAllPhotonsPFBRECOBoosted"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducerBoosted")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducerBoosted"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFGammasElectronCleaned = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(10000.0),
        Diff_z = cms.double(10000.0),
        candidateSource = cms.InputTag("pfAllPhotonsPFBRECOElectronCleaned"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducerElectronCleaned")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducerElectronCleaned"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFGammasLowPtElectronCleaned = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(10000.0),
        Diff_z = cms.double(10000.0),
        candidateSource = cms.InputTag("pfAllPhotonsPFBRECOLowPtElectronCleaned"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFGammasMuonCleaned = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(10000.0),
        Diff_z = cms.double(10000.0),
        candidateSource = cms.InputTag("pfAllPhotonsPFBRECOMuonCleaned"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducerMuonCleaned")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducerMuonCleaned"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFNeutralHadrons = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(10000.0),
        Diff_z = cms.double(10000.0),
        candidateSource = cms.InputTag("pfAllNeutralHadronsPFBRECO"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducer")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFNeutralHadronsBoosted = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(10000.0),
        Diff_z = cms.double(10000.0),
        candidateSource = cms.InputTag("pfAllNeutralHadronsPFBRECOBoosted"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducerBoosted")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducerBoosted"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFNeutralHadronsElectronCleaned = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(10000.0),
        Diff_z = cms.double(10000.0),
        candidateSource = cms.InputTag("pfAllNeutralHadronsPFBRECOElectronCleaned"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducerElectronCleaned")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducerElectronCleaned"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFNeutralHadronsLowPtElectronCleaned = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(10000.0),
        Diff_z = cms.double(10000.0),
        candidateSource = cms.InputTag("pfAllNeutralHadronsPFBRECOLowPtElectronCleaned"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned"),
    trackType = cms.string('candidate')
)


process.tauIsoDepositPFNeutralHadronsMuonCleaned = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFTauExtractor'),
        DR_Max = cms.double(1.0),
        DR_Veto = cms.double(0.0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(10000.0),
        Diff_z = cms.double(10000.0),
        candidateSource = cms.InputTag("pfAllNeutralHadronsPFBRECOMuonCleaned"),
        dRmatchPFTau = cms.double(0.1),
        dRvetoPFTauSignalConeConstituents = cms.double(0.01),
        tauSource = cms.InputTag("hpsPFTauProducerMuonCleaned")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducerMuonCleaned"),
    trackType = cms.string('candidate')
)


process.tauMatch = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("prunedGenParticles"),
    maxDPtRel = cms.double(999.9),
    maxDeltaR = cms.double(999.9),
    mcPdgId = cms.vint32(15),
    mcStatus = cms.vint32(2),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducer")
)


process.tauMatchBoosted = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("prunedGenParticles"),
    maxDPtRel = cms.double(999.9),
    maxDeltaR = cms.double(999.9),
    mcPdgId = cms.vint32(15),
    mcStatus = cms.vint32(2),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducerBoosted")
)


process.tauMatchElectronCleaned = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("prunedGenParticles"),
    maxDPtRel = cms.double(999.9),
    maxDeltaR = cms.double(999.9),
    mcPdgId = cms.vint32(15),
    mcStatus = cms.vint32(2),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducerElectronCleaned")
)


process.tauMatchLowPtElectronCleaned = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("prunedGenParticles"),
    maxDPtRel = cms.double(999.9),
    maxDeltaR = cms.double(999.9),
    mcPdgId = cms.vint32(15),
    mcStatus = cms.vint32(2),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducerLowPtElectronCleaned")
)


process.tauMatchMuonCleaned = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(True),
    matched = cms.InputTag("prunedGenParticles"),
    maxDPtRel = cms.double(999.9),
    maxDeltaR = cms.double(999.9),
    mcPdgId = cms.vint32(15),
    mcStatus = cms.vint32(2),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("hpsPFTauProducerMuonCleaned")
)


process.updatedJets = cms.EDProducer("PATJetUpdater",
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsReapplyJEC")),
    jetSource = cms.InputTag("slimmedJets"),
    mightGet = cms.optional.untracked.vstring,
    printWarning = cms.bool(True),
    sort = cms.bool(True),
    tagInfoSources = cms.VInputTag(),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("", "pileupJetIdUpdated:fullDiscriminant")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("", "pileupJetIdUpdated:fullId")
        )
    )
)


process.updatedPatJetCorrFactors = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L1FastJet',
        'L2Relative',
        'L3Absolute'
    ),
    mightGet = cms.optional.untracked.vstring,
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("slimmedJets"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.updatedPatJets = cms.EDProducer("PATJetUpdater",
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(),
    jetCorrFactorsSource = cms.VInputTag("updatedPatJetCorrFactors"),
    jetSource = cms.InputTag("slimmedJets"),
    mightGet = cms.optional.untracked.vstring,
    printWarning = cms.bool(True),
    sort = cms.bool(True),
    tagInfoSources = cms.VInputTag(),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.HLT = cms.EDFilter("HLTHighLevel",
    HLTPaths = cms.vstring(
        'HLT_PFJet450_v*',
        'HLT_PFJet500_v*',
        'HLT_PFHT1050_v*',
        'HLT_PFHT500_PFMET100_PFMHT100_IDTight_v*',
        'HLT_IsoMu27_v*',
        'HLT_Mu50_v',
        'HLT_Ele35_WPTight_Gsf_v',
        'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v',
        'HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1_v',
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v',
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v',
        'HLT_DoubleEle33_CaloIdL_MW_v',
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v',
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v',
        'HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v',
        'HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v',
        'HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg_v',
        'HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_MET90_v',
        'HLT_Ele115_CaloIdVT_GsfTrkIdT_v*',
        'HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v*',
        'HLT_Photon200_v*'
    ),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    andOr = cms.bool(True),
    eventSetupPathsKey = cms.string(''),
    throw = cms.bool(False)
)


process.LooseFilter = cms.EDFilter("ElectronFilter",
    BM = cms.InputTag("offlineBeamSpot"),
    Rho = cms.InputTag("fixedGridRhoFastjetAll"),
    conv = cms.InputTag("reducedConversions"),
    electrons = cms.InputTag("slimmedElectrons"),
    vertex = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.LooseMuonFilter = cms.EDFilter("PATMuonRefSelector",
    cut = cms.string('pt > 3.0 && isPFMuon && (isGlobalMuon || isTrackerMuon)'),
    src = cms.InputTag("slimmedMuons")
)


process.LowPtFilter = cms.EDFilter("LowPtElectronFilter",
    LowPtEIdScoreCut = cms.string('4'),
    electrons = cms.InputTag("slimmedLowPtElectrons")
)


process.pfAllChargedHadronsPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(
        211, -211, 321, -321, 999211,
        2212, -2212
    ),
    src = cms.InputTag("pfNoPileUpIsoPFBRECO")
)


process.pfAllChargedHadronsPFBRECOBoosted = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(
        211, -211, 321, -321, 999211,
        2212, -2212
    ),
    src = cms.InputTag("pfNoPileUpIsoPFBRECOBoosted")
)


process.pfAllChargedHadronsPFBRECOElectronCleaned = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(
        211, -211, 321, -321, 999211,
        2212, -2212
    ),
    src = cms.InputTag("pfNoPileUpIsoPFBRECOElectronCleaned")
)


process.pfAllChargedHadronsPFBRECOLowPtElectronCleaned = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(
        211, -211, 321, -321, 999211,
        2212, -2212
    ),
    src = cms.InputTag("pfNoPileUpIsoPFBRECOLowPtElectronCleaned")
)


process.pfAllChargedHadronsPFBRECOMuonCleaned = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(
        211, -211, 321, -321, 999211,
        2212, -2212
    ),
    src = cms.InputTag("pfNoPileUpIsoPFBRECOMuonCleaned")
)


process.pfAllChargedParticlesPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(
        211, -211, 321, -321, 999211,
        2212, -2212, 11, -11, 13,
        -13
    ),
    src = cms.InputTag("pfNoPileUpIsoPFBRECO")
)


process.pfAllChargedParticlesPFBRECOBoosted = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(
        211, -211, 321, -321, 999211,
        2212, -2212, 11, -11, 13,
        -13
    ),
    src = cms.InputTag("pfNoPileUpIsoPFBRECOBoosted")
)


process.pfAllChargedParticlesPFBRECOElectronCleaned = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(
        211, -211, 321, -321, 999211,
        2212, -2212, 11, -11, 13,
        -13
    ),
    src = cms.InputTag("pfNoPileUpIsoPFBRECOElectronCleaned")
)


process.pfAllChargedParticlesPFBRECOLowPtElectronCleaned = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(
        211, -211, 321, -321, 999211,
        2212, -2212, 11, -11, 13,
        -13
    ),
    src = cms.InputTag("pfNoPileUpIsoPFBRECOLowPtElectronCleaned")
)


process.pfAllChargedParticlesPFBRECOMuonCleaned = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(
        211, -211, 321, -321, 999211,
        2212, -2212, 11, -11, 13,
        -13
    ),
    src = cms.InputTag("pfNoPileUpIsoPFBRECOMuonCleaned")
)


process.pfAllNeutralHadronsAndPhotonsPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(22, 111, 130, 310, 2112),
    src = cms.InputTag("pfNoPileUpIsoPFBRECO")
)


process.pfAllNeutralHadronsAndPhotonsPFBRECOBoosted = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(22, 111, 130, 310, 2112),
    src = cms.InputTag("pfNoPileUpIsoPFBRECOBoosted")
)


process.pfAllNeutralHadronsAndPhotonsPFBRECOElectronCleaned = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(22, 111, 130, 310, 2112),
    src = cms.InputTag("pfNoPileUpIsoPFBRECOElectronCleaned")
)


process.pfAllNeutralHadronsAndPhotonsPFBRECOLowPtElectronCleaned = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(22, 111, 130, 310, 2112),
    src = cms.InputTag("pfNoPileUpIsoPFBRECOLowPtElectronCleaned")
)


process.pfAllNeutralHadronsAndPhotonsPFBRECOMuonCleaned = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(22, 111, 130, 310, 2112),
    src = cms.InputTag("pfNoPileUpIsoPFBRECOMuonCleaned")
)


process.pfAllNeutralHadronsPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(111, 130, 310, 2112),
    src = cms.InputTag("pfNoPileUpIsoPFBRECO")
)


process.pfAllNeutralHadronsPFBRECOBoosted = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(111, 130, 310, 2112),
    src = cms.InputTag("pfNoPileUpIsoPFBRECOBoosted")
)


process.pfAllNeutralHadronsPFBRECOElectronCleaned = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(111, 130, 310, 2112),
    src = cms.InputTag("pfNoPileUpIsoPFBRECOElectronCleaned")
)


process.pfAllNeutralHadronsPFBRECOLowPtElectronCleaned = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(111, 130, 310, 2112),
    src = cms.InputTag("pfNoPileUpIsoPFBRECOLowPtElectronCleaned")
)


process.pfAllNeutralHadronsPFBRECOMuonCleaned = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(111, 130, 310, 2112),
    src = cms.InputTag("pfNoPileUpIsoPFBRECOMuonCleaned")
)


process.pfAllPhotonsPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(22),
    src = cms.InputTag("pfNoPileUpIsoPFBRECO")
)


process.pfAllPhotonsPFBRECOBoosted = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(22),
    src = cms.InputTag("pfNoPileUpIsoPFBRECOBoosted")
)


process.pfAllPhotonsPFBRECOElectronCleaned = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(22),
    src = cms.InputTag("pfNoPileUpIsoPFBRECOElectronCleaned")
)


process.pfAllPhotonsPFBRECOLowPtElectronCleaned = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(22),
    src = cms.InputTag("pfNoPileUpIsoPFBRECOLowPtElectronCleaned")
)


process.pfAllPhotonsPFBRECOMuonCleaned = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(22),
    src = cms.InputTag("pfNoPileUpIsoPFBRECOMuonCleaned")
)


process.pfPileUpAllChargedParticlesPFBRECO = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(
        211, -211, 321, -321, 999211,
        2212, -2212, 11, -11, 13,
        -13
    ),
    src = cms.InputTag("pfPileUpIsoPFBRECO")
)


process.pfPileUpAllChargedParticlesPFBRECOBoosted = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(
        211, -211, 321, -321, 999211,
        2212, -2212, 11, -11, 13,
        -13
    ),
    src = cms.InputTag("pfPileUpIsoPFBRECOBoosted")
)


process.pfPileUpAllChargedParticlesPFBRECOElectronCleaned = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(
        211, -211, 321, -321, 999211,
        2212, -2212, 11, -11, 13,
        -13
    ),
    src = cms.InputTag("pfPileUpIsoPFBRECOElectronCleaned")
)


process.pfPileUpAllChargedParticlesPFBRECOLowPtElectronCleaned = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(
        211, -211, 321, -321, 999211,
        2212, -2212, 11, -11, 13,
        -13
    ),
    src = cms.InputTag("pfPileUpIsoPFBRECOLowPtElectronCleaned")
)


process.pfPileUpAllChargedParticlesPFBRECOMuonCleaned = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(
        211, -211, 321, -321, 999211,
        2212, -2212, 11, -11, 13,
        -13
    ),
    src = cms.InputTag("pfPileUpIsoPFBRECOMuonCleaned")
)


process.recoTauPileUpVertices = cms.EDFilter("RecoTauPileUpVertexSelector",
    filter = cms.bool(False),
    minTrackSumPt = cms.double(5),
    src = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.recoTauPileUpVerticesBoosted = cms.EDFilter("RecoTauPileUpVertexSelector",
    filter = cms.bool(False),
    minTrackSumPt = cms.double(5),
    src = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.recoTauPileUpVerticesElectronCleaned = cms.EDFilter("RecoTauPileUpVertexSelector",
    filter = cms.bool(False),
    minTrackSumPt = cms.double(5),
    src = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.recoTauPileUpVerticesLowPtElectronCleaned = cms.EDFilter("RecoTauPileUpVertexSelector",
    filter = cms.bool(False),
    minTrackSumPt = cms.double(5),
    src = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.recoTauPileUpVerticesMuonCleaned = cms.EDFilter("RecoTauPileUpVertexSelector",
    filter = cms.bool(False),
    minTrackSumPt = cms.double(5),
    src = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.selectedPatTausNoNewIDs = cms.EDFilter("PATTauSelector",
    cut = cms.string("pt > 8.0 && abs(eta)<2.3 && tauID(\'decayModeFinding\')> 0.5"),
    src = cms.InputTag("patTaus")
)


process.selectedPatTausNoNewIDsBoosted = cms.EDFilter("PATTauSelector",
    cut = cms.string("pt > 8.0 && abs(eta)<2.3 && tauID(\'decayModeFinding\')> 0.5"),
    src = cms.InputTag("patTausBoosted")
)


process.selectedPatTausNoNewIDsElectronCleaned = cms.EDFilter("PATTauSelector",
    cut = cms.string("pt > 8.0 && abs(eta)<2.3 && tauID(\'decayModeFinding\')> 0.5"),
    src = cms.InputTag("patTausElectronCleaned")
)


process.selectedPatTausNoNewIDsLowPtElectronCleaned = cms.EDFilter("PATTauSelector",
    cut = cms.string("pt > 8.0 && abs(eta)<2.3 && tauID(\'decayModeFinding\')> 0.5"),
    src = cms.InputTag("patTausLowPtElectronCleaned")
)


process.selectedPatTausNoNewIDsMuonCleaned = cms.EDFilter("PATTauSelector",
    cut = cms.string("pt > 8.0 && abs(eta)<2.3 && tauID(\'decayModeFinding\')> 0.5"),
    src = cms.InputTag("patTausMuonCleaned")
)


process.tauGenJetsSelectorAllHadrons = cms.EDFilter("TauGenJetDecayModeSelector",
    filter = cms.bool(False),
    select = cms.vstring(
        'oneProng0Pi0',
        'oneProng1Pi0',
        'oneProng2Pi0',
        'oneProngOther',
        'threeProng0Pi0',
        'threeProng1Pi0',
        'threeProngOther',
        'rare'
    ),
    src = cms.InputTag("tauGenJets")
)


process.tauGenJetsSelectorAllHadronsBoosted = cms.EDFilter("TauGenJetDecayModeSelector",
    filter = cms.bool(False),
    select = cms.vstring(
        'oneProng0Pi0',
        'oneProng1Pi0',
        'oneProng2Pi0',
        'oneProngOther',
        'threeProng0Pi0',
        'threeProng1Pi0',
        'threeProngOther',
        'rare'
    ),
    src = cms.InputTag("tauGenJetsBoosted")
)


process.tauGenJetsSelectorAllHadronsElectronCleaned = cms.EDFilter("TauGenJetDecayModeSelector",
    filter = cms.bool(False),
    select = cms.vstring(
        'oneProng0Pi0',
        'oneProng1Pi0',
        'oneProng2Pi0',
        'oneProngOther',
        'threeProng0Pi0',
        'threeProng1Pi0',
        'threeProngOther',
        'rare'
    ),
    src = cms.InputTag("tauGenJetsElectronCleaned")
)


process.tauGenJetsSelectorAllHadronsLowPtElectronCleaned = cms.EDFilter("TauGenJetDecayModeSelector",
    filter = cms.bool(False),
    select = cms.vstring(
        'oneProng0Pi0',
        'oneProng1Pi0',
        'oneProng2Pi0',
        'oneProngOther',
        'threeProng0Pi0',
        'threeProng1Pi0',
        'threeProngOther',
        'rare'
    ),
    src = cms.InputTag("tauGenJetsLowPtElectronCleaned")
)


process.tauGenJetsSelectorAllHadronsMuonCleaned = cms.EDFilter("TauGenJetDecayModeSelector",
    filter = cms.bool(False),
    select = cms.vstring(
        'oneProng0Pi0',
        'oneProng1Pi0',
        'oneProng2Pi0',
        'oneProngOther',
        'threeProng0Pi0',
        'threeProng1Pi0',
        'threeProngOther',
        'rare'
    ),
    src = cms.InputTag("tauGenJetsMuonCleaned")
)


process.TCPNtuples = cms.EDAnalyzer("TCPNtuples",
    BoostedTauCollection = cms.InputTag("slimmedTausBoosted"),
    ECleanedTauCollection = cms.InputTag("slimmedTausElectronCleaned"),
    ElectronCollection = cms.InputTag("slimmedElectrons"),
    JetCollection = cms.InputTag("updatedJets"),
    LowPtECleanedTauCollection = cms.InputTag("slimmedTausLowPtElectronCleaned"),
    LowPtEIdScoreCut = cms.string('4'),
    LowPtElectronCollection = cms.InputTag("slimmedLowPtElectrons"),
    MCleanedTauCollection = cms.InputTag("slimmedTausMuonCleaned"),
    METCollection = cms.InputTag("slimmedMETs"),
    MuonCollection = cms.InputTag("slimmedMuons"),
    PhotonCollection = cms.InputTag("slimmedPhotons"),
    UnCleanedTauCollection = cms.InputTag("slimmedTausUnCleaned"),
    VertexCollection = cms.InputTag("offlineSlimmedPrimaryVertices"),
    effAreasConfigFile = cms.FileInPath('BoostedDiTau/MiniAODSkimmer/data/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt'),
    rhoTag = cms.InputTag("fixedGridRhoFastjetAll")
)


process.lumiSummary = cms.EDAnalyzer("LumiAnalyzer",
    genEventInfo = cms.InputTag("generator")
)


process.tcpGenNtuples = cms.EDAnalyzer("GenAnalyzer",
    GenJetCollection = cms.InputTag("slimmedGenJets"),
    GenParticleCollection = cms.InputTag("prunedGenParticles"),
    genEventInfo = cms.InputTag("generator"),
    pileupSummaryInfo = cms.InputTag("slimmedAddPileupInfo"),
    puDataFileName = cms.FileInPath('BoostedDiTau/MiniAODSkimmer/data/PileupHistogram-goldenJSON-13tev-2017-69200ub-99bins.root'),
    puDataFileNameDown = cms.FileInPath('BoostedDiTau/MiniAODSkimmer/data/PileupHistogram-goldenJSON-13tev-2017-66000ub-99bins.root'),
    puDataFileNameUp = cms.FileInPath('BoostedDiTau/MiniAODSkimmer/data/PileupHistogram-goldenJSON-13tev-2017-72400ub-99bins.root'),
    puMCFileName = cms.FileInPath('BoostedDiTau/MiniAODSkimmer/data/PileupMC2017.root')
)


process.tcpMetfilter = cms.EDAnalyzer("TCPMETFilter",
    badChargedCandFilterSel = cms.string('Flag_BadChargedCandidateFilter'),
    badPFMuonFilterSel = cms.string('Flag_BadPFMuonFilter'),
    beamHaloFilterSel = cms.string('Flag_globalSuperTightHalo2016Filter'),
    ecalBadCalFilterSel = cms.string('Flag_ecalBadCalibFilter'),
    ecalTPFilterSel = cms.string('Flag_EcalDeadCellTriggerPrimitiveFilter'),
    eeBadScFilterSel = cms.string('Flag_eeBadScFilter'),
    hbheFilterSel = cms.string('Flag_HBHENoiseFilter'),
    hbheIsoFilterSel = cms.string('Flag_HBHENoiseIsoFilter'),
    metFilters = cms.InputTag("TriggerResults","","PAT"),
    primaryVertexFilterSel = cms.string('Flag_goodVertices')
)


process.tcpPrefiring = cms.EDAnalyzer("TCPPrefiring",
    PrefiringWeight = cms.InputTag("prefiringweight","nonPrefiringProb"),
    PrefiringWeightDown = cms.InputTag("prefiringweight","nonPrefiringProbDown"),
    PrefiringWeightUp = cms.InputTag("prefiringweight","nonPrefiringProbUp")
)


process.tcpTrigNtuples = cms.EDAnalyzer("TCPTrigNtuples",
    TriggerResults = cms.InputTag("TriggerResults","","HLT")
)


process.testTrigObj = cms.EDAnalyzer("TCPTrigObjectAnalyzer",
    bits = cms.InputTag("TriggerResults","","HLT"),
    objects = cms.InputTag("slimmedPatTrigger"),
    prescales = cms.InputTag("patTrigger")
)


process.output = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('MINIAODSIM'),
        filterName = cms.untracked.string('')
    ),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('miniAOD_TauReco_ak4PFJets_Background_2016.root'),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_slimmedPhotons_*_*',
        'keep *_slimmedOOTPhotons_*_*',
        'keep *_slimmedElectrons_*_*',
        'keep *_slimmedMuons_*_*',
        'keep recoTrackExtras_slimmedMuonTrackExtras_*_*',
        'keep TrackingRecHitsOwned_slimmedMuonTrackExtras_*_*',
        'keep SiPixelClusteredmNewDetSetVector_slimmedMuonTrackExtras_*_*',
        'keep SiStripClusteredmNewDetSetVector_slimmedMuonTrackExtras_*_*',
        'keep *_slimmedTaus_*_*',
        'keep *_slimmedTausBoosted_*_*',
        'keep *_slimmedCaloJets_*_*',
        'keep *_slimmedJets_*_*',
        'keep recoBaseTagInfosOwned_slimmedJets_*_*',
        'keep *_slimmedJetsAK8_*_*',
        'drop recoBaseTagInfosOwned_slimmedJetsAK8_*_*',
        'keep *_slimmedJetsPuppi_*_*',
        'keep *_slimmedMETs_*_*',
        'keep *_slimmedMETsNoHF_*_*',
        'keep *_slimmedMETsPuppi_*_*',
        'keep *_slimmedSecondaryVertices_*_*',
        'keep *_slimmedLambdaVertices_*_*',
        'keep *_slimmedKshortVertices_*_*',
        'keep *_slimmedJetsAK8PFPuppiSoftDropPacked_SubJets_*',
        'keep recoPhotonCores_reducedEgamma_*_*',
        'keep recoGsfElectronCores_reducedEgamma_*_*',
        'keep recoConversions_reducedEgamma_*_*',
        'keep recoSuperClusters_reducedEgamma_*_*',
        'keep recoCaloClusters_reducedEgamma_*_*',
        'keep EcalRecHitsSorted_reducedEgamma_*_*',
        'keep recoGsfTracks_reducedEgamma_*_*',
        'keep HBHERecHitsSorted_reducedEgamma_*_*',
        'keep *_slimmedHcalRecHits_*_*',
        'drop *_*_caloTowers_*',
        'drop *_*_pfCandidates_*',
        'drop *_*_genJets_*',
        'keep *_offlineBeamSpot_*_*',
        'keep *_offlineSlimmedPrimaryVertices_*_*',
        'keep *_offlineSlimmedPrimaryVerticesWithBS_*_*',
        'keep patPackedCandidates_packedPFCandidates_*_*',
        'keep *_isolatedTracks_*_*',
        'keep *_oniaPhotonCandidates_*_*',
        'keep *_bunchSpacingProducer_*_*',
        'keep double_fixedGridRhoAll__*',
        'keep double_fixedGridRhoFastjetAll__*',
        'keep double_fixedGridRhoFastjetAllTmp__*',
        'keep double_fixedGridRhoFastjetAllCalo__*',
        'keep double_fixedGridRhoFastjetCentral_*_*',
        'keep double_fixedGridRhoFastjetCentralCalo__*',
        'keep double_fixedGridRhoFastjetCentralChargedPileUp__*',
        'keep double_fixedGridRhoFastjetCentralNeutral__*',
        'keep *_slimmedPatTrigger_*_*',
        'keep patPackedTriggerPrescales_patTrigger__*',
        'keep patPackedTriggerPrescales_patTrigger_l1max_*',
        'keep patPackedTriggerPrescales_patTrigger_l1min_*',
        'keep *_l1extraParticles_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep GlobalExtBlkBXVector_simGtExtUnprefireable_*_*',
        'keep *_gtStage2Digis__*',
        'keep *_gmtStage2Digis_Muon_*',
        'keep *_caloStage2Digis_Jet_*',
        'keep *_caloStage2Digis_Tau_*',
        'keep *_caloStage2Digis_EGamma_*',
        'keep *_caloStage2Digis_EtSum_*',
        'keep *_TriggerResults_*_HLT',
        'keep *_TriggerResults_*_*',
        'keep patPackedCandidates_lostTracks_*_*',
        'keep HcalNoiseSummary_hcalnoise__*',
        'keep recoCSCHaloData_CSCHaloData_*_*',
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*',
        'keep LumiScalerss_scalersRawToDigi_*_*',
        'keep CTPPSLocalTrackLites_ctppsLocalTrackLiteProducer_*_*',
        'keep recoForwardProtons_ctppsProtons_*_*',
        'keep recoTracks_displacedStandAloneMuons__*',
        'keep recoTracks_displacedGlobalMuons__*',
        'keep recoTracks_displacedTracks__*',
        'keep *_prefiringweight_*_*',
        'keep *_slimmedLowPtElectrons_*_*',
        'keep *_gsfTracksOpenConversions_*_*',
        'keep patPackedGenParticles_packedGenParticles_*_*',
        'keep recoGenParticles_prunedGenParticles_*_*',
        'keep *_packedPFCandidateToGenAssociation_*_*',
        'keep *_lostTracksToGenAssociation_*_*',
        'keep LHEEventProduct_*_*_*',
        'keep GenFilterInfo_*_*_*',
        'keep GenLumiInfoHeader_generator_*_*',
        'keep GenLumiInfoProduct_*_*_*',
        'keep GenEventInfoProduct_generator_*_*',
        'keep recoGenParticles_genPUProtons_*_*',
        'keep *_slimmedGenJetsFlavourInfos_*_*',
        'keep *_slimmedGenJets__*',
        'keep *_slimmedGenJetsAK8__*',
        'keep *_slimmedGenJetsAK8SoftDropSubJets__*',
        'keep *_genMetTrue_*_*',
        'keep LHERunInfoProduct_*_*_*',
        'keep GenRunInfoProduct_*_*_*',
        'keep *_genParticles_xyz0_*',
        'keep *_genParticles_t0_*',
        'keep PileupSummaryInfos_slimmedAddPileupInfo_*_*',
        'keep L1GtTriggerMenuLite_l1GtTriggerMenuLite__*',
        'keep *_slimmedTausUnCleaned_*_*',
        'keep *_slimmedTausElectronCleaned_*_*',
        'keep *_slimmedTausLowPtElectronCleaned_*_*',
        'keep *_slimmedTausMuonCleaned_*_*',
        'keep *_lumiSummary_*_*',
        'keep *_slimmedPhotons_*_*'
    )
)


process.MessageLogger = cms.Service("MessageLogger",
    cerr = cms.untracked.PSet(
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            reportEvery = cms.untracked.int32(1000)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        enable = cms.untracked.bool(True),
        enableStatistics = cms.untracked.bool(True),
        lineLength = cms.optional.untracked.int32,
        noLineBreaks = cms.optional.untracked.bool,
        noTimeStamps = cms.untracked.bool(False),
        resetStatistics = cms.untracked.bool(False),
        statisticsThreshold = cms.untracked.string('WARNING'),
        threshold = cms.untracked.string('INFO'),
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            limit = cms.optional.untracked.int32,
            reportEvery = cms.untracked.int32(1),
            timespan = cms.optional.untracked.int32
        )
    ),
    cout = cms.untracked.PSet(
        enable = cms.untracked.bool(False),
        enableStatistics = cms.untracked.bool(False),
        lineLength = cms.optional.untracked.int32,
        noLineBreaks = cms.optional.untracked.bool,
        noTimeStamps = cms.optional.untracked.bool,
        resetStatistics = cms.untracked.bool(False),
        statisticsThreshold = cms.optional.untracked.string,
        threshold = cms.optional.untracked.string,
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            limit = cms.optional.untracked.int32,
            reportEvery = cms.untracked.int32(1),
            timespan = cms.optional.untracked.int32
        )
    ),
    debugModules = cms.untracked.vstring(),
    default = cms.untracked.PSet(
        limit = cms.optional.untracked.int32,
        lineLength = cms.untracked.int32(80),
        noLineBreaks = cms.untracked.bool(False),
        noTimeStamps = cms.untracked.bool(False),
        reportEvery = cms.untracked.int32(1),
        statisticsThreshold = cms.untracked.string('INFO'),
        threshold = cms.untracked.string('INFO'),
        timespan = cms.optional.untracked.int32,
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            limit = cms.optional.untracked.int32,
            reportEvery = cms.untracked.int32(1),
            timespan = cms.optional.untracked.int32
        )
    ),
    files = cms.untracked.PSet(
        allowAnyLabel_=cms.optional.untracked.PSetTemplate(
            enableStatistics = cms.untracked.bool(False),
            extension = cms.optional.untracked.string,
            filename = cms.optional.untracked.string,
            lineLength = cms.optional.untracked.int32,
            noLineBreaks = cms.optional.untracked.bool,
            noTimeStamps = cms.optional.untracked.bool,
            output = cms.optional.untracked.string,
            resetStatistics = cms.untracked.bool(False),
            statisticsThreshold = cms.optional.untracked.string,
            threshold = cms.optional.untracked.string,
            allowAnyLabel_=cms.optional.untracked.PSetTemplate(
                limit = cms.optional.untracked.int32,
                reportEvery = cms.untracked.int32(1),
                timespan = cms.optional.untracked.int32
            )
        )
    ),
    suppressDebug = cms.untracked.vstring(),
    suppressFwkInfo = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    allowAnyLabel_=cms.optional.untracked.PSetTemplate(
        limit = cms.optional.untracked.int32,
        reportEvery = cms.untracked.int32(1),
        timespan = cms.optional.untracked.int32
    )
)


process.TFileService = cms.Service("TFileService",
    closeFileFast = cms.untracked.bool(True),
    fileName = cms.string('TCPNtuple.root')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useGangedStripsInME1a = cms.bool(False),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring(
        'HCAL',
        'ZDC',
        'CASTOR',
        'EcalBarrel',
        'EcalEndcap',
        'EcalPreshower',
        'TOWER'
    )
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP")


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string('')
)


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    DDDetector = cms.ESInputTag("",""),
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    attribute = cms.string('MuStructure'),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    value = cms.string('MuonBarrelDT')
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService",
    maxExtrapolationTimeInSec = cms.uint32(0)
)


process.EcalLaserCorrectionServiceMC = cms.ESProducer("EcalLaserCorrectionServiceMC",
    appendToDataLabel = cms.string('')
)


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GEMGeometryESModule = cms.ESProducer("GEMGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(False),
    fromDD4Hep = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(-1),
    version = cms.string('Parabolic')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    fromDD4hep = cms.untracked.bool(False),
    fromDDD = cms.untracked.bool(False)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TrackerAdditionalParametersPerDet = cms.ESProducer("TrackerAdditionalParametersPerDetESModule",
    appendToDataLabel = cms.string('')
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer",
    usePhase2Stacks = cms.bool(False)
)


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(-1)
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.ak10PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak10PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFCHSL1Fastjet',
        'ak10PFCHSL2Relative',
        'ak10PFCHSL3Absolute',
        'ak10PFCHSResidual'
    )
)


process.ak10PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFCHSL1Offset',
        'ak10PFCHSL2Relative',
        'ak10PFCHSL3Absolute',
        'ak10PFCHSResidual'
    )
)


process.ak10PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak10PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFCHSL2Relative',
        'ak10PFCHSL3Absolute'
    )
)


process.ak10PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFCHSL2Relative',
        'ak10PFCHSL3Absolute',
        'ak10PFCHSResidual'
    )
)


process.ak10PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L2Relative')
)


process.ak10PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L3Absolute')
)


process.ak10PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak10PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak10PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFL1Fastjet',
        'ak10PFL2Relative',
        'ak10PFL3Absolute',
        'ak10PFResidual'
    )
)


process.ak10PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFL1Offset',
        'ak10PFL2Relative',
        'ak10PFL3Absolute',
        'ak10PFResidual'
    )
)


process.ak10PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak10PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFL2Relative',
        'ak10PFL3Absolute'
    )
)


process.ak10PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak10PFL2Relative',
        'ak10PFL3Absolute',
        'ak10PFResidual'
    )
)


process.ak10PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L2Relative')
)


process.ak10PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L3Absolute')
)


process.ak10PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK10PF'),
    level = cms.string('L2L3Residual')
)


process.ak1PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak1PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFCHSL1Fastjet',
        'ak1PFCHSL2Relative',
        'ak1PFCHSL3Absolute',
        'ak1PFCHSResidual'
    )
)


process.ak1PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFCHSL1Offset',
        'ak1PFCHSL2Relative',
        'ak1PFCHSL3Absolute',
        'ak1PFCHSResidual'
    )
)


process.ak1PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak1PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFCHSL2Relative',
        'ak1PFCHSL3Absolute'
    )
)


process.ak1PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFCHSL2Relative',
        'ak1PFCHSL3Absolute',
        'ak1PFCHSResidual'
    )
)


process.ak1PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L2Relative')
)


process.ak1PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L3Absolute')
)


process.ak1PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak1PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak1PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFL1Fastjet',
        'ak1PFL2Relative',
        'ak1PFL3Absolute',
        'ak1PFResidual'
    )
)


process.ak1PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFL1Offset',
        'ak1PFL2Relative',
        'ak1PFL3Absolute',
        'ak1PFResidual'
    )
)


process.ak1PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak1PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFL2Relative',
        'ak1PFL3Absolute'
    )
)


process.ak1PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak1PFL2Relative',
        'ak1PFL3Absolute',
        'ak1PFResidual'
    )
)


process.ak1PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L2Relative')
)


process.ak1PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L3Absolute')
)


process.ak1PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK1PF'),
    level = cms.string('L2L3Residual')
)


process.ak2PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak2PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFCHSL1Fastjet',
        'ak2PFCHSL2Relative',
        'ak2PFCHSL3Absolute',
        'ak2PFCHSResidual'
    )
)


process.ak2PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFCHSL1Offset',
        'ak2PFCHSL2Relative',
        'ak2PFCHSL3Absolute',
        'ak2PFCHSResidual'
    )
)


process.ak2PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak2PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFCHSL2Relative',
        'ak2PFCHSL3Absolute'
    )
)


process.ak2PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFCHSL2Relative',
        'ak2PFCHSL3Absolute',
        'ak2PFCHSResidual'
    )
)


process.ak2PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L2Relative')
)


process.ak2PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L3Absolute')
)


process.ak2PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak2PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak2PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFL1Fastjet',
        'ak2PFL2Relative',
        'ak2PFL3Absolute',
        'ak2PFResidual'
    )
)


process.ak2PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFL1Offset',
        'ak2PFL2Relative',
        'ak2PFL3Absolute',
        'ak2PFResidual'
    )
)


process.ak2PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak2PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFL2Relative',
        'ak2PFL3Absolute'
    )
)


process.ak2PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak2PFL2Relative',
        'ak2PFL3Absolute',
        'ak2PFResidual'
    )
)


process.ak2PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L2Relative')
)


process.ak2PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L3Absolute')
)


process.ak2PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK2PF'),
    level = cms.string('L2L3Residual')
)


process.ak3PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak3PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFCHSL1Fastjet',
        'ak3PFCHSL2Relative',
        'ak3PFCHSL3Absolute',
        'ak3PFCHSResidual'
    )
)


process.ak3PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFCHSL1Offset',
        'ak3PFCHSL2Relative',
        'ak3PFCHSL3Absolute',
        'ak3PFCHSResidual'
    )
)


process.ak3PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak3PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFCHSL2Relative',
        'ak3PFCHSL3Absolute'
    )
)


process.ak3PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFCHSL2Relative',
        'ak3PFCHSL3Absolute',
        'ak3PFCHSResidual'
    )
)


process.ak3PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L2Relative')
)


process.ak3PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L3Absolute')
)


process.ak3PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak3PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak3PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFL1Fastjet',
        'ak3PFL2Relative',
        'ak3PFL3Absolute',
        'ak3PFResidual'
    )
)


process.ak3PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFL1Offset',
        'ak3PFL2Relative',
        'ak3PFL3Absolute',
        'ak3PFResidual'
    )
)


process.ak3PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak3PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFL2Relative',
        'ak3PFL3Absolute'
    )
)


process.ak3PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak3PFL2Relative',
        'ak3PFL3Absolute',
        'ak3PFResidual'
    )
)


process.ak3PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L2Relative')
)


process.ak3PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L3Absolute')
)


process.ak3PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK3PF'),
    level = cms.string('L2L3Residual')
)


process.ak4CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet',
        'ak4CaloL2Relative',
        'ak4CaloL3Absolute'
    )
)


process.ak4CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet',
        'ak4CaloL2Relative',
        'ak4CaloL3Absolute',
        'ak4CaloL6SLB'
    )
)


process.ak4CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet',
        'ak4CaloL2Relative',
        'ak4CaloL3Absolute',
        'ak4CaloResidual'
    )
)


process.ak4CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ak4CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Offset',
        'ak4CaloL2Relative',
        'ak4CaloL3Absolute'
    )
)


process.ak4CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Offset',
        'ak4CaloL2Relative',
        'ak4CaloL3Absolute',
        'ak4CaloResidual'
    )
)


process.ak4CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak4CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL2Relative',
        'ak4CaloL3Absolute'
    )
)


process.ak4CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL2Relative',
        'ak4CaloL3Absolute',
        'ak4CaloL6SLB'
    )
)


process.ak4CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL2Relative',
        'ak4CaloL3Absolute',
        'ak4CaloResidual'
    )
)


process.ak4CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2Relative')
)


process.ak4CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L3Absolute')
)


process.ak4CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak4CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak4CaloJetsSoftMuonTagInfos")
)


process.ak4CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.ak4JPTL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4L1JPTFastjet',
        'ak4JPTL2Relative',
        'ak4JPTL3Absolute'
    )
)


process.ak4JPTL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4L1JPTFastjet',
        'ak4JPTL2Relative',
        'ak4JPTL3Absolute',
        'ak4JPTResidual'
    )
)


process.ak4JPTL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4L1JPTOffset',
        'ak4JPTL2Relative',
        'ak4JPTL3Absolute'
    )
)


process.ak4JPTL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4L1JPTOffset',
        'ak4JPTL2Relative',
        'ak4JPTL3Absolute',
        'ak4JPTResidual'
    )
)


process.ak4JPTL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak4JPTL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4L1JPTOffset',
        'ak4JPTL2Relative',
        'ak4JPTL3Absolute'
    )
)


process.ak4JPTL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4L1JPTOffset',
        'ak4JPTL2Relative',
        'ak4JPTL3Absolute',
        'ak4JPTResidual'
    )
)


process.ak4JPTL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L2Relative')
)


process.ak4JPTL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L3Absolute')
)


process.ak4JPTResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L2L3Residual')
)


process.ak4L1JPTFastjet = cms.ESProducer("L1JPTOffsetCorrectionESProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.string('ak4CaloL1Fastjet')
)


process.ak4L1JPTOffset = cms.ESProducer("L1JPTOffsetCorrectionESProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.string('ak4CaloL1Offset')
)


process.ak4PFCHSL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFCHSL1Fastjet',
        'ak4PFCHSL2Relative',
        'ak4PFCHSL3Absolute'
    )
)


process.ak4PFCHSL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFCHSL1Fastjet',
        'ak4PFCHSL2Relative',
        'ak4PFCHSL3Absolute',
        'ak4PFCHSResidual'
    )
)


process.ak4PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFCHSL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFCHSL1Offset',
        'ak4PFCHSL2Relative',
        'ak4PFCHSL3Absolute'
    )
)


process.ak4PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFCHSL1Offset',
        'ak4PFCHSL2Relative',
        'ak4PFCHSL3Absolute',
        'ak4PFCHSResidual'
    )
)


process.ak4PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak4PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFCHSL2Relative',
        'ak4PFCHSL3Absolute'
    )
)


process.ak4PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFCHSL2Relative',
        'ak4PFCHSL3Absolute',
        'ak4PFCHSResidual'
    )
)


process.ak4PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2Relative')
)


process.ak4PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L3Absolute')
)


process.ak4PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak4PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet',
        'ak4PFL2Relative',
        'ak4PFL3Absolute'
    )
)


process.ak4PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet',
        'ak4PFL2Relative',
        'ak4PFL3Absolute',
        'ak4PFL6SLB'
    )
)


process.ak4PFL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet',
        'ak4PFL2Relative',
        'ak4PFL3Absolute',
        'ak4PFResidual'
    )
)


process.ak4PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Offset',
        'ak4PFL2Relative',
        'ak4PFL3Absolute'
    )
)


process.ak4PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Offset',
        'ak4PFL2Relative',
        'ak4PFL3Absolute',
        'ak4PFResidual'
    )
)


process.ak4PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak4PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL2Relative',
        'ak4PFL3Absolute'
    )
)


process.ak4PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL2Relative',
        'ak4PFL3Absolute',
        'ak4PFL6SLB'
    )
)


process.ak4PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL2Relative',
        'ak4PFL3Absolute',
        'ak4PFResidual'
    )
)


process.ak4PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2Relative')
)


process.ak4PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L3Absolute')
)


process.ak4PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak4PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak4PFJetsSoftMuonTagInfos")
)


process.ak4PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2L3Residual')
)


process.ak4TrackL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet',
        'ak4TrackL2Relative',
        'ak4TrackL3Absolute'
    )
)


process.ak4TrackL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4TrackL2Relative',
        'ak4TrackL3Absolute'
    )
)


process.ak4TrackL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5TRK'),
    level = cms.string('L2Relative')
)


process.ak4TrackL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5TRK'),
    level = cms.string('L3Absolute')
)


process.ak5PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak5PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFCHSL1Fastjet',
        'ak5PFCHSL2Relative',
        'ak5PFCHSL3Absolute',
        'ak5PFCHSResidual'
    )
)


process.ak5PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFCHSL1Offset',
        'ak5PFCHSL2Relative',
        'ak5PFCHSL3Absolute',
        'ak5PFCHSResidual'
    )
)


process.ak5PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak5PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFCHSL2Relative',
        'ak5PFCHSL3Absolute'
    )
)


process.ak5PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFCHSL2Relative',
        'ak5PFCHSL3Absolute',
        'ak5PFCHSResidual'
    )
)


process.ak5PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L2Relative')
)


process.ak5PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L3Absolute')
)


process.ak5PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak5PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak5PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFL1Fastjet',
        'ak5PFL2Relative',
        'ak5PFL3Absolute',
        'ak5PFResidual'
    )
)


process.ak5PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFL1Offset',
        'ak5PFL2Relative',
        'ak5PFL3Absolute',
        'ak5PFResidual'
    )
)


process.ak5PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak5PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFL2Relative',
        'ak5PFL3Absolute'
    )
)


process.ak5PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak5PFL2Relative',
        'ak5PFL3Absolute',
        'ak5PFResidual'
    )
)


process.ak5PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2Relative')
)


process.ak5PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L3Absolute')
)


process.ak5PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK5PF'),
    level = cms.string('L2L3Residual')
)


process.ak6PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak6PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFCHSL1Fastjet',
        'ak6PFCHSL2Relative',
        'ak6PFCHSL3Absolute',
        'ak6PFCHSResidual'
    )
)


process.ak6PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFCHSL1Offset',
        'ak6PFCHSL2Relative',
        'ak6PFCHSL3Absolute',
        'ak6PFCHSResidual'
    )
)


process.ak6PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak6PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFCHSL2Relative',
        'ak6PFCHSL3Absolute'
    )
)


process.ak6PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFCHSL2Relative',
        'ak6PFCHSL3Absolute',
        'ak6PFCHSResidual'
    )
)


process.ak6PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L2Relative')
)


process.ak6PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L3Absolute')
)


process.ak6PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak6PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak6PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFL1Fastjet',
        'ak6PFL2Relative',
        'ak6PFL3Absolute',
        'ak6PFResidual'
    )
)


process.ak6PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFL1Offset',
        'ak6PFL2Relative',
        'ak6PFL3Absolute',
        'ak6PFResidual'
    )
)


process.ak6PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak6PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFL2Relative',
        'ak6PFL3Absolute'
    )
)


process.ak6PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak6PFL2Relative',
        'ak6PFL3Absolute',
        'ak6PFResidual'
    )
)


process.ak6PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L2Relative')
)


process.ak6PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L3Absolute')
)


process.ak6PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK6PF'),
    level = cms.string('L2L3Residual')
)


process.ak7CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet',
        'ak7CaloL2Relative',
        'ak7CaloL3Absolute'
    )
)


process.ak7CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7CaloL1Offset',
        'ak7CaloL2Relative',
        'ak7CaloL3Absolute',
        'ak7CaloL6SLB'
    )
)


process.ak7CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7CaloL1Fastjet',
        'ak7CaloL2Relative',
        'ak7CaloL3Absolute',
        'ak7CaloResidual'
    )
)


process.ak7CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ak7CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7CaloL1Offset',
        'ak7CaloL2Relative',
        'ak7CaloL3Absolute'
    )
)


process.ak7CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7CaloL1Offset',
        'ak7CaloL2Relative',
        'ak7CaloL3Absolute',
        'ak7CaloResidual'
    )
)


process.ak7CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak7CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7CaloL2Relative',
        'ak7CaloL3Absolute'
    )
)


process.ak7CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7CaloL2Relative',
        'ak7CaloL3Absolute',
        'ak7CaloL6SLB'
    )
)


process.ak7CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7CaloL2Relative',
        'ak7CaloL3Absolute',
        'ak7CaloResidual'
    )
)


process.ak7CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L2Relative')
)


process.ak7CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L3Absolute')
)


process.ak7CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak7CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak7CaloJetsSoftMuonTagInfos")
)


process.ak7CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7Calo'),
    level = cms.string('L2L3Residual')
)


process.ak7JPTL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7L1JPTFastjet',
        'ak7JPTL2Relative',
        'ak7JPTL3Absolute'
    )
)


process.ak7JPTL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7L1JPTFastjet',
        'ak7JPTL2Relative',
        'ak7JPTL3Absolute',
        'ak7JPTResidual'
    )
)


process.ak7JPTL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7L1JPTOffset',
        'ak7JPTL2Relative',
        'ak7JPTL3Absolute'
    )
)


process.ak7JPTL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7L1JPTOffset',
        'ak7JPTL2Relative',
        'ak7JPTL3Absolute',
        'ak7JPTResidual'
    )
)


process.ak7JPTL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7L1JPTOffset',
        'ak7JPTL2Relative',
        'ak7JPTL3Absolute'
    )
)


process.ak7L1JPTFastjet = cms.ESProducer("L1JPTOffsetCorrectionESProducer",
    algorithm = cms.string('AK7JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.string('ak7CaloL1Fastjet')
)


process.ak7L1JPTOffset = cms.ESProducer("L1JPTOffsetCorrectionESProducer",
    algorithm = cms.string('AK7JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.string('ak7CaloL1Offset')
)


process.ak7PFCHSL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFCHSL1Fastjet',
        'ak7PFCHSL2Relative',
        'ak7PFCHSL3Absolute'
    )
)


process.ak7PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak7PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFCHSL1Fastjet',
        'ak7PFCHSL2Relative',
        'ak7PFCHSL3Absolute',
        'ak7PFCHSResidual'
    )
)


process.ak7PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFCHSL1Offset',
        'ak7PFCHSL2Relative',
        'ak7PFCHSL3Absolute',
        'ak7PFCHSResidual'
    )
)


process.ak7PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak7PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFCHSL2Relative',
        'ak7PFCHSL3Absolute'
    )
)


process.ak7PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFCHSL2Relative',
        'ak7PFCHSL3Absolute',
        'ak7PFCHSResidual'
    )
)


process.ak7PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L2Relative')
)


process.ak7PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L3Absolute')
)


process.ak7PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak7PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet',
        'ak7PFL2Relative',
        'ak7PFL3Absolute'
    )
)


process.ak7PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet',
        'ak7PFL2Relative',
        'ak7PFL3Absolute',
        'ak7PFL6SLB'
    )
)


process.ak7PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak7PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFL1Fastjet',
        'ak7PFL2Relative',
        'ak7PFL3Absolute',
        'ak7PFResidual'
    )
)


process.ak7PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFL1Offset',
        'ak7PFL2Relative',
        'ak7PFL3Absolute'
    )
)


process.ak7PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFL1Offset',
        'ak7PFL2Relative',
        'ak7PFL3Absolute',
        'ak7PFResidual'
    )
)


process.ak7PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak7PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFL2Relative',
        'ak7PFL3Absolute'
    )
)


process.ak7PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFL2Relative',
        'ak7PFL3Absolute',
        'ak7PFL6SLB'
    )
)


process.ak7PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak7PFL2Relative',
        'ak7PFL3Absolute',
        'ak7PFResidual'
    )
)


process.ak7PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L2Relative')
)


process.ak7PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L3Absolute')
)


process.ak7PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak7PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak7PFJetsSoftMuonTagInfos")
)


process.ak7PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK7PF'),
    level = cms.string('L2L3Residual')
)


process.ak8PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak8PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFCHSL1Fastjet',
        'ak8PFCHSL2Relative',
        'ak8PFCHSL3Absolute',
        'ak8PFCHSResidual'
    )
)


process.ak8PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFCHSL1Offset',
        'ak8PFCHSL2Relative',
        'ak8PFCHSL3Absolute',
        'ak8PFCHSResidual'
    )
)


process.ak8PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak8PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFCHSL2Relative',
        'ak8PFCHSL3Absolute'
    )
)


process.ak8PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFCHSL2Relative',
        'ak8PFCHSL3Absolute',
        'ak8PFCHSResidual'
    )
)


process.ak8PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L2Relative')
)


process.ak8PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L3Absolute')
)


process.ak8PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak8PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak8PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFL1Fastjet',
        'ak8PFL2Relative',
        'ak8PFL3Absolute',
        'ak8PFResidual'
    )
)


process.ak8PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFL1Offset',
        'ak8PFL2Relative',
        'ak8PFL3Absolute',
        'ak8PFResidual'
    )
)


process.ak8PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak8PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFL2Relative',
        'ak8PFL3Absolute'
    )
)


process.ak8PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak8PFL2Relative',
        'ak8PFL3Absolute',
        'ak8PFResidual'
    )
)


process.ak8PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L2Relative')
)


process.ak8PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L3Absolute')
)


process.ak8PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK8PF'),
    level = cms.string('L2L3Residual')
)


process.ak9PFCHSL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak9PFCHSL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFCHSL1Fastjet',
        'ak9PFCHSL2Relative',
        'ak9PFCHSL3Absolute',
        'ak9PFCHSResidual'
    )
)


process.ak9PFCHSL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFCHSL1Offset',
        'ak9PFCHSL2Relative',
        'ak9PFCHSL3Absolute',
        'ak9PFCHSResidual'
    )
)


process.ak9PFCHSL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak9PFCHSL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFCHSL2Relative',
        'ak9PFCHSL3Absolute'
    )
)


process.ak9PFCHSL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFCHSL2Relative',
        'ak9PFCHSL3Absolute',
        'ak9PFCHSResidual'
    )
)


process.ak9PFCHSL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L2Relative')
)


process.ak9PFCHSL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L3Absolute')
)


process.ak9PFCHSResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak9PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak9PFL1FastjetL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFL1Fastjet',
        'ak9PFL2Relative',
        'ak9PFL3Absolute',
        'ak9PFResidual'
    )
)


process.ak9PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFL1Offset',
        'ak9PFL2Relative',
        'ak9PFL3Absolute',
        'ak9PFResidual'
    )
)


process.ak9PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ak9PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFL2Relative',
        'ak9PFL3Absolute'
    )
)


process.ak9PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak9PFL2Relative',
        'ak9PFL3Absolute',
        'ak9PFResidual'
    )
)


process.ak9PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L2Relative')
)


process.ak9PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L3Absolute')
)


process.ak9PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('AK9PF'),
    level = cms.string('L2L3Residual')
)


process.ctppsBeamParametersFromLHCInfoESSource = cms.ESProducer("CTPPSBeamParametersFromLHCInfoESSource",
    appendToDataLabel = cms.string(''),
    beamDivX45 = cms.double(0.1),
    beamDivX56 = cms.double(0.1),
    beamDivY45 = cms.double(0.1),
    beamDivY56 = cms.double(0.1),
    lhcInfoLabel = cms.string(''),
    vtxOffsetX45 = cms.double(0.01),
    vtxOffsetX56 = cms.double(0.01),
    vtxOffsetY45 = cms.double(0.01),
    vtxOffsetY56 = cms.double(0.01),
    vtxOffsetZ45 = cms.double(0.01),
    vtxOffsetZ56 = cms.double(0.01),
    vtxStddevX = cms.double(0.02),
    vtxStddevY = cms.double(0.02),
    vtxStddevZ = cms.double(0.02)
)


process.ctppsInterpolatedOpticalFunctionsESSource = cms.ESProducer("CTPPSInterpolatedOpticalFunctionsESSource",
    appendToDataLabel = cms.string(''),
    lhcInfoLabel = cms.string(''),
    opticsLabel = cms.string('')
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    MergePosition = cms.untracked.bool(True),
    appendToDataLabel = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.ic5CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet',
        'ic5CaloL2Relative',
        'ic5CaloL3Absolute'
    )
)


process.ic5CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5CaloL1Offset',
        'ic5CaloL2Relative',
        'ic5CaloL3Absolute',
        'ic5CaloL6SLB'
    )
)


process.ic5CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5CaloL1Fastjet',
        'ic5CaloL2Relative',
        'ic5CaloL3Absolute',
        'ic5CaloResidual'
    )
)


process.ic5CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ic5CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5CaloL1Offset',
        'ic5CaloL2Relative',
        'ic5CaloL3Absolute'
    )
)


process.ic5CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5CaloL1Offset',
        'ic5CaloL2Relative',
        'ic5CaloL3Absolute',
        'ic5CaloResidual'
    )
)


process.ic5CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ic5CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5CaloL2Relative',
        'ic5CaloL3Absolute'
    )
)


process.ic5CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5CaloL2Relative',
        'ic5CaloL3Absolute',
        'ic5CaloL6SLB'
    )
)


process.ic5CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5CaloL2Relative',
        'ic5CaloL3Absolute',
        'ic5CaloResidual'
    )
)


process.ic5CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L2Relative')
)


process.ic5CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L3Absolute')
)


process.ic5CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ic5CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ic5CaloJetsSoftMuonTagInfos")
)


process.ic5CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5Calo'),
    level = cms.string('L2L3Residual')
)


process.ic5PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet',
        'ic5PFL2Relative',
        'ic5PFL3Absolute'
    )
)


process.ic5PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet',
        'ic5PFL2Relative',
        'ic5PFL3Absolute',
        'ic5PFL6SLB'
    )
)


process.ic5PFL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5PFL1Fastjet',
        'ic5PFL2Relative',
        'ic5PFL3Absolute',
        'ic5PFResidual'
    )
)


process.ic5PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ic5PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5PFL1Offset',
        'ic5PFL2Relative',
        'ic5PFL3Absolute'
    )
)


process.ic5PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5PFL1Offset',
        'ic5PFL2Relative',
        'ic5PFL3Absolute',
        'ic5PFResidual'
    )
)


process.ic5PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.ic5PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5PFL2Relative',
        'ic5PFL3Absolute'
    )
)


process.ic5PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5PFL2Relative',
        'ic5PFL3Absolute',
        'ic5PFL6SLB'
    )
)


process.ic5PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ic5PFL2Relative',
        'ic5PFL3Absolute',
        'ic5PFResidual'
    )
)


process.ic5PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L2Relative')
)


process.ic5PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L3Absolute')
)


process.ic5PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ic5PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ic5PFJetsSoftMuonTagInfos")
)


process.ic5PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('IC5PF'),
    level = cms.string('L2L3Residual')
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useGangedStripsInME1a = cms.bool(False),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    DDDetector = cms.ESInputTag("",""),
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    attribute = cms.string('MuStructure'),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False),
    value = cms.string('MuonBarrelDT')
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.kt4CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet',
        'kt4CaloL2Relative',
        'kt4CaloL3Absolute'
    )
)


process.kt4CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4CaloL1Offset',
        'kt4CaloL2Relative',
        'kt4CaloL3Absolute',
        'kt4CaloL6SLB'
    )
)


process.kt4CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4CaloL1Fastjet',
        'kt4CaloL2Relative',
        'kt4CaloL3Absolute',
        'kt4CaloResidual'
    )
)


process.kt4CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.kt4CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4CaloL1Offset',
        'kt4CaloL2Relative',
        'kt4CaloL3Absolute'
    )
)


process.kt4CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4CaloL1Offset',
        'kt4CaloL2Relative',
        'kt4CaloL3Absolute',
        'kt4CaloResidual'
    )
)


process.kt4CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.kt4CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4CaloL2Relative',
        'kt4CaloL3Absolute'
    )
)


process.kt4CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4CaloL2Relative',
        'kt4CaloL3Absolute',
        'kt4CaloL6SLB'
    )
)


process.kt4CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4CaloL2Relative',
        'kt4CaloL3Absolute',
        'kt4CaloResidual'
    )
)


process.kt4CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L2Relative')
)


process.kt4CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L3Absolute')
)


process.kt4CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("kt4CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt4CaloJetsSoftMuonTagInfos")
)


process.kt4CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4Calo'),
    level = cms.string('L2L3Residual')
)


process.kt4PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet',
        'kt4PFL2Relative',
        'kt4PFL3Absolute'
    )
)


process.kt4PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet',
        'kt4PFL2Relative',
        'kt4PFL3Absolute',
        'kt4PFL6SLB'
    )
)


process.kt4PFL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4PFL1Fastjet',
        'kt4PFL2Relative',
        'kt4PFL3Absolute',
        'kt4PFResidual'
    )
)


process.kt4PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.kt4PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4PFL1Offset',
        'kt4PFL2Relative',
        'kt4PFL3Absolute'
    )
)


process.kt4PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4PFL1Offset',
        'kt4PFL2Relative',
        'kt4PFL3Absolute',
        'kt4PFResidual'
    )
)


process.kt4PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.kt4PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4PFL2Relative',
        'kt4PFL3Absolute'
    )
)


process.kt4PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4PFL2Relative',
        'kt4PFL3Absolute',
        'kt4PFL6SLB'
    )
)


process.kt4PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt4PFL2Relative',
        'kt4PFL3Absolute',
        'kt4PFResidual'
    )
)


process.kt4PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L2Relative')
)


process.kt4PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L3Absolute')
)


process.kt4PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("kt4PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt4PFJetsSoftMuonTagInfos")
)


process.kt4PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT4PF'),
    level = cms.string('L2L3Residual')
)


process.kt6CaloL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4CaloL1Fastjet',
        'kt6CaloL2Relative',
        'kt6CaloL3Absolute'
    )
)


process.kt6CaloL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6CaloL1Offset',
        'kt6CaloL2Relative',
        'kt6CaloL3Absolute',
        'kt6CaloL6SLB'
    )
)


process.kt6CaloL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6CaloL1Fastjet',
        'kt6CaloL2Relative',
        'kt6CaloL3Absolute',
        'kt6CaloResidual'
    )
)


process.kt6CaloL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.kt6CaloL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6CaloL1Offset',
        'kt6CaloL2Relative',
        'kt6CaloL3Absolute'
    )
)


process.kt6CaloL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6CaloL1Offset',
        'kt6CaloL2Relative',
        'kt6CaloL3Absolute',
        'kt6CaloResidual'
    )
)


process.kt6CaloL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.kt6CaloL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6CaloL2Relative',
        'kt6CaloL3Absolute'
    )
)


process.kt6CaloL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6CaloL2Relative',
        'kt6CaloL3Absolute',
        'kt6CaloL6SLB'
    )
)


process.kt6CaloL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6CaloL2Relative',
        'kt6CaloL3Absolute',
        'kt6CaloResidual'
    )
)


process.kt6CaloL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L2Relative')
)


process.kt6CaloL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L3Absolute')
)


process.kt6CaloL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("kt6CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt6CaloJetsSoftMuonTagInfos")
)


process.kt6CaloResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6Calo'),
    level = cms.string('L2L3Residual')
)


process.kt6PFL1FastL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet',
        'kt6PFL2Relative',
        'kt6PFL3Absolute'
    )
)


process.kt6PFL1FastL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'ak4PFL1Fastjet',
        'kt6PFL2Relative',
        'kt6PFL3Absolute',
        'kt6PFL6SLB'
    )
)


process.kt6PFL1FastL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6PFL1Fastjet',
        'kt6PFL2Relative',
        'kt6PFL3Absolute',
        'kt6PFResidual'
    )
)


process.kt6PFL1Fastjet = cms.ESProducer("L1FastjetCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.kt6PFL1L2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6PFL1Offset',
        'kt6PFL2Relative',
        'kt6PFL3Absolute'
    )
)


process.kt6PFL1L2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6PFL1Offset',
        'kt6PFL2Relative',
        'kt6PFL3Absolute',
        'kt6PFResidual'
    )
)


process.kt6PFL1Offset = cms.ESProducer("L1OffsetCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.string('offlinePrimaryVertices')
)


process.kt6PFL2L3 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6PFL2Relative',
        'kt6PFL3Absolute'
    )
)


process.kt6PFL2L3L6 = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6PFL2Relative',
        'kt6PFL3Absolute',
        'kt6PFL6SLB'
    )
)


process.kt6PFL2L3Residual = cms.ESProducer("JetCorrectionESChain",
    correctors = cms.vstring(
        'kt6PFL2Relative',
        'kt6PFL3Absolute',
        'kt6PFResidual'
    )
)


process.kt6PFL2Relative = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L2Relative')
)


process.kt6PFL3Absolute = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L3Absolute')
)


process.kt6PFL6SLB = cms.ESProducer("L6SLBCorrectionESProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("kt6PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("kt6PFJetsSoftMuonTagInfos")
)


process.kt6PFResidual = cms.ESProducer("LXXXCorrectionESProducer",
    algorithm = cms.string('KT6PF'),
    level = cms.string('L2L3Residual')
)


process.muonGeometryConstants = cms.ESProducer("MuonGeometryConstantsESModule",
    appendToDataLabel = cms.string(''),
    fromDD4Hep = cms.bool(False)
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiPixelQualityFromDbRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        )
    ),
    siPixelQualityLabel = cms.string('')
)


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGainRcd')
        ),
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )
    ),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiStripDetVOffRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ),
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )
    ),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.trackerGeometryDB = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.trackerNumberingGeometryDB = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDD4hep = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('120X_upgrade2018_realistic_v1'),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet()
)


process.HcalTimeSlewEP = cms.ESSource("HcalTimeSlewEP",
    appendToDataLabel = cms.string('HBHE'),
    timeSlewParametersM2 = cms.VPSet(
        cms.PSet(
            slope = cms.double(-3.178648),
            tmax = cms.double(16.0),
            tzero = cms.double(23.960177)
        ),
        cms.PSet(
            slope = cms.double(-1.5610227),
            tmax = cms.double(10.0),
            tzero = cms.double(11.977461)
        ),
        cms.PSet(
            slope = cms.double(-1.075824),
            tmax = cms.double(6.25),
            tzero = cms.double(9.109694)
        )
    ),
    timeSlewParametersM3 = cms.VPSet(
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(15.5),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-3.2),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(32.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ),
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        )
    )
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HBRecalibration = cms.bool(False),
    HBmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHB.txt'),
    HBreCalibCutoff = cms.double(20.0),
    HERecalibration = cms.bool(False),
    HEmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHE.txt'),
    HEreCalibCutoff = cms.double(20.0),
    HFRecalParameterBlock = cms.PSet(
        HFdepthOneParameterA = cms.vdouble(
            0.004123, 0.00602, 0.008201, 0.010489, 0.013379,
            0.016997, 0.021464, 0.027371, 0.034195, 0.044807,
            0.058939, 0.125497
        ),
        HFdepthOneParameterB = cms.vdouble(
            -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05,
            2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107,
            0.000425, 0.000209
        ),
        HFdepthTwoParameterA = cms.vdouble(
            0.002861, 0.004168, 0.0064, 0.008388, 0.011601,
            0.014425, 0.018633, 0.023232, 0.028274, 0.035447,
            0.051579, 0.086593
        ),
        HFdepthTwoParameterB = cms.vdouble(
            -2e-06, -0.0, -7e-06, -6e-06, -2e-06,
            1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05,
            0.000157, -3e-06
        )
    ),
    HFRecalibration = cms.bool(False),
    SiPMCharacteristics = cms.VPSet(
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(36000)
        ),
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(2500)
        ),
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ),
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ),
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ),
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ),
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(0)
        )
    ),
    hb = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.19),
        gainWidth = cms.vdouble(0.0),
        mcShape = cms.int32(125),
        noiseCorrelation = cms.vdouble(0.0),
        pedestal = cms.double(3.285),
        pedestalWidth = cms.double(0.809),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.49, 1.8, 7.2, 37.9),
        qieSlope = cms.vdouble(0.912, 0.917, 0.922, 0.923),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        zsThreshold = cms.int32(8)
    ),
    hbUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        noiseCorrelation = cms.vdouble(0.26, 0.254),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(150),
            intlumiToNeutrons = cms.double(367000000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(-5)
        ),
        recoShape = cms.int32(208),
        zsThreshold = cms.int32(16)
    ),
    he = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.23),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(125),
        noiseCorrelation = cms.vdouble(0.0),
        pedestal = cms.double(3.163),
        pedestalWidth = cms.double(0.9698),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.38, 2.0, 7.6, 39.6),
        qieSlope = cms.vdouble(0.912, 0.916, 0.92, 0.922),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        zsThreshold = cms.int32(9)
    ),
    heUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        noiseCorrelation = cms.vdouble(0.26, 0.254),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(75),
            intlumiToNeutrons = cms.double(29200000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(5)
        ),
        recoShape = cms.int32(208),
        zsThreshold = cms.int32(16)
    ),
    hf = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        noiseCorrelation = cms.vdouble(0.0),
        pedestal = cms.double(9.354),
        pedestalWidth = cms.double(2.516),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(-0.87, 1.4, 7.8, -29.6),
        qieSlope = cms.vdouble(0.359, 0.358, 0.36, 0.367),
        qieType = cms.int32(0),
        recoShape = cms.int32(301),
        zsThreshold = cms.int32(-9999)
    ),
    hfUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        noiseCorrelation = cms.vdouble(0.0),
        pedestal = cms.double(13.33),
        pedestalWidth = cms.double(3.33),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(0.0697, -0.7405, 12.38, -671.9),
        qieSlope = cms.vdouble(0.297, 0.298, 0.298, 0.313),
        qieType = cms.int32(1),
        recoShape = cms.int32(301),
        zsThreshold = cms.int32(-9999)
    ),
    ho = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.006, 0.0087),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(201),
        noiseCorrelation = cms.vdouble(0.0),
        pedestal = cms.double(12.06),
        pedestalWidth = cms.double(0.6285),
        photoelectronsToAnalog = cms.double(4.0),
        qieOffset = cms.vdouble(-0.44, 1.4, 7.1, 38.5),
        qieSlope = cms.vdouble(0.907, 0.915, 0.92, 0.921),
        qieType = cms.int32(0),
        recoShape = cms.int32(201),
        zsThreshold = cms.int32(24)
    ),
    iLumi = cms.double(-1.0),
    killHE = cms.bool(False),
    testHEPlan1 = cms.bool(True),
    testHFQIE10 = cms.bool(False),
    toGet = cms.untracked.vstring('GainWidths'),
    useHBUpgrade = cms.bool(False),
    useHEUpgrade = cms.bool(False),
    useHFUpgrade = cms.bool(True),
    useHOUpgrade = cms.bool(True),
    useIeta18depth1 = cms.bool(False),
    useLayer0Weight = cms.bool(True)
)


process.loadRecoTauTagMVAsFromPrepDB = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string(''),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet( (
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwoLTv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwoLTv1')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff50')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff40')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwoLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwoLTv1_mvaOutput_normalization')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwLTv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwLTv1')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff50')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff40')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwLTv1_mvaOutput_normalization')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwoLTv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwoLTv1')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff50')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff40')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwoLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwoLTv1_mvaOutput_normalization')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwLTv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwLTv1')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff50')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff40')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwLTv1_mvaOutput_normalization')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBoldDMwLTv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBoldDMwLTv1')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff50')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff40')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBoldDMwLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBoldDMwLTv1_mvaOutput_normalization')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBnewDMwLTv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBnewDMwLTv1')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff50')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff40')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBnewDMwLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBnewDMwLTv1_mvaOutput_normalization')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWoldDMwLTv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWoldDMwLTv1')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff50')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff40')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_mvaOutput_normalization')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWnewDMwLTv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWnewDMwLTv1')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff50')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff40')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_mvaOutput_normalization')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff50')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff40')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_mvaOutput_normalization')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff50')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff40')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_mvaOutput_normalization')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff50')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff40')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_mvaOutput_normalization')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff50')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff40')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_mvaOutput_normalization')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff95'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff95')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff50')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_WPEff40')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v1_mvaOutput_normalization')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_WPEff95'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_WPEff95')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_WPEff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_WPEff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_WPEff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_WPEff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_WPEff50')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_WPEff40')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2017v2_mvaOutput_normalization')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_WPEff95'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_WPEff95')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_WPEff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_WPEff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_WPEff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_WPEff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_WPEff50')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_WPEff40')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2017v2_mvaOutput_normalization')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_WPEff95'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_WPEff95')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_WPEff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_WPEff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_WPEff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_WPEff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_WPEff50')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_WPEff40')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMdR0p3wLT2017v2_mvaOutput_normalization')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoPhase2_v1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoPhase2')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoPhase2_v1_WPEff95'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoPhase2_WPEff95')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoPhase2_v1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoPhase2_WPEff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoPhase2_v1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoPhase2_WPEff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoPhase2_v1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoPhase2_WPEff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoPhase2_v1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoPhase2_WPEff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoPhase2_v1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoPhase2_WPEff50')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoPhase2_v1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoPhase2_WPEff40')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoPhase2_v1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoPhase2_mvaOutput_normalization')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff99')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff96')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff91')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff85')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff79')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff99')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff96')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff91')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff85')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff79')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff99')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff96')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff91')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff85')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff79')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff99')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff96')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff91')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff85')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff79')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff99')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff96')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff91')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff85')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff79')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff99')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff96')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff91')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff85')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff79')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff99')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff96')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff91')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff85')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff79')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff99')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff96')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff91')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff85')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff79')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff99')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff96')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff91')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff85')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff79')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff99')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff96')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff91')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff85')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff79')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff99')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff96')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff91')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff85')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff79')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff99')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff96')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff91')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff85')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff79')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff99')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff96')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff91')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff85')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff79')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff99')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff96')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff91')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff85')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff79')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff99')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff96')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff91')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff85')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff79')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff99')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff96')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff91')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff85')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff79')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff99')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff96')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff91')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff85')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff79')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff99')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff96')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff91')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff85')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff79')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff99')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff96')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff91')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff85')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff79')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff99')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff96')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff91')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff85')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff79')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff99')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff96')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff91')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff85')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff79')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff99')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff96')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff91')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff85')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff79')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff99')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff96')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff91')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff85')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff79')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff99')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff96')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff91')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff85')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff79')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_BL')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_BL_WPeff98'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_BL_WPeff98')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_BL_WPeff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_BL_WPeff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_BL_WPeff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_BL_WPeff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_BL_WPeff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_BL_WPeff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_BL_WPeff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_BL_WPeff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_BL')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_BL_WPeff98'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_BL_WPeff98')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_BL_WPeff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_BL_WPeff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_BL_WPeff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_BL_WPeff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_BL_WPeff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_BL_WPeff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_BL_WPeff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_BL_WPeff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_BL')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_BL_WPeff98'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_BL_WPeff98')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_BL_WPeff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_BL_WPeff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_BL_WPeff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_BL_WPeff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_BL_WPeff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_BL_WPeff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_BL_WPeff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_BL_WPeff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_BL')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_BL_WPeff98'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_BL_WPeff98')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_BL_WPeff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_BL_WPeff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_BL_WPeff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_BL_WPeff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_BL_WPeff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_BL_WPeff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_BL_WPeff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_BL_WPeff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_EC')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_EC_WPeff98'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_EC_WPeff98')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_EC_WPeff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_EC_WPeff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_EC_WPeff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_EC_WPeff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_EC_WPeff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_EC_WPeff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_EC_WPeff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_woGwoGSF_EC_WPeff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_EC')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_EC_WPeff98'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_EC_WPeff98')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_EC_WPeff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_EC_WPeff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_EC_WPeff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_EC_WPeff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_EC_WPeff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_EC_WPeff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_EC_WPeff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_NoEleMatch_wGwoGSF_EC_WPeff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_EC')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_EC_WPeff98'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_EC_WPeff98')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_EC_WPeff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_EC_WPeff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_EC_WPeff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_EC_WPeff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_EC_WPeff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_EC_WPeff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_EC_WPeff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_woGwGSF_EC_WPeff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_EC')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_EC_WPeff98'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_EC_WPeff98')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_EC_WPeff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_EC_WPeff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_EC_WPeff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_EC_WPeff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_EC_WPeff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_EC_WPeff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_EC_WPeff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v3_noeveto_gbr_wGwGSF_EC_WPeff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_BL')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff98'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff98')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_BL')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff98'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff98')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_BL')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_BL_WPEff98'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_BL_WPEff98')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_BL_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_BL_WPEff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_BL_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_BL_WPEff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_BL_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_BL_WPEff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_BL_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_BL_WPEff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_BL')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_BL_WPEff98'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_BL_WPEff98')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_BL_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_BL_WPEff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_BL_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_BL_WPEff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_BL_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_BL_WPEff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_BL_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_BL_WPEff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_FWEC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_FWEC')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_FWEC_WPEff98'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_FWEC_WPEff98')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_FWEC_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_FWEC_WPEff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_FWEC_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_FWEC_WPEff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_FWEC_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_FWEC_WPEff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_FWEC_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_FWEC_WPEff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_VFWEC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_VFWEC')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_VFWEC_WPEff98'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_VFWEC_WPEff98')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_VFWEC_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_VFWEC_WPEff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_VFWEC_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_VFWEC_WPEff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_VFWEC_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_VFWEC_WPEff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_VFWEC_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_woGwoGSF_VFWEC_WPEff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_FWEC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_FWEC')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_FWEC_WPEff98'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_FWEC_WPEff98')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_FWEC_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_FWEC_WPEff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_FWEC_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_FWEC_WPEff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_FWEC_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_FWEC_WPEff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_FWEC_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_FWEC_WPEff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_VFWEC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_VFWEC')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_VFWEC_WPEff98'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_VFWEC_WPEff98')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_VFWEC_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_VFWEC_WPEff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_VFWEC_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_VFWEC_WPEff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_VFWEC_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_VFWEC_WPEff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_VFWEC_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_NoEleMatch_wGwoGSF_VFWEC_WPEff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_FWEC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_FWEC')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_FWEC_WPEff98'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_FWEC_WPEff98')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_FWEC_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_FWEC_WPEff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_FWEC_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_FWEC_WPEff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_FWEC_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_FWEC_WPEff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_FWEC_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_FWEC_WPEff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_VFWEC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_VFWEC')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_VFWEC_WPEff98'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_VFWEC_WPEff98')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_VFWEC_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_VFWEC_WPEff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_VFWEC_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_VFWEC_WPEff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_VFWEC_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_VFWEC_WPEff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_VFWEC_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_woGwGSF_VFWEC_WPEff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_FWEC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_FWEC')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_FWEC_WPEff98'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_FWEC_WPEff98')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_FWEC_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_FWEC_WPEff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_FWEC_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_FWEC_WPEff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_FWEC_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_FWEC_WPEff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_FWEC_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_FWEC_WPEff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_VFWEC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_VFWEC')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_VFWEC_WPEff98'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_VFWEC_WPEff98')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_VFWEC_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_VFWEC_WPEff90')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_VFWEC_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_VFWEC_WPEff80')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_VFWEC_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_VFWEC_WPEff70')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_VFWEC_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronPhase2MVA6v1_gbr_wGwGSF_VFWEC_WPEff60')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_againstMuonMVAv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_againstMuonMVAv1')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_againstMuonMVAv1_WPeff99_5'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_againstMuonMVAv1_WPeff99_5')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_againstMuonMVAv1_WPeff99_0'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_againstMuonMVAv1_WPeff99_0')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_againstMuonMVAv1_WPeff98_0'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_againstMuonMVAv1_WPeff98_0')
        ),
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_againstMuonMVAv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_againstMuonMVAv1_mvaOutput_normalization')
        )
     ) )
)


process.prefer("es_hardcode")

process.patPFTauIsolationTask = cms.Task(process.tauIsoDepositPFCandidates, process.tauIsoDepositPFChargedHadrons, process.tauIsoDepositPFGammas, process.tauIsoDepositPFNeutralHadrons)


process.pfNoPileUpIsoPFBRECOTask = cms.Task(process.pfNoPileUpIsoPFBRECO, process.pfPileUpIsoPFBRECO)


process.pfSortByTypePFBRECOTask = cms.Task(process.pfAllChargedHadronsPFBRECO, process.pfAllChargedParticlesPFBRECO, process.pfAllNeutralHadronsAndPhotonsPFBRECO, process.pfAllNeutralHadronsPFBRECO, process.pfAllPhotonsPFBRECO, process.pfPileUpAllChargedParticlesPFBRECO)


process.updateHPSPFTausTask = cms.Task(process.hpsPFTauBasicDiscriminators)


process.hpsPFTauBasicDiscriminatorsTask = cms.Task(process.hpsPFTauBasicDiscriminators)


process.hpsPFTauBasicDiscriminatorsdR03Task = cms.Task(process.hpsPFTauBasicDiscriminatorsdR03)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTTask = cms.Task(process.hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLT, process.hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTTask = cms.Task(process.hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLT, process.hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw)


process.hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTTask = cms.Task(process.hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLT, process.hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw)


process.hpsPFTauMVAIsolation2Task = cms.Task(process.hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTTask, process.hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTTask, process.hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTTask)


process.hpsPFTauVertexAndImpactParametersTask = cms.Task(process.hpsPFTauPrimaryVertexProducer, process.hpsPFTauSecondaryVertexProducer, process.hpsPFTauTransverseImpactParameters)


process.mvaIsolation2TaskRun2 = cms.Task(process.discriminationByIsolationMVArun2v1, process.discriminationByIsolationMVArun2v1raw, process.hpsPFTauBasicDiscriminators)


process.produceHPSPFTausTask = cms.Task(process.hpsPFTauProducer, process.hpsPFTauProducerSansRefs, process.hpsSelectionDiscriminator)


process.electronCleanedPackedCandidateTask = cms.Task(process.LooseFilter, process.PackedCandsElectronCleaned)


process.muonCleanedPackedCandidateTask = cms.Task(process.LooseMuonFilter, process.PackedCandsMuonCleaned)


process.lowPtElectronCleanedPackedCandidateTask = cms.Task(process.LowPtFilter, process.PackedCandsLowPtElectronCleaned)


process.recoTauCommonTask = cms.Task(process.recoTauAK4Jets08RegionPAT, process.recoTauPileUpVertices)


process.rerunMvaIsolationTask = cms.Task(process.deepTau2017v2p1, process.patTauDiscriminationByElectronRejectionMVA62018, process.patTauDiscriminationByElectronRejectionMVA62018Raw, process.rerunDiscriminationByIsolationOldDMMVArun2017v2, process.rerunDiscriminationByIsolationOldDMMVArun2017v2raw)


process.newTauIDsTask = cms.Task(process.rerunMvaIsolationTask, process.selectedPatTaus)


process.rerunMvaIsolationTaskElectronCleaned = cms.Task(process.deepTau2017v2p1ElectronCleaned, process.patTauDiscriminationByElectronRejectionMVA62018ElectronCleaned, process.patTauDiscriminationByElectronRejectionMVA62018RawElectronCleaned, process.rerunDiscriminationByIsolationOldDMMVArun2017v2ElectronCleaned, process.rerunDiscriminationByIsolationOldDMMVArun2017v2rawElectronCleaned)


process.newTauIDsTaskElectronCleaned = cms.Task(process.rerunMvaIsolationTaskElectronCleaned, process.selectedPatTausElectronCleaned)


process.rerunMvaIsolationTaskMuonCleaned = cms.Task(process.deepTau2017v2p1MuonCleaned, process.patTauDiscriminationByElectronRejectionMVA62018MuonCleaned, process.patTauDiscriminationByElectronRejectionMVA62018RawMuonCleaned, process.rerunDiscriminationByIsolationOldDMMVArun2017v2MuonCleaned, process.rerunDiscriminationByIsolationOldDMMVArun2017v2rawMuonCleaned)


process.newTauIDsTaskMuonCleaned = cms.Task(process.rerunMvaIsolationTaskMuonCleaned, process.selectedPatTausMuonCleaned)


process.rerunMvaIsolationTaskLowPtElectronCleaned = cms.Task(process.deepTau2017v2p1LowPtElectronCleaned, process.patTauDiscriminationByElectronRejectionMVA62018LowPtElectronCleaned, process.patTauDiscriminationByElectronRejectionMVA62018RawLowPtElectronCleaned, process.rerunDiscriminationByIsolationOldDMMVArun2017v2LowPtElectronCleaned, process.rerunDiscriminationByIsolationOldDMMVArun2017v2rawLowPtElectronCleaned)


process.newTauIDsTaskLowPtElectronCleaned = cms.Task(process.rerunMvaIsolationTaskLowPtElectronCleaned, process.selectedPatTausLowPtElectronCleaned)


process.rerunMvaIsolationTaskBoosted = cms.Task(process.deepTau2017v2p1Boosted, process.patTauDiscriminationByElectronRejectionMVA62018Boosted, process.patTauDiscriminationByElectronRejectionMVA62018RawBoosted, process.rerunDiscriminationByIsolationOldDMMVArun2017v2Boosted, process.rerunDiscriminationByIsolationOldDMMVArun2017v2rawBoosted)


process.newTauIDsTaskBoosted = cms.Task(process.rerunMvaIsolationTaskBoosted, process.selectedPatTausBoosted)


process.patJetCorrectionsTask = cms.Task(process.patJetCorrFactors)


process.patHPSPFTauDiscriminationTask = cms.Task(process.updateHPSPFTausTask)


process.patPFCandidateIsoDepositSelectionTask = cms.Task(process.pfNoPileUpIsoPFBRECOTask, process.pfSortByTypePFBRECOTask)


process.PFTauTask = cms.Task(process.ak4PFJetsLegacyHPSPiZeros, process.ak4PFJetsRecoTauChargedHadrons, process.combinatoricRecoTaus, process.hpsPFTauBasicDiscriminatorsTask, process.hpsPFTauBasicDiscriminatorsdR03Task, process.hpsPFTauDiscriminationByDeadECALElectronRejection, process.hpsPFTauDiscriminationByDecayModeFinding, process.hpsPFTauDiscriminationByDecayModeFindingNewDMs, process.hpsPFTauDiscriminationByDecayModeFindingOldDMs, process.hpsPFTauDiscriminationByLooseElectronRejection, process.hpsPFTauDiscriminationByMVA6ElectronRejection, process.hpsPFTauDiscriminationByMVA6rawElectronRejection, process.hpsPFTauDiscriminationByMediumElectronRejection, process.hpsPFTauDiscriminationByMuonRejection3, process.hpsPFTauDiscriminationByTightElectronRejection, process.hpsPFTauMVAIsolation2Task, process.hpsPFTauPrimaryVertexProducer, process.hpsPFTauSecondaryVertexProducer, process.hpsPFTauTransverseImpactParameters, process.produceHPSPFTausTask, process.recoTauCommonTask)


process.produceAndDiscriminateHPSPFTausTask = cms.Task(process.hpsPFTauBasicDiscriminatorsTask, process.hpsPFTauBasicDiscriminatorsdR03Task, process.hpsPFTauDiscriminationByDeadECALElectronRejection, process.hpsPFTauDiscriminationByDecayModeFinding, process.hpsPFTauDiscriminationByDecayModeFindingNewDMs, process.hpsPFTauDiscriminationByDecayModeFindingOldDMs, process.hpsPFTauDiscriminationByLooseElectronRejection, process.hpsPFTauDiscriminationByMVA6ElectronRejection, process.hpsPFTauDiscriminationByMVA6rawElectronRejection, process.hpsPFTauDiscriminationByMediumElectronRejection, process.hpsPFTauDiscriminationByMuonRejection3, process.hpsPFTauDiscriminationByTightElectronRejection, process.hpsPFTauMVAIsolation2Task, process.hpsPFTauVertexAndImpactParametersTask, process.produceHPSPFTausTask)


process.recoTauClassicHPSTask = cms.Task(process.ak4PFJetsLegacyHPSPiZeros, process.ak4PFJetsRecoTauChargedHadrons, process.combinatoricRecoTaus, process.produceAndDiscriminateHPSPFTausTask)


process.miniAODTausTaskBoosted = cms.Task(process.ak4PFJetsLegacyHPSPiZerosBoosted, process.ak4PFJetsRecoTauChargedHadronsBoosted, process.boostedTauSeedsPAT, process.ca8PFJetsCHSprunedForBoostedTausPAT, process.combinatoricRecoTausBoosted, process.hpsPFTauBasicDiscriminatorsBoosted, process.hpsPFTauBasicDiscriminatorsdR03Boosted, process.hpsPFTauDiscriminationByDeadECALElectronRejectionBoosted, process.hpsPFTauDiscriminationByDecayModeFindingBoosted, process.hpsPFTauDiscriminationByDecayModeFindingNewDMsBoosted, process.hpsPFTauDiscriminationByDecayModeFindingOldDMsBoosted, process.hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTBoosted, process.hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTrawBoosted, process.hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTBoosted, process.hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTrawBoosted, process.hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTBoosted, process.hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTrawBoosted, process.hpsPFTauPrimaryVertexProducerBoosted, process.hpsPFTauProducerBoosted, process.hpsPFTauProducerSansRefsBoosted, process.hpsPFTauSecondaryVertexProducerBoosted, process.hpsPFTauTransverseImpactParametersBoosted, process.hpsSelectionDiscriminatorBoosted, process.newTauIDsTaskBoosted, process.patTausBoosted, process.pfAllChargedHadronsPFBRECOBoosted, process.pfAllChargedParticlesPFBRECOBoosted, process.pfAllNeutralHadronsAndPhotonsPFBRECOBoosted, process.pfAllNeutralHadronsPFBRECOBoosted, process.pfAllPhotonsPFBRECOBoosted, process.pfNoPileUpIsoPFBRECOBoosted, process.pfPileUpAllChargedParticlesPFBRECOBoosted, process.pfPileUpIsoPFBRECOBoosted, process.recoTauAK4Jets08RegionPATBoosted, process.recoTauPileUpVerticesBoosted, process.selectedPatTausNoNewIDsBoosted, process.tauGenJetMatchBoosted, process.tauGenJetsBoosted, process.tauGenJetsSelectorAllHadronsBoosted, process.tauIsoDepositPFCandidatesBoosted, process.tauIsoDepositPFChargedHadronsBoosted, process.tauIsoDepositPFGammasBoosted, process.tauIsoDepositPFNeutralHadronsBoosted, process.tauMatchBoosted)


process.miniAODTausTaskElectronCleaned = cms.Task(process.ak4PFJetsLegacyHPSPiZerosElectronCleaned, process.ak4PFJetsPATElectronCleaned, process.ak4PFJetsRecoTauChargedHadronsElectronCleaned, process.combinatoricRecoTausElectronCleaned, process.electronCleanedPackedCandidateTask, process.hpsPFTauBasicDiscriminatorsElectronCleaned, process.hpsPFTauBasicDiscriminatorsdR03ElectronCleaned, process.hpsPFTauDiscriminationByDeadECALElectronRejectionElectronCleaned, process.hpsPFTauDiscriminationByDecayModeFindingElectronCleaned, process.hpsPFTauDiscriminationByDecayModeFindingNewDMsElectronCleaned, process.hpsPFTauDiscriminationByDecayModeFindingOldDMsElectronCleaned, process.hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTElectronCleaned, process.hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTrawElectronCleaned, process.hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTElectronCleaned, process.hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTrawElectronCleaned, process.hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTElectronCleaned, process.hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTrawElectronCleaned, process.hpsPFTauDiscriminationByMuonRejectionSimpleElectronCleaned, process.hpsPFTauPrimaryVertexProducerElectronCleaned, process.hpsPFTauProducerElectronCleaned, process.hpsPFTauProducerSansRefsElectronCleaned, process.hpsPFTauSecondaryVertexProducerElectronCleaned, process.hpsPFTauTransverseImpactParametersElectronCleaned, process.hpsSelectionDiscriminatorElectronCleaned, process.newTauIDsTaskElectronCleaned, process.patJetsPATElectronCleaned, process.patTausElectronCleaned, process.pfAllChargedHadronsPFBRECOElectronCleaned, process.pfAllChargedParticlesPFBRECOElectronCleaned, process.pfAllNeutralHadronsAndPhotonsPFBRECOElectronCleaned, process.pfAllNeutralHadronsPFBRECOElectronCleaned, process.pfAllPhotonsPFBRECOElectronCleaned, process.pfNoPileUpIsoPFBRECOElectronCleaned, process.pfPileUpAllChargedParticlesPFBRECOElectronCleaned, process.pfPileUpIsoPFBRECOElectronCleaned, process.recoTauAK4Jets08RegionPATElectronCleaned, process.recoTauPileUpVerticesElectronCleaned, process.selectedPatTausNoNewIDsElectronCleaned, process.tauGenJetMatchElectronCleaned, process.tauGenJetsElectronCleaned, process.tauGenJetsSelectorAllHadronsElectronCleaned, process.tauIsoDepositPFCandidatesElectronCleaned, process.tauIsoDepositPFChargedHadronsElectronCleaned, process.tauIsoDepositPFGammasElectronCleaned, process.tauIsoDepositPFNeutralHadronsElectronCleaned, process.tauMatchElectronCleaned)


process.miniAODTausTaskMuonCleaned = cms.Task(process.ak4PFJetsLegacyHPSPiZerosMuonCleaned, process.ak4PFJetsPATMuonCleaned, process.ak4PFJetsRecoTauChargedHadronsMuonCleaned, process.combinatoricRecoTausMuonCleaned, process.hpsPFTauBasicDiscriminatorsMuonCleaned, process.hpsPFTauBasicDiscriminatorsdR03MuonCleaned, process.hpsPFTauDiscriminationByDeadECALElectronRejectionMuonCleaned, process.hpsPFTauDiscriminationByDecayModeFindingMuonCleaned, process.hpsPFTauDiscriminationByDecayModeFindingNewDMsMuonCleaned, process.hpsPFTauDiscriminationByDecayModeFindingOldDMsMuonCleaned, process.hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTMuonCleaned, process.hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTrawMuonCleaned, process.hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTMuonCleaned, process.hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTrawMuonCleaned, process.hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTMuonCleaned, process.hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTrawMuonCleaned, process.hpsPFTauDiscriminationByMuonRejectionSimpleMuonCleaned, process.hpsPFTauPrimaryVertexProducerMuonCleaned, process.hpsPFTauProducerMuonCleaned, process.hpsPFTauProducerSansRefsMuonCleaned, process.hpsPFTauSecondaryVertexProducerMuonCleaned, process.hpsPFTauTransverseImpactParametersMuonCleaned, process.hpsSelectionDiscriminatorMuonCleaned, process.muonCleanedPackedCandidateTask, process.newTauIDsTaskMuonCleaned, process.patJetsPATMuonCleaned, process.patTausMuonCleaned, process.pfAllChargedHadronsPFBRECOMuonCleaned, process.pfAllChargedParticlesPFBRECOMuonCleaned, process.pfAllNeutralHadronsAndPhotonsPFBRECOMuonCleaned, process.pfAllNeutralHadronsPFBRECOMuonCleaned, process.pfAllPhotonsPFBRECOMuonCleaned, process.pfNoPileUpIsoPFBRECOMuonCleaned, process.pfPileUpAllChargedParticlesPFBRECOMuonCleaned, process.pfPileUpIsoPFBRECOMuonCleaned, process.recoTauAK4Jets08RegionPATMuonCleaned, process.recoTauPileUpVerticesMuonCleaned, process.selectedPatTausNoNewIDsMuonCleaned, process.tauGenJetMatchMuonCleaned, process.tauGenJetsMuonCleaned, process.tauGenJetsSelectorAllHadronsMuonCleaned, process.tauIsoDepositPFCandidatesMuonCleaned, process.tauIsoDepositPFChargedHadronsMuonCleaned, process.tauIsoDepositPFGammasMuonCleaned, process.tauIsoDepositPFNeutralHadronsMuonCleaned, process.tauMatchMuonCleaned)


process.miniAODTausTaskLowPtElectronCleaned = cms.Task(process.ak4PFJetsLegacyHPSPiZerosLowPtElectronCleaned, process.ak4PFJetsPATLowPtElectronCleaned, process.ak4PFJetsRecoTauChargedHadronsLowPtElectronCleaned, process.combinatoricRecoTausLowPtElectronCleaned, process.hpsPFTauBasicDiscriminatorsLowPtElectronCleaned, process.hpsPFTauBasicDiscriminatorsdR03LowPtElectronCleaned, process.hpsPFTauDiscriminationByDeadECALElectronRejectionLowPtElectronCleaned, process.hpsPFTauDiscriminationByDecayModeFindingLowPtElectronCleaned, process.hpsPFTauDiscriminationByDecayModeFindingNewDMsLowPtElectronCleaned, process.hpsPFTauDiscriminationByDecayModeFindingOldDMsLowPtElectronCleaned, process.hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTLowPtElectronCleaned, process.hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTrawLowPtElectronCleaned, process.hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTLowPtElectronCleaned, process.hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTrawLowPtElectronCleaned, process.hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTLowPtElectronCleaned, process.hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTrawLowPtElectronCleaned, process.hpsPFTauDiscriminationByMuonRejectionSimpleLowPtElectronCleaned, process.hpsPFTauPrimaryVertexProducerLowPtElectronCleaned, process.hpsPFTauProducerLowPtElectronCleaned, process.hpsPFTauProducerSansRefsLowPtElectronCleaned, process.hpsPFTauSecondaryVertexProducerLowPtElectronCleaned, process.hpsPFTauTransverseImpactParametersLowPtElectronCleaned, process.hpsSelectionDiscriminatorLowPtElectronCleaned, process.lowPtElectronCleanedPackedCandidateTask, process.newTauIDsTaskLowPtElectronCleaned, process.patJetsPATLowPtElectronCleaned, process.patTausLowPtElectronCleaned, process.pfAllChargedHadronsPFBRECOLowPtElectronCleaned, process.pfAllChargedParticlesPFBRECOLowPtElectronCleaned, process.pfAllNeutralHadronsAndPhotonsPFBRECOLowPtElectronCleaned, process.pfAllNeutralHadronsPFBRECOLowPtElectronCleaned, process.pfAllPhotonsPFBRECOLowPtElectronCleaned, process.pfNoPileUpIsoPFBRECOLowPtElectronCleaned, process.pfPileUpAllChargedParticlesPFBRECOLowPtElectronCleaned, process.pfPileUpIsoPFBRECOLowPtElectronCleaned, process.recoTauAK4Jets08RegionPATLowPtElectronCleaned, process.recoTauPileUpVerticesLowPtElectronCleaned, process.selectedPatTausNoNewIDsLowPtElectronCleaned, process.tauGenJetMatchLowPtElectronCleaned, process.tauGenJetsLowPtElectronCleaned, process.tauGenJetsSelectorAllHadronsLowPtElectronCleaned, process.tauIsoDepositPFCandidatesLowPtElectronCleaned, process.tauIsoDepositPFChargedHadronsLowPtElectronCleaned, process.tauIsoDepositPFGammasLowPtElectronCleaned, process.tauIsoDepositPFNeutralHadronsLowPtElectronCleaned, process.tauMatchLowPtElectronCleaned)


process.makePatTausTask = cms.Task(process.patPFCandidateIsoDepositSelectionTask, process.patPFTauIsolationTask, process.patTaus, process.tauGenJetMatch, process.tauGenJets, process.tauGenJetsSelectorAllHadrons, process.tauMatch)


process.miniAODTausTask = cms.Task(process.ak4PFJetsLegacyHPSPiZeros, process.ak4PFJetsPAT, process.ak4PFJetsRecoTauChargedHadrons, process.combinatoricRecoTaus, process.hpsPFTauBasicDiscriminatorsTask, process.hpsPFTauBasicDiscriminatorsdR03Task, process.hpsPFTauDiscriminationByDeadECALElectronRejection, process.hpsPFTauDiscriminationByDecayModeFinding, process.hpsPFTauDiscriminationByDecayModeFindingNewDMs, process.hpsPFTauDiscriminationByDecayModeFindingOldDMs, process.hpsPFTauDiscriminationByMuonRejectionSimple, process.hpsPFTauDiscriminationByMuonRejectionSimpleBoosted, process.hpsPFTauMVAIsolation2Task, process.hpsPFTauPrimaryVertexProducer, process.hpsPFTauSecondaryVertexProducer, process.hpsPFTauTransverseImpactParameters, process.makePatTausTask, process.newTauIDsTask, process.patJetsPAT, process.produceHPSPFTausTask, process.recoTauCommonTask, process.selectedPatTausNoNewIDs)


process.makePatTaus = cms.Sequence(process.makePatTausTask)


process.patFixedConePFTauDiscrimination = cms.Sequence()


process.patHPSPFTauDiscrimination = cms.Sequence(process.patHPSPFTauDiscriminationTask)


process.patPFCandidateIsoDepositSelection = cms.Sequence(process.patPFCandidateIsoDepositSelectionTask)


process.patPFTauIsolation = cms.Sequence(process.patPFTauIsolationTask)


process.patShrinkingConePFTauDiscrimination = cms.Sequence()


process.pfNoPileUpIsoPFBRECOSequence = cms.Sequence(process.pfNoPileUpIsoPFBRECOTask)


process.pfSortByTypePFBRECOSequence = cms.Sequence(process.pfSortByTypePFBRECOTask)


process.updateHPSPFTaus = cms.Sequence(process.updateHPSPFTausTask)


process.PFTau = cms.Sequence(process.PFTauTask)


process.hpsPFTauMVAIsolation2Seq = cms.Sequence(process.hpsPFTauBasicDiscriminatorsTask, process.hpsPFTauBasicDiscriminatorsdR03Task, process.hpsPFTauMVAIsolation2Task)


process.hpsPFTauVertexAndImpactParametersSeq = cms.Sequence(process.hpsPFTauVertexAndImpactParametersTask)


process.mvaIsolation2SeqRun2 = cms.Sequence(process.mvaIsolation2TaskRun2)


process.produceAndDiscriminateHPSPFTaus = cms.Sequence(process.produceAndDiscriminateHPSPFTausTask)


process.produceHPSPFTaus = cms.Sequence(process.produceHPSPFTausTask)


process.recoTauClassicHPSSequence = cms.Sequence(process.recoTauClassicHPSTask)


process.recoTauCommonSequence = cms.Sequence(process.recoTauCommonTask)


process.miniAODTausSequence = cms.Sequence(process.miniAODTausTask)


process.miniAODTausSequenceBoosted = cms.Sequence(process.miniAODTausTaskBoosted)


process.miniAODTausSequenceElectronCleaned = cms.Sequence(process.miniAODTausTaskElectronCleaned)


process.miniAODTausSequenceMuonCleaned = cms.Sequence(process.miniAODTausTaskMuonCleaned)


process.miniAODTausSequenceLowPtElectronCleaned = cms.Sequence(process.miniAODTausTaskLowPtElectronCleaned)


process.rerunMvaIsolationSequence = cms.Sequence(cms.Sequence(cms.Task(process.rerunDiscriminationByIsolationOldDMMVArun2017v2, process.rerunDiscriminationByIsolationOldDMMVArun2017v2raw))+process.deepTau2017v2p1+cms.Sequence(cms.Task(process.patTauDiscriminationByElectronRejectionMVA62018, process.patTauDiscriminationByElectronRejectionMVA62018Raw)))


process.rerunMvaIsolationSequenceElectronCleaned = cms.Sequence(cms.Sequence(cms.Task(process.rerunDiscriminationByIsolationOldDMMVArun2017v2ElectronCleaned, process.rerunDiscriminationByIsolationOldDMMVArun2017v2rawElectronCleaned))+process.deepTau2017v2p1ElectronCleaned+cms.Sequence(cms.Task(process.patTauDiscriminationByElectronRejectionMVA62018ElectronCleaned, process.patTauDiscriminationByElectronRejectionMVA62018RawElectronCleaned)))


process.rerunMvaIsolationSequenceMuonCleaned = cms.Sequence(cms.Sequence(cms.Task(process.rerunDiscriminationByIsolationOldDMMVArun2017v2MuonCleaned, process.rerunDiscriminationByIsolationOldDMMVArun2017v2rawMuonCleaned))+process.deepTau2017v2p1MuonCleaned+cms.Sequence(cms.Task(process.patTauDiscriminationByElectronRejectionMVA62018MuonCleaned, process.patTauDiscriminationByElectronRejectionMVA62018RawMuonCleaned)))


process.rerunMvaIsolationSequenceLowPtElectronCleaned = cms.Sequence(cms.Sequence(cms.Task(process.rerunDiscriminationByIsolationOldDMMVArun2017v2LowPtElectronCleaned, process.rerunDiscriminationByIsolationOldDMMVArun2017v2rawLowPtElectronCleaned))+process.deepTau2017v2p1LowPtElectronCleaned+cms.Sequence(cms.Task(process.patTauDiscriminationByElectronRejectionMVA62018LowPtElectronCleaned, process.patTauDiscriminationByElectronRejectionMVA62018RawLowPtElectronCleaned)))


process.rerunMvaIsolationSequenceBoosted = cms.Sequence(cms.Sequence(cms.Task(process.rerunDiscriminationByIsolationOldDMMVArun2017v2Boosted, process.rerunDiscriminationByIsolationOldDMMVArun2017v2rawBoosted))+process.deepTau2017v2p1Boosted+cms.Sequence(cms.Task(process.patTauDiscriminationByElectronRejectionMVA62018Boosted, process.patTauDiscriminationByElectronRejectionMVA62018RawBoosted)))


process.makeUpdatedPatJets = cms.Sequence(process.updatedPatJetCorrFactors+process.updatedPatJets)


process.patJetCorrections = cms.Sequence(process.patJetCorrectionsTask)


process.prefiringweightMaker = cms.Path(process.prefiringweight)


process.TauReco = cms.Path(process.miniAODTausSequence)


process.TauRecoElectronCleaned = cms.Path(process.miniAODTausSequenceElectronCleaned)


process.TauRecoMuonCleaned = cms.Path(process.miniAODTausSequenceMuonCleaned)


process.TauRecoBoosted = cms.Path(process.miniAODTausSequenceBoosted)


process.TauRecoLowPtElectronCleaned = cms.Path(process.miniAODTausSequenceLowPtElectronCleaned)


process.slimpath = cms.Path(process.slimmedTausUnCleaned+process.slimmedTausBoosted+process.slimmedTausElectronCleaned+process.slimmedTausMuonCleaned+process.slimmedTausLowPtElectronCleaned)


process.pileupjetidpath = cms.Path(process.pileupJetIdUpdated+process.patJetCorrFactorsReapplyJEC+process.updatedJets)


process.main_path = cms.Path()


process.tcpNtupleMaker = cms.Path(process.TCPNtuples)


process.tcpGenNtupleMaker = cms.Path(process.tcpGenNtuples)


process.tcpTrigNtupleMaker = cms.Path(process.tcpTrigNtuples)


process.testTrigObjMaker = cms.Path(process.testTrigObj)


process.tcpPrefiringMaker = cms.Path(process.tcpPrefiring)


process.tcpMetfilterMaker = cms.Path(process.tcpMetfilter)


process.out = cms.EndPath(process.output)


process.schedule = cms.Schedule(*[ process.prefiringweightMaker, process.TauReco, process.TauRecoElectronCleaned, process.TauRecoMuonCleaned, process.TauRecoBoosted, process.TauRecoLowPtElectronCleaned, process.slimpath, process.pileupjetidpath, process.main_path, process.tcpMetfilterMaker, process.tcpTrigNtupleMaker, process.tcpGenNtupleMaker, process.tcpNtupleMaker, process.tcpPrefiringMaker, process.testTrigObjMaker ])
