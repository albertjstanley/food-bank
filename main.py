from multiprocessing import dummy
from food_bank.classifier import dummy_function
from food_bank.camera_reader import CameraReader

# dummy_function()
CameraReader().get_and_display_image()