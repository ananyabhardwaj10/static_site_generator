from leafnode import LeafNode
import unittest

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "This is the link to Google.com", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=https://www.google.com>This is the link to Google.com</a>")
    
    def test_leaf_to_html_bold(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")