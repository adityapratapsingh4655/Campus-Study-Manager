import json

FILE_NAME = "data.json"


def load_data():
    try:
        file = open(FILE_NAME, "r")
        data = json.load(file)
        file.close()
        return data
    except:
        return {
            "tasks": [],
            "marks": []
        }


def save_data(data):
    file = open(FILE_NAME, "w")
    json.dump(data, file, indent=4)
    file.close()


def add_task(data):
    task = input("Enter task: ")

    new_task = {
        "task": task,
        "completed": False
    }

    data["tasks"].append(new_task)
    print("Task added successfully!")


def show_tasks(data):
    if len(data["tasks"]) == 0:
        print("No tasks found.")
        return

    print("\n--- Tasks ---")

    for i in range(len(data["tasks"])):
        task = data["tasks"][i]

        if task["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        print(i + 1, ".", task["task"], "-", status)


def complete_task(data):
    show_tasks(data)

    if len(data["tasks"]) == 0:
        return

    number = int(input("Enter task number to complete: "))

    if number >= 1 and number <= len(data["tasks"]):
        data["tasks"][number - 1]["completed"] = True
        print("Task completed!")
    else:
        print("Invalid task number.")


def delete_task(data):
    show_tasks(data)

    if len(data["tasks"]) == 0:
        return

    number = int(input("Enter task number to delete: "))

    if number >= 1 and number <= len(data["tasks"]):
        data["tasks"].pop(number - 1)
        print("Task deleted!")
    else:
        print("Invalid task number.")


def add_marks(data):
    subject = input("Enter subject name: ")
    marks = float(input("Enter marks: "))

    record = {
        "subject": subject,
        "marks": marks
    }

    data["marks"].append(record)

    print("Marks added successfully!")


def show_marks(data):
    if len(data["marks"]) == 0:
        print("No marks found.")
        return

    print("\n--- Academic Records ---")

    for record in data["marks"]:
        print(record["subject"], ":", record["marks"])


def calculate_average(data):
    if len(data["marks"]) == 0:
        print("No marks available.")
        return

    total = 0

    for record in data["marks"]:
        total = total + record["marks"]

    average = total / len(data["marks"])

    print("Average marks:", average)


data = load_data()

while True:
    print("\n==============================")
    print("     CAMPUS STUDY MANAGER")
    print("==============================")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Add Marks")
    print("6. Show Marks")
    print("7. Calculate Average")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task(data)
        save_data(data)

    elif choice == "2":
        show_tasks(data)

    elif choice == "3":
        complete_task(data)
        save_data(data)

    elif choice == "4":
        delete_task(data)
        save_data(data)

    elif choice == "5":
        add_marks(data)
        save_data(data)

    elif choice == "6":
        show_marks(data)

    elif choice == "7":
        calculate_average(data)

    elif choice == "8":
        save_data(data)
        print("Thank you for using Campus Study Manager!")
        break

    else:
        print("Invalid choice. Please try again.")