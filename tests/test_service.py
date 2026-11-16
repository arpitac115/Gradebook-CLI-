import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch

from gradebook.service import (
    add_student,
    add_grade,
    compute_average
)


class TestGradebookService(unittest.TestCase):

    def setUp(self):

        self.temp_dir = tempfile.TemporaryDirectory()
        self.data_path = str(
            Path(self.temp_dir.name) / "gradebook.json"
        )

        self.patcher = patch(
            "gradebook.service.load_data"
        )

        self.mock_load = self.patcher.start()

        self.data = {
            "students": [],
            "courses": [],
            "enrollments": []
        }

        self.mock_load.side_effect = lambda: self.data

        self.save_patcher = patch(
            "gradebook.service.save_data"
        )

        self.mock_save = self.save_patcher.start()

    def tearDown(self):

        self.patcher.stop()
        self.save_patcher.stop()
        self.temp_dir.cleanup()

    def test_add_student(self):

        student_id = add_student("John")

        self.assertEqual(student_id, 1)

        self.assertEqual(
            self.data["students"],
            [{"id": 1, "name": "John"}]
        )

        self.mock_save.assert_called_once()

    def test_add_grade(self):

        self.data["students"].append({
            "id": 1,
            "name": "John"
        })

        self.data["courses"].append({
            "code": "CS101",
            "title": "Introduction to CS"
        })

        self.data["enrollments"].append({
            "student_id": 1,
            "course_code": "CS101",
            "grades": []
        })

        add_grade(1, "CS101", 95)

        self.assertEqual(
            self.data["enrollments"][0]["grades"],
            [95]
        )

        self.mock_save.assert_called_once()

    def test_compute_average(self):

        self.data["students"].append({
            "id": 1,
            "name": "John"
        })

        self.data["courses"].append({
            "code": "CS101",
            "title": "Introduction to CS"
        })

        self.data["enrollments"].append({
            "student_id": 1,
            "course_code": "CS101",
            "grades": [80, 90, 100]
        })

        average = compute_average(1, "CS101")

        self.assertEqual(average, 90)

    def test_add_grade_for_unenrolled_student(self):

        with self.assertRaises(ValueError):
            add_grade(1, "CS101", 95)


if __name__ == "__main__":
    unittest.main()

