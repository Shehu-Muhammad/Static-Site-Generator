def markdown_to_blocks(markdown):
    new_list = markdown.split("\n\n")
    trimmed_list = []
    for item in new_list:
        if item != "":
            trimmed_list.append(item.strip())
    return trimmed_list