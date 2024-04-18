#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    data = response.json()
    user_id = sys.argv[1]
    employee_name = ""
    for user in data:
        if user.get('id') == int(user_id):
            employee_name = user.get('name')
            break
    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)
    data = response.json()
    total_tasks = 0
    done_tasks = 0
    tasks = []
    for task in data:
        if task.get('userId') == int(user_id):
            total_tasks += 1
            if task.get('completed'):
                done_tasks += 1
                tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                done_tasks, total_tasks))
    for task in tasks:
        print("\t {}".format(task))
