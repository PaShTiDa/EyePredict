import matplotlib.pyplot as plt
import numpy as np

from dataobjects import *
from eyetrackerevents import *
from parsing.ieyeparser import IEyeParser


class EyeParser(IEyeParser):
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
        return self.allTrials

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
