#!/usr/bin/python3
"""
Using this REST API for a given employee ID
returns information about his/her TODO list progress
"""
import urllib.request
import json

def get_employee_tasks(employee_id):
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    employee_name = data[0]["userId"]
    total_tasks = len(data)
    done_tasks = sum(1 for task in data if task["completed"])

    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for task in data:
        if task["completed"]:
            print(f"\t {task['title']}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_tasks(employee_id)
