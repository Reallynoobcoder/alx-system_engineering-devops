#!/usr/bin/python3
"""Fetch TODO list data for all employees and export it in JSON format."""
import json
import requests

if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    all_tasks = {}
    for user in users:
        user_id = user["id"]
        user_tasks = [{"username": user["username"],
                       "task": task["title"],
                       "completed": task["completed"]}
                      for task in todos if task["userId"] == user_id]
        all_tasks[user_id] = user_tasks

    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(all_tasks, jsonfile)
