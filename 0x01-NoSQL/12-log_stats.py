#!/usr/bin/env python3
""" Module to manage a Mondo database """
from pymongo import MongoClient


if __name__ == "__main__":
    """
        Script that provides some stats about Nginx logs stored in MongoDB
    """
    client = MongoClient('mongodb://localhost:27017')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    nginx = client.logs.nginx

    print("{} logs".format(nginx.count_documents({})))
    print("Methods:")

    for method in methods:
        print("\tmethod {}: {}".format(
            method, nginx.count_documents({"method": method})))

    print("{} status check".format(
        nginx.count_documents({"method": "GET", "path": "/status"})))
