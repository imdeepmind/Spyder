import requests

class Fetcher:
  def __init__(self, url):
    self.__url = url
  
  def fetch(self):
    with requests.get(self.__url) as r:
      return r.text