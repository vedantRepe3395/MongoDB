import pymongo
# next two lines from mongodb atlas containing user id password

client = pymongo.MongoClient("mongodb+srv://vedant:vedant@cluster0.atdckpp.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['myinfo_many']
collection = database['many_entry']

record = collection.find({"surname":"repe"})
for i in record:
    print(i)
