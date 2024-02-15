# import redis

# with redis.Redis() as redis_client:
#     # redis_client.set('counter', 1)
#     # print(redis_client.keys('a'))
#     for key in redis_client.scan_iter('*', count=100):
#         print(key, redis_client.get(key))
from datetime import datetime
import sys


def func(n):
    res = []
    cnt = 0
    while cnt < n:
        res.append(cnt)
        cnt += 1
    return res


# print(func(10))


def funs2():
    print("go")
    yield 1
    print("dai esho")
    yield 2
    print("ushli")


def func3(n):
    cnt = 0
    while cnt < n:
        yield cnt
        cnt += 1

# print(func(10)) 
# print(funs2())

# c = funs2()
# print(next(c))
# print("kak good be in main flow program")
# print(next(c))

d = func3(10)
print(3 in d)
print(list(d))



start = datetime.now()
print(f"Start working at: {start}")
d = func3(100_000)
try:
    while True:
        next(d)
except:
    print("the end")

print(f"size of object: {sys.getsizeof(d)}")
print(f"Finish at: {datetime.now()}. Working time: {datetime.now() - start}")

d = func3(10)
print(next(d))
print(next(d))
print(range(10))
