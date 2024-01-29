#!/usr/bin/python3
"""Fetch & display TODO list progress for given employee ID using REST API."""
import requests
from sys import argv


if __name__ == "__main__":
    employee_id = int(argv[1])
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    for user in users:
        if user.get("id") == employee_id:
            employee = user

    tasks = []
    for task in todos:
        if task.get("userId") == employee_id:
            tasks.append(task)

    completed_tasks = []
    for task in tasks:
        if task.get("completed"):
            completed_tasks.append(task)

    print("Employee {} is done with tasks({}/{}):".format(employee.get('name'),
                                                          len(completed_tasks),
                                                          len(tasks)))

    for task in completed_tasks:
        print("\t " + task.get("title"))
