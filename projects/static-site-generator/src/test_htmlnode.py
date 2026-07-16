import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_values(self):
        """Standard key-value dictionary returns formatted HTML attributes with a leading space."""
        node = HTMLNode(
            tag="a",
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"'
        )

    def test_props_to_html_empty_or_none(self):
        """When props is None or empty, should return an empty string."""
        node_none = HTMLNode(tag="p", props=None)
        node_empty = HTMLNode(tag="p", props={})
        
        self.assertEqual(node_none.props_to_html(), "")
        self.assertEqual(node_empty.props_to_html(), "")

    def test_defaults_to_none(self):
        """Nodes instantiated without arguments have fields set to None by default."""
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_to_html_raises_not_implemented(self):
        """Base HTMLNode calls to to_html() must raise a NotImplementedError."""
        node = HTMLNode(tag="p", value="Hello")
        with self.assertRaises(NotImplementedError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()