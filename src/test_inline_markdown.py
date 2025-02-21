import unittest
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from extract_markdown import extract_markdown_images, extract_markdown_links
from text_type import TextType
from textnode import TextNode


class TestSplitDelimiter(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_unclosed(self):
        node = TextNode("This text has an unclosed **bold", TextType.TEXT)
        # Test that it raises ValueError
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_empty_delim(self):
        node = TextNode("This text has an empty **/** delimiter", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This text has an empty ", TextType.TEXT),
                TextNode("/", TextType.BOLD),
                TextNode(" delimiter", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_already_formatted(self):
        node = TextNode("This is already bold", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        # Should return unchanged node
        self.assertListEqual([node], new_nodes)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )

    def test_multiple_images_inline(self):
        text = "![img1](url1.jpg) normal text ![img2](url2.png)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("img1", "url1.jpg"), ("img2", "url2.png")], matches)

    def test_empty_image_parts(self):
        text = "![](empty.jpg) ![alt]()"
        matches = extract_markdown_images(text)
        self.assertListEqual([("", "empty.jpg"), ("alt", "")], matches)

    def test_mixed_links_and_images(self):
        text = "![img](pic.jpg) [link](url.com) ![another](pic2.jpg)"
        img_matches = extract_markdown_images(text)
        link_matches = extract_markdown_links(text)
        self.assertListEqual([("img", "pic.jpg"), ("another", "pic2.jpg")], img_matches)
        self.assertListEqual([("link", "url.com")], link_matches)

    def test_complex_urls(self):
        text = "[link](https://example.com/path?param=value#fragment)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("link", "https://example.com/path?param=value#fragment")], matches)

    def test_no_links_in_text(self):
        node = TextNode("This is plain text.", TextType.TEXT)
        actual = split_nodes_link([node])
        expected = [TextNode("This is plain text.", TextType.TEXT)]
        self.assertEqual(actual, expected)

    def test_only_before_or_after_link(self):
        node1 = TextNode("Text before [link](https://example.com)", TextType.TEXT)
        node2 = TextNode("[link](https://example.com) text after", TextType.TEXT)
        before = split_nodes_link([node1])
        after = split_nodes_link([node2])
        new_nodes1 = [
            TextNode("Text before ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com")
        ]

        new_nodes2 = [
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" text after", TextType.TEXT)
        ]
        self.assertEqual(before, new_nodes1)
        self.assertEqual(after, new_nodes2)

    def test_multiple_links_in_sequence(self):
        node = TextNode("[first](https://first.com) [second](https://second.com)", TextType.TEXT)
        actual = split_nodes_link([node])
        new_nodes = [
            TextNode("first", TextType.LINK, "https://first.com"),
            TextNode(" ", TextType.TEXT),
            TextNode("second", TextType.LINK, "https://second.com")
        ]
        self.assertEqual(actual, new_nodes)

    def alternated_links_with_text(self):
        node = TextNode("Text before [first](https://first.com), some text after, and [second](https://second.com)", TextType.TEXT)
        actual = split_nodes_link([node])
        new_nodes = [
            TextNode("Text before ", TextType.TEXT),
            TextNode("first", TextType.LINK, "https://first.com"),
            TextNode(", some text after, and ", TextType.TEXT),
            TextNode("second", TextType.LINK, "https://second.com")
        ]
        self.assertEqual(actual, new_nodes)

    def no_images_in_text(self):
        node = TextNode("This is plain text without images.", TextType.TEXT)
        actual = split_nodes_image([node])
        new_nodes = [TextNode("This is plain text without images.", TextType.TEXT)]
        self.assertEqual(actual, new_nodes)

    def text_only_before_or_after_an_image(self):
        node1 = TextNode("Text before ![alt1](https://example.com/img1.jpg)", TextType.TEXT)
        node2 = TextNode("![alt2](https://example.com/img2.png) text after", TextType.TEXT)
        before = split_nodes_image([node1])
        after = split_nodes_image[node2]
        new_nodes1 = [
            TextNode("Text before ", TextType.TEXT),
            TextNode("alt1", TextType.IMAGE, "https://example.com/img1.jpg")
        ]

        new_nodes2 = [
            TextNode("alt2", TextType.IMAGE, "https://example.com/img2.png"),
            TextNode(" text after", TextType.TEXT)
        ]
        self.assertEqual(before, new_nodes1)
        self.assertEqual(after, new_nodes2)

    def multiple_images_in_sequence(self):
        node = TextNode("![alt1](https://example.com/img1.jpg) ![alt2](https://example.com/img2.png)", TextType.TEXT)
        actual = split_nodes_image([node])
        new_nodes = [
            TextNode("alt1", TextType.IMAGE, "https://example.com/img1.jpg"),
            TextNode(" ", TextType.TEXT),
            TextNode("alt2", TextType.IMAGE, "https://example.com/img2.png")
        ]
        self.assertEqual(actual, new_nodes)

    def alternated_images_with_text(self):
        node = TextNode("Text before ![alt1](https://example.com/img1.jpg), some text after, and ![alt2](https://example.com/img2.png)", TextType.TEXT)
        actual = split_nodes_image([node])
        new_nodes = [
            TextNode("Text before ", TextType.TEXT),  # Text before the first image
            TextNode("alt1", TextType.IMAGE, "https://example.com/img1.jpg"),  # First image
            TextNode(", some text after, and ", TextType.TEXT),  # Text between the images
            TextNode("alt2", TextType.IMAGE, "https://example.com/img2.png")  # Second image
        ]
        self.assertEqual(actual, new_nodes)