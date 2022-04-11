import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from poms.HomePage import HomePageNotSignedIn
from poms.SignInPage import LoginPage
from poms.DashboardPage import DashboardPage
from poms.HallOfFamePage import HallOfFamePageNotSignedIn

class DeviceCompatibilityTests(unittest.TestCase):
    
    def setUp(self):
        service = r'C:\Users\Rafael\Documents\Projects\Universe Gods\react_game_app_e2e\chromedriver.exe'
        self.ser = Service(service)
        self.addr = 'http://18.209.14.86'
        self.chrome_options = Options()
    
    def sample_steps(self):
        '''
        Sign-in and attempt to click logout and hall of fame buttons
        '''
        page = HomePageNotSignedIn(self.browser)
        page.click_signIn()
        page = LoginPage(self.browser)
        page.log_in('rsg2703', 'password')
        page = DashboardPage(self.browser)
        page.click_logout()
        page = HomePageNotSignedIn(self.browser)
        page.click_hall_of_fame()
        page = HallOfFamePageNotSignedIn(self.browser)
        self.assertIn('hof', self.browser.current_url)
    
    '''
    Test sample steps in different (common) screen sizes
    '''
    def test_1920x1080_window(self):
        self.chrome_options.add_argument('window-size=1920,1080')
        self.browser = webdriver.Chrome(service = self.ser, options = self.chrome_options)
        self.browser.get(self.addr)
        self.sample_steps()
    
    def test_1366x768_window(self):
        self.chrome_options.add_argument('window-size=1366,768')
        self.browser = webdriver.Chrome(service = self.ser, options = self.chrome_options)
        self.browser.get(self.addr)
        self.sample_steps()
    
    def test_360x640_window(self):
        self.chrome_options.add_argument('window-size=360,640')
        self.browser = webdriver.Chrome(service = self.ser, options = self.chrome_options)
        self.browser.get(self.addr)
        self.sample_steps()
        
    def test_414x896_window(self):
        self.chrome_options.add_argument('window-size=414,896')
        self.browser = webdriver.Chrome(service = self.ser, options = self.chrome_options)
        self.browser.get(self.addr)
        self.sample_steps()
        
    def test_1536x864_window(self):
        self.chrome_options.add_argument('window-size=1366,768')
        self.browser = webdriver.Chrome(service = self.ser, options = self.chrome_options)
        self.browser.get(self.addr)
        self.sample_steps()
        
    def test_375x667_window(self):
        self.chrome_options.add_argument('window-size=1366,768')
        self.browser = webdriver.Chrome(service = self.ser, options = self.chrome_options)
        self.browser.get(self.addr)
        self.sample_steps()
    
    def tearDown(self):
        self.browser.quit()
    
if __name__ == "__main__":
        unittest.main()