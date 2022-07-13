import os
import requests

def get_file_minified(path_file):
    f = open(path_file, "r")
    csscode = f.read()
    f.close()
    r = requests.post("http://cssminifier.com/raw", data={"input":csscode})
    return r.text

def save_minified_as(path_file):
    codeminified = r.text
    f2 = open(path_file, "w")
    f2.write(codeminified)
    f2.close()

PATH_FOLDER_FROM = ""
PATH_FOLDER_TO = ""

def minify():



