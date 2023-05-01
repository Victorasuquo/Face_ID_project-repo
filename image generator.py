
# import openai
# import requests
# from requests.structures import CaseInsensitiveDict

# import json

# openai.api_key = ""

# model = "image-alpha-001"
# prompt = "a picture of a cat"


# data = {
#     "model": model,
#     "prompt": prompt,
#     "num_images": 1,
#     "size": "512x512",
#     "response_format": "url"
# }

# data_json = json.dumps(data)



# headers = CaseInsensitiveDict()
# headers["Content-Type"] = "application/json"
# headers["Authorization"] = "Bearer "+openai.api_key

# # resp = requests.post("https://api.openai.com/v1/images/generations", headers=headers, data= data)


# resp = requests.post("https://api.openai.com/v1/images/generations", headers=headers, data=data)

# if resp.status_code != 200:
#     raise ValueError("Failed to generate image "+resp.text)

# response_text = json.loads(resp.text)
# print(response_text['data'][0]['url'])

import openai
import requests
from requests.structures import CaseInsensitiveDict
import json

# Set your OpenAI API key
openai.api_key = "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"

# Define the model and prompt for generating the image
model = "image-alpha-001"
prompt = "a picture of the kind of excercise and elderly person can do to get illed from sadness"

# Create a dictionary with the required parameters for generating the image
data = {
    "model": model,
    "prompt": prompt,
    "num_images": 1,
    "size": "512x512",
    "response_format": "url"
}

# Convert the dictionary to a JSON string
data_json = json.dumps(data)

# Set the headers for the API request
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
headers["Authorization"] = "Bearer "+openai.api_key

# Make a POST request to the OpenAI API with the parameters
resp = requests.post("https://api.openai.com/v1/images/generations", headers=headers, data=data_json)

# Check the status code of the response to make sure it is successful
if resp.status_code != 200:
    raise ValueError("Failed to generate image "+resp.text)

# Get the URL of the generated image from the response
response_text = json.loads(resp.text)
image_url = response_text['data'][0]['url']

# Print the generated image URL
print("Generated image URL: " + image_url)


import openai
import requests
import cv2
import numpy as np

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY_HERE"

# Define the model and prompt for generating the image
model = "image-alpha-001"
prompt = "a picture of a cat"

# Create a dictionary with the required parameters for generating the image
data = {
    "model": model,
    "prompt": prompt,
    "num_images": 1,
    "size": "512x512",
    "response_format": "url"
}

# Convert the dictionary to a JSON string
data_json = json.dumps(data)

# Set the headers for the API request
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
headers["Authorization"] = "Bearer "+openai.api_key

# Make a POST request to the OpenAI API with the parameters
resp = requests.post("https://api.openai.com/v1/images/generations", headers=headers, data=data_json)


# Download the image from the URL
response = requests.get(image_url)
img_array = np.array(bytearray(response.content), dtype=np.uint8)
img = cv2.imdecode(img_array, -1)

# Create a frame and display the image
cv2.namedWindow("Generated Image", cv2.WINDOW_NORMAL)
cv2.imshow("Generated Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
