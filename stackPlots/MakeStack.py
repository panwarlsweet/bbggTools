from pullClass import *
from ROOT import *
import json, os
import shutil, imp
from configs import *
import resource
import numpy as np

gStyle.SetOptStat(0)
TGaxis.SetMaxDigits(4)
CMS_lumi = imp.load_source('CMS_lumi', 'CMS_lumi.py') 

gROOT.SetBatch()
gROOT.SetStyle('Plain')
gStyle.SetOptTitle(0) 
gStyle.SetOptStat(0000) 
gStyle.SetOptFit(0111) 
gStyle.SetErrorX(0.0001);

def FULLGRAPH(h_err):
    Yval=[]
    errorU=[]
    errorD=[]
    Xval=[]
    XerrorU=[]
    XerrorD=[]
    gr=TGraphAsymmErrors()
    n1 = h_err.GetNbinsX()
    print "n1==", n1
    for i in range(0,n1):
      Yval.append(h_err.GetBinContent(i+1))
      errorU.append(h_err.GetBinError(i+1))
      errorD.append(h_err.GetBinError(i+1))
      Xval.append(h_err.GetBinCenter(i+1))
      XerrorU.append(h_err.GetBinWidth(i+1)/2.)
      XerrorD.append(h_err.GetBinWidth(i+1)/2.)      

    gr = TGraphAsymmErrors(n1, np.array(Xval), np.array(Yval), np.array(XerrorD), np.array(XerrorU), np.array(errorD), np.array(errorU))
    gr.SetFillColor(2);
    gr.SetFillStyle(3001);
    return gr
    
dummyTFile = TFile("dummy.root", "RECREATE")

CMS_lumi.lumi_13TeV = ""
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Preliminary"

cNicePaleYellow = TColor.GetColor('#FFFF66')
cNiceGreenDark = TColor.GetColor('#008040')

myCols = [cNicePaleYellow+2,kOrange,cNiceGreenDark-2, kGray+2, kMagenta+1]
BTAG=0.4941
phoMVA=[0.28,0.47,0.9]

datasets = json.load(data_file)


Trees = {}
Cut = "HHbbggMVA > 0.0 "

CutSignal = Cut
if doBlind == True: ### blinding hgg mass window
           Cut += "&& !((CMS_hgg_mass > 115 && CMS_hgg_mass < 135))"
if doSignalRegion == True:
 	Cut += " && leadingJet_DeepCSV > "+ str(BTAG) + " && subleadingJet_DeepCSV > "+ str(BTAG) + ""
if doJetCR == True:  ### jet control region
        Cut += " && leadingJet_DeepCSV < "+ str(BTAG) + " && subleadingJet_DeepCSV < "+ str(BTAG) + ""
if doPhoCR == True:  ### photon control region
	Cut += " && customLeadingPhotonIDMVA < "+ str(phoMVA[2])+ " && customSubLeadingPhotonIDMVA < "+ str(phoMVA[2]) + ""

leg = TLegend(0.50,0.85,0.85,0.69,'','brNDC')
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetTextSize(0.030)
leg.SetMargin(0.2)  
leg.SetNColumns(2)
leg.SetColumnSeparation(0.05)
leg.SetEntrySeparation(0.05)
weightedcut = ""
#weightedcut = "( 1 )*"
Cut_ = TCut(Cut)
cut_data = Cut_
if (doPUweight):
	weightedcut += "( puweight )*("+Cut+")"
