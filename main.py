from food_bank.api import GoogleVisionAPI
from food_bank.camera_reader import CameraReader
from food_bank.nutrition_info import food_item_supported
import numpy as np
import shutil
import os

# Helper fxn
def clean_workspace():
    # removes files in generated_images direcotry 
    shutil.rmtree("generated_images",ignore_errors=True)
    os.mkdir("generated_images")

def filter_to_get_supported_queries(predictions):
    for prediction in predictions: 
        food = prediction.description
        if food_item_supported(food):
            return prediction.description
    return None

# Instantiate singletons
camera_reader = CameraReader()
google_vision_api = GoogleVisionAPI()

while True:
    input("Enter to begin prediction:")
    clean_workspace()
    image_path = camera_reader.get_and_display_image()
    predictions = google_vision_api.predict_on_image_path(image_path)

    print("Google Predictions:")
    for prediction in predictions:
        print("\t" + prediction.description)

    food_detected = filter_to_get_supported_queries(predictions)
    print("Chosen Prediction: ", food_detected)