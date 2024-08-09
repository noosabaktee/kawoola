import base64
import requests
from os import getenv

def imgbb(image):
    with open(image, "rb") as file:
        url = "https://api.imgbb.com/1/upload"
        payload = {
            "key": getenv('IMGBB_KEY'),
            "image": base64.b64encode(file.read()),
        }
        res = requests.post(url, payload)
        link = res.json()['data']['display_url']
        link = link.replace(".co/",".co.com/")
        return link