# import random
import redis

with redis.Redis() as redis_client:
    print("Random number was: ", redis_client.brpop('queue'))
