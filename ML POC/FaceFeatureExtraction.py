import dlib
import numpy as np
from skimage import io
from FeatureExtractionInterface import IExtraction

class FaceExctractor(IExtraction):

    def __init__(self, predictorFilePath):
        self.shape_predictor_path = predictorFilePath

    def transform_to_global_coordinates(self, landmarks, imgPath, xOrigin, yOrigin):
        '''Transforms the X and Y coordinates of the extracted features from relative picture coordinates to screen coordinates'''
        xLL, yLL = self.compute_picture_lowerLeft_coord(imgPath, xOrigin, yOrigin)
        print(xLL, yLL)
        for idx, point in enumerate(landmarks):
            landmarks[idx] = [xLL + point[0, 0], yLL + point[0, 1]]

    def compute_picture_lowerLeft_coord(self, imgPath, xOrigin, yOrigin):
        img = io.imread(imgPath)
        size = img.shape
        return (xOrigin - size[1]//2, yOrigin - size[0]//2) # X and Y dimenstions are flipped when reading the shape of the picture.

    def extractFeatures(self, imgPath):
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor(self.shape_predictor_path)

        print("Processing file: {}".format(imgPath))
        img = io.imread(imgPath)

        # Ask the detector to find the bounding boxes of each face. The 1 in the
        # second argument indicates that we should upsample the image 1 time. This
        # will make everything bigger and allow us to detect more faces.
        dets = detector(img, 1)
        print("Number of faces detected: {}".format(len(dets)))
        for k, d in enumerate(dets):
            print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
                k, d.left(), d.top(), d.right(), d.bottom()))
            # Get the landmarks/parts for the face in box d.
            shape = predictor(img, d)
            landmarks = np.matrix([[p.x, p.y] for p in shape.parts()])
        return landmarks

ex = FaceExctractor("C:\\Users\\Roee\\Desktop\\edf\\shape_predictor_68_face_landmarks.dat")
marks = ex.extractFeatures("C:\\Users\\Roee\\Desktop\\edf\\img\\114_shafir_stav.jpg")
ex.transform_to_global_coordinates(marks, "C:\\Users\\Roee\\Desktop\\edf\\img\\114_shafir_stav.jpg", 960, 540)