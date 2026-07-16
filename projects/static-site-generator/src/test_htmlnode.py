import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


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




class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        """Standard parent node containing simple leaf children renders correctly."""
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        """Deeply nested parent nodes compute HTML recursively."""
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_many_children(self):
        """Checks parent node rendering sequence with multiple types of child leaf nodes."""
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_to_html_with_props(self):
        """Checks properties rendering on parent node level."""
        child = LeafNode("span", "text")
        parent = ParentNode("div", [child], {"class": "container", "id": "main"})
        self.assertEqual(
            parent.to_html(),
            '<div class="container" id="main"><span>text</span></div>'
        )

    def test_to_html_missing_tag_raises_value_error(self):
        """Parent node initialized without a tag raises ValueError on conversion."""
        node = ParentNode(None, [LeafNode("span", "text")])  # type: ignore
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_missing_children_raises_value_error(self):
        """Parent node initialized without child elements raises ValueError on conversion."""
        node = ParentNode("div", None)  # type: ignore
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()