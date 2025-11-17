# classifier.py
import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt

class ImageClassifier:
    """
    Image classification using computer vision
    Demonstrates concepts from Chapter 24
    """
    def __init__(self, model_path='model/keras_model.h5', labels_path='model/labels.txt'):
        """Load the trained model and lables"""
        print("Loading model...")
        self.model = keras.models.load_model(model_path, compile=False)

        # Load labels
        with open(labels_path, 'r') as f:
            self.labels = [line.strip() for line in f.readlines()]

        print(f"Model loaded with {len(self.labels)} classes: {self.labels}")

        # Model exprects 224x224 images
        self.image_size = (224, 224)

    def preprocess_image(self, image_path):
        """
        Prepare image for classification
        This is like the preprocessing we did for text!
        """

        # Open and resize image
        img = Image.open(image_path).convert('RGB')
        img = img.resize(self.image_size)

        # Convert to array and normalize
        img_array = np.array(img)
        img_array = img_array / 255.0 # Normalize pixel values

        # Add batch dimension
        img_array = np.expand_dims(img_array, axis=0)

        return img_array, img
    
    def classify_image(self, image_path):
        """Classify a single image"""

        # Preprocess