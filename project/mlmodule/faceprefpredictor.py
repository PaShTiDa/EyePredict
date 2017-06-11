from ipredict import IPredict
from sklearn import svm

class FacePrefPredictor(IPredict):

    def __init__(self):
        self.classifier = svm.SVC()
        self.isTrained = False

    def changeClassifier(self, newClassifier):
        self.classifier = newClassifier
        self.isTrained = False

    def train_classifier(self, X, y):
        self.classifier.fit(X, y)
        self.isTrained = True

    def get_prediction_accuracy(self):
        if self.isTrained:
            #get accuracy
            #TODO: use kfold to implement 1 subject out or 1 trial out.
            pass
        else:
            #must train first
            pass

