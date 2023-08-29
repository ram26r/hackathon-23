import pymongo
from pymongo import MongoClient

def connect_to_db(url,host,username,password):
    try:
        cluster =  MongoClient("<url here>")
        return cluster
    except:
        return None
    
    
def get_data(db_name,collection_name,column_name,row_name):
    try:
       cluster =  MongoClient("<url here>")
       db = cluster[db_name]
       collection = db[collection_name]
       result = collection.find({column_name:row_name})
       return result
    except:
        return None