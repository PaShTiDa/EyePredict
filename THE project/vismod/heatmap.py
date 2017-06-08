from istaticvis import IStaticVis
import numpy as np

class Heatmap(IStaticVis):

    @staticmethod
    def calculateStaticVisualizations(trialObject, resReduction=10):
        xData = trialObject.data[:,1]
        yData = trialObject.data[:,2]
        allHeatmaps = []
        for stim in trialObject.stimuli:
            heatmap = np.histogram2d(xData, yData, bins=[stim.size[0] // resReduction, stim.size[1] // resReduction], range=stim.extent)
            allHeatmaps.append(heatmap)
        return allHeatmaps

