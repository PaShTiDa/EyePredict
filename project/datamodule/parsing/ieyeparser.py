from abc import ABCMeta, abstractmethod
from parsing.iparser import IParser


class IEyeParser(IParser, metaclass=ABCMeta):

    @abstractmethod
    def parse(self, file):
        pass