'''This code uses the dataset that we used in the first week of the course Analytics Methods. 
We were tasked with finding correlations between columns  on the downloaded dataset'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Reading the csv file into the code using pandas read_csv()
df = pd.read_csv("Random data v2 (1).csv",header=None)

def rowCorrelation():
    # initializing list data structures
    xData = []
    yData = []
    zData = []
    
    # Creating the figure area for the plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # calculates the correlation between all columns and all other columns
    # I stopped the comparison between the columns at 19. Otherwise the plot
    # became very crowded
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
    
    hist, xedges, yedges = np.histogram2d(xData, yData, bins=(20,20))
    xpos, ypos = np.meshgrid(xedges[:-1]+xedges[1:], yedges[:-1]+yedges[1:])
    zpos = np.array(zData).flatten()

    dx = xedges [1] - xedges [0]
    dy = yedges [1] - yedges [0]
    dz = zpos

    cmap = plt.get_cmap('jet') 
    max_height = np.max(dz)  
    min_height = np.min(dz)
    rgba = [cmap((k-min_height)/max_height) for k in dz] 

    ax.bar3d(xData, yData, zpos, dx, dy, dz, color=rgba, zsort='average')
    plt.xticks([1,3,5,7,9,11,13,15,17,19])
    plt.yticks([1,3,5,7,9,11,13,15,17,19])
    plt.title("3d model of column correlations")
    plt.xlabel("X data")
    plt.ylabel("Y data")
    plt.show()

rowCorrelation()
