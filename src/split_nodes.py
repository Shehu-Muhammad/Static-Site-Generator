from text_type import TextType
from textnode import TextNode
from extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        splits = node.text.split(delimiter)
        if len(splits) %2 == 0:
            raise ValueError("invalid markdown, formatted split not closed")
        for i in range(len(splits)):
            if splits[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(splits[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(splits[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
            continue

        # For each image tuple (alt, url) in images...
        for alt, url in images:
            # Use the full image markdown pattern
            image_markdown = f"![{alt}]({url})"
            sections = node.text.split(image_markdown, 1)
            text = sections[0]
            if text != "":
                new_nodes.append(TextNode(text, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            more_text = sections[1]
            if more_text != "":
                new_nodes.append(TextNode(more_text, TextType.TEXT))

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        text = node.text

        while True:
            # Extract the links from the current text
            links = extract_markdown_links(text)
            if not links:
                # If no links are found, append the entire remaining text
                if text:
                    new_nodes.append(TextNode(text, TextType.TEXT))
                break

            # Extract the first link
            alt, url = links[0]
            link_markdown = f"[{alt}]({url})"

            if link_markdown in text:
                # Split into parts: before, the link, and after
                sections = text.split(link_markdown, 1)
                before_text = sections[0]
                after_text = sections[1]

                # Append the portion before the link if it exists
                if before_text:
                    new_nodes.append(TextNode(before_text, TextType.TEXT))

                # Append the link node
                new_nodes.append(TextNode(alt, TextType.LINK, url))

                # Update `text` to only the remaining part (after the link)
                text = after_text

    return new_nodes
