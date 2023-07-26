#Imports are meant to be run on snowmass21 server
from array import array
from pyLCIO import IOIMPL, EVENT, UTIL
import ROOT
from ROOT import TH1D, TH2D, TFile, TLorentzVector, TTree, TMath
import glob
from optparse import OptionParser

fnames = "/data/fmeloni/DataMuC_MuColl_v1/muonGun/reco/muonGun_reco_660.slcio"

reader = IOIMPL.LCFactory.getInstance().createLCReader()
reader.open(f)

i = 0
print("Reader")
print(dir(reader))
print("")
for event in reader:
    if i ==0:
        print("event")
        print(dir(event))
        print("")
        print("Collection")
        print(dir(event.getCollection("VBTrackerHits")))
        j=0
        for hit in event.getCollection("VBTrackerHits"):
            if j==0:
                print("Hit")
                print(dir(hit))
                print("")
                j+=1
    i+=1