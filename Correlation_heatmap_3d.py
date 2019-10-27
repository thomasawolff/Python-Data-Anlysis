
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


df = pd.read_csv("Random data v2 (1).csv",header=None)

def rowCorrelation():
    xData = []
    yData = []
    zData = []

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # calculates the correlation between all columns and all other columns
    for i in range(0,19):
        for e in range(0,19):
            dataFlow = dict(zip([(i,e+1)],[np.corrcoef(df[i],df[e+1])[0,1]]))
            if list(dataFlow.values())[0] < .9:
                xData.append(list(dataFlow.keys())[0][0])
                yData.append(list(dataFlow.keys())[0][1])
                zData.append(list(dataFlow.values())[0])

    ## tuple of the two columns being correlated and their correlation
    ## in the dictionary as key value pairs in 3d data structure.
    ## Ex: {(19, 17): -0.015262993060948592}

    #make histogram stuff - set bins - I choose 20x20 because I have a lot of data
    hist, xedges, yedges = np.histogram2d(xData, yData, bins=(20,20))
    xpos, ypos = np.meshgrid(xedges[:-1]+xedges[1:], yedges[:-1]+yedges[1:])
    zpos = np.array(zData).flatten()

    dx = xedges [1] - xedges [0]
    dy = yedges [1] - yedges [0]
    dz = zpos

    cmap = plt.get_cmap('jet') # Get desired colormap - you can change this!
    max_height = np.max(dz)   # get range of colorbars so we can normalize
    min_height = np.min(dz)
    # scale each z to [0,1], and get their rgb values
    rgba = [cmap((k-min_height)/max_height) for k in dz] 

    ax.bar3d(xData, yData, zpos, dx, dy, dz, color=rgba, zsort='average')
    plt.xticks([1,3,5,7,9,11,13,15,17,19])
    plt.yticks([1,3,5,7,9,11,13,15,17,19])
    plt.title("3d model of column correlations")
    plt.xlabel("X data")
    plt.ylabel("Y data")
    plt.show()

rowCorrelation()
