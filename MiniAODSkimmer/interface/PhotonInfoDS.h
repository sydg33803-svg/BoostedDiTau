#ifndef BoostedDiTau_MiniAODSkimmer_PhotonInfoDS_h
#define BoostedDiTau_MiniAODSkimmer_PhotonInfoDS_h

#include <vector>

class PhotonInfo {
public:
    float pt;
    float eta;
    float phi;
    float energy;

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
