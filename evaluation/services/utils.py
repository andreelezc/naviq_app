import requests


def download_file_from_url(url, destination):
    response = requests.get(url)
    with open(destination, 'wb') as f:
        f.write(response.content)
