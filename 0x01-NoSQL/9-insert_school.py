#!/usr/bin/env python3
"""
This is our python module
"""


def insert_school(mongo_collection, **kwargs):
    """
    function that inserts new objs in collection
    """
    return mongo_collection.insert_one(kwargs).inserted_id
