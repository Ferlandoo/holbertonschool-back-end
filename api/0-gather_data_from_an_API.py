#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    users = response.json()
    user = users[0]
    user_id = user.get('id')
    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)
    todos = response.json()
    completed_tasks = []
    for task in todos:
        if task.get('userId') == user_id:
            if task.get('completed') is True:
                completed_tasks.append(task.get('title'))
    print('Employee {} is done with tasks({}/{}):'.format(
        user.get('name'), len(completed_tasks), len(todos)))
    for task in completed_tasks:
        print('\t {}'.format(task))
