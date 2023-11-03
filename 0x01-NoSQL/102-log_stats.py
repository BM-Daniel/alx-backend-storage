#!/usr/bin/env python3

'''
Improve 12-log_stats.py by adding the top 10 of the most present IPs in the
collection nginx of the database logs:
'''

from pymongo import MongoClient


def nginx_stats_check():
    '''
    Nginx function
    '''
    client = MongoClient()
    collection = client.logs.nginx

    number_of_documents = collection.count_documents({})
    print("{} logs".format(number_of_documents))
    print("Methods:")

    methods_list = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods_list:
        method_count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, method_count))

    status = collection.count_documents({"method": "GET", "path": "/status"})

    print("{} status check".format(status))
    print("IPs:")

    top_IPs = collection.aggregate([
        {"$group": {
            "_id": "$ip",
            "count": {"$sum": 1}
        }},
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}
    ])

    for top_ip in top_IPs:
        count = top_ip.get("count")
        ip_address = top_ip.get("ip")

        print("\t{}: {}".format(ip_address, count))


if __name__ == "__main__":
    nginx_stats_check()
