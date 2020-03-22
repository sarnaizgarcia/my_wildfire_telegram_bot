from data_source.image_data_source import image_connection
from repository.images_repo import images_repo

# print(image_connection._read_json_file())

# querys = {
#     'una_query': 1,
#     'dos': 2
# }

# print(image_connection.request('silvia', 'post', querys))
print(images_repo.create_images(-120.70418, 38.32974, '2017-01-01', '2020-01-01'))
print(images_repo.request_image())
