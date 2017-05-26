from IParser import ParserInterface
import numpy as np
import pickle
import matplotlib.pyplot as plt
from Data_Objects import *

class Parser(ParserInterface):
    def __init__(self):
        self.file = None
        self.startState = {"SFIX" : 1, "SSACC": 2, "SBLINK": 3}
        self.endState = {"EFIX": 1, "ESACC": 2, "EBLINK": 3}
        self.currentState = ""
        self.statesDict = {}
        self.trialNum = 0
        self.allTrials = []

    def parse(self, file_path, header = 115):
        self.file = open(file_path, 'r')
        for i in range(header): #skip header lines. TODO use a more sophisticated way to skip header
            self.file.readline()
        while 1: # read all trials from file
            if not self.__getToNextTrial(): # move the file cursor to the beginning of the data of the next trial, return false when reach flag_RunEnd.
                break
            self.__extractTrial() #extract current trial and save the relevant data as npy file.
        with open("./all_trials.pkl", 'wb') as file:
            pickle.dump(self.allTrials, file, pickle.HIGHEST_PROTOCOL) # save the numpy arrays in order using the pickle module.
        print("Successfully read " + str(self.trialNum) + " trials")
        self.file.close()

    def __readUntilFlag(self, flag):
        '''This function gets a string and reads the currently parsed file until the line in which this string appears'''
        while 1:
            line = self.file.readline()
            if line.startswith("MSG"):
                if flag in line:
                    break
            if not line[0].isdigit():
                self.__updateState(line)
                continue


    def __getToNextTrial(self):
        '''Moves the file cursor to the next MSG line, and stops if it reaches a TrialStart flag with a Probe Task'''
        while 1:
            line = self.file.readline()
            if line.startswith("MSG"):
                trialStatus, trialNum, trialTime, trialTask= self.__parseMsg(line)
                if trialStatus == "TrialStart" and (trialTask == "Probe" or trialTask == "BDM"):
                    return True
                if trialStatus == "RunEnd":
                    return False
            if not line[0].isdigit():
                self.__updateState(line)

    def __extractTrial(self):
        '''Reads file data from the current row until the next MSG with a RESPONSE flag'''
        trialData = []
        self.trialNum += 1
        while 1:
            line = self.file.readline()
            if line.startswith("MSG"):
                trialStatus, trialNum, trialTime, trialTask = self.__parseMsg(line)
                if trialStatus == "Response" or trialStatus == "RespondFaster":
                    break
            if not line[0].isdigit():
                self.__updateState(line)
                continue
            if self.currentState != "BLINK":
                data = line.split()
                trialData.append([float(data[0]), float(data[1]), float(data[2])])
        trial = np.asarray(trialData)
        self.allTrials.append(trial)

    def __updateState(self, line):
        '''Update the current state of the eye tracking. Either FIX, SACC or BLINK'''
        data = line.split()
        if data[0] in self.startState:
            self.currentState = data[0][1:]
            return True
        if data[0] in self.endState:
            self.statesDict[(data[2], data[3])] = data[0][1:]
            self.currentState = ""
            return True
        return False

    def __parseMsg(self, msg):
        '''Parse a MSG string sent by the experimenters to the eyetracker and extract relevant data'''
        data = msg.split()
        flagData = data[2].split('_')
        trialStatus = flagData[1]
        trialNum = int(flagData[4][5:])
        trialTime = float(flagData[5][4:])
        trialTask = flagData[2][4:]
        return (trialStatus, trialNum, trialTime, trialTask)

p = Parser() #initiate the parser object
p.parse("C:\\Users\\Roee\\Desktop\\edf\\c.asc", header=84) # call parse on the current file (represents 42 trials of one subject.
background = np.zeros([1920, 1080], dtype=int) # initiate background array (white)
s1 = Subject("MOSHE", "./all_trials.pkl") # get subject data from the parsed file
trial1 = s1.trials[0] # get the first trial from the subject trial array
arr = trial1.data # get the actuall data for this trial

plt.xlim([0, 1920])
plt.ylim([0, 1080])
minx = min(arr[:, 1])
maxx = max(arr[:, 1])
miny = min(arr[:, 2])
maxy = max(arr[:, 2])
heatmap, xedges, yedges = np.histogram2d(arr[:,1], arr[:,2], bins = [int((maxx-minx)/5), int((maxy-miny)/5)]) # create the heatmap
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]] # calculate heatmap extent
heatmap = np.ma.masked_where(heatmap == 0, heatmap, copy=False) # choos lower bound values (currently shows anything with value > 0) for visualization
#background = np.ma.masked_where(background == 0, background, copy=False)
plt.imshow(heatmap.T, extent=extent, origin='lower', cmap = 'jet', alpha = 0.4) #parameters for heatmap
plt.colorbar() # legend
plt.show() # show all
