#!/usr/bin/env python3
""" Module to test client """

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

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

    def test_public_repos_url(self):
        """Test the _public_repos_url property of GithubOrgClient"""
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {'repos_url': 'https://api.github.com/orgs/google/repos'}
            github_client = GithubOrgClient('google')

            result = github_client._public_repos_url

            self.assertEqual(result, 'https://api.github.com/orgs/google/repos')

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test the public_repos method of GithubOrgClient"""
        mock_repos_payload = [
            {'name': 'repo1'},
            {'name': 'repo2'},
            {'name': 'repo3'}
        ]
        mock_get_json.return_value = mock_repos_payload

        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = 'https://api.github.com/orgs/google/repos'
            github_client = GithubOrgClient('google')
            result = github_client.public_repos()

            self.assertEqual(result, ['repo1', 'repo2', 'repo3'])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with('https://api.github.com/orgs/google/repos')

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test the has_license method of GithubOrgClient"""
        github_client = GithubOrgClient('google')
        result = github_client.has_license(repo, license_key)
        self.assertEqual(result, expected)
