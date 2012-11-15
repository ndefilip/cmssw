import logging
import os.path

from Vispa.Main.Directories import pluginDirectory
from Vispa.Plugins.EdmBrowser.EventContentView import EventContentView
from Vispa.Plugins.EdmBrowser.EventContentDataAccessor import EventContentDataAccessor

from PyQt4.QtCore import QCoreApplication,Qt,SIGNAL
from PyQt4.QtGui import QDialog,QVBoxLayout,QHBoxLayout,QPushButton,QMessageBox,QFileDialog

class EventContentDialog(QDialog):
    """ This dialog allows to compare the configuration input/output with dataformats"""
    def __init__(self, parent=None, helpMessage=""):
        logging.debug(__name__ + ": __init__")
        QDialog.__init__(self, parent)
        self._helpMessage=helpMessage
        self._inputFileName=None
        self._configDataAccessor=None
        self._eventContent=None
        self.resize(800,500)
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle("Browse event content...")
        self.fill()
        self._dataAccessor = EventContentDataAccessor()
        self._eventContentView.setDataAccessor(self._dataAccessor)

    def fill(self):
        logging.debug(__name__ +': fill')
        self.setLayout(QVBoxLayout())
        self._eventContentView=EventContentView(self)
        self.layout().addWidget(self._eventContentView)

        bottom=QHBoxLayout()
        self.layout().addLayout(bottom)
        input=QPushButton("&Select input file")
        bottom.addWidget(input)
        self.connect(input, SIGNAL('clicked()'), self.selectInputFile)
        help=QPushButton("&Help")
        bottom.addWidget(help)
        self.connect(help, SIGNAL('clicked()'), self.help)
        bottom.addStretch()
        ok=QPushButton("&Ok")
        bottom.addWidget(ok)
        ok.setDefault(True)
        self.connect(ok, SIGNAL('clicked()'), self.accept)

    def setConfigDataAccessor(self, accessor):
        self._configDataAccessor=accessor
        self.updateContent()
    
    def setEventContent(self, name, branches):
        self._eventContent=(name,branches)
        self.updateContent()
    
    def updateContent(self):
        self._dataAccessor.clear()
        if self._inputFileName!=None:
            self._dataAccessor.addContentFile(self._inputFileName)
        else:
            self._dataAccessor.addBranches("RECO_3_3_0",[['CSCDetIdCSCRecHit2DsOwnedRangeMap', 'csc2DRecHits', '', 'RECO'], ['CSCDetIdCSCSegmentsOwnedRangeMap', 'cscSegments', '', 'RECO'], ['CaloTowersSorted', 'towerMaker', '', 'RECO'], ['DTChamberIdDTRecSegment4DsOwnedRangeMap', 'dt4DSegments', '', 'RECO'], ['DTLayerIdDTDigiSimLinkMuonDigiCollection', 'simMuonDTDigis', '', 'HLT'], ['DTLayerIdDTRecHit1DPairsOwnedRangeMap', 'dt1DRecHits', '', 'RECO'], ['DetIdedmEDCollection', 'siStripDigis', '', 'HLT'], ['DetIdedmEDCollection', 'siStripDigis', '', 'RECO'], ['EcalRecHitsSorted', 'reducedEcalRecHitsEB', '', 'RECO'], ['EcalRecHitsSorted', 'reducedEcalRecHitsEE', '', 'RECO'], ['EcalRecHitsSorted', 'ecalRecHit', 'EcalRecHitsEB', 'RECO'], ['EcalRecHitsSorted', 'ecalRecHit', 'EcalRecHitsEE', 'RECO'], ['EcalRecHitsSorted', 'ecalPreshowerRecHit', 'EcalRecHitsES', 'RECO'], ['GenEventInfoProduct', 'generator', '', 'HLT'], ['HBHERecHitsSorted', 'hbhereco', '', 'RECO'], ['HFRecHitsSorted', 'hfreco', '', 'RECO'], ['HORecHitsSorted', 'horeco', '', 'RECO'], ['HcalNoiseSummary', 'hcalnoise', '', 'RECO'], ['L1AcceptBunchCrossings', 'scalersRawToDigi', '', 'HLT'], ['L1AcceptBunchCrossings', 'scalersRawToDigi', '', 'RECO'], ['L1GlobalTriggerObjectMapRecord', 'hltL1GtObjectMap', '', 'HLT'], ['L1GlobalTriggerReadoutRecord', 'gtDigis', '', 'HLT'], ['L1GlobalTriggerReadoutRecord', 'gtDigis', '', 'RECO'], ['L1TriggerScalerss', 'scalersRawToDigi', '', 'HLT'], ['L1TriggerScalerss', 'scalersRawToDigi', '', 'RECO'], ['Level1TriggerScalerss', 'scalersRawToDigi', '', 'HLT'], ['Level1TriggerScalerss', 'scalersRawToDigi', '', 'RECO'], ['LumiScalerss', 'scalersRawToDigi', '', 'HLT'], ['LumiScalerss', 'scalersRawToDigi', '', 'RECO'], ['RPCDetIdRPCRecHitsOwnedRangeMap', 'rpcRecHits', '', 'RECO'], ['RPCDigiSimLinkedmDetSetVector', 'simMuonRPCDigis', 'RPCDigiSimLink', 'HLT'], ['SiPixelClusteredmNewDetSetVector', 'siPixelClusters', '', 'RECO'], ['SiStripClusteredmNewDetSetVector', 'siStripClusters', '', 'RECO'], ['SimTracks', 'g4SimHits', '', 'HLT'], ['SimVertexs', 'g4SimHits', '', 'HLT'], ['StripDigiSimLinkedmDetSetVector', 'simMuonCSCDigis', 'MuonCSCStripDigiSimLinks', 'HLT'], ['StripDigiSimLinkedmDetSetVector', 'simMuonCSCDigis', 'MuonCSCWireDigiSimLinks', 'HLT'], ['TrackingRecHitsOwned', 'ckfInOutTracksFromConversions', '', 'RECO'], ['TrackingRecHitsOwned', 'ckfOutInTracksFromConversions', '', 'RECO'], ['TrackingRecHitsOwned', 'electronGsfTracks', '', 'RECO'], ['TrackingRecHitsOwned', 'generalTracks', '', 'RECO'], ['TrackingRecHitsOwned', 'globalMuons', '', 'RECO'], ['TrackingRecHitsOwned', 'pixelTracks', '', 'RECO'], ['TrackingRecHitsOwned', 'standAloneMuons', '', 'RECO'], ['TrackingRecHitsOwned', 'tevMuons', 'default', 'RECO'], ['TrackingRecHitsOwned', 'tevMuons', 'firstHit', 'RECO'], ['TrackingRecHitsOwned', 'tevMuons', 'picky', 'RECO'], ['TrajectorySeeds', 'SETMuonSeed', '', 'RECO'], ['TrajectorySeeds', 'ancientMuonSeed', '', 'RECO'], ['booledmValueMap', 'muidAllArbitrated', '', 'RECO'], ['booledmValueMap', 'muidGMStaChiCompatibility', '', 'RECO'], ['booledmValueMap', 'muidGMTkChiCompatibility', '', 'RECO'], ['booledmValueMap', 'muidGMTkKinkTight', '', 'RECO'], ['booledmValueMap', 'muidGlobalMuonPromptTight', '', 'RECO'], ['booledmValueMap', 'muidTM2DCompatibilityLoose', '', 'RECO'], ['booledmValueMap', 'muidTM2DCompatibilityTight', '', 'RECO'], ['booledmValueMap', 'muidTMLastStationLoose', '', 'RECO'], ['booledmValueMap', 'muidTMLastStationOptimizedLowPtLoose', '', 'RECO'], ['booledmValueMap', 'muidTMLastStationOptimizedLowPtTight', '', 'RECO'], ['booledmValueMap', 'muidTMLastStationTight', '', 'RECO'], ['booledmValueMap', 'muidTMOneStationLoose', '', 'RECO'], ['booledmValueMap', 'muidTMOneStationTight', '', 'RECO'], ['booledmValueMap', 'muidTrackerMuonArbitrated', '', 'RECO'], ['booledmValueMap', 'PhotonIDProd', 'PhotonCutBasedIDLoose', 'RECO'], ['booledmValueMap', 'PhotonIDProd', 'PhotonCutBasedIDTight', 'RECO'], ['edmErrorSummaryEntrys', 'logErrorHarvester', '', 'RECO'], ['edmHepMCProduct', 'generator', '', 'HLT'], ['edmTriggerResults', 'TriggerResults', '', 'HLT'], ['edmTriggerResults', 'TriggerResults', '', 'RECO'], ['floatedmValueMap', 'eidLoose', '', 'RECO'], ['floatedmValueMap', 'eidRobustHighEnergy', '', 'RECO'], ['floatedmValueMap', 'eidRobustLoose', '', 'RECO'], ['floatedmValueMap', 'eidRobustTight', '', 'RECO'], ['floatedmValueMap', 'eidTight', '', 'RECO'], ['floatedmValueMap', 'pfElectronTranslator', 'pf', 'RECO'], ['ints', 'genParticles', '', 'HLT'], ['l1extraL1EmParticles', 'l1extraParticles', 'Isolated', 'HLT'], ['l1extraL1EmParticles', 'l1extraParticles', 'NonIsolated', 'HLT'], ['l1extraL1EmParticles', 'l1extraParticles', 'Isolated', 'RECO'], ['l1extraL1EmParticles', 'l1extraParticles', 'NonIsolated', 'RECO'], ['l1extraL1EtMissParticles', 'l1extraParticles', 'MET', 'HLT'], ['l1extraL1EtMissParticles', 'l1extraParticles', 'MHT', 'HLT'], ['l1extraL1EtMissParticles', 'l1extraParticles', 'MET', 'RECO'], ['l1extraL1EtMissParticles', 'l1extraParticles', 'MHT', 'RECO'], ['l1extraL1HFRingss', 'l1extraParticles', '', 'HLT'], ['l1extraL1HFRingss', 'l1extraParticles', '', 'RECO'], ['l1extraL1JetParticles', 'l1extraParticles', 'Central', 'HLT'], ['l1extraL1JetParticles', 'l1extraParticles', 'Forward', 'HLT'], ['l1extraL1JetParticles', 'l1extraParticles', 'Tau', 'HLT'], ['l1extraL1JetParticles', 'l1extraParticles', 'Central', 'RECO'], ['l1extraL1JetParticles', 'l1extraParticles', 'Forward', 'RECO'], ['l1extraL1JetParticles', 'l1extraParticles', 'Tau', 'RECO'], ['l1extraL1MuonParticles', 'l1extraParticles', '', 'HLT'], ['l1extraL1MuonParticles', 'l1extraParticles', '', 'RECO'], ['recoBeamSpot', 'offlineBeamSpot', '', 'RECO'], ['recoCaloClusters', 'hfEMClusters', '', 'RECO'], ['recoCaloClusters', 'hybridSuperClusters', 'hybridBarrelBasicClusters', 'RECO'], ['recoCaloClusters', 'multi5x5BasicClusters', 'multi5x5BarrelBasicClusters', 'RECO'], ['recoCaloClusters', 'multi5x5BasicClusters', 'multi5x5EndcapBasicClusters', 'RECO'], ['recoCaloClusters', 'pfElectronTranslator', 'pf', 'RECO'], ['recoCaloClustersToOnerecoClusterShapesAssociation', 'hybridSuperClusters', 'hybridShapeAssoc', 'RECO'], ['recoCaloClustersToOnerecoClusterShapesAssociation', 'multi5x5BasicClusters', 'multi5x5BarrelShapeAssoc', 'RECO'], ['recoCaloClustersToOnerecoClusterShapesAssociation', 'multi5x5BasicClusters', 'multi5x5EndcapShapeAssoc', 'RECO'], ['recoCaloJets', 'ak5CaloJets', '', 'RECO'], ['recoCaloJets', 'ak7CaloJets', '', 'RECO'], ['recoCaloJets', 'iterativeCone5CaloJets', '', 'RECO'], ['recoCaloJets', 'kt4CaloJets', '', 'RECO'], ['recoCaloJets', 'kt6CaloJets', '', 'RECO'], ['recoCaloJets', 'sisCone5CaloJets', '', 'RECO'], ['recoCaloJets', 'sisCone7CaloJets', '', 'RECO'], ['recoCaloMETs', 'corMetGlobalMuons', '', 'RECO'], ['recoCaloMETs', 'met', '', 'RECO'], ['recoCaloMETs', 'metHO', '', 'RECO'], ['recoCaloMETs', 'metNoHF', '', 'RECO'], ['recoCaloMETs', 'metNoHFHO', '', 'RECO'], ['recoCaloMETs', 'metOpt', '', 'RECO'], ['recoCaloMETs', 'metOptHO', '', 'RECO'], ['recoCaloMETs', 'metOptNoHF', '', 'RECO'], ['recoCaloMETs', 'metOptNoHFHO', '', 'RECO'], ['recoCaloMuons', 'calomuons', '', 'RECO'], ['recoCaloTauDiscriminator', 'caloRecoTauDiscriminationAgainstElectron', '', 'RECO'], ['recoCaloTauDiscriminator', 'caloRecoTauDiscriminationByIsolation', '', 'RECO'], ['recoCaloTauDiscriminator', 'caloRecoTauDiscriminationByLeadingTrackFinding', '', 'RECO'], ['recoCaloTauDiscriminator', 'caloRecoTauDiscriminationByLeadingTrackPtCut', '', 'RECO'], ['recoCaloTauTagInfos', 'caloRecoTauTagInfoProducer', '', 'RECO'], ['recoCaloTaus', 'caloRecoTauProducer', '', 'RECO'], ['recoConversions', 'conversions', '', 'RECO'], ['recoConversions', 'trackerOnlyConversions', '', 'RECO'], ['recoDeDxDataedmValueMap', 'dedxHarmonic2', '', 'RECO'], ['recoDeDxDataedmValueMap', 'dedxMedian', '', 'RECO'], ['recoDeDxDataedmValueMap', 'dedxTruncated40', '', 'RECO'], ['recoElectronSeeds', 'electronMergedSeeds', '', 'RECO'], ['recoGenJets', 'ak5GenJets', '', 'HLT'], ['recoGenJets', 'ak7GenJets', '', 'HLT'], ['recoGenJets', 'iterativeCone5GenJets', '', 'HLT'], ['recoGenJets', 'kt4GenJets', '', 'HLT'], ['recoGenJets', 'kt6GenJets', '', 'HLT'], ['recoGenJets', 'sisCone5GenJets', '', 'HLT'], ['recoGenJets', 'sisCone7GenJets', '', 'HLT'], ['recoGenMETs', 'genMetCalo', '', 'HLT'], ['recoGenMETs', 'genMetCaloAndNonPrompt', '', 'HLT'], ['recoGenMETs', 'genMetTrue', '', 'HLT'], ['recoGenParticles', 'genParticles', '', 'HLT'], ['recoGsfElectronCores', 'gsfElectronCores', '', 'RECO'], ['recoGsfElectrons', 'gsfElectrons', '', 'RECO'], ['recoGsfElectrons', 'softPFElectrons', '', 'RECO'], ['recoGsfTrackExtras', 'electronGsfTracks', '', 'RECO'], ['recoGsfTracks', 'electronGsfTracks', '', 'RECO'], ['recoHFEMClusterShapes', 'hfEMClusters', '', 'RECO'], ['recoHcalNoiseRBXs', 'hcalnoise', '', 'RECO'], ['recoIsoDepositedmValueMap', 'muIsoDepositJets', '', 'RECO'], ['recoIsoDepositedmValueMap', 'muIsoDepositTk', '', 'RECO'], ['recoIsoDepositedmValueMap', 'muIsoDepositCalByAssociatorTowers', 'ecal', 'RECO'], ['recoIsoDepositedmValueMap', 'muIsoDepositCalByAssociatorTowers', 'hcal', 'RECO'], ['recoIsoDepositedmValueMap', 'muIsoDepositCalByAssociatorTowers', 'ho', 'RECO'], ['recoJetIDedmValueMap', 'ak5JetID', '', 'RECO'], ['recoJetIDedmValueMap', 'ak7JetID', '', 'RECO'], ['recoJetIDedmValueMap', 'ic5JetID', '', 'RECO'], ['recoJetIDedmValueMap', 'kt4JetID', '', 'RECO'], ['recoJetIDedmValueMap', 'kt6JetID', '', 'RECO'], ['recoJetIDedmValueMap', 'sc5JetID', '', 'RECO'], ['recoJetIDedmValueMap', 'sc7JetID', '', 'RECO'], ['recoJetedmRefToBaseProdTofloatsAssociationVector', 'combinedSecondaryVertexBJetTags', '', 'RECO'], ['recoJetedmRefToBaseProdTofloatsAssociationVector', 'combinedSecondaryVertexMVABJetTags', '', 'RECO'], ['recoJetedmRefToBaseProdTofloatsAssociationVector', 'jetBProbabilityBJetTags', '', 'RECO'], ['recoJetedmRefToBaseProdTofloatsAssociationVector', 'jetProbabilityBJetTags', '', 'RECO'], ['recoJetedmRefToBaseProdTofloatsAssociationVector', 'simpleSecondaryVertexBJetTags', '', 'RECO'], ['recoJetedmRefToBaseProdTofloatsAssociationVector', 'softElectronByIP3dBJetTags', '', 'RECO'], ['recoJetedmRefToBaseProdTofloatsAssociationVector', 'softElectronByPtBJetTags', '', 'RECO'], ['recoJetedmRefToBaseProdTofloatsAssociationVector', 'softMuonBJetTags', '', 'RECO'], ['recoJetedmRefToBaseProdTofloatsAssociationVector', 'softMuonByIP3dBJetTags', '', 'RECO'], ['recoJetedmRefToBaseProdTofloatsAssociationVector', 'softMuonByPtBJetTags', '', 'RECO'], ['recoJetedmRefToBaseProdTofloatsAssociationVector', 'trackCountingHighEffBJetTags', '', 'RECO'], ['recoJetedmRefToBaseProdTofloatsAssociationVector', 'trackCountingHighPurBJetTags', '', 'RECO'], ['recoJetedmRefToBaseProdTorecoJetExtendedAssociationJetExtendedDatasAssociationVector', 'ak5JetExtender', '', 'RECO'], ['recoJetedmRefToBaseProdTorecoJetExtendedAssociationJetExtendedDatasAssociationVector', 'ak7JetExtender', '', 'RECO'], ['recoJetedmRefToBaseProdTorecoJetExtendedAssociationJetExtendedDatasAssociationVector', 'iterativeCone5JetExtender', '', 'RECO'], ['recoJetedmRefToBaseProdTorecoJetExtendedAssociationJetExtendedDatasAssociationVector', 'kt4JetExtender', '', 'RECO'], ['recoJetedmRefToBaseProdTorecoJetExtendedAssociationJetExtendedDatasAssociationVector', 'sisCone5JetExtender', '', 'RECO'], ['recoJetedmRefToBaseProdrecoTracksrecoTrackrecoTracksTorecoTrackedmrefhelperFindUsingAdvanceedmRefVectorsAssociationVector', 'ak5JetTracksAssociatorAtCaloFace', '', 'RECO'], ['recoJetedmRefToBaseProdrecoTracksrecoTrackrecoTracksTorecoTrackedmrefhelperFindUsingAdvanceedmRefVectorsAssociationVector', 'ak5JetTracksAssociatorAtVertex', '', 'RECO'], ['recoJetedmRefToBaseProdrecoTracksrecoTrackrecoTracksTorecoTrackedmrefhelperFindUsingAdvanceedmRefVectorsAssociationVector', 'ak7JetTracksAssociatorAtCaloFace', '', 'RECO'], ['recoJetedmRefToBaseProdrecoTracksrecoTrackrecoTracksTorecoTrackedmrefhelperFindUsingAdvanceedmRefVectorsAssociationVector', 'ak7JetTracksAssociatorAtVertex', '', 'RECO'], ['recoJetedmRefToBaseProdrecoTracksrecoTrackrecoTracksTorecoTrackedmrefhelperFindUsingAdvanceedmRefVectorsAssociationVector', 'ic5JetTracksAssociatorAtVertex', '', 'RECO'], ['recoJetedmRefToBaseProdrecoTracksrecoTrackrecoTracksTorecoTrackedmrefhelperFindUsingAdvanceedmRefVectorsAssociationVector', 'iterativeCone5JetTracksAssociatorAtCaloFace', '', 'RECO'], ['recoJetedmRefToBaseProdrecoTracksrecoTrackrecoTracksTorecoTrackedmrefhelperFindUsingAdvanceedmRefVectorsAssociationVector', 'iterativeCone5JetTracksAssociatorAtVertex', '', 'RECO'], ['recoJetedmRefToBaseProdrecoTracksrecoTrackrecoTracksTorecoTrackedmrefhelperFindUsingAdvanceedmRefVectorsAssociationVector', 'kt4JetTracksAssociatorAtCaloFace', '', 'RECO'], ['recoJetedmRefToBaseProdrecoTracksrecoTrackrecoTracksTorecoTrackedmrefhelperFindUsingAdvanceedmRefVectorsAssociationVector', 'kt4JetTracksAssociatorAtVertex', '', 'RECO'], ['recoJetedmRefToBaseProdrecoTracksrecoTrackrecoTracksTorecoTrackedmrefhelperFindUsingAdvanceedmRefVectorsAssociationVector', 'sisCone5JetTracksAssociatorAtCaloFace', '', 'RECO'], ['recoJetedmRefToBaseProdrecoTracksrecoTrackrecoTracksTorecoTrackedmrefhelperFindUsingAdvanceedmRefVectorsAssociationVector', 'sisCone5JetTracksAssociatorAtVertex', '', 'RECO'], ['recoMETs', 'genMetIC5GenJets', '', 'HLT'], ['recoMETs', 'htMetIC5', '', 'RECO'], ['recoMETs', 'htMetKT4', '', 'RECO'], ['recoMETs', 'htMetKT6', '', 'RECO'], ['recoMETs', 'htMetSC5', '', 'RECO'], ['recoMETs', 'htMetSC7', '', 'RECO'], ['recoMETs', 'tcMet', '', 'RECO'], ['recoMuonMETCorrectionDataedmValueMap', 'muonMETValueMapProducer', 'muCorrData', 'RECO'], ['recoMuonMETCorrectionDataedmValueMap', 'muonTCMETValueMapProducer', 'muCorrData', 'RECO'], ['recoMuonTimeExtraedmValueMap', 'muons', 'combined', 'RECO'], ['recoMuonTimeExtraedmValueMap', 'muons', 'csc', 'RECO'], ['recoMuonTimeExtraedmValueMap', 'muons', 'dt', 'RECO'], ['recoMuons', 'muons', '', 'RECO'], ['recoPFBlocks', 'particleFlowBlock', '', 'RECO'], ['recoPFCandidates', 'particleFlow', '', 'RECO'], ['recoPFCandidates', 'particleFlow', 'electrons', 'RECO'], ['recoPFClusters', 'particleFlowClusterECAL', '', 'RECO'], ['recoPFClusters', 'particleFlowClusterHCAL', '', 'RECO'], ['recoPFClusters', 'particleFlowClusterHFEM', '', 'RECO'], ['recoPFClusters', 'particleFlowClusterHFHAD', '', 'RECO'], ['recoPFClusters', 'particleFlowClusterPS', '', 'RECO'], ['recoPFJets', 'ak5PFJets', '', 'RECO'], ['recoPFJets', 'ak7PFJets', '', 'RECO'], ['recoPFJets', 'iterativeCone5PFJets', '', 'RECO'], ['recoPFJets', 'kt4PFJets', '', 'RECO'], ['recoPFJets', 'kt6PFJets', '', 'RECO'], ['recoPFJets', 'sisCone5PFJets', '', 'RECO'], ['recoPFJets', 'sisCone7PFJets', '', 'RECO'], ['recoPFMETs', 'pfMet', '', 'RECO'], ['recoPFTauDiscriminator', 'fixedConeHighEffPFTauDiscriminationAgainstElectron', '', 'RECO'], ['recoPFTauDiscriminator', 'fixedConeHighEffPFTauDiscriminationAgainstMuon', '', 'RECO'], ['recoPFTauDiscriminator', 'fixedConeHighEffPFTauDiscriminationByECALIsolation', '', 'RECO'], ['recoPFTauDiscriminator', 'fixedConeHighEffPFTauDiscriminationByECALIsolationUsingLeadingPion', '', 'RECO'], ['recoPFTauDiscriminator', 'fixedConeHighEffPFTauDiscriminationByIsolation', '', 'RECO'], ['recoPFTauDiscriminator', 'fixedConeHighEffPFTauDiscriminationByIsolationUsingLeadingPion', '', 'RECO'], ['recoPFTauDiscriminator', 'fixedConeHighEffPFTauDiscriminationByLeadingPionPtCut', '', 'RECO'], ['recoPFTauDiscriminator', 'fixedConeHighEffPFTauDiscriminationByLeadingTrackFinding', '', 'RECO'], ['recoPFTauDiscriminator', 'fixedConeHighEffPFTauDiscriminationByLeadingTrackPtCut', '', 'RECO'], ['recoPFTauDiscriminator', 'fixedConeHighEffPFTauDiscriminationByTrackIsolation', '', 'RECO'], ['recoPFTauDiscriminator', 'fixedConeHighEffPFTauDiscriminationByTrackIsolationUsingLeadingPion', '', 'RECO'], ['recoPFTauDiscriminator', 'fixedConePFTauDiscriminationAgainstElectron', '', 'RECO'], ['recoPFTauDiscriminator', 'fixedConePFTauDiscriminationAgainstMuon', '', 'RECO'], ['recoPFTauDiscriminator', 'fixedConePFTauDiscriminationByECALIsolation', '', 'RECO'], ['recoPFTauDiscriminator', 'fixedConePFTauDiscriminationByECALIsolationUsingLeadingPion', '', 'RECO'], ['recoPFTauDiscriminator', 'fixedConePFTauDiscriminationByIsolation', '', 'RECO'], ['recoPFTauDiscriminator', 'fixedConePFTauDiscriminationByIsolationUsingLeadingPion', '', 'RECO'], ['recoPFTauDiscriminator', 'fixedConePFTauDiscriminationByLeadingPionPtCut', '', 'RECO'], ['recoPFTauDiscriminator', 'fixedConePFTauDiscriminationByLeadingTrackFinding', '', 'RECO'], ['recoPFTauDiscriminator', 'fixedConePFTauDiscriminationByLeadingTrackPtCut', '', 'RECO'], ['recoPFTauDiscriminator', 'fixedConePFTauDiscriminationByTrackIsolation', '', 'RECO'], ['recoPFTauDiscriminator', 'fixedConePFTauDiscriminationByTrackIsolationUsingLeadingPion', '', 'RECO'], ['recoPFTauDiscriminator', 'shrinkingConePFTauDecayModeIndexProducer', '', 'RECO'], ['recoPFTauDiscriminator', 'shrinkingConePFTauDiscriminationAgainstElectron', '', 'RECO'], ['recoPFTauDiscriminator', 'shrinkingConePFTauDiscriminationAgainstMuon', '', 'RECO'], ['recoPFTauDiscriminator', 'shrinkingConePFTauDiscriminationByECALIsolation', '', 'RECO'], ['recoPFTauDiscriminator', 'shrinkingConePFTauDiscriminationByECALIsolationUsingLeadingPion', '', 'RECO'], ['recoPFTauDiscriminator', 'shrinkingConePFTauDiscriminationByIsolation', '', 'RECO'], ['recoPFTauDiscriminator', 'shrinkingConePFTauDiscriminationByIsolationUsingLeadingPion', '', 'RECO'], ['recoPFTauDiscriminator', 'shrinkingConePFTauDiscriminationByLeadingPionPtCut', '', 'RECO'], ['recoPFTauDiscriminator', 'shrinkingConePFTauDiscriminationByLeadingTrackFinding', '', 'RECO'], ['recoPFTauDiscriminator', 'shrinkingConePFTauDiscriminationByLeadingTrackPtCut', '', 'RECO'], ['recoPFTauDiscriminator', 'shrinkingConePFTauDiscriminationByTaNC', '', 'RECO'], ['recoPFTauDiscriminator', 'shrinkingConePFTauDiscriminationByTaNCfrHalfPercent', '', 'RECO'], ['recoPFTauDiscriminator', 'shrinkingConePFTauDiscriminationByTaNCfrOnePercent', '', 'RECO'], ['recoPFTauDiscriminator', 'shrinkingConePFTauDiscriminationByTaNCfrQuarterPercent', '', 'RECO'], ['recoPFTauDiscriminator', 'shrinkingConePFTauDiscriminationByTaNCfrTenthPercent', '', 'RECO'], ['recoPFTauDiscriminator', 'shrinkingConePFTauDiscriminationByTrackIsolation', '', 'RECO'], ['recoPFTauDiscriminator', 'shrinkingConePFTauDiscriminationByTrackIsolationUsingLeadingPion', '', 'RECO'], ['recoPFTauTagInfos', 'pfRecoTauTagInfoProducer', '', 'RECO'], ['recoPFTaus', 'fixedConeHighEffPFTauProducer', '', 'RECO'], ['recoPFTaus', 'fixedConePFTauProducer', '', 'RECO'], ['recoPFTaus', 'shrinkingConePFTauProducer', '', 'RECO'], ['recoPhotonCores', 'photonCore', '', 'RECO'], ['recoPhotons', 'photons', '', 'RECO'], ['recoPreshowerClusterShapes', 'multi5x5PreshowerClusterShape', 'multi5x5PreshowerXClustersShape', 'RECO'], ['recoPreshowerClusterShapes', 'multi5x5PreshowerClusterShape', 'multi5x5PreshowerYClustersShape', 'RECO'], ['recoPreshowerClusters', 'pfElectronTranslator', 'pf', 'RECO'], ['recoPreshowerClusters', 'multi5x5SuperClustersWithPreshower', 'preshowerXClusters', 'RECO'], ['recoPreshowerClusters', 'multi5x5SuperClustersWithPreshower', 'preshowerYClusters', 'RECO'], ['recoRecoEcalCandidates', 'hfRecoEcalCandidate', '', 'RECO'], ['recoSecondaryVertexTagInfos', 'secondaryVertexTagInfos', '', 'RECO'], ['recoSoftLeptonTagInfos', 'softElectronTagInfos', '', 'RECO'], ['recoSoftLeptonTagInfos', 'softMuonTagInfos', '', 'RECO'], ['recoSuperClusters', 'correctedHybridSuperClusters', '', 'RECO'], ['recoSuperClusters', 'correctedMulti5x5SuperClustersWithPreshower', '', 'RECO'], ['recoSuperClusters', 'hfEMClusters', '', 'RECO'], ['recoSuperClusters', 'hybridSuperClusters', '', 'RECO'], ['recoSuperClusters', 'multi5x5SuperClustersWithPreshower', '', 'RECO'], ['recoSuperClusters', 'multi5x5SuperClusters', 'multi5x5EndcapSuperClusters', 'RECO'], ['recoSuperClusters', 'pfElectronTranslator', 'pf', 'RECO'], ['recoSuperClustersToOnerecoHFEMClusterShapesAssociation', 'hfEMClusters', '', 'RECO'], ['recoSuperClustersrecoSuperClusterrecoSuperClustersrecoSuperClusteredmrefhelperFindUsingAdvanceedmRefedmValueMap', 'pfElectronTranslator', 'pf', 'RECO'], ['recoTrackExtras', 'ckfInOutTracksFromConversions', '', 'RECO'], ['recoTrackExtras', 'ckfOutInTracksFromConversions', '', 'RECO'], ['recoTrackExtras', 'electronGsfTracks', '', 'RECO'], ['recoTrackExtras', 'generalTracks', '', 'RECO'], ['recoTrackExtras', 'globalMuons', '', 'RECO'], ['recoTrackExtras', 'globalSETMuons', '', 'RECO'], ['recoTrackExtras', 'pixelTracks', '', 'RECO'], ['recoTrackExtras', 'standAloneMuons', '', 'RECO'], ['recoTrackExtras', 'standAloneSETMuons', '', 'RECO'], ['recoTrackExtras', 'tevMuons', 'default', 'RECO'], ['recoTrackExtras', 'tevMuons', 'firstHit', 'RECO'], ['recoTrackExtras', 'tevMuons', 'picky', 'RECO'], ['recoTrackIPTagInfos', 'impactParameterTagInfos', '', 'RECO'], ['recoTracks', 'ckfInOutTracksFromConversions', '', 'RECO'], ['recoTracks', 'ckfOutInTracksFromConversions', '', 'RECO'], ['recoTracks', 'generalTracks', '', 'RECO'], ['recoTracks', 'globalMuons', '', 'RECO'], ['recoTracks', 'globalSETMuons', '', 'RECO'], ['recoTracks', 'pixelTracks', '', 'RECO'], ['recoTracks', 'standAloneMuons', '', 'RECO'], ['recoTracks', 'standAloneSETMuons', '', 'RECO'], ['recoTracks', 'standAloneMuons', 'UpdatedAtVtx', 'RECO'], ['recoTracks', 'standAloneSETMuons', 'UpdatedAtVtx', 'RECO'], ['recoTracks', 'tevMuons', 'default', 'RECO'], ['recoTracks', 'tevMuons', 'firstHit', 'RECO'], ['recoTracks', 'impactParameterTagInfos', 'ghostTracks', 'RECO'], ['recoTracks', 'tevMuons', 'picky', 'RECO'], ['recoTracksToOnerecoTracksAssociation', 'tevMuons', 'default', 'RECO'], ['recoTracksToOnerecoTracksAssociation', 'tevMuons', 'firstHit', 'RECO'], ['recoTracksToOnerecoTracksAssociation', 'tevMuons', 'picky', 'RECO'], ['recoVertexCompositeCandidates', 'generalV0Candidates', 'Kshort', 'RECO'], ['recoVertexCompositeCandidates', 'generalV0Candidates', 'Lambda', 'RECO'], ['recoVertexs', 'offlinePrimaryVertices', '', 'RECO'], ['recoVertexs', 'offlinePrimaryVerticesWithBS', '', 'RECO'], ['recoVertexs', 'pixelVertices', '', 'RECO'], ['triggerTriggerEvent', 'hltTriggerSummaryAOD', '', 'HLT']])
        if self._configDataAccessor:
            self._dataAccessor.addConfig(self._configDataAccessor)
        if self._eventContent:
            self._dataAccessor.addBranches(self._eventContent[0],self._eventContent[1])
        self._eventContentView.updateContent()
    
    def selectInputFile(self):
        filename = str(QFileDialog.getOpenFileName(self,
                                               'Select input file',
                                               QCoreApplication.instance().getLastOpenLocation(),
                                               "Dataformat file / EDM root file (*.txt *.root)"))
        if filename!="":
            self._inputFileName=filename
            self.updateContent()

    def help(self):
        QMessageBox.about(self, 'Info', self._helpMessage)
        