#!/usr/bin/python3
"""Export data in the CSV format"""


import requests
import sys
import csv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}"\
        .format(sys.argv[1])
    response = requests.get(url)
    user = response.json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}"\
        .format(sys.argv[1])
    response = requests.get(url)
    todos = response.json()
    with open("{}.csv".format(sys.argv[1]), "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow([sys.argv[1], user.get("username"),
                          todo.get("completed"), todo.get("title")])
         for todo in todos]
