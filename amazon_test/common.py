from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
# test
sssssssssssss

class Common_Fuc:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def open_page(self):
        self.driver.get('http://amazon.ecgtool.com/user/login')

    def close_page(self):
        self.driver.quit()

    def find_element(self, by, element):
        if by == 'id':
            return self.driver.find_element(By.ID, element)
        elif by == 'classname':
            return self.driver.find_element(By.CLASS_NAME, element)
        elif by == 'xpath':
            return self.driver.find_element(By.XPATH, element)
        elif by == 'css':
            return self.driver.find_element(By.CSS_SELECTOR, element)

    def login(self, username, password):
        self.open_page()
        self.find_element('id', 'normal_login_user_account').send_keys(username)
        self.find_element('id', 'normal_login_user_password').send_keys(password)
        self.find_element('classname', 'login-form-button').click()
        # self.close_page()
