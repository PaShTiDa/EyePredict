from PredictionInterface import IPredictor
from sklearn import svm

class FacePredictor(IPredictor):

    def __init__(self):
        self.classifier = svm.SVC()

    def changeClassifier(self, newClassifier):
        self.classifier = newClassifier

    def train_classifier(self, X, y):
        self.classifier.fit(X, y)

    def get_prediction_accuracy(self):
        #TODO: Use the Kfold to implement a 1 subject out or 1 trial out strategies.
        pass

