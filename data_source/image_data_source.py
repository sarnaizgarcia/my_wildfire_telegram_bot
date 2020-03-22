import json
import requests

from urllib import parse


class ImageConnetion:
    def _read_json_file(self):
        with open('config.json', 'r') as f:
            datastore = json.load(f)
        return datastore

    # método que recibe como parámetro URL, método http, params url (query params)
    # y un cuerpo de petición opcional. Lee el fichero de config,
    # monta url y hace la petición

    def request(self, url, method, query_params=None, request_body=None):
        dataset = self._read_json_file()
        base_url = dataset.get('base_url')
        port = dataset.get('port')

        final_url = f'{base_url}:{port}/{url}'
        if query_params:
            final_url += '?'
            qstr = parse.urlencode(query_params)

            final_url += qstr

        response = requests.method(final_url)

        return response


image_connection = ImageConnetion()
