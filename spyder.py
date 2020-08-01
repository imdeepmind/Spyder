from parse import Parser
from fetcher import Fetcher


class Spyder:
  def __init__(self, headstart='https://imdeepmind.com'):
    self.headstart = headstart

    self.__run()

  def __run(self, url=None):
    # Fetch the page
    if url:
      fetcher = Fetcher(url)
    else:
      fetcher = Fetcher(self.headstart)
    html = fetcher.fetch()

    # Extract the contents of the page
    parser = Parser(html)
    content = parser.parse()

    print(content)

    for link in content["links"]:
      self.__run(link)

