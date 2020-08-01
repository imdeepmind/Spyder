class Parser:
  def __init__(self, content):
    self.__content = content
    
  def parse(self):
    return {
      'title': "something",
      'description': "description",
      'links': ['https://google.com'],
      'keywords': [
        {
          'keyword': 'test',
          'freq': 5
        }
      ]
    }