#!/usr/bin/env python3
""" Module to test client """

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """method should test that GithubOrgClient.org. """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        mock_response = {'login': org_name}
        mock_get_json.return_value = mock_response

        github_client = GithubOrgClient(org_name)
        result = github_client.org

        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, mock_response)

