#!/usr/bin/env python3
"""
This is our python module
"""

def list_all(mongo_collection):
    """
    This function lists all collections
    """
    return mongo_collection.find()
