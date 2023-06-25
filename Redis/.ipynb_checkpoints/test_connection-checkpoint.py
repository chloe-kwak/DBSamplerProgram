import os

import redis

#HOST = os.environ["REDIS_HOSTNAME"].replace(":6379", "")
#HOST ='dbsampler-new.e3dj3z.ng.0001.apn2.cache.amazonaws.com'
HOST = 'dbsampler-redis.e3dj3z.ng.0001.apn2.cache.amazonaws.com'
r = redis.Redis(host=HOST)

r.ping()

print("Connected to Redis!")
