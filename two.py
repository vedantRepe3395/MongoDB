import pymongo
# next two lines from mongodb atlas containing user id password

client = pymongo.MongoClient("mongodb+srv://vedant:vedant@cluster0.atdckpp.mongodb.net/?retryWrites=true&w=majority")
db = client.test
data = [
    {
        'name': 'vedant',
        'surname': 'repe'
    },
    {
        'name': 'vedant1',
        'surname': 'repe1'
    },
{
        'name': 'vedant2',
        'surname': 'repe2'
    }
]

database = client['myinfo_many']
collection = database['many_entry']
collection.insert_many(data)