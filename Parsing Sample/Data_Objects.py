import pickle

class Subject(object):

    def __init__(self, ID, filePath):
        self.trials = []
        self.ID = str(ID)
        self.__getTrialsFromFile(filePath)

    def __repr__(self):
        return "Subject ID: " + str(self.ID) + " has " + str(len(self.trials)) + " trials"

    def __getTrialsFromFile(self, filePath):
        with open(filePath, 'rb') as file:
            allTrials = pickle.load(file)
            for i in range(len(allTrials)):
                self.trials.append(Trial(self, i+1, allTrials[i]))

class Trial(object):

    def __init__(self, subject, trialNumber, data):
        self.data = data
        self.trialNumber = trialNumber
        self.subject = subject

    def __repr__(self):
        return "Subject: " + str(self.subject.ID) + " Trial number: " + str(self.trialNumber)