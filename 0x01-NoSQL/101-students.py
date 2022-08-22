#!/usr/bin/env python3
""" Module to manage a Mondo database """



def top_students(mongo_collection):
    """
        Function that returns all students sorted by average score
    """
    pipeline = [
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ]
    return mongo_collection.aggregate(pipeline)
