from v4 import page
from v4.base.base import Base


class PageLogin(Base):
    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    # 输入密码
    def page_input_pwd(self, password):
        self.base_input(page.login_password, password)

    # 点击登陆按钮
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    # 获取异常提示信息
    def page_get_err_info(self):
        return self.base_get_text(page.login_error)

    # 截图
    def get_page_get_image(self):
        self.base_get_image()

    # 具体需求步骤
    def page_login(self, username, password):
        self.page_input_username(username)
        self.page_input_pwd(password)
        self.page_click_login_btn()
