##################################################
##################################################
## Configuration parameters to run MakeStack.py ##
##################################################
##################################################
from ROOT import *
doBlind = False
doSignalRegion =False
doJetCR = True

doPhoCR = False
addHiggs = False
hideData = False
addbbH = False
dyjets = False

#do pile up reweighting
doPUweight = True

year = "2017"

doSignal = False

#CSVv2 btagging working poing
# 0.5803 - loose
# 0.8838 - medium
# 0.9693 - tight

#DeepCSV btagging working poing
# 0.1522 - loose
# 0.4941 - medium
# 0.8001 - tight
BTAG = 0.4941

#Luminosity to normalize backgrounds
lumi = 41500#pb-1
MCSF = 1.0
signalFactor = 1
#List of datasets to be used (cross section information defined there)
data_file = open("datasets/MC2017.json")

#number of bins in histograms
nbin = 50
dr = "sqrt( (leadingPhoton.Eta() - subleadingPhoton.Eta())*(leadingPhoton.Eta() - subleadingPhoton.Eta()) + (leadingPhoton.Phi() - subleadingPhoton.Phi())*(leadingPhoton.Phi() - subleadingPhoton.Phi()) )"

#plots will be saved in dirName
prefix = ""
dirSuffix = "ttHMVA/"
dirPrefix = "/afs/cern.ch/work/l/lata/HHbbgg/CMSSW_9_4_6/src/flashgg/bbggTools/stackPlots/"
dirName = dirPrefix + dirSuffix

#Location of root files for each invidivual samples. Name of the root files is defined in datasets/datasets(76).json
#loc = '/eos/cms/store/group/phys_higgs/resonant_HH/RunII/FlatTrees/2016/May2_Mjj70to190_NewCatMVA'
bkgLocation = '/afs/cern.ch/work/l/lata/public/HH_bbyy/2017_LT_limts_withPU_Train10_12_18/'
#higgsLocation = loc + '/Background/Hadd/'
#bkgLocation = loc + '/Background/Hadd/'
#signalLocation = loc + '/Signal/Hadd/'
#dataLocation = loc + '/Data/Hadd/'

#plots to be made
plots = []
#plots.append(["leadingJet_mass", "leadingJet_mass", "m_{jj} [GeV]", 100, 0, 100])
#plots.append(["leadingPhoton_pt", "leadingPhoton_pt", "p_{T}(#gamma_{1}) [GeV]", 40, 30, 150])

#plots.append(["nvtx", "nvtx", "Number of vertices", 50, 0, 50])
#plots.append(["costhetastar_cs", "fabs(CosThetaStar_CS)", "|cos#theta*|_{CS}", nbin, 0, 1])
#plots.append(["costhetastar", "fabs(CosThetaStar)", "|cos#theta*|", nbin, 0, 1])
plots.append(["CMS_hgg_mass", "CMS_hgg_mass", "M(#gamma#gamma) [GeV]", nbin, 100, 180])
#plots.append(["costhetastar", "fabs(CosThetaStar)", "|cos#theta*|", nbin, 0, 1])
#plots.append(["Mjj", "Mjj", "M_{jj} (GeV)", nbin, 60, 180])
#plots.append(["leadingJet_pt", "leadingJet_pt", "p_{T}(j_{1}) [GeV]", nbin, 15, 200] )
#plots.append(["subleadingJet_pt", "subleadingJet_pt", "p_{T}(j_{2}) (GeV)", nbin, 15, 80] )
#plots.append(["leadingJet_eta", "leadingJet_eta", "#eta(j_{1})", nbin, -3, 3] )
#plots.append(["subleadingJet_eta", "subleadingJet_eta", "#eta(j_{2})", nbin,-3, 3] )
#plots.append(["leadingPhoton_eta", "leadingPhoton_eta", "#eta(#gamma_{1})", nbin, -3, 3] )
#plots.append(["MX", "MX", "#tilde{M}_{X} (GeV)", nbin, 100, 1000])
#plots.append(["subleadingPhoton_pt", "subleadingPhoton_pt", "p_{T}(#gamma_{2}) [GeV]", nbin, 30, 150])
#plots.append(["subleadingPhoton_eta", "subleadingPhoton_eta", "#eta(#gamma_{2})", nbin, -3, 3])
#plots.append(["PhoJetMinDr", "PhoJetMinDr", "#DeltaR (#gamma1,#gamma2)", nbin, 0, 5])
#plots.append(["leadingPho_MVA", "customLeadingPhotonIDMVA", "#gamma1_MVA discriminant", nbin, 0, 1])
#plots.append(["subleadingPho_MVA", "customSubLeadingPhotonIDMVA", "#gamma2_MVA discriminant", nbin, 0, 1])
#plots.append(["leadingJet_bDis", "leadingJet_bDis","DeepCSV_j1", nbin, 0, 1])
#plots.append(["subleadingJet_bDis", "subleadingJet_bDis","DeepCSV_j2", nbin, 0, 1])
#plots.append(["dijet_pt", "dijet_pt","p_{T}(j1j2)[GeV]", nbin, 20, 500])
#plots.append(["dijet_eta", "dijet_eta","#eta(j1j2)", nbin, -3, 3])
#plots.append(["diphoton_pt", "diphoton_pt","p_{T}(#gamma1#gamma2)[GeV]", nbin, 0, 250])
#plots.append(["diphoton_eta", "diphoton_eta","#eta(#gamma1#gamma2)", nbin, -3, 3])
#plots.append(["diHiggs_pt", "diHiggs_pt","p_{T}(HH)[GeV]", nbin, 20, 500])
#plots.append(["diHiggs_eta", "diHiggs_eta","#eta(HH)", nbin, -3, 3])
#plots.append(["diHiggs_mass", "diHiggs_mass","M_{HH}[GeV]", nbin, 0, 1000])
#plots.append(["HHbbggMVA", "HHbbggMVA","HHbbggMVA", nbin, 0, 1])

#plots.append(["absCosTheta_gg", "absCosTheta_gg", "| cos #theta_{#gamma#gamma} |", nbin, 0, 1])
#plots.append(["absCosTheta_bb", "absCosTheta_bb", "| cos #theta_{jj} |", nbin, 0, 1])
#plots.append(["absCosThetaStar_CS", "absCosThetaStar_CS", "| cos #theta^{CS}_{HH} |", nbin, 0, 1])

#cuts to be used to make plots
Cut =  "" 

