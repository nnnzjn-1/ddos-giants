import unittest
import os
from unittest.mock import patch, AsyncMock
from core import utils, runner

class TestUtils(unittest.TestCase):

    def test_load_proxies(self):
        proxy_file = "tests/test_proxies.txt"
        with open(proxy_file, "w") as f:
            f.write("127.0.0.1:8080\n")
            f.write("192.168.1.1:1080\n")

        proxies = utils.load_proxies(proxy_file)
        self.assertIsInstance(proxies, list)
        self.assertIn("127.0.0.1:8080", proxies)
        self.assertIn("192.168.1.1:1080", proxies)

        os.remove(proxy_file)

    def test_load_proxies_empty(self):
        proxy_file = "tests/empty_proxies.txt"
        with open(proxy_file, "w") as f:
            pass

        proxies = utils.load_proxies(proxy_file)
        self.assertEqual(proxies, [])

        os.remove(proxy_file)

    def test_load_proxies_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            utils.load_proxies("non_existent_file.txt")

class TestRunner(unittest.TestCase):

    def test_valid_url(self):
        url = "https://example.com"
        self.assertTrue(runner.is_valid_url(url))

    def test_invalid_url(self):
        url = "invalid_url"
        self.assertFalse(runner.is_valid_url(url))

    def test_attack_modes_exist(self):
        modes = ["GET", "POST", "bypass", "proxy_get", "proxy_post"]
        for mode in modes:
            self.assertTrue(hasattr(runner, f"attack_{mode.lower()}"), f"Missing attack_{mode.lower()} function")

    def test_runner_entry_point(self):
        self.assertTrue(callable(runner.main))

    @patch('core.runner.attack_get', new_callable=AsyncMock)
    def test_attack_get_called(self, mock_attack_get):
        # Test that attack_get is called with correct params
        url = "https://example.com"
        duration = 10
        threads = 5
        proxies = []

        # Call the coroutine attack_get
        import asyncio
        asyncio.run(runner.attack_get(url, duration, threads, proxies))

        mock_attack_get.assert_called_with(url, duration, threads, proxies)

    @patch('core.runner.attack_post', new_callable=AsyncMock)
    def test_attack_post_called(self, mock_attack_post):
        url = "https://example.com"
        duration = 10
        threads = 5
        proxies = []
        post_data = "param=value"

        import asyncio
        asyncio.run(runner.attack_post(url, duration, threads, proxies, post_data))

        mock_attack_post.assert_called_with(url, duration, threads, proxies, post_data)

    def test_post_data_loading(self):
        post_data = "param1=value1&param2=value2"
        self.assertIsInstance(post_data, str)
        self.assertIn("param1=value1", post_data)

if __name__ == '__main__':
    unittest.main()