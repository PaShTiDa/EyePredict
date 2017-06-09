import dlib
import pickle
import numpy as np
from skimage import io
from iextraction import IExtraction
import matplotlib.pyplot as plt

class FacePrefExctractor(IExtraction):

    def __init__(self, predictorFilePath):
        self.shape_predictor_path = predictorFilePath

    def __transform_to_global_coordinates(self, landmarks, imgPath, xOrigin, yOrigin):
        '''Transforms the X and Y coordinates of the extracted features from relative picture coordinates to screen coordinates'''
        xLL, yLL = self.__compute_picture_lowerLeft_coord(imgPath, xOrigin, yOrigin)
        for idx, point in enumerate(landmarks):
            landmarks[idx] = [xLL + point[0, 0], yLL + point[0, 1]]

    def __compute_picture_lowerLeft_coord(self, imgPath, xOrigin, yOrigin):
        img = io.imread(imgPath)
        print(img.shape)
        size = img.shape
        return (xOrigin - size[1]//2, yOrigin - size[0]//2) # X and Y dimenstions are flipped when reading the shape of the picture.

    def convert_landmarks_to_features(self, landmarks, heatmap, resReduction):
        features = []
        pointsX = []
        pointsY = []
        for idx, point in enumerate(landmarks):
            pointsX.append(point[0,0])
            pointsY.append(420-point[0,1])
            try:
                print("Point (" + str(point[0,0]//10) +"," + str(point[0,1]//10) + ")")
                p = heatmap[point[0,0]//resReduction, (420-point[0,1])//resReduction]
                features.append(int(p))
            except:
                print("Point (" + str(point[0,0]) +"," + str(point[0,1]) + " out of bounds")
                features.append(0)
        print(features)
        print(len(features))
        plt.scatter(pointsX, pointsY)
        plt.show()
        return features


    def extractFeatures(self, imgPath, xOrigin, yOrigin):
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
            #self.__transform_to_global_coordinates(landmarks, imgPath, xOrigin, yOrigin)
        return landmarks

ex = FaceExctractor("C:\\Users\\Roee\\Desktop\\edf\\shape_predictor_68_face_landmarks.dat")
marks = ex.extractFeatures("C:\\Users\\Roee\\Desktop\\edf\\img\\114_shafir_stav.jpg", 960, 540)

with open("./heatmap.pkl", 'rb') as file:
    heatmap = pickle.load(file)


img = plt.imread("C:\\Users\\Roee\\Desktop\\edf\\img\\114_shafir_stav.jpg")
extent = [0,280,0,420]
heatmap = np.ma.masked_where(heatmap < 1, heatmap, copy=False) # choose lower bound values (currently shows anything with value > 0) for visualization
plt.imshow(img, extent = extent)
plt.imshow(heatmap.T, extent = extent, origin='lower', cmap = 'jet', alpha = 0.7)
feats = ex.convert_landmarks_to_features(marks, heatmap, 10)
