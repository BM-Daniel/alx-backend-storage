#!/usr/bin/env python3

'''
Write a Python function that returns the list of school having a specific topic
'''

import pymongo


def schools_by_topic(mongo_collection, topic):
    '''Python function'''
    schools = []

    for i in mongo_collection.find({'topics': topic}):
        schools.append(i)

    return schools
