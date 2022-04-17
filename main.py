from multiprocessing import dummy
from food_bank.api import GoogleVisionAPI
from food_bank.classifier import dummy_function
from food_bank.camera_reader import CameraReader
import numpy as np

# dummy_function()
image_path = CameraReader().get_and_display_image()
predictions = GoogleVisionAPI().predict_on_image_path(image_path)
for prediction in predictions:
    print(prediction.description)