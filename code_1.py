import vk, os
import time
import requests
from pprint import pprint
import pandas as pd

with open('token_vk.txt', 'r') as file_object:
    token_vk = file_object.read().strip()


class VkUser:
    def __init__ (self, token_vk, version):
        self.params = {
            'access_token': token_vk,
            'v': version
            }
class VkUser:
    url = 'https://api.vk.com/method/'
    def __init__ (self, token_vk, version):
        self.params = {
            'access_token': token_vk,
            'v': version
            }
    def save_photo(self, owner_id):
        url_photo = 'https://api.vk.com/method/photos.get'
        params = {
            'owner_id': 'id вести ',
            'album_id': 'id вести № альбома',
            'rev': False,
            'extended': True,
            'photo_sizes': False,
            'access_token': token_vk,
            'count': 5,
            'v': '5.131'
            }
        res = requests.get(url_photo, params=params)
        res_str = res.json()
        # pprint(res_str)
        res_str_response = res_str['response']['items']
        # pprint(res_str_response)
        list = []
        for item in res_str_response:
            list.append(item['sizes'][-1]['url'])
            link = list[0]
            print(link)
            filename = 'photo.jpg'
            foto_download = requests.get(link)
            with open(filename, 'wb') as file:
                file.write(foto_download.content)
        return res_str

if __name__ == '__main__':
    vk = VkUser(token_vk, '5.131')
    vk.save_photo()


with open('token_ya.txt', 'r') as file_object:
    token_ya = file_object.read().strip()

class YandexDisk:
    def __init__(self, token_ya):
        self.token = token_ya

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href_json = self._get_upload_link(disk_file_path=disk_file_path)
        href = href_json['href']
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')

if __name__ == '__main__':
    ya = YandexDisk(token_ya)
ya.upload_file_to_disk('List/photo.jpg', 'photo.jpg')