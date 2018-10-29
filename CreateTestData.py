#coding=utf-8
import unittest
from selenium import webdriver


class BrowserTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_baidu(self):
        self.assertEqual(5, 3+2)

    def test_sougou(self):
        self.assertEqual(6, 3 + 3)

    def test_souhu(self):
        self.assertEqual(9, 3 + 4)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()


