import os
import time
import json

states = [" [ ] ", " [x] "]

if os.path.isfile("data.json"):
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
else:
    data = {}
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file)

def cleanscreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def main():
    cleanscreen()
    print("Your tasks:")
    print("")
    for task, state in data.items():
        print(state, task)
    print("""
1. Add Task   | 2. Remove Task
3. Check Task | 4. Uncheck Task
              | 5. Exit
    """)
    try:
        option = int(input("---> "))
    except ValueError:
        print("Error, insert a number")
        time.sleep(1)
    else:
        if option == 1:
            add()
        elif option == 2:
            remove()
        elif option == 3:
            check()
        elif option == 4:
            uncheck()
        elif option == 5:
            quit()

def add():
    cleanscreen()
    task = input("Enter the new task name: ")
    data[task] = states[0]
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file)
    time.sleep(1)

def remove():
    cleanscreen()
    task = input("Enter the task name to remove: ")
    try:
        data.pop(task)
    except KeyError:
        print("Error, insert a task name not a number")
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file)
    time.sleep(1)

def check():
    cleanscreen()
    task = input("Enter the task name to check: ")
    if task in data:
        data[task] = states[1]
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data, file)
    else:
        print("Task does not exist")
    time.sleep(1)

def uncheck():
    cleanscreen()
    task = input("Enter the task name to uncheck: ")
    if task in data:
        data[task] = states[0]
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data, file)
    else:
        print("Task does not exist")
    time.sleep(1)

while True:
    main()
