import fastapi
from pymongo import MongoClient
import os

from dotenv import load_dotenv
load_dotenv()

mongodb_uri = os.environ.get('MONGO_URI')
port = 4000

client = MongoClient(mongodb_uri, port)
database = client["test_db"]






