#!/usr/bin/env python3

'''
Write a Python function that lists all documents in a collection
'''


def list_all(mongo_collection):
    '''Python function'''
    documents = []

    for i in mongo_collection.find({}):
        documents.append(i)

    return documents
