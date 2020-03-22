import json
import requests

from urllib import parse


class ImageConnetion:
    def _read_json_file(self):
        with open('config.json', 'r') as f:
            datastore = json.load(f)
        return datastore

    def request(self, url, method, query_params=None, request_body=None):
        dataset = self._read_json_file()
        base_url = dataset.get('base_url')
        port = dataset.get('port')

        final_url = f'{base_url}:{port}/{url}'
        if query_params:
            final_url += '?'
            qstr = parse.urlencode(query_params)

            final_url += qstr

        if method == 'post':
            response = requests.post(final_url, json=request_body)
        elif method == 'get':
            response = requests.get(final_url)

        if response.status_code != 200:
            raise Exception
        return response.request.body


image_connection = ImageConnetion()
