"""
    页面对象编写技巧
        类名：使用大驼峰将模块名称抄进来，有下划线去掉下划线
        方法：根据业务需求每个操作步骤单独封装一个方法
        方法名：page_xxx
"""
from selenium import webdriver


class PageLogin:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(50)
        self.driver.get('http://amazon.ecgtool.com/user/login')

    # 输入用户名
    def page_input_username(self, username):
        self.driver.find_element_by_id('normal_login_user_account').send_keys(username)

    # 输入密码
    def page_input_pwd(self, password):
        self.driver.find_element_by_id('normal_login_user_password').send_keys(password)

    # 点击登陆
    def page_click_login_btn(self):
        self.driver.find_element_by_class_name('login-form-button').click()

    # 获取异常信息
    def page_get_err_text(self):
        return self.driver.find_element_by_xpath("/html/body/div[2]/span/div/div/div/span").text

    # 组装登陆业务方法，给业务层调用
    def page_login(self, username, password):
        self.page_input_username(username)
        self.page_input_pwd(password)
        self.page_click_login_btn()
        self.page_get_err_text()
