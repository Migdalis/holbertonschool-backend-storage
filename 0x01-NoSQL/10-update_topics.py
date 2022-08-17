#!/usr/bin/env python3
""" Module to manage a Mondo database """


def update_topics(mongo_collection, name, topics):
    """ 
        Function that changes all topics of a school document based on the name
    """
    update = mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
