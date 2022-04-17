import io
import os
# Imports the Google Cloud client library
from google.cloud import vision

class GoogleVisionResponse:
    def __init__(self, description,score):
        self.description = description
        self.score = score
    
    def __repr__(self):
        return f"<GVResponse description={self.description} score={self.score}>"

class GoogleVisionAPI:
    def __init__(self):
        pass
    
    def predict_on_image_bytes(self,bytes):
        self.client = vision.ImageAnnotatorClient()
        image = vision.Image(content=bytes)
        response = self.client.label_detection(image=image)
        labels = response.label_annotations
        response_list = [GoogleVisionResponse(label.description, label.score) for label in labels]
        return response_list