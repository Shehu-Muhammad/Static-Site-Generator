import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_parent_node(self):
        node = ParentNode(
            'div',
            [LeafNode('p', 'Hello')]
        )
        self.assertEqual(node.to_html(),'<div><p>Hello</p></div>')

    def test_multiple_children(self):
        node = ParentNode(
            "div",
            [
                LeafNode("p", "first"),
                LeafNode("p", "second"),
                LeafNode("p", "third")
            ]
        )
        self.assertEqual(node.to_html(), "<div><p>first</p><p>second</p><p>third</p></div>")

    def test_nested_nodes(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "section",
                    [LeafNode("p", "nested")]
                )
            ]
        )
        self.assertEqual(node.to_html(), "<div><section><p>nested</p></section></div>")

    def test_invalid_empty_children(self):
        # This should raise a ValueError
        with self.assertRaises(ValueError):
            ParentNode("div", [])

    def test_children_without_tags(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

    def test_parent_with_props(self):
        node = ParentNode(
            "div",
            [LeafNode("p", "hello")],
            {"class": "greeting", "id": "hello-div"}
        )
        self.assertEqual(
            node.to_html(),
            '<div class="greeting" id="hello-div"><p>hello</p></div>'
        )

    def test_deep_nesting(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "section",
                    [
                        ParentNode(
                            "article",
                            [LeafNode("p", "deep")]
                        )
                    ]
                )
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<div><section><article><p>deep</p></article></section></div>"
        )

    def test_none_props(self):
        node = ParentNode(
            "div",
            [LeafNode("p", "hello")],
            None
        )
        self.assertEqual(node.to_html(), "<div><p>hello</p></div>")

    def test_missing_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None)

    def test_missing_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("p", "text")])