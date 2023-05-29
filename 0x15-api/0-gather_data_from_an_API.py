#!/usr/bin/python3

"""
Requesting information from API
"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users_url = url + f"users/{sys.argv[1]}"
    todos_url = url + f"todos"

    users = requests.get(users_url).json()
    todos = requests.get(todos_url, params={"userId": sys.argv[1]}).json()

    total_task = len(todos)
    completed = 0
    titles = []
    for todo in todos:
        if todo['completed']:
            completed += 1
            titles.append(todo['title'])
    result = f"Employee {users['name']} is done with tasks\
                    ({completed}/{total_task})"
    print(result)
    for title in titles:
        print(f"\t {title}")
