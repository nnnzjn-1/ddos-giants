import unittest
import os
from core import utils, runner

class TestUtils(unittest.TestCase):

    def test_load_proxies(self):
        # إعداد ملف بروكسي مؤقت للاختبار
        proxy_file = "tests/test_proxies.txt"
        with open(proxy_file, "w") as f:
            f.write("127.0.0.1:8080\n")
            f.write("192.168.1.1:1080\n")

        proxies = utils.load_proxies(proxy_file)
        self.assertIsInstance(proxies, list)
        self.assertIn("127.0.0.1:8080", proxies)
        self.assertIn("192.168.1.1:1080", proxies)

        os.remove(proxy_file)  # حذف الملف بعد الاختبار

    def test_load_proxies_empty(self):
        proxy_file = "tests/empty_proxies.txt"
        with open(proxy_file, "w") as f:
            pass  # ملف فارغ

        proxies = utils.load_proxies(proxy_file)
        self.assertEqual(proxies, [])

        os.remove(proxy_file)

class TestRunner(unittest.TestCase):

    def test_valid_url(self):
        url = "https://example.com"
        self.assertTrue(runner.is_valid_url(url))

    def test_invalid_url(self):
        url = "invalid_url"
        self.assertFalse(runner.is_valid_url(url))

    def test_attack_modes_exist(self):
        # تأكد أن كل الأوضاع موجودة في runner.py
        modes = ["GET", "POST", "bypass", "proxy_get", "proxy_post"]
        for mode in modes:
            self.assertTrue(hasattr(runner, f"attack_{mode.lower()}"), f"Missing attack_{mode.lower()} function")

    def test_runner_entry_point(self):
        # مجرد اختبار استدعاء دالة main بدون تنفيذ الهجوم
        # تأكد أن الدالة main موجودة وقابلة للاستدعاء
        self.assertTrue(callable(runner.main))

if __name__ == '__main__':
    unittest.main()