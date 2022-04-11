from selenium.webdriver.common.by import By
from poms.Page import PageNotSignedIn, PageSignedIn

class HomePage():
    
    def __init__(self, browser):
        pass

class HomePageNotSignedIn(PageNotSignedIn, HomePage):
    
    def __init__(self, browser):
        PageNotSignedIn.__init__(self, browser)
        HomePage.__init__(self, browser)
        self.get_started_btn = browser.find_element(By.XPATH, '//*[@id="Sign-in Button "]')
    
    def click_get_started(self):
        self.get_started_btn.click()

class HomePageSignedIn(PageSignedIn, HomePage):
    
    def __init__(self, browser):
        PageSignedIn.__init__(self, browser)
        HomePage.__init__(self, browser)
        self.my_hero_btn = browser.find_element(By.XPATH, '/html/body/div/main/div/div/div/a')

    def click_my_hero(self):
        self.my_hero_btn.click()
        