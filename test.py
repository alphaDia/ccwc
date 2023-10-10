import subprocess
import unittest

import utilities


class TestCCWC(unittest.TestCase):
    def setUp(self) -> None:
        self.path = ["test_data/text1.txt", "test_data/text2.txt"]

    def test_all_file_metric(self):
        ccwc_process = subprocess.run(
            ["python3", "ccwc.py", self.path[0]],
            capture_output=True,
            encoding="utf-8",
        )
        cat_process = subprocess.run(
            ["cat", self.path[0]], capture_output=True
        )
        metric = [int(v) for v in ccwc_process.stdout.split(" ")[:-1]]

        self.assertEqual(
            utilities.count_lines(cat_process.stdout),
            metric[0],
            "number of lines",
        )
        self.assertEqual(
            utilities.count_words(cat_process.stdout),
            metric[1],
            "number of words",
        )
        self.assertEqual(
            utilities.count_bytes(cat_process.stdout),
            metric[2],
            "number of bytes",
        )

    def test_number_of_lines(self):
        ccwc_process = subprocess.run(
            ["python3", "ccwc.py", "-l", self.path[0]],
            capture_output=True,
            encoding="utf-8",
        )
        cat_process = subprocess.run(
            ["cat", self.path[0]], capture_output=True
        )
        number_of_lines = int(ccwc_process.stdout.split(" ")[:-1][0])

        self.assertEqual(
            utilities.count_lines(cat_process.stdout), number_of_lines
        )

    def test_number_of_words(self):
        ccwc_process = subprocess.run(
            ["python3", "ccwc.py", "-w", self.path[0]],
            capture_output=True,
            encoding="utf-8",
        )
        cat_process = subprocess.run(
            ["cat", self.path[0]], capture_output=True
        )
        number_of_words = int(ccwc_process.stdout.split(" ")[:-1][0])

        self.assertEqual(
            utilities.count_words(cat_process.stdout), number_of_words
        )

    def test_number_of_bytes(self):
        ccwc_process = subprocess.run(
            ["python3", "ccwc.py", "-c", self.path[0]],
            capture_output=True,
            encoding="utf-8",
        )
        cat_process = subprocess.run(
            ["cat", self.path[0]], capture_output=True
        )
        number_of_bytes = int(ccwc_process.stdout.split(" ")[:-1][0])

        self.assertEqual(
            utilities.count_bytes(cat_process.stdout), number_of_bytes
        )

    def test_number_of_characters(self):
        ccwc_process = subprocess.run(
            ["python3", "ccwc.py", "-m", self.path[0]],
            capture_output=True,
            encoding="utf-8",
        )
        cat_process = subprocess.run(
            ["cat", self.path[0]], capture_output=True
        )
        number_of_chars = int(ccwc_process.stdout.split(" ")[:-1][0])

        self.assertEqual(
            utilities.count_characters(cat_process.stdout), number_of_chars
        )


class TestCCWCWithoutArguments(unittest.TestCase):
    def setUp(self) -> None:
        self.path = ["test_data/text1.txt", "test_data/text2.txt"]

    def test_all_file_metric(self):
        cat_process = subprocess.run(
            ["cat", self.path[0]], capture_output=True
        )
        ccwc_process = subprocess.run(
            ["python3", "ccwc.py"],
            input=cat_process.stdout.decode(),
            capture_output=True,
            encoding="utf-8",
        )
        metric = [int(v) for v in ccwc_process.stdout.split(" ")[:-1]]

        self.assertEqual(
            utilities.count_lines(cat_process.stdout),
            metric[0],
            "number of lines",
        )
        self.assertEqual(
            utilities.count_words(cat_process.stdout),
            metric[1],
            "number of words",
        )
        self.assertEqual(
            utilities.count_bytes(cat_process.stdout),
            metric[2],
            "number of bytes",
        )

    def test_number_of_lines(self):
        cat_process = subprocess.run(
            ["cat", self.path[0]], capture_output=True
        )
        ccwc_process = subprocess.run(
            ["python3", "ccwc.py", "-l"],
            input=cat_process.stdout.decode(),
            capture_output=True,
            encoding="utf-8",
        )
        number_of_lines = int(ccwc_process.stdout.split(" ")[:-1][0])

        self.assertEqual(
            utilities.count_lines(cat_process.stdout), number_of_lines
        )

    def test_number_of_words(self):
        cat_process = subprocess.run(
            ["cat", self.path[0]], capture_output=True
        )
        ccwc_process = subprocess.run(
            ["python3", "ccwc.py", "-w"],
            input=cat_process.stdout.decode(),
            capture_output=True,
            encoding="utf-8",
        )
        number_of_words = int(ccwc_process.stdout.split(" ")[:-1][0])

        self.assertEqual(
            utilities.count_words(cat_process.stdout), number_of_words
        )

    def test_number_of_bytes(self):
        cat_process = subprocess.run(
            ["cat", self.path[0]], capture_output=True
        )
        ccwc_process = subprocess.run(
            ["python3", "ccwc.py", "-c"],
            input=cat_process.stdout.decode(),
            capture_output=True,
            encoding="utf-8",
        )
        number_of_bytes = int(ccwc_process.stdout.split(" ")[:-1][0])

        self.assertEqual(
            utilities.count_bytes(cat_process.stdout), number_of_bytes
        )

    def test_number_of_characters(self):
        cat_process = subprocess.run(
            ["cat", self.path[0]], capture_output=True
        )
        ccwc_process = subprocess.run(
            ["python3", "ccwc.py", "-m"],
            input=cat_process.stdout.decode(),
            capture_output=True,
            encoding="utf-8",
        )
        number_of_chars = int(ccwc_process.stdout.split(" ")[:-1][0])

        self.assertEqual(
            utilities.count_characters(cat_process.stdout), number_of_chars
        )


if __name__ == "__main__":
    unittest.main()
