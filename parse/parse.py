import re
from bs4 import BeautifulSoup
import spacy

sp = spacy.load('en_core_web_sm')
all_stopwords = sp.Defaults.stop_words

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
      href = link.get('href')
      if re.match('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', href):
        page_links.append(href)
    
    return list(set(page_links))

  def __get_keywords(self):
    page_text = self.__soup.get_text()

    # word tokenizing
    words = page_text.split(' ')

    # removing stop words
    words_without_sw= [word for word in words if not word in all_stopwords]

    # Building the word frequency dict
    word_dict = {}
    for word in words_without_sw:
      if word in word_dict:
        word_dict[word] += 1
      else:
        word_dict[word] = 1
    
    filtered_words = []
    for word in word_dict:
      if word_dict[word] >= 3:
        filtered_words.append(word)

    return filtered_words

  def parse(self):
    return {
      'title': self.__get_page_title(),
      'description': self.__get_page_description(),
      'links': self.__get_page_links(),
      'keywords': self.__get_keywords()
    }