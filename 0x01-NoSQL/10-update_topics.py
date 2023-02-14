#!/usr/bin/env python3
""" python script using PyMongo """


def update_topics(mongo_collection, name, topics):
    """ Changes field in document based on name field """
    n_field = {"name": name}
    v_field = {"$set": {"topics": topics}}
    mongo_collection.update_many(n_field, v_field)
