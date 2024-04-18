#!/usr/bin/python3
"""Export data in the JSON format"""


import requests
import json

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    todos = response.json()
    data = {}
    for user in users:
        data[user.get("id")] = [{
            "username": user.get("username"),
            "task": todo.get("title"),
            "completed": todo.get("completed")
        } for todo in todos if user.get("id") == todo.get("userId")]
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)
