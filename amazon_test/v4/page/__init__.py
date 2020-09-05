from selenium.webdriver.common.by import By

"""以下为测试环境url"""
url = "http://1111"

"""以下为登陆页面元素配置信息，临时存放地"""
login_username = By.ID, "normal_login_user_account"
login_password = By.ID, "normal_login_user_password"
login_btn = By.CLASS_NAME, "login-form-button"
login_error = By.XPATH, "/html/body/div[2]/span/div/div/div/span"


"""以下为新建广告活动页面元素配置信息"""
new_campaigns_user_account = By.CLASS_NAME, "ant-select-selection__placeholder"
new_campaigns_name = By.ID, "basic_form_campaign_name"
new_campaigns_time_start = By.ID, "basic_form_startTime"
new_campaigns_time_end = By.ID, "basic_form_endTime"
new_campaigns_daily_budget = By.ID, "basic_form_campaign_daily_budget"

