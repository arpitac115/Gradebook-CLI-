# Gradebook CLI

A simple Python command-line application to manage students, courses, enrollments and grades.

## Features
- Add students and courses.
- Enroll students in courses.
- Add and view grades.
- Calculate course averages and GPA.
- Store data in JSON files.

## Project Structure

```text
gradebook/
├── main.py
├── gradebook/
│   ├── __init__.py
│   ├── models.py
│   ├── storage.py
│   └── service.py
├── data/
│   └── gradebook.json
├── logs/
│   └── app.log
├── tests/
│   └── test_service.py
├── scripts/
│   └── seed.py
└── README.md
```

## Setup

Clone the repository:

```bash
git clone <https://github.com/arpitac115/Gradebook-CLI-.git>
cd gradebook
```

Create and activate a virtual environment:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

No external packages are required.

## Run Sample Data

```bash
python scripts/seed.py
```

This creates 3 students, 2 courses, enrollments and sample grades in `data/gradebook.json`.

## Usage

Run commands from the project folder.

| Operation | Command |
|---|---|
| Add student | `python main.py add-student --name "John"` |
| Add course | `python main.py add-course --code CS101 --title "Intro to CS"` |
| Enroll | `python main.py enroll --student-id 1 --course CS101` |
| Add grade | `python main.py add-grade --student-id 1 --course CS101 --grade 95` |
| List students | `python main.py list students` |
| List courses | `python main.py list courses` |
| List enrollments | `python main.py list enrollments` |
| Calculate average | `python main.py avg --student-id 1 --course CS101` |
| Calculate GPA | `python main.py gpa --student-id 1` |

### Example Output

```text
Student added successfully. ID: 4

Average for student 1 in CS101: 87.50

GPA for student 1: 88.75
```

## Run Tests

```bash
python -m unittest discover -s tests -v
```

Tests cover student creation, grade addition, average calculation and an error case.

## Design decisions & limitations

- Uses JSON files for data storage.
- Uses separate modules for models, storage and business logic.
- Uses a simple mean of course averages for GPA.
- Supports numeric grades between 0 and 100.
- Provides a command-line interface only.


____________________
Student Gradebook – Command Line Application
A Python-based CLI tool for maintaining student records, managing courses, recording marks and calculating academic averages.
Main Functions
Register students and create courses.
Add students to courses.
Record and store student grades.
Display student, course and enrollment details.
Calculate course averages and student GPA.
Save application data in JSON format.
Folder Layout
gradebook/
├── main.py
├── gradebook/
│   ├── __init__.py
│   ├── models.py
│   ├── storage.py
│   └── service.py
├── data/
│   └── gradebook.json
├── logs/
│   └── app.log
├── scripts/
│   └── seed.py
├── tests/
│   └── test_service.py
└── README.md
Getting Started
Make sure Python is installed, then create a virtual environment:
python -m venv venv
Activate it:
Windows
venv\Scripts\activate
macOS / Linux
source venv/bin/activate
The project uses Python's standard library, so no additional packages are needed.
Prepare Example Records
Run the seed script from the main project directory:
python scripts/seed.py
This adds sample students, courses, enrollments and grades to the JSON data file.
Running the Application
Use the following commands from the project directory:
# Register a student
python main.py add-student --name "Maya"

# Create a course
python main.py add-course --code IT202 --title "Programming Basics"

# Enroll a student
python main.py enroll --student-id 1 --course IT202

# Record a grade
python main.py add-grade --student-id 1 --course IT202 --grade 89

# Display records
python main.py list students
python main.py list courses
python main.py list enrollments

# Find a course average
python main.py avg --student-id 1 --course IT202

# Find a student's GPA
python main.py gpa --student-id 1
Running Unit Tests
Execute the test suite using:
python -m unittest discover -s tests -v
The tests check student creation, grade recording, average calculations and error handling.
Design Decisions & Limitations
JSON is used for simple local data storage.
Models, file operations and application logic are kept in separate modules.
GPA is calculated as the average of the student's course averages.
Grades must be numeric values from 0 to 100.
The application runs through a command-line interface and does not use a graphical interface.
