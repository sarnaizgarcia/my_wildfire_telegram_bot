import traceback

from data_source.image_data_source import image_connection
from data_source.earth_images import earth_images


class ImagesRepo:

    def create_images(self, longitude, latitude, begin_date, end_date):
        images_data = {
            'longitude': longitude,
            'latitude': latitude,
            'begin_date': begin_date,
            'end_date': end_date
        }

        try:
            image_result = image_connection.request(
                '/images', 'post', query_params=None, request_body=images_data)
            return {'message': image_result}
        except Exception:
            print(traceback.format_exc())
            return {'message': 'Error while creating images.'}

    def request_image(self):
        try:
            image_data = image_connection.request('/images', 'get')
            return earth_images.get_earth_images(image_data.get('url'))
        except Exception:
            return {'message': 'Error while getting images.'}


images_repo = ImagesRepo()
