import FWCore.ParameterSet.Config as cms
import flashgg.bbggTools.parameters as param
import flashgg.Taggers.flashggTags_cff as flashggTags
import flashgg.bbggTools.KinFitParams as KinFit
### For more information on each parameter, see parameters.py

bbggtree = cms.EDAnalyzer('bbggTree',
        benchmark=param._benchmark,
	is2016=param._is2016,
	triggerTag=param._triggerTag,
	myTriggers=param._myTriggers,
	metTag=param._metTag,
	DiPhotonTag=param._DiPhotonTag,
	JetTag=param._JetTag,
	inputTagJets= flashggTags.UnpackedJetCollectionVInputTag, #param._inputTagJets,
	GenTag=param._GenTag,
	rhoFixedGridCollection=param._rhoFixedGridCollection,
	PhotonPtOverDiPhotonMass=param._PhotonPtOverDiPhotonMass,
	PhotonEta=param._PhotonEta,
	PhotonR9=param._PhotonR9,
	PhotonElectronVeto=param._PhotonElectronVeto,
	PhotonDoElectronVeto=param._PhotonDoElectronVeto,
	PhotonDoID=param._PhotonDoID,
	PhotonDoISO=param._PhotonDoISO,
	DiPhotonPt=param._DiPhotonPt,
	DiPhotonEta=param._DiPhotonEta,
	DiPhotonMassWindow=param._DiPhotonMassWindow,
	DiPhotonOnlyFirst=param._DiPhotonOnlyFirst,
	JetPtOverDiJetMass=param._JetPtOverDiJetMass,
	JetEta=param._JetEta,
	JetBDiscriminant=param._JetBDiscriminant,
	JetDoPUID=param._JetDoPUID,
	JetDrPho=param._JetDrPho,
	n_bJets=param._n_bJets,
	DiJetPt=param._DiJetPt,
	DiJetEta=param._DiJetEta,
	DiJetMassWindow=param._DiJetMassWindow,
	CandidateMassWindow=param._CandidateMassWindow,
	CandidatePt=param._CandidatePt,
	CandidateEta=param._CandidateEta,
	bTagType=param._bTagType,
	phoIDlooseEB=param._phoIDlooseEB,
	phoIDmediumEB=param._phoIDmediumEB,
	phoIDtightEB=param._phoIDtightEB,
	phoIDlooseEE=param._phoIDlooseEE,
	phoIDmediumEE=param._phoIDmediumEE,
	phoIDtightEE=param._phoIDtightEE,
	phoISOlooseEB=param._phoISOlooseEB,
	phoISOmediumEB=param._phoISOmediumEB,
	phoISOtightEB=param._phoISOtightEB,
	phoISOlooseEE=param._phoISOlooseEE,
	phoISOmediumEE=param._phoISOmediumEE,
	phoISOtightEE=param._phoISOtightEE,
	nhCorrEB=param._nhCorrEB,
	phCorrEB=param._phCorrEB,
	nhCorrEE=param._nhCorrEE,
	phCorrEE=param._phCorrEE,
	PhotonWhichID=param._PhotonWhichID,
	PhotonWhichISO=param._PhotonWhichISO,
	JetDoID=param._JetDoID,
	doPhotonCR=param._doPhotonCR,
	ptRes=KinFit._ptRes,
	etaRes=KinFit._etaRes,
	phiRes=KinFit._phiRes,
	etaBins=KinFit._etaBins,
	DoMVAPhotonID=param._DoMVAPhotonID,
	MVAPhotonID=param._MVAPhotonID,
	PhotonMVAEstimator=param._PhotonMVAEstimator,
	doJetRegression=param._doJetRegression,
	bRegFileLeading=param._bRegFileLeading,
	bRegFileSubLeading=param._bRegFileSubLeading,
	jetSmear=param._jetSmear,
	randomLabel=param._randomLabel,
	jetScale=param._jetScale,
        doPhotonScale=param._doPhotonScale,
        doPhotonExtraScale=param._doPhotonExtraScale,
        doPhotonSmearing=param._doPhotonSmearing,
        PhotonCorrectionFile=param._PhotonCorrectionFile,
        doCustomPhotonMVA=param._doCustomPhotonMVA,
        addNonResMVA=param._addNonResMVA,
        NonResMVAWeights_LowMass=param._NonResMVAWeights_LowMass,
        NonResMVAWeights_HighMass=param._NonResMVAWeights_HighMass,
        ResMVAWeights_LowMass=param._ResMVAWeights_LowMass,
        ResMVAWeights_HighMass=param._ResMVAWeights_HighMass,
        NonResMVAVars=param._NonResMVAVars,
        addNonResMVA2017=param._addNonResMVA2017,
        NonResMVA2017Weights=param._NonResMVA2017Weights,                   
        NonResMVA2017Vars=param._NonResMVA2017Vars,
        doSigmaMdecorr=param._doSigmaMdecorr,
        sigmaMdecorr_File=param._sigmaMdecorrFile
#	doSelectionTree=param._doSelectionTree
)
