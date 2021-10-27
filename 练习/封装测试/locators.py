from selenium.webdriver.common.by import By

class MainPageLogin(object):
    user_name = (By.ID, "txtUsername")
    user_pwd = (By.ID, "txtPassword")
    login_click=(By.ID, "btnLogin")

class OperationLocators(object):
    pim_view = (By.ID, "menu_pim_viewPimModule")
    add_user = (By.ID, "btnAdd")
    user_firstName=(By.ID, "firstName")
    user_lastName=(By.ID, "lastName")
    user_id=(By.ID, "employeeId")
    save=(By.ID, "btnSave")
    login_detail=(By.ID, "chkLogin")
    user_name=(By.ID, "user_name")
    user_pwd=(By.ID, "user_password")
    user_re_pwd=(By.ID, "re_password")
    user_re_pwd=(By.ID, "re_password")
    user_status=(By.ID, "status")