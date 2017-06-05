from abc import ABCMeta, abstractmethod

class IExtraction(metaclass=ABCMeta):

    @abstractmethod
    def extractFeatures(self, imgPath):
        return