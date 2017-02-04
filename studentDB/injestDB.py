import pymongo
from pymongo import MongoClient
import datetime
import csv
import sys


def injestCsv(file,posts):
    f = open(file,"r") # Opening the csv file
    reader = csv.DictReader(f)
    headers = reader.fieldnames
    for line in reader:
        data = {} # creating an empty data field
        for h in headers:
            print(h+" :"+line[h])
            data[h] = line[h]
        # Insert the data into the collection
        posts.insert_one(data)

fileinput = "t1.csv"



if __name__ == "__main__":
    print("Hello world!")

    client = MongoClient()

    # Accessing the db
    db = client['big-database']

    # Accessing the collection
    collection = db['csv-collection']

    # accessing the posts object
    posts = db.posts

    # injesting the csv file into the collection. Headers have to be present in the csv file
    injestCsv(fileinput,posts)

    print("Done!")
