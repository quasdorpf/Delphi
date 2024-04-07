from PIL import Image
from transformers import pipeline

import os
import io
import tensorflow

class image_captioning:
    def __init__(self, input_file):
        self.api_key = "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"

        self.i_file = input_file

        self.img_codebase = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base")

        self.language = "en"

    def change_file(user_input_file):
        self.i_file = user_input_file
        
    def ai_summary(self):
        output = self.img_codebase(self.i_file)
        return output[0]['generated_text']


input_file = "apple.jpg"
image = image_captioning(input_file)
print(image.ai_summary())

