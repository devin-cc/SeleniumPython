from selenium import webdriver
from v4 import page


class GetDriver:
    # 设置类属性
    driver = None

    # 获取driver
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # 实例化浏览器
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.get(page.url)
        return cls.driver
