#!/usr/bin/env python3
"""
This is our python module
"""
from pymongo import MongoClient
"""
This is our pymongo module
"""

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    count = collection.count_documents({})
    print(count, "logs")
    print("Methods:")

    countget = collection.count_documents({"method": "GET"})
    print("\tmethod GET:", countget)
    countget = collection.count_documents({"method": "POST"})
    print("\tmethod POST:", countget)
    countget = collection.count_documents({"method": "PUT"})
    print("\tmethod PUT:", countget)
    countget = collection.count_documents({"method": "PATCH"})
    print("\tmethod PATCH:", countget)
    countget = collection.count_documents({"method": "DELETE"})
    print("\tmethod DELETE:", countget)

    countget = collection.count_documents({"method": "GET", "path": "/status"})
    print(countget, "status check")
