import sqlite3
import redis


def get_my_friends():
    connection = sqlite3.connect(database="database.db")
    cursor = connection.cursor()

    redis_client = redis.Redis()

    cache_value = redis_client.get('user_friends')
    if cache_value is not None:
        return cache_value

    cursor.execute("SELECT Id, name FROM users;")
    result = cursor.fetchall()
    redis_client.set('user_friends', str(result), ex=10)

    cursor.close()
    redis_client.close()

    return result


if __name__ == '__main__':
    print(get_my_friends())
