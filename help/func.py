import base64
import requests

def imgbb(image):
    with open(image, "rb") as file:
        url = "https://api.imgbb.com/1/upload"
        payload = {
            "key": "fdcf0312cf01b248646f62051c0cf9b4",
            "image": base64.b64encode(file.read()),
        }
        res = requests.post(url, payload)
        return res.json()['data']['display_url']