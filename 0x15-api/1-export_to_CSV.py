#!/usr/bin/python3
"""Fetch & display TODO list progress and export data in CSV format."""
import requests
import csv
from sys import argv

if __name__ == "__main__":
    employee_id = int(argv[1])
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos",
                         params={"userId": employee_id}).json()

    with open(f"{employee_id}.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, user['username'],
                            task['completed'], task['title']])
