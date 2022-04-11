from selenium.webdriver.common.by import By
from poms.Page import PageSignedIn

class EditProfilePage(PageSignedIn):
    
    def __init__(self, browser):
        super().__init__(browser)
        self.name_box = self.browser.find_element(By.ID, 'nameBox')
        self.nickname_box = self.browser.find_element(By.ID, 'nicknameBox')
        self.avatar_btn_1 = self.browser.find_element(By.XPATH, '//*[@id="https://robohash.org/eteosqui.png?size=300x300&set=set1"]')
        self.avatar_btn_2 = self.browser.find_element(By.XPATH, '//*[@id="https://robohash.org/adnesciuntconsequatur.png?size=300x300&set=set1"]')
        self.avatar_btn_3 = self.browser.find_element(By.XPATH, '//*[@id="https://robohash.org/sequisimiliquepraesentium.png?size=300x300&set=set1"]')
        self.avatar_btn_4 = self.browser.find_element(By.XPATH, '//*[@id="https://robohash.org/eamollitiadolores.png?size=300x300&set=set1"]')
        self.avatar_btn_5 = self.browser.find_element(By.XPATH, '//*[@id="https://robohash.org/nihilconsequaturet.png?size=300x300&set=set1"]')
        self.update_btn = self.browser.find_element(By.ID, 'updateBtn')
        self.profile_btn = self.browser.find_element(By.ID, 'profileBtn')
        
    def type_name(self, name):
        self.name_box.clear()
        self.name_box.send_keys(name)
        
    def type_nickname(self, nickname):
        self.nickname_box.clear()
        self.nickname_box.send_keys(nickname)
        
    def click_avatar(self, avatar_no):        
        self.avatar_buttons = [self.avatar_btn_1.click,
                               self.avatar_btn_2.click,
                               self.avatar_btn_3.click,
                               self.avatar_btn_4.click,
                               self.avatar_btn_5.click]
        
        self.avatar_buttons[avatar_no - 1]()
    
    def click_update(self):
        self.update_btn.click()
        
    def update_user(self, name, nickname, avatar_no):
        self.type_name(name)
        self.type_nickname(nickname)
        self.click_avatar(avatar_no)
        self.click_update()
        
    def click_profile(self):
        self.profile_btn.click()
    