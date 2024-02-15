# import random
import redis

with redis.Redis() as redis_client:
    print(redis_client.rpop('queue'))
