#coding=utf-8
import unittest
from selenium import webdriver


class BrowserTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_baidu(self):
        self.driver.get("http://www.baidu.com")
        tx = self.driver.find_element_by_id("su")
        self.assertEqual(u"百度一下", tx.get_attribute("value"))

    def test_sougou(self):
        self.driver.get("https://www.sogou.com/")
        self.assertIn(u"关于搜狗", self.driver.page_source)

    def test_souhu(self):
        self.driver.get("http://www.sohu.com/")
        self.assertIn(u"邮箱", self.driver.page_source)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()



