from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnode
import unittest

class TestingTextNode(unittest.TestCase):
    def test_node_text(self):
        text = "This is a **sample** text and a _piece of_ `code`"

        node = text_to_textnode(text)

        self.assertEqual(node, [TextNode("This is a ", TextType.TEXT), TextNode("sample", TextType.BOLD), TextNode(" text and a ", TextType.TEXT), TextNode("piece of", TextType.ITALICS), TextNode(" ", TextType.TEXT), TextNode("code", TextType.CODE)])

    def test_node_link_image(self):
        text = "This is a _sample of_ ![an image](https://www.imgur.com/fJRm4Vk.jpeg) and a **link** [to boot dev](https://www.boot.dev.com)"

        node = text_to_textnode(text)

        self.assertEqual(node, [TextNode("This is a ", TextType.TEXT), TextNode("sample of", TextType.ITALICS), TextNode("an image", TextType.IMAGE, "https://www.imgur.com/fJRm4Vk.jpeg"), TextNode(" and a ", TextType.TEXT), TextNode("link", TextType.BOLD), TextNode("to boot dev", TextType.LINK, "https://www.boot.dev.com")])