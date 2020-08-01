import re
from bs4 import BeautifulSoup
import spacy

sp = spacy.load('en_core_web_sm')
all_stopwords = sp.Defaults.stop_words

class Parser:
  def __init__(self, content):
    self.__soup = BeautifulSoup(content, 'html.parser')
  
  def __get_page_title(self):
    print(self.__soup)
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

  def __clean_text(self, text):
    text = text.lower()

    text = re.sub(r"i'm", "i am", text)
    text = re.sub(r"aren't", "are not", text)
    text = re.sub(r"couldn't", "could not", text)
    text = re.sub(r"didn't", "did not", text)
    text = re.sub(r"doesn't", "does not", text)
    text = re.sub(r"don't", "do not", text)
    text = re.sub(r"hadn't", "had not", text)
    text = re.sub(r"hasn't", "has not", text)
    text = re.sub(r"haven't", "have not", text)
    text = re.sub(r"isn't", "is not", text)
    text = re.sub(r"hadn't", "had not", text)
    text = re.sub(r"hadn't", "had not", text)
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"can't", "cannot", text)
    text = re.sub(r"mightn't", "might not", text)
    text = re.sub(r"mustn't", "must not", text)
    text = re.sub(r"needn't", "need not", text)
    text = re.sub(r"shouldn't", "should not", text)
    text = re.sub(r"wasn't", "was not", text)
    text = re.sub(r"weren't", "were not", text)
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"wouldn't", "would not", text)

    text = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', '', text, flags=re.MULTILINE)
    text = re.sub(r'(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)', '', text)
    text = re.sub(r'\b[0-9]+\b\s*', '', text)

    return text

  def __get_keywords(self):
    page_text = self.__soup.get_text()

    # clean the text
    page_text = self.__clean_text(page_text)

    # word tokenizing
    words = [word for word in page_text.split(' ') if word]
    
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