import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from poms.HomePage import HomePageNotSignedIn, HomePageSignedIn
from poms.HallOfFamePage import HallOfFamePageNotSignedIn
from poms.AboutPage import AboutPageNotSignedIn
from poms.PlayersPage import PlayersPageNotSignedIn
from poms.SignInPage import LoginPage, RegisterPage
from poms.DashboardPage import DashboardPage

class NavBarTests(unittest.TestCase):
    
    def setUp(self):
        service = r'C:\Users\Rafael\Documents\Projects\Universe Gods\react_game_app_e2e\chromedriver.exe'
        ser = Service(service)
        self.browser = webdriver.Chrome(service = ser)
        self.addr = 'http://18.209.14.86'
        
    def test_univ_gods_logo_link(self):
        '''
        Universe Gods logo takes user to homepage
        '''
        self.browser.get(self.addr)
        self.browser.implicitly_wait(1)
        page = HomePageNotSignedIn(self.browser)
        page.click_signIn()
        page = LoginPage(self.browser)
        self.browser.implicitly_wait(1)
        page = LoginPage(self.browser)
        page.click_univ_gods()
        page = HomePageNotSignedIn(self.browser)
        self.assertIsInstance(page, HomePageNotSignedIn)
    
    def test_globe_icon_link(self):
        '''
        Globe icon takes user to homepage
        '''
        self.browser.get(self.addr)
        self.browser.implicitly_wait(1)
        page = HomePageNotSignedIn(self.browser)
        page.click_signIn()
        page = LoginPage(self.browser)
        self.browser.implicitly_wait(1)
        page = LoginPage(self.browser)
        page.click_globe()
        page = HomePageNotSignedIn(self.browser)
        self.assertIsInstance(page, HomePageNotSignedIn)
    
    def test_home_link(self):
        '''
        Home button works correctly
        '''
        self.browser.get(self.addr)
        self.browser.implicitly_wait(1)
        page = HomePageNotSignedIn(self.browser)
        page.click_signIn()
        page = LoginPage(self.browser)
        self.browser.implicitly_wait(1)
        page = LoginPage(self.browser)
        page.click_home()
        page = HomePageNotSignedIn(self.browser)
        self.assertIsInstance(page, HomePageNotSignedIn)
    
    def test_hall_of_fame_link(self):
        '''
        Hall of fame button works correctly
        '''
        self.browser.get(self.addr)
        self.browser.implicitly_wait(1)
        page = HomePageNotSignedIn(self.browser)
        page.click_hall_of_fame()
        page = HallOfFamePageNotSignedIn(self.browser)
        self.assertIsInstance(page, HallOfFamePageNotSignedIn)
    
    def test_about_link(self):
        '''
        About button works correctly
        '''
        self.browser.get(self.addr)
        self.browser.implicitly_wait(1)
        page = HomePageNotSignedIn(self.browser)
        page.click_about()
        page = AboutPageNotSignedIn(self.browser)
        self.assertIsInstance(page, AboutPageNotSignedIn)
    
    def test_players_link(self):
        '''
        Players link works correctly
        '''
        self.browser.get(self.addr)
        self.browser.implicitly_wait(1)
        page = HomePageNotSignedIn(self.browser)
        page.click_players()
        self.browser.implicitly_wait(5)
        page = PlayersPageNotSignedIn(self.browser)
        self.assertIsInstance(page, PlayersPageNotSignedIn)
    
    def test_sign_in_link(self):
        '''
        Sign-in button works correctly
        '''
        self.browser.get(self.addr)
        self.browser.implicitly_wait(1)
        page = HomePageNotSignedIn(self.browser)
        page.click_signIn()
        page = LoginPage(self.browser)
        self.assertIsInstance(page, LoginPage)
        
    def test_dashboard_link(self):
        '''
        My Hero button works correctly
        '''
        self.browser.get(self.addr)
        self.browser.implicitly_wait(1)
        page = HomePageNotSignedIn(self.browser)
        page.click_signIn()
        page = LoginPage(self.browser)
        page.log_in('rsg2703', 'password')
        page = DashboardPage(self.browser)
        page.click_home()
        page = HomePageSignedIn(self.browser)
        page.click_dashboard()
        page = DashboardPage(self.browser)
        self.assertIsInstance(page, DashboardPage)
        
    def test_logout_link(self):
        '''
        Logout button works correctly
        '''
        self.browser.get(self.addr)
        self.browser.implicitly_wait(1)
        page = HomePageNotSignedIn(self.browser)
        page.click_signIn()
        page = LoginPage(self.browser)
        page.log_in('rsg2703', 'password')
        page = DashboardPage(self.browser)
        page.click_logout()
        page = HomePageNotSignedIn(self.browser)
        self.assertIsInstance(page, HomePageNotSignedIn)
    
    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
        unittest.main()
        