#!/usr/bin/env python3
"""
test_utils
"""
from parameterized import parameterized, parameterized_class
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    method to test access_nested_map to
    ensure it returns what it is supposed to.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, n_map, val_path, value):
        """
        tests the access_nested_map
        """
        self.assertEqual(access_nested_map(n_map, val_path), value)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, n_map, val_path):
        """
        test missing key
        """
        self.assertRaises(KeyError, access_nested_map, n_map, val_path)


if __name__ == '__main__':
    unittest.main()
