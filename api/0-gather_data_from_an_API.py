#!/usr/bin/python3
import sys
import requests

def get_employee_info(employee_id):
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/'
    response = requests.get(url)
    return response.json()

def get_employee_todos(employee_id):
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response = requests.get(url)
    return response.json()

def main(employee_id):
    employee = get_employee_info(employee_id)
    employee_name = employee.get("name")

    emp_todos = get_employee_todos(employee_id)
    tasks = {todo.get("title"): todo.get("completed") for todo in emp_todos}

    total_tasks = len(tasks)
    completed_tasks = [completed for completed in tasks.values() if completed]
    completed_tasks_count = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks({completed_tasks_count}/{total_tasks}):")
    for title, completed in tasks.items():
        if completed:
            print(f"\t {title}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            employee_id = int(sys.argv[1])
            main(employee_id)
        except ValueError:
            print("Usage: ./script_name.py <employee_id> (employee_id must be an integer)")
    else:
        print("Usage: ./script_name.py <employee_id>")
        