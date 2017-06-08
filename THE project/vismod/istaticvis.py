from abc import abstractmethod, ABCMeta

class IStaticVis(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def calculateStaticVisualizations(trialObject):
        return

