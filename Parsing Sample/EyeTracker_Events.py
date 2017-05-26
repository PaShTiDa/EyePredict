from enum import Enum

class Event(Enum):
    RunStart = "RunStart"
    TrialStart = "TrialStart"
    Fixation = "Fixation"
    Response = "Response"
    RunEnd = "RunEnd"
    CueStart = "CueStart"
    RespondFaster = "RespondFaster"
    PresentIsOld = "PresentIsOld"
    ResponseIsOld = "ResponseIsOld"
    PresentIsGo = "PresentIsGo"
    ResponseIsGo = "ResponseIsGo"

class Task(Enum):
    BDM = "BDM"
    BDMDemo = "BDMDemo"
    Training = "Training"
    TrainingDemo = "TrainingDemo"
    Probe = "Probe"
    ProbeDemo = "ProbeDemo"
    Memory = "Memory"
    MemoryDemo = "MemoryDemo"
    BinaryRanking = "BinaryRanking"
    BinaryRankingDemo = "BinaryRankingDemo"
    ResponseToStimuli = "ResponseRoStimuli"
    ResponseToStimuliDemo = "ResponseToStimuliDemno"
    FaceLocalizer = "FaceLocalizer"