cut = TCut(weightedcut)
for plot in plots:

    c1=TCanvas("c1","",800,800)
    c1.cd()
    #pad1 = TPad("pad1", "pad1", 0.001256281,0.09055627,0.9987437,0.9611902)
    pad1 = TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
    pad1.Draw()
    pad1.SetBottomMargin(0.0) # joins upper and lower plot
    pad1.cd()
    #pad1.Range(-136.5777,-1.859872,1113.03,3.749023)
    pad1.SetFillColor(0)
    pad1.SetBorderMode(0)
    pad1.SetBorderSize(2)
    pad1.SetTopMargin(0.100236246)
    pad1.SetFrameBorderMode(0)
    pad1.Draw()
    
    backgroundHists = []
    j=0
    hs=THStack("hs",";"+plot[2]+";Events;;")
    h1=TH1F("h1",";"+plot[2]+";Events;;",plot[3],plot[4],plot[5])
    h2=TH1F("h2",";"+plot[2]+";Events;;",plot[3],plot[4],plot[5])
    h_err=TH1F("h_err","",plot[3],plot[4],plot[5])
    h1.SetLabelSize(0.003, "Y")
    Hist=[]
    print "cut=", cut
    for background in datasets["background"]:
        print background
        name=['GJet_Pt_20to40_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8','GJet_Pt_40toInf_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8','DiPhotonJetsBox_MGG_80toInf_13TeV_Sherpa','QCD_Pt_40toInf_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8','QCD_Pt_30to40_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8']
	
        if "QCD" in background: continue
        for i,fi in enumerate(datasets["background"][background]["files"]):
            print fi            
            thisTreeLoc = fi["file"]
            myfile = TFile.Open(bkgLocation+thisTreeLoc)
            tree=myfile.Get("tagsDumper/trees/"+name[j]+"_13TeV_DoubleHTag_0")
            nev = tree.GetEntries()
            j=j+1

            if "GJets" in background:
              tree.Draw(plot[1]+">>locHist_GJets("+str(plot[3])+","+str(plot[4])+","+str(plot[5])+")",cut)
              locHist_GJets.SetDirectory(0)
              #locHist_GJets.Scale(1./locHist_GJets.Integral())
              locHist_GJets.Scale(MCSF*lumi*fi["xsec"]*fi["sfactor"]/fi["weight"])
              locHist_GJets.SetLineColor(myCols[0])
              locHist_GJets.SetFillColor(myCols[0])
              if i!=0 : Hist.append(locHist_GJets)
              if i==0 : Hist.append(locHist_GJets)
              if i==1: leg.AddEntry(locHist_GJets,datasets["background"][background]["legend"])
	      hs.Add(locHist_GJets)

            if "DiPhoJets" in background:
              tree.Draw(plot[1]+">>locHist_DiPhoJets("+str(plot[3])+","+str(plot[4])+","+str(plot[5])+")",cut)
              locHist_DiPhoJets.SetDirectory(0)
              #locHist_DiPhoJets.Scale(1./locHist_DiPhoJets.Integral())
              locHist_DiPhoJets.Scale(MCSF*lumi*fi["xsec"]*fi["sfactor"]/fi["weight"])
              locHist_DiPhoJets.SetLineColor(myCols[1])
              locHist_DiPhoJets.SetFillColor(myCols[1])
              Hist.append(locHist_DiPhoJets)
              leg.AddEntry(locHist_DiPhoJets,datasets["background"][background]["legend"])
              hs.Add(locHist_DiPhoJets)

##### stacking the signal ########
    """for signal in datasets["signal"]:
        print signal
        name=['GluGluToHHTo2B2G_node_SM_13TeV_madgraph']
        for i,fi in enumerate(datasets["signal"][signal]["files"]):
            thisTreeLoc = fi["file"]
            myfile = TFile.Open(bkgLocation+thisTreeLoc)
            tree=myfile.Get("tagsDumper/trees/"+name[0]+"_13TeV_DoubleHTag_0")
            if "nrSM" in signal:
              tree.Draw(plot[1]+">>locHist_nrSM("+str(plot[3])+","+str(plot[4])+","+str(plot[5])+")",cut)
              locHist_nrSM.SetDirectory(0)
              #leg.AddEntry(locHist_nrSM,datasets["signal"][signal]["legend"])
              #hs.Add(locHist_nrSM)
	      h1 = locHist_nrSM.Clone("h1")
	      h1.Scale(lumi*fi["xsec"]*fi["sfactor"]/fi["weight"])
              h1.SetLineColor(kRed)
              h1.SetLineWidth(5)
              leg.AddEntry(h1,datasets["signal"][signal]["legend"])"""

    if plot[1]=="CMS_hgg_mass" or plot[1]=="diHiggs_mass" or plot[1]=="Mjj":
	    hs.SetMaximum(30000)
    elif plot[1]=="MX":
        hs.SetMaximum(50000)
    elif plot[1]=="absCosThetaStar_CS":
        hs.SetMaximum(40000)
    elif plot[1]=="absCosTheta_bb":
        hs.SetMaximum(20000)
#    hs.SetMaximum(800)
    hs.SetMinimum(1)
####### Stacking the Data #########
    name=['Data']
    if datasets["data"] not in Trees:
        myfile = TFile.Open(bkgLocation+"Data.root")
        tree=myfile.Get("tagsDumper/trees/"+name[0]+"_13TeV_DoubleHTag_0")
        print tree 
        tree=myfile.Get("tagsDumper/trees/"+name[0]+"_13TeV_DoubleHTag_0")
        tree.Draw(plot[1]+">>locHist_Data("+str(plot[3])+","+str(plot[4])+","+str(plot[5])+")",cut_data)
        h2 = locHist_Data.Clone("h2")
        locHist_Data.SetDirectory(0)
        h2.SetMarkerStyle(20)
        h2.SetMarkerSize(1.0)
        h2.SetMarkerColor(1)
        h2.SetLineColor(1)
        h2.SetLineWidth(2)
        h2.SetBinErrorOption(TH1.kPoisson)
        leg.AddEntry(h2,"Data", "lpf")

    h_err.Add(Hist[0])
    h_err.Add(Hist[1]) 
    h_err.Add(Hist[2])   
    hs.Draw("hist")  #### Stak MC

    h2.SetLineColor(kBlack)
    h2.Draw("same p e1") ### Draw Data

    UncBand_ = TGraphAsymmErrors()
    UncBand_ = FULLGRAPH(h_err) 
    UncBand_.SetFillColor(1)
    #UncBand_.SetFillStyle(3001)
    UncBand_.Draw("E2 same")   ###### stat. unc.

    leg.AddEntry(UncBand_,"Stat. Unc.","lpf");
    leg.Draw("same")
    
    
    c1.cd()
    pad2 = TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
    pad2.Draw()
    pad2.SetBorderMode(0)
    pad2.SetBorderSize(2)
    pad2.SetGridy()
    pad2.SetTopMargin(0.0)
    pad2.SetBottomMargin(0.3)
    #pad2.SetGridx()
    pad2.Draw()

    h3= TH1F()
    h4 = hs.GetStack().Last().Clone("h4") 
    h3=h2.Clone("h3")
    h3.SetLineColor(kBlack)
    h3.SetLineWidth(2)
    h3.SetMinimum(0.0)
    h3.SetMaximum(2.0)
    h3.Divide(h4)
    
    y = h3.GetYaxis()
    y.SetTitle("#bf{Data/MC}")
    y.SetNdivisions(505)
    y.SetTitleSize(20)
    y.SetTitleFont(43)
    y.SetTitleOffset(1.55)
    y.SetLabelFont(62)
    y.SetLabelSize(0.1)
 
    # Adjust x-axis settings
    x = h3.GetXaxis()
    x.SetTitle("#bf{"+plot[2]+"}")
    x.SetTitleSize(25)
    x.SetTitleFont(43)
    x.SetTitleOffset(4.0)
    x.SetLabelFont(62)
    x.SetLabelSize(0.12)

    h3.SetMarkerStyle(8)
    pad2.cd()  
    
    h3.Draw("LPE1")
    Unc_=FULLGRAPH(h3)
    Unc_.SetFillColor(1)
    Unc_.Draw("E2 same")   ###### stat. unc.



    iPos = 32
    if( iPos==0 ): CMS_lumi.relPosX = 0.13

    CMS_lumi.CMS_lumi(c1, 1, iPos)
    dummyTFile.cd()
    hs.Write()
    h2.Write()
    h_err.Write()
    UncBand_.Write()
    c1.Write()
    c1.SaveAs(plot[1]+".png")
    c1.SaveAs(plot[1]+".pdf")
    c1.SaveAs(plot[1]+".ps")
    c1.SaveAs(plot[1]+".C")
    c1.SaveAs(plot[1]+".root")

dummyTFile.Close()
#os.system("rm dummy.root")

    



