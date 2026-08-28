#ifndef BoostedDiTau_MiniAODSkimmer_PhotonInfoDS_h
#define BoostedDiTau_MiniAODSkimmer_PhotonInfoDS_h

#include <vector>

class PhotonInfo {
public:
    float pt;
    float eta;
    float phi;
    float energy;

    // Raw cut-based ID variables (Fall17-94X-V2)
    float hOverE;            // single-tower H/E (hcalOverEcalBc)
    float sigmaIetaIeta;     // full5x5 sigma_iEta_iEta
    float chargedHadronIso;  // PF charged hadron isolation (uncorrected)
    float neutralHadronIso;  // PF neutral hadron isolation (uncorrected)
    float photonIso;         // PF photon isolation (uncorrected)

    // Cut-based ID decisions (1 = pass, 0 = fail, -1 = not evaluated)
    int passLooseId;
    int passMediumId;
    int passTightId;
    bool trigmatch;
    bool trigmatchMu23Ele12;
    bool trigmatchMu12Ele23;


    PhotonInfo() :
        pt(-999.), eta(-999.), phi(-999.), energy(-999.)
    {}
};

class PhotonInfoDS {
public:
    std::vector<PhotonInfo> data;

    void clear() { data.clear(); }

    void push_back(const PhotonInfo& p) { data.push_back(p); }
};

#endif
