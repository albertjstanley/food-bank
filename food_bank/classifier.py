from food_bank.api import GoogleVisionAPI

def dummy_function():
    import io
    import os
    # The name of the image file to annotate
    file_name = os.path.abspath('misc/example_images/banana.jpg')

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    
    GoogleVisionAPI().predict_on_image_bytes(content)

class Classifier:
    def __init__(self):
        pass

    def predict_from_image_path(self):
        pass

    def predict_from_bytes(self):
        pass
    
