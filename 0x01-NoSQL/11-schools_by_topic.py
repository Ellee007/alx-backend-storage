#!/usr/bin/env python3
"""
This is our module
"""


def schools_by_topic(mongo_collection, topic):
    """
    This is a function
    """
    mylist = mongo_collection.find()
    returnedlist = []
    for elem in mylist:
        if topic in elem.get("topics"):
            returnedlist.append(elem)
    return returnedlist
