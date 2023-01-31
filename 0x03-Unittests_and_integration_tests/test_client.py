#!/usr/bin/env python3
"""
test_client
"""
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    tests GithubOrgClient method
    """

    @parameterized.expand([("google"), ("abc")])
    @patch("client.get_json")
    def test_org(self, org_name, mock):
        """
        test get org
        """
        info = GithubOrgClient(org_name)
        info.org()
        mock.assert_called_once_with("https://api.github.com/orgs/{}".format(
                                     org_name))


if __name__ == "__main__":
    unittest.main()
