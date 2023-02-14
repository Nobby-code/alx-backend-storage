#!/usr/bin/env python3
""" insertion using PyMongo """


def insert_school(mongo_collection, **kwargs):
    """ Insertng new document in collection based on kwargs """
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
