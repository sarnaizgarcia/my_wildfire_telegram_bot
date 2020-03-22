from data_source.image_data_source import image_connection

print(image_connection._read_json_file())

querys = {
    'una_query': 1,
    'dos': 2
}

print(image_connection.request('silvia', 'post', querys))
