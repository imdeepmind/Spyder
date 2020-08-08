from os import getenv
from pymongo import MongoClient

client = MongoClient(getenv("MONGO_URI"))
db = client["Spyder"]