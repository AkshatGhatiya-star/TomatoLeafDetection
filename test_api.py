import os
import requests

# Use absolute path so Python never gets confused
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(BASE_DIR, "sample_leaf.jpg")

url = "http://127.0.0.1:5000/predict"
with open(image_path, "rb") as img:
    file = {"image": img}
    res = requests.post(url, files=file)

print(res.json())
