import requests
import sys

def get(url):
    return str(requests.get(url).text)

def save(url, path):
    open(path, "w").write(str(requests.get(url).text))
    return "written " + str(sys.getsizeof(str(requests.get(url).text))) + "bytes"
