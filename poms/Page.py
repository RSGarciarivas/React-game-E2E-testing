from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page():
    
    def __init__(self, browser):
        self.browser = browser
        self.navbar_logo = self.browser.find_element(By.XPATH, '/html/body/div/nav/div/a')
        self.navbar_globe = self.browser.find_element(By.XPATH, '//*[@id="Navbar"]/div/a/i')
        self.home_btn = self.browser.find_element(By.XPATH, '//*[@id="root"]/nav/div/ul/li[1]/a')
        self.hof_btn = self.browser.find_element(By.XPATH, '//*[@id="Navbar"]/div/ul/li[2]/a')
        self.about_btn = self.browser.find_element(By.XPATH, '//*[@id="Navbar"]/div/ul/li[3]/a')
        self.players_btn = self.browser.find_element(By.XPATH, '//*[@id="Navbar"]/div/ul/li[4]/a')
        self.compact_menu_btn = self.browser.find_element(By.XPATH, '//*[@id="Navbar"]/div/div/i')
            
    def click_univ_gods(self):
        self.navbar_logo.click
    
    def click_globe(self):
        self.navbar_globe.click()    

    def click_home(self):
        if self.compact_menu_btn.is_displayed():
            self.compact_menu_btn.click()
        self.home_btn.click()
    
    def click_hall_of_fame(self):
        if self.compact_menu_btn.is_displayed():
            self.compact_menu_btn.click()
        self.hof_btn.click()
    
    def click_about(self):
        if self.compact_menu_btn.is_displayed():
            self.compact_menu_btn.click()
        self.about_btn.click()
        
    def click_players(self):
        if self.compact_menu_btn.is_displayed():
            self.compact_menu_btn.click()
        self.players_btn.click()

class PageNotSignedIn(Page):
    '''
    Navigation bar buttons specific to when user is not signed in
    '''
    def __init__(self, browser):
        super().__init__(browser)
        self.signIn_btn = self.browser.find_element(By.ID, 'Sign-in Button ')
        
    def click_signIn(self):
        if self.compact_menu_btn.is_displayed():
            self.compact_menu_btn.click()
        self.signIn_btn.click()

class PageSignedIn(Page):
    '''
    Navigation bar buttons specific to when user is signed in
    '''
    def __init__(self, browser):
        super().__init__(browser)
        self.dashboard_btn = WebDriverWait(self.browser, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="Navbar"]/div/ul/li[5]/a')))
        self.logout_btn = self.browser.find_element(By.XPATH, '//*[@id="Sign-in Button "]/button')
        
    def click_dashboard(self):
        if self.compact_menu_btn.is_displayed():
            self.compact_menu_btn.click()
        self.dashboard_btn.click()
        
    def click_logout(self):
        if self.compact_menu_btn.is_displayed():
            self.compact_menu_btn.click()
        self.logout_btn.click()
    