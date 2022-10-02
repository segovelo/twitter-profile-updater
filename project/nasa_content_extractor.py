import requests
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv('NASA_API_KEY')

class Content():
    def __init__(self, title = None, imageURL = None, imageHDURL = None, date = None):
        self.title = title
        self.imageURL = imageURL
        self.imageHDURL = imageHDURL
        self.date = date

class NASAContentExtractor():
    def __init__(self):
        pass

    def reverse(self, x):
        year = x[:4]
        month = x[5:7]
        day = x[8:]
        return '-'.join([day,month,year])

    def get_content(self):
        json = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={api_key}').json()
        if json['media_type'] != 'image':
            return None

        title = json['title']
        imageURL = json['url']
        imageHDURL = json['hdurl']
        date = json['date']
        content = Content(title, imageURL, imageHDURL, self.reverse(date))
        return content
