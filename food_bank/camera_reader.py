import datetime
import cv2
from cv2 import VideoCapture, imshow, imwrite, waitKey, destroyWindow
import PIL
from PIL import Image
from pathlib import Path
from datetime import datetime
import time

GENERATED_IMAGES_DIR = Path("generated_images")

class CameraReader:
    def __init__(self):
        pass

    def _get_unique_identifier(self):
        return str(datetime.now())

    def _save_image(self, numpy_array):
        im = Image.fromarray(numpy_array,mode="RGB")
        identifier = self._get_unique_identifier()
        image_path = str(GENERATED_IMAGES_DIR  / f"{identifier}.jpeg")
        im.save(image_path, "JPEG")
        return image_path
    
    def _take_photo(self):
        cam_port = 0
        cam = VideoCapture(cam_port)
        time.sleep(1)
        # reading the input using the camera
        result, image = cam.read()
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        if result:
            return rgb_image
        else: 
            raise ValueError()

    def get_and_display_image(self):
        # initialize the camera
        # If you have multiple camera connected with 
        # current device, assign a value in cam_port 
        # variable according to that
        image = self._take_photo()
        image_path = self._save_image(image)
        return image_path