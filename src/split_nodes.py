from text_type import TextType
from textnode import TextNode
from extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
            
        current_text = node.text
        while current_text:  # Keep processing as long as we have text
            images = extract_markdown_images(current_text)
            if not images:
                # No more images found, add remaining text and break
                new_nodes.append(TextNode(current_text, TextType.TEXT))
                break
                
            # Process the first image found
            alt, url = images[0]
            image_markdown = f"![{alt}]({url})"
            sections = current_text.split(image_markdown, 1)
            
            # Add text before image if it exists
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
                
            # Add the image node
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            
            # Continue with remaining text
            current_text = sections[1] if len(sections) > 1 else ""
            
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

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