import requests
import os
from PIL import Image
import io

class imageDownloader():
    def __init__(self):
        pass

    def download_image(self, url, hdurl):
        
        img_data = requests.get(hdurl).content
        image = Image.open(io.BytesIO(img_data))
        width = image.width
        height = image.height
        if width > 8190 or height > 8190:
            img_data = requests.get(url).content
        
        if not os.path.exists('tmp'): os.makedirs('tmp')
        with open('tmp/banner.jpg', 'wb') as handler:
            handler.write(img_data)
        