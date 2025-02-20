
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []  # Normalize to []
        self.props = props if props is not None else {}  # Normalize to {}

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        result = ""
        # Loop through each key-value pari in self.props
        for key, value in self.props.items():
            result += f" {key}=\"{value}\""
        return result
    
    def __repr__(self):
        return (
            f"HTMLNode(tag={repr(self.tag)}, value={repr(self.value)}, "
            f"children={repr(self.children)}, props={repr(self.props)})"
        )
    
    