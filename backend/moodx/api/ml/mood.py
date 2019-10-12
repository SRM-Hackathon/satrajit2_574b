from django.conf import settings

import os
import cv2
import imutils
import numpy as np
from keras.models import load_model
import keras.preprocessing.image as KPI


class MoodPredictor:
    DETECTION_MODEL_PATH = os.path.join(settings.MEDIA_ROOT, 'facedetect.xml')
    EMOTION_MODEL_PATH = os.path.join(settings.MEDIA_ROOT, 'xception-emotions.hdf5')

    EMOTIONS = ["angry", "disgust", "scared",
                "happy", "sad", "surprised", "neutral"]

    def __init__(self):
        print(f'Helllo from ml {__name__}')
        self.face_detection = cv2.CascadeClassifier(self.DETECTION_MODEL_PATH)
        self.emotion_classifier = load_model(
            self.EMOTION_MODEL_PATH,
            compile=False
        )
        print('INITIALIZED GRAPH')
        

    def get_mood(self, filepath):
        image = cv2.imread(filepath)
        image = imutils.resize(image, width=300)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = self.face_detection.detectMultiScale(
            image,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        if len(faces) > 0:
            faces = sorted(
                faces, reverse=True,
                key=lambda x: (x[2] - x[0]) * (x[3] - x[1])
            )[0]

            (fX, fY, fW, fH) = faces

            # Extract the ROI of the face from the grayscale image, resize it to a fixed 28x28 pixels, and then prepare
            # the ROI for classification via the CNN
            roi = image[fY:fY + fH, fX:fX + fW]
            roi = cv2.resize(roi, (64, 64))
            roi = roi.astype("float") / 255.0
            roi = KPI.img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)

            preds = self.emotion_classifier.predict(roi)[0]
            # emotion_probability = np.max(preds)
            label = self.EMOTIONS[preds.argmax()]
            return label

        return self.EMOTIONS[-1]
