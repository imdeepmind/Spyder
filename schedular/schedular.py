import redis
from rq import Queue

class Schedular:
  def __init__(self, background_process):
    self.__background_process = background_process

    r = redis.Redis()
    self.__q = Queue(connection=r)

  def add(self, arguments):
    job = self.__q.enqueue(self.__background_process, arguments)

    print(f"Added a new job with id {job.id}")
