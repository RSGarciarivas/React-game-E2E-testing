import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
import json
import numpy as np
from poms.HomePage import HomePageNotSignedIn
from poms.SignInPage import LoginPage
from poms.DashboardPage import DashboardPage

class SignInTests(unittest.TestCase):
    
    def setUp(self):
        service = r'C:\Users\Rafael\Documents\Projects\Universe Gods\react_game_app_e2e\chromedriver.exe'
        ser = Service(service)
        self.browser = webdriver.Chrome(service = ser)
        self.addr = 'http://18.209.14.86'
        
    def test_sign_in_no_username(self):
        '''
        Attempt to sign-in without username
        '''
        self.browser.get(self.addr)
        page = HomePageNotSignedIn(self.browser)
        page.click_signIn()
        self.browser.implicitly_wait(1)
        page = LoginPage(self.browser)
        page.log_in('', 'password')
        self.assertIn('sign-in', self.browser.current_url)
        
    def test_sign_in_no_password(self):
        '''
        Attempt to sign-in without password
        '''
        self.browser.get(self.addr)
        page = HomePageNotSignedIn(self.browser)
        page.click_signIn()
        self.browser.implicitly_wait(1)
        page = LoginPage(self.browser)
        page.log_in('rsg2703', '')
        self.assertIn('sign-in', self.browser.current_url)    
    
    def test_sign_in_no_data(self):
        '''
        Attempt to sign-in without username nor password
        '''
        self.browser.get(self.addr)
        page = HomePageNotSignedIn(self.browser)
        page.click_signIn()
        self.browser.implicitly_wait(1)
        page = LoginPage(self.browser)
        page.log_in('', '')
        self.assertIn('sign-in', self.browser.current_url)
    
    def test_correct_sign_in(self):
        '''
        Pick 20 random users and log in with each
        '''
        data_path = r'C:\Users\Rafael\Documents\Projects\Universe Gods\react_game_app_e2e'
        user_data1 = json.load(open(os.path.join(data_path, 'MOCK_DATA.json')))
        user_data2 = json.load(open(os.path.join(data_path, 'MOCK_DATA-2.json')))
        user_data3 = json.load(open(os.path.join(data_path, 'MOCK_DATA-3.json')))
        user_data = user_data1 + user_data2 + user_data3
        random_picks = np.random.randint(0, len(user_data), size = 20)
        users = [user_data[n] for n in random_picks]
        for user in users:
            username = user['nickname']
            password = user['password']
            
            self.browser.get(self.addr)
            page = HomePageNotSignedIn(self.browser)
            page.click_signIn()
            self.browser.implicitly_wait(1)
            page = LoginPage(self.browser)
            page.log_in(username, password)
            page = DashboardPage(self.browser)
            self.assertIsInstance(page, DashboardPage)
    
    def tearDown(self):
        self.browser.quit()
        
if __name__ == "__main__":
        unittest.main()