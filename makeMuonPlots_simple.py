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
parser.add_option('-o', '--outFile', help='--outFile ntup_tracks.root',
                  type=str, default='ntup_tracks.root')
(options, args) = parser.parse_args()

tree = TTree("tracks_tree", "tracks_tree")

#Initialize the branches for the info to be stored in
x_pos = array('d', [0])
y_pos = array('d', [0])
z_pos = array('d', [0])
time = array ('d', [0])

tree.Branch("x",  x_pos,  'var/D')
tree.Branch("y",  y_pos,  'var/D')
tree.Branch("z", z_pos, 'var/D')
tree.Branch("t", time, 'var/D')

print(tree)
# Set up some options
max_events = -1

# Gather input files
fnames = glob.glob("/data/fmeloni/DataMuC_MuColl_v1/muonGun/recoBIB/*100.slcio")

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
        tracks=event.getCollection("SiTracks")
        if i % 100==0:
            print("processing",i)
        for track in tracks:
            hits=track.getTrackerHits()
            for hit in hits:
                t=hit.getTime()
                typ=hit.getType()
                posV=hit.getPositionVec()
                x=posV.X()
                y=posV.Y()
                z=posV.Z()
                x_pos[0]=x
                y_pos[0]=y
                z_pos[0]=z
                time[0]=t
                tree.Fill()
        # Loop over the reconstructed objects and fill histograms
        #for pfo in pfoCollection:

        i+=1
output_file = TFile(options.outFile, 'RECREATE')
tree.Write()
