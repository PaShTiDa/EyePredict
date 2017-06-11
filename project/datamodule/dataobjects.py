import pickle
import pandas as pd
from skimage import io

class Subject(object):

    def __init__(self, ID, behavioralData, eyeTrackingData=None):
        self.trials = []
        self.ID = str(ID)
        self.behavioralData = behavioralData
        self.eyeTrackingData = eyeTrackingData

    def __repr__(self):
        return "Subject ID: " + str(self.ID) + " has " + str(len(self.trials)) + " trials"

    def __loadTrialsFromMemory(self, filePath):
        with open(filePath, 'rb') as file:
            allTrials = pickle.load(file)
            for i in range(len(allTrials)):
                self.trials.append(Trial(self, i+1, allTrials[i]))

class Trial(object):

    def __init__(self, subject, trialNumber, data, stimuliList):
        self.data = data
        self.trialNumber = trialNumber
        self.subject = subject
        self.stimuli = stimuliList

    def __repr__(self):
        return "Subject: " + str(self.subject.ID) + " Trial number: " + str(self.trialNumber)

class Stimulus(object):

    def __init__(self, path, xOrigin, yOrigin):
        self.path = path
        self.xOrigin = xOrigin
        self.yOrigin = yOrigin
        self.size = self.__calculateSize()
        self.extent = self.__calculateStimExtent()

    def __calculateSize(self):
        img = io.imread(self.path)
        shape = img.shape
        return (shape[1], shape[0])

    def __calculateStimExtent(self):
        xSize = self.size[0]
        ySize = self.size[1]
        return [[self.xOrigin-xSize//2, self.xOrigin+xSize//2], [self.yOrigin-ySize//2, self.yOrigin+ySize//2]]

