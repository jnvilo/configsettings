from __future__ import print_function
import unittest
import mock
import os

from configsettings.config import Configuration

class TestConfigSettings(unittest.TestCase):

    def setUp(self) -> None:
        self.gitlab_url = 'http://gitlab.localhost'
        self.gitlab_token = 'asdjfaklsjfewiropweioavdsfdsjkaf;adsjfkadsfj adskf'
        os.environ['GITLAB_URL'] = self.gitlab_url
        os.environ['GITLAB_TOKEN'] = self.gitlab_token

    def test_can_read_from_environment_settings(self):
        config_vars = {"GITLAB_URL": None,
                       "GITLAB_TOKEN": None }

        c = Configuration("myapp", config_vars=config_vars)

        self.assertEqual(c.GITLAB_URL, self.gitlab_url)
        self.assertEqual(c.GITLAB_TOKEN, self.gitlab_token)