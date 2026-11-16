from .models import Student, Course, Enrollment
from .storage import load_data, save_data

def add_student(name):
    data = load_data()

    student_id = max(
        [student["id"] for student in data["students"]],
        default = 0
    ) + 1

    student = Student(student_id, name)

    data["students"].append({
        "id": student.id,
        "name": student.name
    })

    save_data(data)
    return student_id

def add_course(code, title):

    data = load_data()

    course = Course(code, title)

    if any(c["code"] == code for c in data["courses"]):
        raise ValueError("Course already exists.")

    data["courses"].append({
        "code": course.code,
        "title": course.title
    })

    save_data(data)


def enroll(student_id, course_code):

    data = load_data()

    student_exists = any(
        s["id"] == student_id for s in data["students"]
    )

    course_exists = any(
        c["code"] == course_code for c in data["courses"]
    )

    if not student_exists:
        raise ValueError("Student ID not found.")

    if not course_exists:
        raise ValueError("Course not found.")

    already_enrolled = any(
        e["student_id"] == student_id
        and e["course_code"] == course_code
        for e in data["enrollments"]
    )

    if already_enrolled:
        raise ValueError("Student is already enrolled.")

    enrollment = Enrollment(student_id, course_code)

    data["enrollments"].append({
        "student_id": enrollment.student_id,
        "course_code": enrollment.course_code,
        "grades": enrollment.grades
    })

    save_data(data)


def add_grade(student_id, course_code, grade):

    data = load_data()

    enrollment = next(
        (
            e for e in data["enrollments"]
            if e["student_id"] == student_id
            and e["course_code"] == course_code
        ),
        None
    )

    if enrollment is None:
        raise ValueError("Student is not enrolled in this course.")

    if not isinstance(grade, (int, float)) or not 0 <= grade <= 100:
        raise ValueError("Grade must be between 0 and 100.")

    enrollment["grades"].append(grade)

    save_data(data)


def list_students():

    data = load_data()

    students = [
        Student(s["id"], s["name"])
        for s in data["students"]
    ]

    return sorted(students, key=lambda s: s.name.lower())


def list_courses():

    data = load_data()

    courses = [
        Course(c["code"], c["title"])
        for c in data["courses"]
    ]

    return sorted(courses, key=lambda c: c.code)


def list_enrollments():

    data = load_data()

    enrollments = [
        Enrollment(
            e["student_id"],
            e["course_code"],
            e["grades"]
        )
        for e in data["enrollments"]
    ]

    return sorted(
        enrollments,
        key=lambda e: (e.student_id, e.course_code)
    )


def compute_average(student_id, course_code):

    data = load_data()

    enrollment = next(
        (
            e for e in data["enrollments"]
            if e["student_id"] == student_id
            and e["course_code"] == course_code
        ),
        None
    )

    if enrollment is None:
        raise ValueError("Student is not enrolled in this course.")

    grades = enrollment["grades"]

    if not grades:
        raise ValueError("No grades available for this course.")

    return sum(grades) / len(grades)


def compute_gpa(student_id):
    
    data = load_data()

    student_exists = any(
        s["id"] == student_id for s in data["students"]
    )

    if not student_exists:
        raise ValueError("Student ID not found.")

    course_averages = [
        sum(e["grades"]) / len(e["grades"])
        for e in data["enrollments"]
        if e["student_id"] == student_id and e["grades"]
    ]

    if not course_averages:
        raise ValueError("No course grades available for this student.")

    return sum(course_averages) / len(course_averages)