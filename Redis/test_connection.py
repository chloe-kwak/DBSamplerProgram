import os

import redis

HOST ='dbsampler-redis.e3dj3z.ng.0001.apn2.cache.amazonaws.com' #Primary Endpoint value 
r = redis.Redis(host=HOST)

r.ping()

print("Connected to Redis!")
