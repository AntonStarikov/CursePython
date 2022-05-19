import redis
import json

red = redis.Redis(
    host='redis-16456.c1.asia-northeast1-1.gce.cloud.redislabs.com',
    port=16456,
    password='5ysiDjs2cgiXa3bKLDA8dclvoCwhkSfm'
)
cont = True

while cont:
    action = input('action:\t')
    if action == 'write':
        name = input('name:\t')
        phone = input('phone:\t')
        red.set(name, phone)
    elif action == 'read':
        name = input('name:\t')
        phone = red.get(name)
        if phone:
            print(f'{name}\'s phone is {str(phone)}')
    elif action == 'delete':
        name = input('name:\t')
        phone = red.delete(name)
        if phone:
            print(f"{name}'s phone is deleted")
        else:
            print(f"Not found {name}")
    elif action == 'stop':
        break