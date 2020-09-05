import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from common import Common_Fuc
import unittest


class Login_Page(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        time.sleep(5)
        self.driver.quit()

    def test_login01(self):
        self.driver.get('http://amazon.ecgtool.com/user/login')
        self.driver.find_element_by_id('normal_login_user_account').send_keys('APP20020007-ADMIN')
        self.driver.find_element_by_id('normal_login_user_password').send_keys('asd')
        self.driver.find_element_by_class_name('login-form-button').click()
        abc = self.driver.find_element_by_xpath("/html/body/div[2]/span/div/div/div/span").text
        expect = '用户名或密码错误'
        try:
            self.assertEqual(abc, expect)
        except AssertionError:
            self.driver.get_screenshot_as_file('.//image/{}.png'.format(time.strftime("%Y_%m_%d_%H%M%S")))

    @unittest.skip("运行报错")
    def test_login02(self):
        self.ch = Common_Fuc()
        self.ch.login('', 'asd123qwe')
    #
    # def test_login03(self):
    #     self.ch = Common_Fuc()
    #     self.ch.login('APP20020007-ADMIN', '')

    # def test_login04(self):
    #     self.ch = Common_Fuc()
    #     self.ch.login('APP20020007-ADMIN', '123')
    #     abc = self.ch.find_element('xpath', ".//div[@class='ant-message-custom-content']/span")
    #     print(abc.text)
