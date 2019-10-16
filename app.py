# -*- encoding: utf-8 -*-
from pymongo import MongoClient
uri = "mongodb://inegi:rsF7vS5QFZmUCLTHNo7sEYTN3lOxVkHJSH6Vf3xlSGbj8hXzM3hGxZHNxTe9Fny296ya4BgjnSetDZyrj4b8yA==@inegi.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
db = MongoClient(uri)
mongo = db.inegi