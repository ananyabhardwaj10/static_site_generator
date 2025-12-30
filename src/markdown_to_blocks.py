def markdown_to_block(markdown):
    blocks = markdown.split("\n\n")
    cleaned_block = []

    for block in blocks:
        stripped = block.strip()
        if stripped != "":
            cleaned_block.append(stripped)

    return cleaned_block