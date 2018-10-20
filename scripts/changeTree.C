{
TFile *f = new TFile("output_bbHToGG_M-125_4FS_ybyt_13TeV_amcatnlo.root","UPDATE"); 
TTree *t; f->GetObject("tagsDumper/trees/GJets_HT_200To400_TuneCP5_13TeV_madgraphMLM_pythia8_13TeV_DoubleHTag_0",t); 
if (t) {

    t->SetName("bbggtrees");
    t->SetTitle("bbggtrees"); 
    f->Write(); 
 }
}
