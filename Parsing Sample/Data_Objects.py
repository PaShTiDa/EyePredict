import pickle
import pandas as pd
class Subject(object):

    def __init__(self, ID, behavioralDataPath, eyeTrackingDataPath):
        self.trials = []
        self.ID = str(ID)
        self.__getBehavioralData(behavioralDataPath)
        self.__getTrialsFromFile(eyeTrackingDataPath)

    def __repr__(self):
        return "Subject ID: " + str(self.ID) + " has " + str(len(self.trials)) + " trials"

    def __getTrialsFromFile(self, filePath):
        with open(filePath, 'rb') as file:
            allTrials = pickle.load(file)
            for i in range(len(allTrials)):
                self.trials.append(Trial(self, i+1, allTrials[i]))

    def __getBehavioralData(self, behavioralDataPath):
        self.behavioralData = pd.read_csv(behavioralDataPath, delim_whitespace=True, index_col=False)

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

