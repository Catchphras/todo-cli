# To-Do List CLI App

A command-line To-Do List application built with Python that allows users to manage tasks and track completed items using JSON file storage.

---

## 🚀 Features

- Add new tasks  
- View all tasks  
- Remove tasks by index  
- Mark tasks as completed  
- View completed tasks  
- Persistent storage using JSON files  

---

## 🛠️ Tech Stack

- Python  
- JSON (for data storage)  
- pathlib (for file handling)  

---

## 📂 Project Structure

```

todo-cli/
│── main.py
│── README.md
│── tasks.json (auto-created)
│── completed_tasks.json (auto-created)

````

---

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Catchphras/todo-cli.git
````

### 2. Navigate into the project folder

```bash
cd todo-cli
```

### 3. Run the application

```bash
python main.py
```

---

## 💡 How It Works

* Tasks are stored in `tasks.json`
* Completed tasks are stored in `completed_tasks.json`
* The app reads and writes to these files to maintain data between sessions

---

## 🧪 Example Usage

```
1. Add task
2. View tasks
3. Remove task
4. Mark a task as complete
5. View completed tasks
(Enter 'q' to quit)

Enter the number of an option you want: 1

Enter the task: Study Python
Task added successfully
```

---

## ⚠️ Notes

* Input for removing tasks should match the index shown when viewing tasks
* Basic validation is implemented, but invalid inputs may still cause errors

---

## 🎯 What I Learned

* Working with JSON data in Python
* File handling using `pathlib`
* Structuring programs using functions
* Building an interactive CLI application

---

## 📌 Future Improvements

* Improve error handling
* Add task priorities
* Add due dates
* Improve user interface
* Refactor code for better structure

---

## 🔗 GitHub Repository

[https://github.com/Catchphras/todo-cli.git](https://github.com/Catchphras/todo-cli.git)

```

---
