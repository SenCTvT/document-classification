import pymongo
import urllib
from pymongo import MongoClient
# setting connection to remote client
client = MongoClient("mongodb+srv://sen:hellosen@cluster0-pmuan.mongodb.net/test?retryWrites=true&w=majority")
#configuring database
db = client['test']
#configuring collection
collection = db['Invoice']

print(collection)

# create the data dictionary as per requirement

data = {
     'name' : 'Soumyojit',
     'Age' : '24'
}


def insert_to_db(data):
    result = collection.insert_one(data)
    if result.acknowledged:
        print("Data added successfully")
    else:
        print("Some error occured in insertion, " + result)


def get_all_records():
    results = collection.find({})
    #return results
    for i in results:
        print(i)


#data = get_all_records()
get_all_records()
