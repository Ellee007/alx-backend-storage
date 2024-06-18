#!/usr/bin/env python3
"""
This is our python module
"""


def update_topics(mongo_collection, name, topics):
    """
    This is update function
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
