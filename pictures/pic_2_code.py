from PIL import Image
from transformers import pipeline

import os
import io
import tensorflow

api_key = "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"

input_file = "class_1.jpg"

img_codebase = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base")

language = "en"



def ai_summary(input):
    output = img_codebase(input)
    return output[0]['generated_text']


print(ai_summary(input_file))

