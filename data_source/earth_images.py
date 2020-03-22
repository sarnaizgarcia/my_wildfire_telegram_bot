import requests


class EarthImages:
    def get_earth_images(self, url):
        response = requests.get(url)
        return response.request.body


earth_images = EarthImages()
