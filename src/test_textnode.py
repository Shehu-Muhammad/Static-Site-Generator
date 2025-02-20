import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    # Equal Tests Below
    def test_eq_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_code_with_special_chars(self):
        code_text = "def hello():\n    print('world')"
        node1 = TextNode(code_text, TextType.CODE)
        node2 = TextNode(code_text, TextType.CODE)
        self.assertEqual(node1, node2)

    def test_eq_links(self):
        node = TextNode("https://google.com", TextType.LINKS)
        node2 = TextNode("https://google.com", TextType.LINKS)
        self.assertEqual(node, node2)

    def test_image_node(self):
        # Test with alt text and URL
        image_text = "cute puppy"
        image_url = "https://example.com/puppy.jpg"
        node1 = TextNode(image_text, TextType.IMAGES, url=image_url)
        node2 = TextNode(image_text, TextType.IMAGES, url=image_url)
        self.assertEqual(node1, node2)

    def test_empty_string(self):
        node1 = TextNode("", TextType.NORMAL)
        node2 = TextNode("", TextType.NORMAL)
        self.assertEqual(node1, node2)

    def test_very_long_string(self):
        # Create a really long string
        long_text = "hello" * 1000  # repeats "hello" 1000 times
        node1 = TextNode(long_text, TextType.NORMAL)
        node2 = TextNode(long_text, TextType.NORMAL)
        self.assertEqual(node1, node2)

    def test_italic_equality(self):
        # Testing italic text behavior
        node1 = TextNode("emphasized text", TextType.ITALIC)
        node2 = TextNode("emphasized text", TextType.ITALIC)
        self.assertEqual(node1, node2)

    def test_whitespace_only(self):
        # Test nodes with only spaces, tabs, newlines
        node1 = TextNode("   \t\n", TextType.NORMAL)
        node2 = TextNode("   \t\n", TextType.NORMAL)
        self.assertEqual(node1, node2)

    def test_multiline_text(self):
        # Test multi-line text in non-code type
        text = """This is a
        multi-line
        text block"""
        node1 = TextNode(text, TextType.NORMAL)
        node2 = TextNode(text, TextType.NORMAL)
        self.assertEqual(node1, node2)
    # Not Equal Tests Below

    def test_not_eq_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertNotEqual(node, node2)
    
    def test_empty_string_not_equal(self):
        node1 = TextNode("", TextType.NORMAL)
        node2 = TextNode("", TextType.BOLD)  # Different TextType
        self.assertNotEqual(node1, node2)

    def test_very_long_string_not_equal(self):
        # Create two different long strings
        long_text1 = "hello" * 1000
        long_text2 = "world" * 1000
        node1 = TextNode(long_text1, TextType.NORMAL)
        node2 = TextNode(long_text2, TextType.NORMAL)
        self.assertNotEqual(node1, node2)

    def test_code_not_equal(self):
        code1 = "def hello():\n    print('hi')"
        code2 = "def hello():\n    print('hello')"
        node1 = TextNode(code1, TextType.CODE)
        node2 = TextNode(code2, TextType.CODE)
        self.assertNotEqual(node1, node2)

    def test_image_not_equal(self):
        # Different URLs but same alt text
        alt_text = "cute cat"
        node1 = TextNode(alt_text, TextType.IMAGES, url="https://example.com/cat1.jpg")
        node2 = TextNode(alt_text, TextType.IMAGES, url="https://example.com/cat2.jpg")
        self.assertNotEqual(node1, node2)

    def test_links_different_urls(self):
        # Same text, different URLs
        node1 = TextNode("click here", TextType.LINKS, url="https://example1.com")
        node2 = TextNode("click here", TextType.LINKS, url="https://example2.com")
        self.assertNotEqual(node1, node2)

    def test_url_presence(self):
        # One node with URL, one without
        node1 = TextNode("same text", TextType.LINKS, url="https://example.com")
        node2 = TextNode("same text", TextType.LINKS)
        self.assertNotEqual(node1, node2)

    def test_empty_vs_none_url(self):
        # Empty string URL vs None URL
        node1 = TextNode("test", TextType.LINKS, url="")
        node2 = TextNode("test", TextType.LINKS, url=None)
        self.assertNotEqual(node1, node2)

    def test_italic_vs_bold(self):
        # Same text, different text types
        node1 = TextNode("important text", TextType.ITALIC)
        node2 = TextNode("important text", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_whitespace_different_types(self):
        # Different types with whitespace should not be equal
        node1 = TextNode("   \t\n", TextType.NORMAL)
        node2 = TextNode("   \t\n", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_non_textnode_comparison(self):
        # Test comparison with non-TextNode object
        node = TextNode("text", TextType.NORMAL)
        non_node = "text"
        self.assertNotEqual(node, non_node)

if __name__ == "__main__":
    unittest.main()