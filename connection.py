import pymongo

client = pymongo.MongoClient("mongodb+srv://vedant:vedant@cluster0.atdckpp.mongodb.net/?retryWrites=true&w=majority")
db = client.test