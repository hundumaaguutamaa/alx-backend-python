#!/usr/bin/env python3
""" Module to test client """

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


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
        mock_get_json.return_value = [
            {'name': 'repo1', 'license': {'key': 'apache-2.0'}},
            {'name': 'repo2', 'license': {'key': 'mit'}},
            {'name': 'repo3', 'license': {'key': 'apache-2.0'}}
        ]

        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = 'https://api.github.com/orgs/google/repos'
            github_client = GithubOrgClient('google')
            result = github_client.public_repos()

            self.assertEqual(result, ['repo1', 'repo2', 'repo3'])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with('https://api.github.com/orgs/google/repos')

    @patch('client.get_json')
    def test_public_repos_with_license(self, mock_get_json):
        """Test the public_repos method of GithubOrgClient with a license filter"""
        mock_get_json.return_value = [
            {'name': 'repo1', 'license': {'key': 'apache-2.0'}},
            {'name': 'repo2', 'license': {'key': 'mit'}},
            {'name': 'repo3', 'license': {'key': 'apache-2.0'}}
        ]

        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = 'https://api.github.com/orgs/google/repos'
            github_client = GithubOrgClient('google')
            result = github_client.public_repos(license="apache-2.0")

            self.assertEqual(result, apache2_repos)
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


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test class for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set up class method to initialize patchers"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Side effects for different URLs
        def side_effect(url):
            if url == "https://api.github.com/orgs/google":
                return Mock(json=lambda: cls.org_payload)
            elif url == "https://api.github.com/orgs/google/repos":
                return Mock(json=lambda: cls.repos_payload)
            return Mock(json=lambda: {})

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Tear down class method to stop patchers"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test the public_repos method of GithubOrgClient"""
        github_client = GithubOrgClient('google')
        self.assertEqual(github_client.public_repos(), expected_repos)
    
    def test_public_repos_with_license(self):
        """Test the public_repos method of GithubOrgClient with a license filter"""
        github_client = GithubOrgClient('google')
        self.assertEqual(github_client.public_repos(license="apache-2.0"), apache2_repos)
