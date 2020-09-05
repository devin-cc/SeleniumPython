# 导包
from parameterized import parameterized
from selenium import webdriver

from v4.page.page_login import PageLogin
import unittest


def get_data():
    return [("APP20020007-ADMIN", "123456", "用户名或密码错误"), ("APP20020007-ADMI", "123456", "用户不存在")]


# 新建测试类，并继承TestCase
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login = PageLogin()

    def tearDown(self):
        self.login.driver.quit()

    @parameterized.expand(get_data())
    def test_login(self, username, password, expect):
        # 调用登陆方法
        self.login.page_login(username, password)

        # 获取登陆提示
        msg = self.login.page_get_err_info()

        self.assertIn(msg, expect)

        self.login.get_page_get_image()
