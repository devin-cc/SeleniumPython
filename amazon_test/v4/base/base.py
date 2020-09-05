from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

"""
    1,以下方法中，解包只需一次，在查找元素解包
    2，driver为虚拟，谁调用，谁传入，无需关注来源
    3，loc:真正使用loc的方法只有查找元素的方法
"""


class Base:
    # 初始化
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(40)
        self.driver.get("http://amazon.ecgtool.com/user/login")

    # 查找元素方法（提供：点击，输入，获取文本）使用
    def base_find_element(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击方法
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 输入方法
    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)

    # 获取文本方法
    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    # 截图方法
    def base_get_image(self):
        self.driver.get_screenshot_as_file(".//image/fail.png")
