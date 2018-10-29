#coding=utf-8
import time
import unittest
import HTMLTestRunner


class BrowserTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_baidu(self):
        self.assertEqual(5, 3+2)

    def test_sougou(self):
        self.assertEqual(6, 3 + 3)

    def test_souhu(self):
        self.assertEqual(7, 3 + 4)

    def tearDown(self):
        pass


testunit = unittest.TestSuite()
testunit.addTest(BrowserTest("test_baidu"))
testunit.addTest(BrowserTest("test_sougou"))
testunit.addTest(BrowserTest("test_souhu"))
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
HtmlFile = "./"+now+"HTMLtemplate.html"
with open(HtmlFile, "wb") as fp:
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"百度测试报告", description=u"用例测试情况")
    runner.run(testunit)


