## Description

This project is a command-line Todo application built using Python and object-oriented programming principles. The application allows users to add, view, update, and delete todo items through a simple text-based menu. All tasks are stored locally using a JSON file, which ensures that todo data is preserved even after the program is closed and restarted. The project focuses on practicing OOP design, file handling, and persistent data storage without using a database.

## JSON and Object Conversion

When the application starts, it attempts to open the `todos.json` file and read its contents. The JSON data is deserialized using Python’s `json` module and loaded into a Python list, where each item represents a todo task as a dictionary. This list is stored as an attribute of the `TodoList` class and is used throughout the program as the in-memory representation of all tasks.

Whenever a task is added, updated, or deleted, the in-memory Python data structure is serialized back into JSON format and written to the `todos.json` file. This continuous conversion between JSON data and Python objects ensures that all changes are saved immediately and reloaded automatically the next time the application runs.
