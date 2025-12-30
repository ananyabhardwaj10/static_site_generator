import unittest
from textnode import TextNode, TextType
from markdown_to_textnode import split_nodes_delimiter


class TestMarkdownToTextNode(unittest.TestCase):
    def test_text_codeBlock(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT)]
        self.assertEqual(new_nodes, expected)

    def test_text_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [TextNode("This is text with a ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" word", TextType.TEXT)]
        self.assertEqual(new_nodes, expected)

    def test_text_italics(self):
        node = TextNode("This is text with an _italicised_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALICS)
        expected = [TextNode("This is text with an ", TextType.TEXT), TextNode("italicised", TextType.ITALICS), TextNode(" word", TextType.TEXT)]
        self.assertEqual(new_nodes, expected)
        