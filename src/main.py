from textnode import TextNode, TextType

def main():
    node1 = TextNode("Hello World", TextType.TEXT)
    node2 = TextNode("Hello World", TextType.BOLD)

    # Print the nodes (this automatically uses __repr__)
    print(node1)
    print(node2)

    # Compare nodes (this automatically uses __eq__)
    print(node1 == node2)

main()
