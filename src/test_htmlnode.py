import unittest

from htmlnode import HtmlNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HtmlNode(props={"href": "http://some.website.com", "target": "_blank"})
        expected_html = ' href="http://some.website.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_html)
