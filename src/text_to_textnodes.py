from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode
from text_type import TextType

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

# def text_to_textnodes(text):
#     nodes = [TextNode(text, TextType.TEXT)]
#     print("Initial nodes:", nodes)
    
#     nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
#     print("After BOLD split:", nodes)
    
#     nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
#     print("After ITALIC split:", nodes)
    
#     nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
#     print("After CODE split:", nodes)
    
#     nodes = split_nodes_image(nodes)
#     print("After IMAGE split:", nodes)
    
#     nodes = split_nodes_link(nodes)
#     print("After LINK split:", nodes)
    
#     return nodes