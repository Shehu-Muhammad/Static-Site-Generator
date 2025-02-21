from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        self.tag = tag
        self.children = children
        self.props = props
        if tag is None:
            raise ValueError('ParentNode must have a tag')
        if children is None:
            raise ValueError('ParentNode must have children')
        if not children: # this validates that children exists and isn't empty
            raise ValueError('ParentNode must have children')
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        # Create opening tag with props if they exist
        if self.props:
            props_str = " ".join([f'{key}="{value}"' for key, value in self.props.items()])
            result = f'<{self.tag} {props_str}>'
        else:
            result = f'<{self.tag}>'

        # Process children...
        # Loop through children...
        for child in self.children:
            # Call to_html() on the child and add it to result
            result += child.to_html()

        # Add closing tag
        result += f'</{self.tag}>'
        return result