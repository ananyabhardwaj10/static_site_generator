from textnode import TextNode, TextType
from markdown_to_textnode import split_nodes_delimiter
from extract_markdown import split_nodes_image, split_nodes_link


def text_to_textnode(text):
    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALICS)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes