
from pullClass import *
from ROOT import *
import json, os
import shutil, imp
from configs import *
import resource

gStyle.SetOptStat(0)
TGaxis.SetMaxDigits(3)

helper   = imp.load_source('fix'     , 'help.py')
tdrstyle = imp.load_source('tdrstyle', 'tdrstyle.py')
CMS_lumi = imp.load_source('CMS_lumi', 'CMS_lumi.py') 

gROOT.SetBatch()
gROOT.SetStyle('Plain')
gStyle.SetOptTitle(0) 
gStyle.SetOptStat(0000) 
gStyle.SetOptFit(0111) 
gStyle.SetErrorX(0.0001);

dummyTFile = TFile("dummy.root", "RECREATE")


NiceBlue = '#51A7F9'
NiceBlueDark = '#2175E0'
NiceGreen = '#6FBF41'
NiceGreen2 = '#35DC3D'
NiceYellow = '#FBE12A'
NiceYellow2 = '#FEEA01'
NiceOrange = '#F0951A'
NiceRed = '#FA4912'
NicePurple = '#885BB2'
NicePaleYellow = '#FFFF66'
NiceMidnight = '#000080'
NiceTangerine = '#FF8000'
cNiceBlue = TColor.GetColor('#51A7F9')
cNiceBlueDark = TColor.GetColor('#2175E0')
cNiceGreen = TColor.GetColor('#6FBF41')
cNiceGreen2 = TColor.GetColor(NiceGreen2)
cNiceGreenDark = TColor.GetColor('#008040')
cNiceYellow = TColor.GetColor('#FBE12A')
cNiceYellow2 = TColor.GetColor(NiceYellow2)
cNiceOrange = TColor.GetColor('#F0951A')
cNiceRed = TColor.GetColor('#FA4912')
cNicePurple = TColor.GetColor('#885BB2')
cNicePaleYellow = TColor.GetColor('#FFFF66')
cNiceMidnight = TColor.GetColor('#000080')
cNiceTangerine = TColor.GetColor('#FF8000')

myCols = [cNicePaleYellow,kOrange,cNiceGreenDark-2, kGray+2, kMagenta+1]


datasets = json.load(data_file)

Trees = {}
#cut = '"leadingJet_bDis > 0.8"'+','+'"subleadingJet_bDis > 0.8"'
cut = "HHbbggMVA > 0.0"
print "cut=", cut

CutSignal = Cut
if doJetCR == True:
	Cut += " && leadingJet_bDis < "+ str(BTAG) + " && subleadingJet_bDis < "+ str(BTAG) + " "

leg = TLegend(0.60,0.80,0.98,0.95,'','brNDC')
leg.SetBorderSize(1)
leg.SetFillColor(0)
leg.SetTextSize(0.030)
leg.SetMargin(0.2)  
leg.SetNColumns(2)
leg.SetColumnSeparation(0.05)
leg.SetEntrySeparation(0.05)


for plot in plots:
    Histos = []

    c1=TCanvas("c1","",1000,1000)
    c1.SetLogy()
    #c1.Update()
    backgroundHists = []
    j=0
    hs=THStack("hs",";"+plot[2]+";Events;;")
    h1=TH1F("h1",";"+plot[2]+";Events;;",plot[3],plot[4],plot[5])
    print datasets["data"]
    dataName = plot[0]+"_hist"+"_data"

    for background in datasets["background"]:
        print background
        name=['GJet_Pt_20to40_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8','GJet_Pt_40toInf_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8','DiPhotonJetsBox_MGG_80toInf_13TeV_Sherpa','QCD_Pt_40toInf_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8','QCD_Pt_30to40_DoubleEMEnriched_MGG_80toInf_TuneCP5_13TeV_Pythia8']
	
        #if "QCD" in background: continue
        for i,fi in enumerate(datasets["background"][background]["files"]):
            print fi            
            thisTreeLoc = fi["file"]
            myfile = TFile.Open(bkgLocation+thisTreeLoc)
            myfile.ls()
            print "j==",j
            tree=myfile.Get("tagsDumper/trees/"+name[j]+"_13TeV_DoubleHTag_0")
            print tree
            nev = tree.GetEntries()
            #tree.Print()
            j=j+1
            #if tree.leadingJet_bDis > 0.8 and tree.subleadingJet_bDis > 0.8 and tree.HHbbggMVA > 0.4:
            if "GJets" in background:
              tree.Draw(plot[1]+">>locHist_GJets("+str(plot[3])+","+str(plot[4])+","+str(plot[5])+")","HHbbggMVA > 0.4")
              locHist_GJets.SetDirectory(0)
              #locHist_GJets.Scale(1./locHist_GJets.Integral())
              locHist_GJets.Scale(MCSF*lumi*fi["xsec"]*fi["sfactor"]/fi["weight"])
              locHist_GJets.SetLineColor(myCols[0])
              locHist_GJets.SetFillColor(myCols[0])
              #locHist_GJets.Draw("hist")
              if i==1: leg.AddEntry(locHist_GJets,datasets["background"][background]["legend"])
	      hs.Add(locHist_GJets)
            if "DiPhoJets" in background:
              tree.Draw(plot[1]+">>locHist_DiPhoJets("+str(plot[3])+","+str(plot[4])+","+str(plot[5])+")","HHbbggMVA > 0.4")
              locHist_DiPhoJets.SetDirectory(0)
              #locHist_DiPhoJets.Scale(1./locHist_DiPhoJets.Integral())
              locHist_DiPhoJets.Scale(MCSF*lumi*fi["xsec"]*fi["sfactor"]/fi["weight"])
              locHist_DiPhoJets.SetLineColor(myCols[1])
              locHist_DiPhoJets.SetFillColor(myCols[1])
              locHist_DiPhoJets.Draw("histsame")
              leg.AddEntry(locHist_DiPhoJets,datasets["background"][background]["legend"])
              hs.Add(locHist_DiPhoJets)
            if "QCD" in background:
	      tree.Draw(plot[1]+">>locHist_QCD("+str(plot[3])+","+str(plot[4])+","+str(plot[5])+")","HHbbggMVA > 0.4")
              locHist_QCD.SetDirectory(0)
              #locHist_QCD.Scale(1./locHist_QCD.Integral())
	      locHist_QCD.Scale(MCSF*lumi*fi["xsec"]*fi["sfactor"]/fi["weight"])
              locHist_QCD.SetLineColor(myCols[2])
              locHist_QCD.SetFillColor(myCols[2])
              locHist_QCD.Draw("histsame")
              if i==1: leg.AddEntry(locHist_QCD,datasets["background"][background]["legend"])             
              hs.Add(locHist_QCD)

    hs.SetMaximum(1e3)
    hs.SetMinimum(1e-2)
    #hs.Draw("hist")
    name=['Data']
    if datasets["data"] not in Trees:
        myfile = TFile.Open(bkgLocation+"Data.root")
        tree=myfile.Get("tagsDumper/trees/"+name[0]+"_13TeV_DoubleHTag_0")
        print tree
        tree.Draw(plot[1]+">>locHist_Data("+str(plot[3])+","+str(plot[4])+","+str(plot[5])+")","HHbbggMVA > 0.4")
        locHist_Data.SetDirectory(0)
        locHist_Data.SetMarkerStyle(20)
        locHist_Data.SetMarkerSize(1.0)
        locHist_Data.SetMarkerColor(1)
        locHist_Data.SetLineColor(1)
        locHist_Data.SetLineWidth(2)
        locHist_Data.SetBinErrorOption(TH1.kPoisson)
        h1 = locHist_Data.Clone("h1")
        #h1.Draw("same p e1")
        leg.AddEntry(locHist_Data,"Data", "lf")
    hs.Draw("hist")
    h1.Draw("same p e1")   
    leg.Draw()
    dummyTFile.cd()
    c1.Write()
    c1.SaveAs(plot[1]+".png")
    c1.SaveAs(plot[1]+".pdf")
    print Histos
dummyTFile.Close()
#os.system("rm dummy.root")

    



