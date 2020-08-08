from os import getenv
from pymongo import MongoClient

from utils import logger

try:
  logger.info("Connecting with the db...")
  client = MongoClient(getenv("MONGO_URI"))
  db = client["Spyder"]
  logger.info("Connected with the db...")
except Exception as ex:
  logger.exception(ex)
  logger.info("Can not initialize a DB connection")
  exit()