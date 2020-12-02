from app import is_alive_host

import unittest


class TestApi(unittest.TestCase):
    def test_alive_host(self):
        self.assertTrue(is_alive_host("vk.com"))

    def test_down_host(self):
        self.assertFalse(is_alive_host("shava.rim"))
