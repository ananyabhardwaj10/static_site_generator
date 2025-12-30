import unittest
from blocks import BlockType, block_to_block_type, markdown_to_html_node


class TestBlocks(unittest.TestCase):
    def testing_blocks_heading(self):
        markdown = """
## Heading level 2
"""
        block = block_to_block_type(markdown)
        self.assertEqual(block, BlockType.HEADING)

    def testing_blocks_paragraphs(self):
        markdown = """
Normal paragraph text with **bold**, _italics_, and `code`.
"""
        block = block_to_block_type(markdown)
        self.assertEqual(block, BlockType.PARAGRAPH)

    def testing_blocks_code(self):
        markdown = """```
def hello():
    print("codeblock")
```"""
        block = block_to_block_type(markdown)
        self.assertEqual(block, BlockType.CODE)
    
    def testing_blocks_quote(self):
        markdown = """
> this is a quote
> that spans multiple lines
"""
        block = block_to_block_type(markdown)
        self.assertEqual(block, BlockType.QUOTE)

    def testing_blocks_unordered_list(self):
        markdown = """
- first item
- second item 
- third item
"""
        block = block_to_block_type(markdown)
        self.assertEqual(block, BlockType.UNORDERED_LIST)

    def testing_blocks_ordered_list(self):
        markdown = """
1. first item
2. second item
3. third item
"""
        block = block_to_block_type(markdown)
        self.assertEqual(block, BlockType.ORDERED_LIST)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )