from abc import abstractmethod, ABCMeta

class IPredictor(metaclass=ABCMeta):

    @abstractmethod
    def train_classifier(self, X, y):
        return

    @abstractmethod
    def get_prediction_accuracy(self):
        return
