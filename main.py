import requests
import random
import sys
import shutil
from tqdm.auto import tqdm

tiktok = input("Please input video url: ")
filename = input("Please input video name: ")


def get_details(tiktok, filename):
    url = "https://api.tikmate.app/api/lookup"
    payload = {
        'url': tiktok
    }
    response = requests.post(url, data=payload).json()
    url = response['token']
    download = "https://pride.nowmvideo.com/download/"+url+"/"+filename+".mp4?hd=1"
    return download


def download_file(url, filename):
    try:
        with requests.get(url, stream=True) as req:
            size = int(req.headers.get('Content-Length'))
            filename = filename+".mp4"
            with tqdm.wrapattr(req.raw, "read", total=size, desc="")as raw:
                with open("videos/"+filename, 'wb') as f:
                    shutil.copyfileobj(raw, f)
    except Exception as e:
        print(e)
        return None


download = get_details(tiktok, filename)
print(download)
download_file(download, filename)