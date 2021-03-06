import os
import time
import requests
import pathlib
PATH_ROOT = pathlib.Path().resolve()

def get_file_minified(path_file):
    f = open(path_file, "r")
    csscode = f.read()
    f.close()
    r = requests.post("https://www.toptal.com/developers/cssminifier/raw", data={"input":csscode})
    return r.text

def save_as(content, path_file):
    f2 = open(path_file, "w")
    f2.write(content)
    f2.close()

PATH_FOLDER_FROM = f"{PATH_ROOT}/landings/prj-marketing/css"
PATH_FOLDER_TO = f"{PATH_ROOT}/landings/prj-marketing/css-mini"

def minify():
    files = os.scandir(PATH_FOLDER_FROM)

    if not os.path.exists(PATH_FOLDER_TO):
        os.makedirs(PATH_FOLDER_TO, exist_ok=False)
        time.sleep(1)

    for filename in files:
        if filename.is_dir():
            continue
        filename = filename.name
        print(f"{filename}")
        file_data = os.path.splitext(filename)
        name = file_data[0]
        ext = file_data[1] #lleva el .

        if not ext==".css":
            continue

        path_file = f"{PATH_FOLDER_FROM}/{filename}"
        path_to =  f"{PATH_FOLDER_TO}/{name}.mini{ext}"

        if os.path.exists(path_to):
            os.remove(path_to)
            time.sleep(1)

        print(f"from: {path_file}")
        print(f"to: {path_to}")
        cssmini = get_file_minified(path_file)
        time.sleep(3)
        save_as(cssmini, path_to)

minify()



