import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from gradebook.models import Student, Course, Enrollment
from gradebook.storage import save_data


def seed_data():

    students = [
        Student(1, "Johanne"),
        Student(2, "Samaira"),
        Student(3, "Alizeh")
    ]

    courses = [
        Course("CS771", "Introduction to ML"),
        Course("MTH111", "Linear Algebra")
    ]

    enrollments = [
        Enrollment(1, "CS771", [90, 85]),
        Enrollment(1, "MTH111", [88, 92]),
        Enrollment(2, "CS771", [78, 92]),
        Enrollment(3, "MTH111", [95, 89])
    ]

    data = {
        "students": [
            {
                "id": student.id,
                "name": student.name
            }
            for student in students
        ],

        "courses": [
            {
                "code": course.code,
                "title": course.title
            }
            for course in courses
        ],

        "enrollments": [
            {
                "student_id": enrollment.student_id,
                "course_code": enrollment.course_code,
                "grades": enrollment.grades
            }
            for enrollment in enrollments
        ]
    }

    save_data(data)

    print("Sample data creation successful")
    print("3 students added")
    print("2 courses added")
    print("4 enrollments created")
    print("Sample grades added")
    print("Data saved to data/gradebook.json")


if __name__ == "__main__":
    seed_data()