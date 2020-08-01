import re
from bs4 import BeautifulSoup

class Parser:
  def __init__(self, content):
    self.__soup = BeautifulSoup(content, 'html.parser')
  
  def __get_page_title(self):
    if self.__soup.title.string:
      return self.__soup.title.string
    return None
  
  def __get_page_description(self):
    title = self.__soup.find("meta",  property="description")
    if title:
      return title
    return None
  
  def __check_link(self, url):
    return re.match('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', url)

  def __remove_duplicate_links(self, links):
    return list(set(links))

  def __get_page_links(self):
    page_links = []

    for link in self.__soup.find_all('a'):
      href = link.get('href')
      if self.__check_link(href):
        page_links.append(href)
    
    return self.__remove_duplicate_links(page_links)

  def parse(self):
    return {
      'title': self.__get_page_title(),
      'description': self.__get_page_description(),
      'links': self.__get_page_links(),
      'keywords': [ # TODO: Need to work on extracting keywords
        {
          'keyword': 'test',
          'freq': 5
        }
      ]
    }