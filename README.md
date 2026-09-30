# Campus Study Manager

A simple **Python-based command-line application** designed to help students manage their daily tasks and academic marks in one place.

The project uses a **JSON file** to store data, so tasks and marks remain saved even after the program is closed.

## Features

* Add new study tasks
* View all tasks
* Mark tasks as completed
* Delete tasks
* Add marks for different subjects
* View academic records
* Calculate average marks
* Automatically save data to a JSON file
* Load previously saved data when the program starts
* Simple menu-driven command-line interface

## Technologies Used

* **Python**
* **JSON**
* Python `json` module
* Command-line interface (CLI)

## Concepts Used

This project demonstrates several basic Python programming concepts:

* Variables and data types
* Input and output
* Conditional statements (`if`, `elif`, `else`)
* `while` loops
* `for` loops
* Functions
* Lists
* Dictionaries
* Indexing
* `append()` and `pop()`
* File handling
* JSON data storage
* Exception handling using `try-except`
* Arithmetic operations
* Type conversion using `int()` and `float()`

## Project Structure

```text
Campus-Study-Manager/
│
├── main.py
├── data.json
└── README.md
```

### `main.py`

Contains the complete Python program and all the functions required to manage tasks and academic records.

### `data.json`

Stores the tasks and marks entered by the user.

Example:

```json
{
    "tasks": [
        {
            "task": "Complete Python assignment",
            "completed": false
        }
    ],
    "marks": [
        {
            "subject": "Python",
            "marks": 85
        }
    ]
}
```

### `README.md`

Contains information about the project, its features, technologies, and usage.

## How to Run

### 1. Install Python

Make sure Python is installed on your computer.

You can check by running:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### 3. Open the Project Folder

```bash
cd Campus-Study-Manager
```

### 4. Run the Program

```bash
python main.py
```

## How to Use

When the program starts, it displays the following menu:

```text
==============================
     CAMPUS STUDY MANAGER
==============================
1. Add Task
2. Show Tasks
3. Complete Task
4. Delete Task
5. Add Marks
6. Show Marks
7. Calculate Average
8. Exit
```

### Add Task

Select option `1` and enter the task you want to add.

Example:

```text
Enter task: Complete Python assignment
Task added successfully!
```

### Show Tasks

Select option `2` to view all saved tasks.

Example:

```text
--- Tasks ---
1 . Complete Python assignment - Pending
2 . Study for mathematics exam - Completed
```

### Complete Task

Select option `3` and enter the task number.

```text
Enter task number to complete: 1
Task completed!
```

### Delete Task

Select option `4` and enter the task number you want to delete.

```text
Enter task number to delete: 2
Task deleted!
```

### Add Marks

Select option `5` and enter the subject and marks.

```text
Enter subject name: Python
Enter marks: 85
Marks added successfully!
```

### Show Marks

Select option `6` to display academic records.

```text
--- Academic Records ---
Python : 85.0
Mathematics : 78.0
```

### Calculate Average

Select option `7` to calculate the average of all stored marks.

```text
Average marks: 81.5
```

### Exit

Select option `8` to save the data and exit the application.

## Data Storage

The project stores information in `data.json`.

The JSON file contains two main sections:

```text
tasks
marks
```

Tasks contain:

```text
task
completed
```

Marks contain:

```text
subject
marks
```

This allows the program to preserve user data between different executions.

## Functions

The project is divided into separate functions to make the code easier to understand and maintain.

| Function              | Purpose                           |
| --------------------- | --------------------------------- |
| `load_data()`         | Loads saved data from `data.json` |
| `save_data()`         | Saves current data to `data.json` |
| `add_task()`          | Adds a new task                   |
| `show_tasks()`        | Displays all tasks                |
| `complete_task()`     | Marks a task as completed         |
| `delete_task()`       | Deletes a task                    |
| `add_marks()`         | Adds academic marks               |
| `show_marks()`        | Displays academic records         |
| `calculate_average()` | Calculates average marks          |

## Future Improvements

Possible improvements for future versions include:

* Edit existing tasks
* Add task deadlines
* Add task priorities
* Search for tasks
* Delete academic records
* Calculate percentage and grade
* Add subject-wise performance tracking
* Add input validation for invalid marks
* Create a graphical user interface (GUI)
* Add user accounts
* Generate academic performance reports

## Limitations

This is a beginner-level command-line project. The current version:

* Does not have user authentication.
* Uses a local JSON file for storage.
* Does not validate every possible invalid input.
* Does not provide a graphical interface.
* Calculates a simple average without considering different subject weightages.

## Author

Name: Aditya Pratap Singh

Reg No: 26BHI10041

