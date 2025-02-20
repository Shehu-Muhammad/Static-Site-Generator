import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    # Test 1: No props
    def test_props_to_html_no_props(self):
        node1 = HTMLNode()
        actual = node1.props_to_html()
        expected = ""
        self.assertEqual(actual, expected)  # Should print: ""

    def test_props_to_html_one_prop(self):
        # Test 2: One prop
        node2 = HTMLNode(props={"class": "button"})
        actual = node2.props_to_html()
        expected = ' class="button"'
        self.assertEqual(actual, expected) # Should print: " class="button""

    def test_props_to_html_multiple_props(self):
        # Test 3: Multiple props
        node3 = HTMLNode(props={
            "href": "https://google.com",
            "target": "_blank"
        })
        actual = node3.props_to_html()
        expected = " href=\"https://google.com\" target=\"_blank\""
        self.assertEqual(actual, expected) # Should print: " href="https://google.com" target="_blank""

    def test_props_to_html_empty_string_value(self):
        # Case: Prop value is an empty string
        node = HTMLNode(props={"class": ""})
        actual = node.props_to_html()
        expected = ' class=""'  # Expect it to be included but empty
        self.assertEqual(actual, expected)

    def test_props_to_html_special_characters(self):
        # Case: Prop value contains special characters like `&`
        node = HTMLNode(props={"class": "button-list & link"})
        actual = node.props_to_html()
        expected = ' class="button-list & link"'
        self.assertEqual(actual, expected)

    def test_props_with_non_string_values(self):
        # Props with various types of values
        node = HTMLNode(props={"data-count": 5, "hidden": True})
        actual = repr(node)
        expected = (
            "HTMLNode(tag=None, value=None, children=[], props={'data-count': 5, 'hidden': True})"
        )
        self.assertEqual(actual, expected)
        # Test props_to_html to see if it stringifies them correctly
        actual_props = node.props_to_html()
        expected_props = ' data-count="5" hidden="True"'
        self.assertEqual(actual_props, expected_props)
        
    def test_node_with_children(self):
        # Create child nodes
        child1 = HTMLNode(tag="span", value="Child 1")
        child2 = HTMLNode(tag="span", value="Child 2")
        
        # Create a parent node with child nodes
        parent = HTMLNode(tag="div", children=[child1, child2])
        
        # Check that __repr__ includes child information
        actual = repr(parent)
        # Expected should match the new format of __repr__
        expected = (
            "HTMLNode(tag='div', value=None, children="
            "[HTMLNode(tag='span', value='Child 1', children=[], props={}), "
            "HTMLNode(tag='span', value='Child 2', children=[], props={})], props={})"
        )
        self.assertEqual(actual, expected)

    def test_extremely_nested_children(self):
            # Create a deeply nested structure
            grandchild = HTMLNode(tag="b", value="Bold text")
            child = HTMLNode(tag="div", children=[grandchild])
            parent = HTMLNode(tag="section", children=[child])
            
            # Check the representation of the nested structure
            actual = repr(parent)
            expected = (
                "HTMLNode(tag='section', value=None, children=["
                "HTMLNode(tag='div', value=None, children=["
                "HTMLNode(tag='b', value='Bold text', children=[], props={})], props={})], props={})"
            )
            self.assertEqual(actual, expected)

    def test_deeply_nested_nodes(self):
        # Create a deeply nested structure
        grandchild = HTMLNode(tag="em", value="Grandchild")
        child = HTMLNode(tag="span", value="Child", children=[grandchild])
        parent = HTMLNode(tag="div", children=[child])
        
        # Check the representation of the deeply nested structure
        actual = repr(parent)
        expected = (
            "HTMLNode(tag='div', value=None, children=["
            "HTMLNode(tag='span', value='Child', children=["
            "HTMLNode(tag='em', value='Grandchild', children=[], props={})], props={})], props={})"
        )
        self.assertEqual(actual, expected)
    
    def test_empty_htmlnode_repr(self):
        # No parameters provided to HTMLNode
        node = HTMLNode()
        actual = repr(node)
        expected = "HTMLNode(tag=None, value=None, children=[], props={})"
        self.assertEqual(actual, expected) # HTMLNode(tag=None, value=None, children=None, props=None)

    def test_htmlnode_repr(self):
        test_cases = [
            {
                "node": HTMLNode(),
                "expected": "HTMLNode(tag=None, value=None, children=[], props={})",
            },
            {
                "node": HTMLNode(tag="div"),
                "expected": "HTMLNode(tag='div', value=None, children=[], props={})",
            },
            {
                "node": HTMLNode(tag="a", value="Click here", children=[], props={"href": "https://example.com"}),
                "expected": (
                    "HTMLNode(tag='a', value='Click here', children=[], "
                    "props={'href': 'https://example.com'})"
                ),
            },
            {
                "node": HTMLNode(props={}),
                "expected": "HTMLNode(tag=None, value=None, children=[], props={})",
            },
        ]
        for case in test_cases:
            with self.subTest(case=case):
                self.assertEqual(repr(case["node"]), case["expected"])
    
    def test_htmlnode_with_empty_props(self):
        node = HTMLNode(props={})
        actual = repr(node)
        expected = "HTMLNode(tag=None, value=None, children=[], props={})"
        self.assertEqual(actual, expected)
    
    def test_node_with_no_tag_but_value(self):
        node = HTMLNode(value="Just a text node")
        actual = repr(node)
        expected = "HTMLNode(tag=None, value='Just a text node', children=[], props={})"
        self.assertEqual(actual, expected)

    def test_empty_string_tag(self):
        node = HTMLNode(tag="", value="Empty tag test")
        actual = repr(node)
        expected = "HTMLNode(tag='', value='Empty tag test', children=[], props={})"
        self.assertEqual(actual, expected)
