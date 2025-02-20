from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        # Initialize the base class
        super().__init__(tag=tag, value=value, children=None, props=props)
        if value is None:
            raise ValueError("LeafNode must have a value")  # Ensure value is required
        self.children = None  # Explicitly enforce no children for LeafNode

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")  # Validate value before rendering

        # If tag is None, simply return the raw value
        if self.tag is None:
            return self.value

        # Use the base class's props_to_html to build the attribute string
        attributes_str = self.props_to_html()

        # Format the HTML string
        if attributes_str:
            return f'<{self.tag}{attributes_str}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag}>{self.value}</{self.tag}>'