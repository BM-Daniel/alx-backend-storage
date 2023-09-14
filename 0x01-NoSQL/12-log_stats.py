#!/usr/bin/env python3

'''
Write a Python script that provides some stats about Nginx logs stored in
MongoDB
'''

import pymongo


if __name__ == "__main__":
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    nginx_logs = client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    logs_number = nginx_logs.count_documents({})
    print(f"{logs_number} logs")

    print("Methods:")
    for i in methods:
        method_number = nginx_logs.count_documents({'method': i})
        print(f"\tmethod {i}: {method_number}")

    verify = nginx_logs.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{verify} status check")
