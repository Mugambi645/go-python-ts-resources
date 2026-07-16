import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        """Two nodes with identical text and type (default URL None) should be equal"""
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        """Two nodes with matching URLs should be equal"""
        node = TextNode("Click here", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("Click here", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        """Nodes with different text should not be equal"""
        node = TextNode("Hello", TextType.NORMAL)
        node2 = TextNode("World", TextType.NORMAL)
        self.assertNotEqual(node, node2)

    def test_not_eq_type(self):
        """Nodes with different text types should not be equal"""
        node = TextNode("Bold block", TextType.BOLD)
        node2 = TextNode("Bold block", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        """Nodes where one has a URL and the other has None (or a different URL) should not be equal"""
        node = TextNode("Linked text", TextType.LINK, "https://google.com")
        node2 = TextNode("Linked text", TextType.LINK)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()