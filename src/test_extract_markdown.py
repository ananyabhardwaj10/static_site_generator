import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestMarkdownImagesLinks(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches1 = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches1)

    def test_extract_markdown_images1(self):
        matches2 = extract_markdown_images("This is the ![Image of Taj Mahal](https://www.google.com/search?sca_esv=b386a5f6b630f72d&sxsrf=AE3TifNXb3q3FZVp-sUydQ0IzdB9tMzXbA:1766141034209&udm=2&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIeuYzzFkfneXafNx6OMdA4MRT57TpI4o2tavIRfF1e7-xTLfbOlRZsi_SKi4JeEBY7pnUnsYZ2YolLXlDdpWd5X8Dl3ww1kgiAU4MTvhlsxynlXYG66bQ0LfJUkXjx90u6LziqyMljOah4l7FbuzQ5ppUaZOESIdhGWk6sqjHiMsayGn74Q&q=taj+mahal&sa=X&ved=2ahUKEwjVl96HvMmRAxVg3jgGHQb5KacQtKgLegQIERAB&biw=1536&bih=730&dpr=1.25#sv=CAMSVhoyKhBlLVV3STZDWkx4V1lLamVNMg5Vd0k2Q1pMeFdZS2plTToOZmd4UkQxMHpmTjBQN00gBCocCgZtb3NhaWMSEGUtVXdJNkNaTHhXWUtqZU0YADABGAcgv_f_qwkwAkoKCAEQAhgCIAIoAg)")
        self.assertListEqual([("Image of Taj Mahal", "https://www.google.com/search?sca_esv=b386a5f6b630f72d&sxsrf=AE3TifNXb3q3FZVp-sUydQ0IzdB9tMzXbA:1766141034209&udm=2&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIeuYzzFkfneXafNx6OMdA4MRT57TpI4o2tavIRfF1e7-xTLfbOlRZsi_SKi4JeEBY7pnUnsYZ2YolLXlDdpWd5X8Dl3ww1kgiAU4MTvhlsxynlXYG66bQ0LfJUkXjx90u6LziqyMljOah4l7FbuzQ5ppUaZOESIdhGWk6sqjHiMsayGn74Q&q=taj+mahal&sa=X&ved=2ahUKEwjVl96HvMmRAxVg3jgGHQb5KacQtKgLegQIERAB&biw=1536&bih=730&dpr=1.25#sv=CAMSVhoyKhBlLVV3STZDWkx4V1lLamVNMg5Vd0k2Q1pMeFdZS2plTToOZmd4UkQxMHpmTjBQN00gBCocCgZtb3NhaWMSEGUtVXdJNkNaTHhXWUtqZU0YADABGAcgv_f_qwkwAkoKCAEQAhgCIAIoAg")], matches2)

    def test_extract_markdown_links1(self):
        matches = extract_markdown_links("This is a text with a link [to boot dev](https://www.boot.dev.com)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev.com")], matches)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev.com) and another [to google](https://www.google.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
        [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev.com"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "to google", TextType.LINK, "https://www.google.com"
            ),
        ],
            new_nodes,
        )