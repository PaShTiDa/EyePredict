from abc import ABCMeta, abstractmethod

class ParserInterface(metaclass=ABCMeta):

    @abstractmethod
    def parse(self, file):
        return