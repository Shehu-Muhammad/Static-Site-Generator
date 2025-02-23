import re

def extract_markdown_images(text):
    image_reg = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(image_reg, text)
    return matches

def extract_markdown_links(text):
    link_reg = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(link_reg, text)
    return matches
