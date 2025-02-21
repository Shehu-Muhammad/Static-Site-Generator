import unittest

from textnode import TextNode, TextType
from text_to_html_converter import text_node_to_html_node

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
        node = TextNode("https://google.com", TextType.LINK)
        node2 = TextNode("https://google.com", TextType.LINK)
        self.assertEqual(node, node2)

    def test_image_node(self):
        # Test with alt text and URL
        image_text = "cute puppy"
        image_url = "https://example.com/puppy.jpg"
        node1 = TextNode(image_text, TextType.IMAGE, url=image_url)
        node2 = TextNode(image_text, TextType.IMAGE, url=image_url)
        self.assertEqual(node1, node2)

    def test_empty_string(self):
        node1 = TextNode("", TextType.TEXT)
        node2 = TextNode("", TextType.TEXT)
        self.assertEqual(node1, node2)

    def test_very_long_string(self):
        # Create a really long string
        long_text = "hello" * 1000  # repeats "hello" 1000 times
        node1 = TextNode(long_text, TextType.TEXT)
        node2 = TextNode(long_text, TextType.TEXT)
        self.assertEqual(node1, node2)

    def test_italic_equality(self):
        # Testing italic text behavior
        node1 = TextNode("emphasized text", TextType.ITALIC)
        node2 = TextNode("emphasized text", TextType.ITALIC)
        self.assertEqual(node1, node2)

    def test_whitespace_only(self):
        # Test nodes with only spaces, tabs, newlines
        node1 = TextNode("   \t\n", TextType.TEXT)
        node2 = TextNode("   \t\n", TextType.TEXT)
        self.assertEqual(node1, node2)

    def test_multiline_text(self):
        # Test multi-line text in non-code type
        text = """This is a
        multi-line
        text block"""
        node1 = TextNode(text, TextType.TEXT)
        node2 = TextNode(text, TextType.TEXT)
        self.assertEqual(node1, node2)
    # Not Equal Tests Below

    def test_not_eq_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)
    
    def test_empty_string_not_equal(self):
        node1 = TextNode("", TextType.TEXT)
        node2 = TextNode("", TextType.BOLD)  # Different TextType
        self.assertNotEqual(node1, node2)

    def test_very_long_string_not_equal(self):
        # Create two different long strings
        long_text1 = "hello" * 1000
        long_text2 = "world" * 1000
        node1 = TextNode(long_text1, TextType.TEXT)
        node2 = TextNode(long_text2, TextType.TEXT)
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
        node1 = TextNode(alt_text, TextType.IMAGE, url="https://example.com/cat1.jpg")
        node2 = TextNode(alt_text, TextType.IMAGE, url="https://example.com/cat2.jpg")
        self.assertNotEqual(node1, node2)

    def test_links_different_urls(self):
        # Same text, different URLs
        node1 = TextNode("click here", TextType.LINK, url="https://example1.com")
        node2 = TextNode("click here", TextType.LINK, url="https://example2.com")
        self.assertNotEqual(node1, node2)

    def test_url_presence(self):
        # One node with URL, one without
        node1 = TextNode("same text", TextType.LINK, url="https://example.com")
        node2 = TextNode("same text", TextType.LINK)
        self.assertNotEqual(node1, node2)

    def test_empty_vs_none_url(self):
        # Empty string URL vs None URL
        node1 = TextNode("test", TextType.LINK, url="")
        node2 = TextNode("test", TextType.LINK, url=None)
        self.assertNotEqual(node1, node2)

    def test_italic_vs_bold(self):
        # Same text, different text types
        node1 = TextNode("important text", TextType.ITALIC)
        node2 = TextNode("important text", TextType.BOLD)
        self.assertNotEqual(node1, node2)


    def test_whitespace_different_types(self):
        # Different types with whitespace should not be equal
        node1 = TextNode("   \t\n", TextType.TEXT)
        node2 = TextNode("   \t\n", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_non_textnode_comparison(self):
        # Test comparison with non-TextNode object
        node = TextNode("text", TextType.TEXT)
        non_node = "text"
        self.assertNotEqual(node, non_node)
    
    def test_text_node_conversion(self):
        text_node = TextNode("Hello, world!", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == None
        assert html_node.value == "Hello, world!"

    def test_text_node_to_html_node(self):
        # Test basic text conversion
        text_node = TextNode("Just plain text", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertIsNone(html_node.tag)
        self.assertEqual(html_node.value, "Just plain text")
        self.assertEqual(html_node.props, {})

        # Test bold text conversion
        text_node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")

        # Test italic
        text_node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, 'Italic text')

        # Test code
        text_node = TextNode("print('hello')", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "print('hello')")

        # Test link
        text_node = TextNode("Click me", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click me")
        self.assertEqual(html_node.props["href"], "https://www.boot.dev")

        # Test image
        text_node = TextNode("Alt text", TextType.IMAGE, "https://example.com/img.png")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "") # Empty string for images
        self.assertEqual(html_node.props["src"], "https://example.com/img.png")
        self.assertEqual(html_node.props["alt"], "Alt text")
