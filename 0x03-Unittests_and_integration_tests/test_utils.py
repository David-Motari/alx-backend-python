#!/usr/bin/env python3
"""
test_utils
"""
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
import requests


class TestAccessNestedMap(unittest.TestCase):
    """
    method to test access_nested_map to
    ensure it returns what it is supposed to.
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, n_map, val_path, value):
        """
        tests the access_nested_map
        """
        self.assertEqual(access_nested_map(n_map, val_path), value)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, n_map, val_path):
        """
        test missing key
        """
        self.assertRaises(KeyError, access_nested_map, n_map, val_path)


class TestGetJson(unittest.TestCase):
    """
    tests the get_json methon in utils
    """

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, get_url, get_payload):
        """
        tests get_json
        """
        with patch("requests.get") as mock_reqs:
            mock_reqs.return_value.json.return_value = get_payload
            self.assertEqual(get_json(get_url), get_payload)


class TestMemoize(unittest.TestCase):
    """
    test for memoize
    """

    def test_memoize(self):
        """
        tests the memoize method
        """
        class TestClass:
            """
            test class
            """

            def a_method(self):
                """ method"""
                return 42

            @memoize
            def a_property(self):
                """property"""
                return self.a_method()

        with patch.object(TestClass, "a_method") as mock_t:
            cls_test = TestClass()
            cls_test.a_property()
            cls_test.a_property
            mock_t.assert_called_once()


if __name__ == "__main__":
    unittest.main()
