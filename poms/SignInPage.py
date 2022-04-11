from selenium.webdriver.common.by import By
from poms.Page import PageNotSignedIn

class SignInPage(PageNotSignedIn):
    
    def __init__(self, browser):
        super().__init__(browser)
        self.toggle_btn = browser.find_element(By.ID, 'toggle-forms')
        self.submit_btn = browser.find_element(By.XPATH, '//*[@id="root"]/main/div/section/form/div/button')
        
    def click_toggle(self):
        self.toggle_btn.click()
        
    def click_submit(self):
        self.submit_btn.click()
        
class LoginPage(SignInPage):
    
    def __init__(self, browser):
        super().__init__(browser)
        self.nickname_box = browser.find_element(By.XPATH, '//*[@id="root"]/main/div/section/form/input[1]')
        self.password_box = browser.find_element(By.XPATH, '//*[@id="root"]/main/div/section/form/input[2]')
        
    def type_nickname(self, nickname):
        self.nickname_box.send_keys(nickname)

    def type_password(self, password):
        self.password_box.send_keys(password)
    
    def log_in(self, nickname, password):
        self.type_nickname(nickname)
        self.type_password(password)
        self.click_submit()
    
class RegisterPage(SignInPage):
    
    def __init__(self, browser):
        super().__init__(browser)
        self.click_toggle()
        self.name_box = browser.find_element(By.XPATH, '//*[@id="root"]/main/div/section/form/input[1]')
        self.nickname_box = browser.find_element(By.XPATH, '//*[@id="root"]/main/div/section/form/input[2]')
        self.password_box1 = browser.find_element(By.XPATH, '//*[@id="root"]/main/div/section/form/input[3]')
        self.password_box2 = browser.find_element(By.XPATH, '//*[@id="root"]/main/div/section/form/input[4]')
    
    def type_name(self, name):
        self.name_box.send_keys(name)
        
    def type_nickname(self, nickname):
        self.nickname_box.send_keys(nickname)
        
    def type_password(self, password):
        self.password_box1.send_keys(password)
        
    def confirm_password(self, password):
        self.password_box2.send_keys(password)
        
    def register_user(self, name, nickname, password):
        self.type_name(name)
        self.type_nickname(nickname)
        self.type_password(password)
        self.confirm_password(password)
        self.click_submit()
    
    def register_user_diff_passwords(self, name, nickname, password):
        self.type_name(name)
        self.type_nickname(nickname)
        self.type_password(password)
        self.confirm_password(password + ' ')
        self.click_submit()
