#!/usr/bin/env python3
""" Module to manage a Mondo database """


def insert_school(mongo_collection, **kwargs):
    """ 
        Function that inserts a new document in a collection based on kwargs
    """
    new = mongo_collection.insert_one(kwargs)
    return new.inserted_id
