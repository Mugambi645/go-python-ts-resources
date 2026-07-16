import unittest
from htmlnode import HTMLNode, LeafNode


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



class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        """Standard leaf node renders correctly with tag wrapping."""
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_with_props(self):
        """Leaf node appends properties inside the opening tag."""
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), 
            '<a href="https://www.google.com">Click me!</a>'
        )

    def test_leaf_to_html_raw_text(self):
        """If the tag is None, the value should be returned as raw text."""
        node = LeafNode(None, "This is raw text.")
        self.assertEqual(node.to_html(), "This is raw text.")

    def test_leaf_to_html_no_value_raises_value_error(self):
        """A LeafNode missing a value should raise a ValueError when converted."""
        # We explicitly pass None as a value to trigger the safety validation
        node = LeafNode("p", None)  # type: ignore
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()