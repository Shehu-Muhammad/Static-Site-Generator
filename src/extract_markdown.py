import re
from text_type import TextType
from textnode import TextNode

def extract_markdown_images(text):
    image_reg = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(image_reg, text)
    return matches

def extract_markdown_links(text):
    link_reg = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(link_reg, text)
    return matches
