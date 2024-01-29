#!/usr/bin/python3
"""Fetch & display TODO list progress and export data in JSON format."""
import json
import requests
from sys import argv

if __name__ == "__main__":
    employee_id = int(argv[1])
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos",
                         params={"userId": employee_id}).json()

    tasks = [{"task": task["title"], "completed": task["completed"],
              "username": user["username"]} for task in todos]

    json_data = {str(employee_id): tasks}

    with open(f"{employee_id}.json", 'w') as jsonfile:
        json.dump(json_data, jsonfile)
