import os
import pprint
import time
import urllib.error
import urllib.request

def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e, url)

def download_file_to_dir(url, dst_dir):
    download_file(url, os.path.join(dst_dir, os.path.basename(url)))

if __name__ == '__main__':
    μsNames = ["honoka", "eli", "kotori", "umi", "rin", "maki", "nozomi", "hanayo", "nico"]
    AqoursNames = ["chika", "riko", "kanan", "dia", "you", "yoshiko", "hanamaru", "mari", "ruby"]
    
    # Directory to save
    dstPath = "data/LoveLive/SIF_7th_wp/Aqours"
    os.makedirs(dstPath, exist_ok=True)
    for name in AqoursNames:
        url = "https://lovelive-sif.bushimo.jp/7thproject/assets/img/wp/sif_7th_wp_" + name + ".jpg"
        download_file_to_dir(url, dstPath)
