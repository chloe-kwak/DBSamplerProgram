from entities import Restaurant, Review

import json
import os

import redis

#HOST = os.environ["REDIS_HOSTNAME"].replace(":6379", "")
HOST ='dbsampler-new.e3dj3z.ng.0001.apn2.cache.amazonaws.com'
r = redis.Redis(host=HOST)


class ObjectEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


def store_restaurant_summary_in_cache(restaurant):
    key = restaurant.name
    r.set(key, json.dumps(restaurant, cls=ObjectEncoder), ex=900)

    return True


def fetch_restaurant_summary_from_cache(restaurant_name):
    response = r.get(restaurant_name)
    if response:
        data = json.loads(response)
        restaurant = Restaurant(data)
        restaurant.reviews = [Review(review) for review in data["reviews"]]
        return restaurant
    return None
