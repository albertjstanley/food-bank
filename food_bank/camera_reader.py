import datetime
import cv2
from cv2 import VideoCapture, imshow, imwrite, waitKey, destroyWindow
import PIL
from PIL import Image
from pathlib import Path
from datetime import datetime

GENERATED_IMAGES_DIR = Path("generated_images")

class CameraReader:
    def __init__(self):
        pass

    def _get_unique_identifier(self):
        return str(datetime.now())

    def _save_image(self, numpy_array):
        im = Image.fromarray(numpy_array,mode="RGB")
        identifier = self._get_unique_identifier()
        im.save(str(GENERATED_IMAGES_DIR  / f"{identifier}.jpeg"), "JPEG")
    
    def _take_photo(self):
        cam_port = 0
        cam = VideoCapture(cam_port)
        input("waiting")
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
        self._save_image(image)
        input()
        
        # If image will detected without any error, 
        # show result
        # if result:
        
        #     # showing result, it take frame name and image 
        #     # output
        #     imshow("GeeksForGeeks", image)
        
        #     # saving image in local storage
        #     imwrite("GeeksForGeeks.png", image)
        
        #     # If keyboard interrupt occurs, destroy image 
        #     # window
        #     waitKey(0)
        #     destroyWindow("GeeksForGeeks")
        
        # # If captured image is corrupted, moving to else part
        # else:
        #     print("No image detected. Please! try again")