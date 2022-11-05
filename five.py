import connection as c

print(c.db)
database = c.client['basic']
collection = database['basic1']

data = [
    {
        "item": "canvas",
        "qty": 100,
        "size": {"h": 28, "w": 35.5, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "journal",
        "qty": 25,
        "size": {"h": 14, "w": 21, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "mat",
        "qty": 85,
        "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "mousepad",
        "qty": 25,
        "size": {"h": 19, "w": 22.85, "uom": "cm"},
        "status": "P",
    },
    {
        "item": "notebook",
        "qty": 50,
        "size": {"h": 8.5, "w": 11, "uom": "in"},
        "status": "P",
    },
    {
        "item": "paper",
        "qty": 100,
        "size": {"h": 8.5, "w": 11, "uom": "in"},
        "status": "D",
    },
    {
        "item": "planner",
        "qty": 75,
        "size": {"h": 22.85, "w": 30, "uom": "cm"},
        "status": "D",
    },
    {
        "item": "postcard",
        "qty": 45,
        "size": {"h": 10, "w": 15.25, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "sketchbook",
        "qty": 80,
        "size": {"h": 14, "w": 21, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "sketch pad",
        "qty": 95,
        "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
        "status": "A",
    },
]

# collection.insert_many(data)

"""
#to select all data from batabase
record=collection.find()
for i in record:
    print(i)
"""
"""
# similar to ==
record = collection.find({'status':'A'})
for i in record:
    print(i)
"""

"""
# return all data contains status==a or ==p
record = collection.find({'status': {"$in": ['A', 'P']}})
for i in record:
    print(i)
"""
"""
# greater than
record = collection.find({'status': {"$gt":'C'}})
for i in record:
    print(i)
"""

"""
# greater than equal to
record = collection.find({'status': {"$gte":'C'}})
for i in record:
    print(i)
"""

"""
# and conditions
record = collection.find({'status': {"$gte":'C'}, 'item': 'paper'})
for i in record:
    print(i)
"""

"""
# or condition
record = collection.find({'$or':[{'status': 'A'}, {'item': 'paper'}]})
for i in record:
    print(i)
"""
"""
# update  
collection.update_one({'status': 'Z'}, {'$set':{'status': 'A'}})
collection.update_many({'status': 'Z'}, {'$set':{'status': 'A'}})
"""

"""
# delete 
collection.delete_one({'item': 'sketchbook', 'qty': 80,})
collection.delete_many({'item': 'sketchbook', 'qty': 80,})
"""
