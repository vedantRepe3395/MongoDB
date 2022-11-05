import pymongo
# next two lines from mongodb atlas containing user id password

client = pymongo.MongoClient("mongodb+srv://vedant:vedant@cluster0.atdckpp.mongodb.net/?retryWrites=true&w=majority")
db = client.test

data = {
    'name': 'vedant',
    'surname':'repe'
        }
database = client['myinfo']
collection = database['vedant']
collection.insert_one(data)