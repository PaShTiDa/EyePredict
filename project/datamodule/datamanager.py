import os

subjects = []
stimuli = []
screenResolution = None
stimuliPath = ""
eyeTrackerDataPath = ""
eyeTrackerDataFiles = []
behavioralDataFiles = []
behavioralDataPath = ""


def verifyPath(taskPropertiesPath):
    """
    verifys the path is valid, and contains 3 directories:
    Eye-tracking data, Behavioral data, Images
    :return: bool True/False
    """
    global screenResolution, eyeTrackerDataPath, behavioralDataPath, stimuliPath
    with open(taskPropertiesPath, 'r') as file:
        for line in file:
            if line.startswith("#"):
                continue
            split = line.split()
            if len(split) >= 2:
                if split[0] == "ScreenResolution":
                    if len(split) == 3:
                        screenResolution = (split[1], split[2])
                    else:
                        return False
                elif split[0] == "Path2Stimuli" and os.path.isdir(split[1]):
                    stimuliPath = split[1]
                elif split[0] == "Path2EDF" and os.path.isdir(split[1]):
                    eyeTrackerDataPath = split[1]
                elif split[0] == "Path2Datafile" and os.path.isdir(split[1]):
                    behavioralDataPath = split[1]
                elif split[0] == "StimIdentifier":
                    stimulus = split[1]
                    split = file.readline().split()
                    if len(split) != 5:
                        return False
                    stimLocation = (split[1], split[2], split[3], split[4])
                    stimuli.append((stimulus, stimLocation))
                else:
                    return False
            else:
                return False
    return True


def verifyData():
    """
    checks the folders content.
    expects the same number of edf and txt files,
    with appropriately fitting file names for each couple.
    (do we need to test the files aren't empty?)
    :return: bool True/False
    """
    global eyeTrackerDataFiles, behavioralDataFiles
    eyeTrackerDataFiles = [f[:-4] for f in os.listdir(eyeTrackerDataPath) if os.path.isfile(os.path.join(eyeTrackerDataPath, f)) and f.endswith(".edf")]
    behavioralDataFiles = [f[:-4] for f in os.listdir(eyeTrackerDataPath) if os.path.isfile(os.path.join(eyeTrackerDataPath, f)) and f.endswith(".txt")]
    eyeTrackerDataFiles = set(eyeTrackerDataFiles)
    behavioralDataFiles = set(behavioralDataFiles)
    if eyeTrackerDataFiles == behavioralDataFiles:
        return True
    else:
        return False

def BrowseDirectory(path):
    """
    Button "Browse" gets a directory path, and sends it to this function.
    """
    rc = True

    # Verify Data
    error = ""
    if(not verifyPath(path)):
        error = "Bad data path.\n Eye-Predict expects the main folder to contain 3 subfolders:\n Eye-tracking data, Behavioral data, Images"
        rc = False
    if(not verifyData()):
        error = "..."
    if(not rc):
        Error(error)
        return -1

    # Load Data

    raise NotImplementedError

def Error(errorString):
    """
    pops a gui error dialog box
    :param errorString: the error to prompt
    :return: non
    """


print(verifyPath("C:\\Users\\Roee\\Desktop\\edf\\task.tsk"))
print(verifyData())


