import json

import requests

from . import app


AUTH_HEADER = f'Bearer {app.config["DROPBOX_TOKEN"]}'
UPLOAD_LINK = 'https://content.dropboxapi.com/2/files/upload'
SHARING_LINK = (
    'https://api.dropboxapi.com/2/sharing/create_shared_link_with_settings'
)


def upload_files_to_dropbox(images):
    urls = []
    if images is not None:
        for image in images:
            dropbox_args = json.dumps(
                {'path': f'/{image.filename}', 'autorename': True}
            )
            response = requests.post(
                UPLOAD_LINK,
                image.read(),
                headers={
                    'Authorization': AUTH_HEADER,
                    'Content-Type': 'application/octet-stream',
                    'Dropbox-API-Arg': dropbox_args
                }
            )
            path = response.json()['path_lower']
            response = requests.post(
                SHARING_LINK,
                json={'path': path},
                headers={
                    'Authorization': AUTH_HEADER,
                    'Content-Type': 'application/json',
                }
            )
            data = response.json()
            if 'url' not in data:
                data = data['error']['shared_link_already_exists']['metadata']
            url = data['url']
            url = url.replace('&dl=0', '&raw=1')
            urls.append(url)
    return urls
