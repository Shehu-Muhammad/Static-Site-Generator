import unittest
from extract_title import extract_title

class TestTextNode(unittest.TestCase):

    def test_extract_title(self):
        test1 = "# Hello\nsome text"
        self.assertEqual(extract_title(test1), "Hello")  # Note the expected result is just "Hello"
        
        # You might also want to test the error case
        test2 = "## Not a title\nsome text"
        with self.assertRaises(Exception):
            extract_title(test2)