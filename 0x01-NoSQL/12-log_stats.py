#!/usr/bin/env python3

'''
Write a Python script that provides some stats about Nginx logs stored in
MongoDB
'''

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_database = client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    log_count = nginx_database.count_documents({})
    print(f'{log_count} logs')

    print('Methods:')
    for method in methods:
        count_method = nginx_database.count_documents({'method': method})
        print(f'\tmethod {method}: {count_method}')

    check = nginx_database.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f'{check} status check')
