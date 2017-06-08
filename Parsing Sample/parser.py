import matplotlib.pyplot as plt
import numpy as np

from iparser import IParser
from dataobjects import *
from eyetrackerevents import *


class Parser(IParser):
    def __init__(self):
        self.file = None
        self.startState = {"SFIX" : 1, "SSACC": 2, "SBLINK": 3}
        self.endState = {"EFIX": 1, "ESACC": 2, "EBLINK": 3}
        self.currentState = ""
        self.statesDict = {}
        self.trialNum = 0
        self.allTrials = []
        self.screenResolution = () # a tuple of (xmin, ymin. xmax, ymax)

    def parse(self, file_path):
        self.file = open(file_path, 'r')
        self.__readScreenResolution()
        while 1: # read all trials from file
            if not self.__getToNextTrial(): # move the file cursor to the beginning of the data of the next trial, return false when reach flag_RunEnd.
                break
            self.__extractTrial() #extract current trial
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

    def __readScreenResolution(self):
        while 1:
            line = self.file.readline()
            data = line.split()
            if len(data) != 7:
                continue
            elif data[0] == "MSG" and data[2] == "GAZE_COORDS":
                self.screenResolution = (0, 0, float(data[5]) + 1, float(data[6]) + 1)
                break
            else:
                continue

    def __getToNextTrial(self):
        '''Moves the file cursor to the next MSG line, and stops if it reaches a TrialStart flag with a Probe Task'''
        event = ""
        while 1:
            line = self.file.readline()
            if line.startswith("MSG"):
                msg = self.__parseMsg(line)
                if msg != None:
                    event = msg[0]
                else:
                    continue
                if event == Event.TrialStart.name:
                    return True
                if event == Event.RunEnd.name:
                    return False
            if not line[0].isdigit():
                self.__updateState(line)

    def __extractTrial(self):
        '''Reads file data from the current row until the next MSG with an event flag'''
        trialData = []
        self.trialNum += 1
        while 1:
            line = self.file.readline()
            if line.startswith("MSG"):
                msg = self.__parseMsg(line)
                if msg == None:
                    print("Bad message line: " + line)
                    return False
                event = msg[0]
                #if str(event) == "ScaleStart": # uncomment to get all trial data, including the subjects gaze on the scale.
                #   continue
                if event in Event.__members__: # break at next Event
                    break
                else:
                    print("Unrecognized Event:" + event)
                    return False
            if not line[0].isdigit():
                self.__updateState(line)
                continue
            if self.currentState != "BLINK":
                data = line.split()
                trialData.append([float(data[0]), float(data[1]), self.screenResolution[3] - float(data[2])]) # screenResolution[3] = ymax
        trial = np.asarray(trialData)
        self.allTrials.append(trial)
        return True

    def __updateState(self, line):
        '''Update the current state of the eye tracking. Either FIX, SACC or BLINK'''
        data = line.split()
        if len(data) == 0:
            return False
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
        if not msg.startswith("MSG"):
            return None
        data = msg.split()
        if len(data)< 3 or (not data[2].startswith("flag")):
            return None
        flagData = data[2].split('_')
        if not len(flagData) == 6:
            return None
        event = flagData[1]
        task = flagData[2][4:]
        run = int(flagData[3][3:])
        trialNum = int(flagData[4][5:])
        time = float(flagData[5][4:])
        return (event, task, run, trialNum, time)

p = Parser() #initiate the parser object
p.parse("./test.asc") # call parse on the current asc file
s1 = Subject("Test", "./behavioralData.txt","./all_trials.pkl") # get subject data from the parsed file
trial1 = s1.trials[2] # get the third trial, which is the Stav Shafir example trial
arr = trial1.data # get the actuall data for this trial
plt.xlim([0, 1920]) # set X axis limits
plt.ylim([0, 1080]) # set Y axis limits
minx = min(arr[:, 1])
maxx = max(arr[:, 1])
miny = min(arr[:, 2])
maxy = max(arr[:, 2])
heatmap, xedges, yedges = np.histogram2d(arr[:,1], arr[:,2], bins = [280//10, 420//10], range=[[820, 1100], [330, 750]]) # create the heatmap # to increase resolution divide by a lower number
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]] # calculate heatmap extent
#print(extent)
#print(heatmap.T)
#print(heatmap.shape)
with open("./heatmap.pkl", 'wb') as file:
    pickle.dump(heatmap, file, pickle.HIGHEST_PROTOCOL)  # save the numpy arrays in order using the pickle module.
heatmap = np.ma.masked_where(heatmap < 1, heatmap, copy=False) # choose lower bound values (currently shows anything with value > 0) for visualization
img = io.imread("./114_shafir_stav.jpg") # read the Stav Shafir img
refPoint =[960, 540] # center point for the image
plt.imshow(img, extent=[refPoint[0]-140, refPoint[0]+140, refPoint[1]-210, refPoint[1]+210]) # plot the image
plt.imshow(heatmap.T, extent=extent, origin='lower', cmap = 'jet', alpha = 0.7) #plot the heatmap
#plt.colorbar() # uncomment to see the legend
#plt.axis('off) #uncomment to remove X and Y axes.
plt.show() # show all
