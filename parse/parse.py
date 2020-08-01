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
  
  def __get_page_links(self):
    page_links = []

    for link in self.__soup.find_all('a'):
      page_links.append(link.get('href'))
    
    return page_links

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