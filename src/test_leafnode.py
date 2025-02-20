import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_basic_functionality(self):
        # Test 1: Basic functionality with tag and value
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_tag_with_props(self):
        # Test 2: Tag with props (attributes)
        node = LeafNode("a", "Click me!", {"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">Click me!</a>')

    def test_no_tag_returns_raw_value(self):
        # Test 3: No tag, raw value should be returned
        node = LeafNode(None, "Just text!")
        self.assertEqual(node.to_html(), "Just text!")

    def test_no_props(self):
        # Test 4: No props, should not add blank attributes
        node = LeafNode("h1", "Title")
        self.assertEqual(node.to_html(), "<h1>Title</h1>")

    def test_special_characters_in_props(self):
        # Test 5: Special characters in props
        node = LeafNode("button", "Click <me>", {"data-action": "save&close"})
        self.assertEqual(node.to_html(), '<button data-action="save&close">Click <me></button>')

    def test_empty_props(self):
        # Test 6: Empty props
        node = LeafNode("p", "Paragraph", {})
        self.assertEqual(node.to_html(), "<p>Paragraph</p>")

    def test_missing_value_raises_error(self):
        # Test 7: Missing value (should raise ValueError)
        with self.assertRaises(ValueError) as context:
            LeafNode("p", None)
        self.assertEqual(str(context.exception), "LeafNode must have a value")