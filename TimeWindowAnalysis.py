# Import relevant packages
import uproot
import vector
import awkward as ak
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math
import matplotlib.colors as colors
from scipy.stats import norm

treeBIB=uproot.open("/Users/isaac/Desktop/mucolstudies/ntup_hitsBIB1[123]0.root")["tracks_tree"]

vertStartTime=norm.ppf(q=np.linspace(0,0.05,10),scale=0.03)
vertEndTime=norm.ppf(q=np.linspace(0.95,1,10),scale=0.03)
innerOuterStartTime=norm.ppf(q=np.linspace(0,0.05,10),scale=0.06)
innerOuterEndTime=norm.ppf(q=np.linspace(0.95,1,10),scale=0.06)

layerPerModule={
    1 : 8,
    2 : 8,
    3 : 3,
    4 : 7,
    5 : 3,
    6 : 4
} #dictionairy to help loop over all layers later


startTime=[]
endTime=[]
minCount=[]
for i in range(6):
    print(i)
    startTime.append([])
    endTime.append([])
    minCount.append([])
    for j in range(layerPerModule[i+1]):
        print(j)
        minimum=math.inf
        minStart=0
        minEnd=1
        inside=((treeBIB["module"].array()==(i+1)) & (treeBIB["layer"].array()==(j)))
        if i <=1:
            for startNum, start in enumerate(vertStartTime):
                countInside=np.sum((treeBIB["t"].array()[inside] >= start) & (treeBIB["t"].array()[inside] <= vertEndTime[startNum]))
                if minimum > countInside:
                    minimum=countInside
                    minStart=start
                    minEnd=vertEndTime[startNum]
        else:
            for startNum, start in enumerate(innerOuterStartTime):
                countInside=np.sum((treeBIB["t"].array()[inside] >= start) & (treeBIB["t"].array()[inside] <= innerOuterEndTime[startNum]))
                if minimum > countInside:
                    minimum=countInside
                    minStart=start
                    minEnd=innerOuterEndTime[startNum]
        
        startTime[i].append(minStart)
        endTime[i].append(minEnd)
        minCount[i].append(minimum)

startTime=[]
endTime=[]
minCount=[]
for i in range(6):
    print(i)
    startTime.append([])
    endTime.append([])
    minCount.append([])
    for j in range(layerPerModule[i+1]):
        print(j)
        minimum=math.inf
        minStart=0
        minEnd=1
        inside=((treeBIB["module"].array()==(i+1)) & (treeBIB["layer"].array()==(j)))
        countInside=treeBIB["t"].array()[inside]
        if i <=1:
            for startNum, start in enumerate(vertStartTime):
                countsKept=np.sum((countInside >= start) & (countInside <= vertEndTime[startNum]))
                if minimum > countsKept:
                    minimum=countsKept
                    minStart=start
                    minEnd=vertEndTime[startNum]
        else:
            for startNum, start in enumerate(innerOuterStartTime):
                countInside=np.sum((countInside >= start) & (countInside <= innerOuterEndTime[startNum]))
                if minimum > countsKept:
                    minimum=countsKept
                    minStart=start
                    minEnd=innerOuterEndTime[startNum]
        
        startTime[i].append(minStart)
        endTime[i].append(minEnd)
        minCount[i].append(minimum)

sumation=0
for i in minCount:
    for j in i:
        sumation+=j
print("Sumation")
print(sumation)
print("BIB reduced")
print(1-sumation/len(treeBIB["x"].array()))
print("minimum start")
print(minStart)
print("minimum end")
print(minEnd)