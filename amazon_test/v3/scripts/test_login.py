# 导包
import unittest
from parameterized import parameterized
from v3.page.page_login import PageLogin


# 新建测试类
class TestLogin(unittest.TestCase):
    # 初始化方法
    def setUp(self):
        self.login = PageLogin()

    # 结束方法
    def tearDown(self):
        self.login.driver.quit()

    # 新建测试方法
    @parameterized.expand([("APP20020007-ADMIN", "123456", "用户名或密码错误"), ("APP20020007-ADMI", "123456", "用户不存在")])
    def test_login(self, username, password, expect):
        # 调用测试登陆方法
        self.login.page_login(username, password)
        # 获取登陆结果
        msg = self.login.page_get_err_text()

        # 断言
        self.assertIn(expect, msg)

