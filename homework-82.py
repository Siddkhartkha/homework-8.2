import requests

ya_token = 'AQAAAAAHDG3ZAADLW6Xpj-UyxUutsI5_0VjuM9o'

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, disk_file, path_file):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {"path": disk_file, "overwrite": "true"}
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'OAuth {}'.format(self.token)
                   }
        # Файл загружается из папки на компьютере в папку с аналогичным названием на Яндекс.Диске
        response = requests.get(url=upload_url,
                                params=params,
                                headers=headers)
        href = response.json()['href']
        with open(path_file, 'rb') as f:
            requests.put(href, files={'file': f})
            print('File uploaded!')


if __name__ == '__main__':
    uploader = YaUploader(token=ya_token)
    file_name = 'file.txt'
    disk_path = 'my_folder/' + file_name
    ya_path = 'my_folder/' + file_name
    uploader.upload(disk_file=disk_path, path_file=ya_path)