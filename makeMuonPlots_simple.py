from array import array
import pyLCIO
import ROOT
from ROOT import TH1D, TH2D, TFile, TLorentzVector, TTree, TMath
import glob
from optparse import OptionParser

#Boilerplate added for downloads
Bfield = 3.56  # T
parser = OptionParser()
parser.add_option('-i', '--inFile', help='--inFile Output_REC.slcio',
                  type=str, default='Output_REC.slcio')
parser.add_option('-o', '--outFile', help='--outFile ntup_tracks',
                  type=str, default='ntup_tracks')
(options, args) = parser.parse_args()

tree = TTree("tracks_tree", "tracks_tree")

#Initialize the branches for the info to be stored in
pt = array('d', [0])
pt_truth = array('d', [0])
phi = array('d', [0])
theta = array('d', [0])
d0 = array('d', [0])
z0 = array('d', [0])
z_truth = array('d', [0])
sigma_d0 = array('d', [0])
sigma_z0 = array('d', [0])
omega = array('d', [0])
chi2 = array('d', [0])
ndf = array('i', [0])
nhits = array('i', [0])
pdgID = array('i', [0])

tree.Branch("pT",  pt,  'var/D')
tree.Branch("pTtruth",  pt_truth,  'var/D')
tree.Branch("phi", phi, 'var/D')
tree.Branch("theta", theta, 'var/D')
tree.Branch("d0", d0, 'var/D')
tree.Branch("z0", z0, 'var/D')
tree.Branch("z_truth", z_truth, 'var/D')
tree.Branch("sigma_d0", sigma_d0, 'var/D')
tree.Branch("sigma_z0", sigma_z0, 'var/D')
tree.Branch("omega", omega, 'var/D')
tree.Branch("chi2", chi2, 'var/D')
tree.Branch("ndf", ndf, 'var/I')
tree.Branch("nhits", nhits, 'var/I')
tree.Branch("pdgID", pdgID, 'var/I')

# Set up some options
max_events = -1

# Gather input files
fnames = glob.glob("/data/fmeloni/DataMuC_MuColl_v1/muonGun/reco/*.slcio")

# Loop over events
i = 0
for f in fnames:
    reader = pyLCIO.IOIMPL.LCFactory.getInstance().createLCReader()
    reader.open(f)

    for event in reader:
        if max_events > 0 and i >= max_events: break

        # Get the collections we care about
        IBH= event.getCollection("IBTrackerHits")
        IBHR = event.getCollection("IBTrackerHitsRelations")
        if i%100 == 0:
            print("Processing event %i."%i)
            print("IBH:")
            print(dir(IBH))
            print("IBHR:")
            print(dir(IBHR))
        # Loop over the reconstructed objects and fill histograms
        #for pfo in pfoCollection:

        i+=1

