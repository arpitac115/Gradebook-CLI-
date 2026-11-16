import argparse
import logging
from pathlib import Path

from gradebook.service import (
    add_student,
    add_course,
    enroll,
    add_grade,
    list_students,
    list_courses,
    list_enrollments,
    compute_average,
    compute_gpa
)

Path("logs").mkdir(parents=True, exist_ok=True)
 
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

def parse_grade(value):
    try:
        grade = float(value)

        if not 0 <= grade <= 100:
            raise ValueError

        return grade

    except ValueError:
        raise ValueError(
            "Invalid grade. Please enter a number between 0 and 100."
        )

def create_parser():
    parser = argparse.ArgumentParser(
        description="Gradebook CLI - Manage students, courses and grades."
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    student_parser = subparsers.add_parser(
        "add-student",
        help="Add a new student"
    )

    student_parser.add_argument(
        "--name",
        required=True,
        help="Name of the student"
    )

    course_parser = subparsers.add_parser(
        "add-course",
        help="Add a new course"
    )

    course_parser.add_argument(
        "--code",
        required=True,
        help="Course code"
    )

    course_parser.add_argument(
        "--title",
        required=True,
        help="Course title"
    )

    enroll_parser = subparsers.add_parser(
        "enroll",
        help="Enroll a student in a course"
    )

    enroll_parser.add_argument(
        "--student-id",
        type=int,
        required=True,
        help="Student ID"
    )

    enroll_parser.add_argument(
        "--course",
        required=True,
        help="Course code"
    )

    grade_parser = subparsers.add_parser(
        "add-grade",
        help="Add a grade to a student's course"
    )

    grade_parser.add_argument(
        "--student-id",
        type=int,
        required=True,
        help="Student ID"
    )

    grade_parser.add_argument(
        "--course",
        required=True,
        help="Course code"
    )

    grade_parser.add_argument(
        "--grade",
        required=True,
        help="Grade between 0 and 100"
    )

    list_parser = subparsers.add_parser(
        "list",
        help="List students, courses or enrollments"
    )

    list_parser.add_argument(
        "type",
        choices=["students", "courses", "enrollments"],
        help="What you want to list"
    )

    list_parser.add_argument(
        "--sort",
        choices=["name", "code"],
        help="Sort students by name or courses by code"
    )

    avg_parser = subparsers.add_parser(
        "avg",
        help="Calculate a student's average in a course"
    )

    avg_parser.add_argument(
        "--student-id",
        type=int,
        required=True,
        help="Student ID"
    )

    avg_parser.add_argument(
        "--course",
        required=True,
        help="Course code"
    )

    gpa_parser = subparsers.add_parser(
        "gpa",
        help="Calculate a student's overall GPA"
    )

    gpa_parser.add_argument(
        "--student-id",
        type=int,
        required=True,
        help="Student ID"
    )

    return parser

def main():

    parser = create_parser()
    args = parser.parse_args()

    try:

        if args.command == "add-student":
            student_id = add_student(args.name)

            print(f"Student added successfully. ID: {student_id}")
            logger.info("Student added: %s", args.name)

        elif args.command == "add-course":
            add_course(args.code, args.title)

            print(f"Course {args.code} added successfully.")
            logger.info("Course added: %s", args.code)

        elif args.command == "enroll":
            enroll(args.student_id, args.course)

            print(
                f"Student {args.student_id} enrolled "
                f"in {args.course} successfully."
            )

            logger.info(
                "Student %s enrolled in %s",
                args.student_id,
                args.course
            )

        elif args.command == "add-grade":
            grade = parse_grade(args.grade)

            add_grade(
                args.student_id,
                args.course,
                grade
            )

            print(
                f"Grade {grade} added successfully "
                f"for student {args.student_id}."
            )

            logger.info(
                "Grade %s added for student %s in %s",
                grade,
                args.student_id,
                args.course
            )

        elif args.command == "list":

            if args.type == "students":
                students = list_students()

                if args.sort == "name":
                    students.sort(
                        key=lambda student: student.name.lower()
                    )

                for student in students:
                    print(student)

                if not students:
                    print("No students found.")

            elif args.type == "courses":
                courses = list_courses()

                if args.sort == "code":
                    courses.sort(
                        key=lambda course: course.code
                    )

                for course in courses:
                    print(course)

                if not courses:
                    print("No courses found.")

            elif args.type == "enrollments":
                enrollments = list_enrollments()

                for enrollment in enrollments:
                    print(enrollment)

                if not enrollments:
                    print("No enrollments found.")

        elif args.command == "avg":
            average = compute_average(
                args.student_id,
                args.course
            )

            print(
                f"Average for student {args.student_id} "
                f"in {args.course}: {average:.2f}"
            )

            logger.info(
                "Average calculated for student %s in %s",
                args.student_id,
                args.course
            )

        elif args.command == "gpa":
            gpa = compute_gpa(args.student_id)

            print(
                f"GPA for student {args.student_id}: {gpa:.2f}"
            )

            logger.info(
                "GPA calculated for student %s",
                args.student_id
            )

    except ValueError as error:
        print(f"Error: {error}")
        logger.error("Operation failed: %s", error)

    except Exception as error:
        print(f"An unexpected error occurred: {error}")
        logger.exception("Unexpected application error")


if __name__ == "__main__":
    main()