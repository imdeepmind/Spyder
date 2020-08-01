from parse import Parser
from fetcher import Fetcher


class Spyder:
  def __init__(self, headstart='https://imdeepmind.com'):
    self.headstart = headstart

    # Fetch the page
    fetcher = Fetcher(self.headstart)
    html = fetcher.fetch()

    print(html)

    # Extract the contents of the page
    # parser = Parser(html)
    # content = parser.parse()

    # print(content)