Student Management System

How to run the program?

Open Python (IDLE, VS Code, or console).

Copy and paste the code into a file named, for example:

-Students.py
-Run the program.
-A menu will appear on the screen.
-Enter a number (1–6) and press Enter to use the system.
-Included Functions

🔹1. Register
Allows you to add a new student by entering:

-ID
-Name
-Age
-Grade
-Status

-Displays all students saved in the system.

🔹3. Search

Allows you to find a student by:
-ID
-Name

🔹4. Update
-Allows you to modify a student's data using their ID.
🔹 5. Delete
- Deletes a student using their ID.
🔹 6. Exit
- Closes the program.

* Example of use

Step 1: Registor student
Option: 1
- ID: 15876587
- Name: Jaime
- Age: 17
- Course: Python
- Status: active
Result:
Student added
Step 2: Show students
Option: 2
Result:
{'id': '1', 'name': 'Jaime', 'age': '17', 'course': 'Python', 'status': 'active'}
Step 3: Search student
Option: 3
Enter ID or name: Jaime
Result:
{'id': '1', 'name': 'Jaime', 'age': '17', 'course': 'Python', 'status': 'active'}
Step 4: Update student
Option: 4

- ID to update: 1

- New name: Jaime Pérez

- New age: 18

- New course: Java

- New status: active

- Result:

Updated

Step 5: Delete student

Option: 5

- ID to delete: 1

Result:

Deleted

Conclusion

The program allows for easy student management through an interactive menu, using lists and dictionaries in Python.
