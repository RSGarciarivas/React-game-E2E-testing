import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from poms.HomePage import HomePageNotSignedIn
from poms.SignInPage import LoginPage, RegisterPage
from poms.DashboardPage import DashboardPage
import time
import os
import numpy as np
import json

class RegisterUserTests(unittest.TestCase):
    
    def setUp(self):
        service = r'C:\Users\Rafael\Documents\Projects\Universe Gods\react_game_app_e2e\chromedriver.exe'
        ser = Service(service)
        self.browser = webdriver.Chrome(service = ser)
        addr = 'http://18.209.14.86'
        self.browser.get(addr)
        
    def test_register_new_user(self):
        '''
        Attempt to register new user (correctly)
        '''
        page = HomePageNotSignedIn(self.browser)
        page.click_signIn()
        self.browser.implicitly_wait(1)
        page = RegisterPage(self.browser)
        unique_user = str(time.time())
        page.register_user('Test', unique_user, 'password')
        page = DashboardPage(self.browser)
        self.assertIsInstance(page, DashboardPage)
        
    def test_register_user_different_passwords(self):
        '''
        Attempt to register without passwords matching
        '''
        page = HomePageNotSignedIn(self.browser)
        page.click_signIn()
        self.browser.implicitly_wait(1)
        page = RegisterPage(self.browser)
        unique_user = str(time.time())
        page.register_user_diff_passwords('Test', unique_user, 'password')
        self.assertIn('sign-in', self.browser.current_url)
        
    def test_no_repeatable_users(self):
        '''
        Attempt to register with an already-existing username
        '''
        data_path = r'C:\Users\Rafael\Documents\Projects\Universe Gods\react_game_app_e2e'
        user_data1 = json.load(open(os.path.join(data_path, 'MOCK_DATA.json')))
        user_data2 = json.load(open(os.path.join(data_path, 'MOCK_DATA-2.json')))
        user_data3 = json.load(open(os.path.join(data_path, 'MOCK_DATA-3.json')))
        user_data = user_data1 + user_data2 + user_data3
        page = HomePageNotSignedIn(self.browser)
        page.click_signIn()
        self.browser.implicitly_wait(1)
        page = RegisterPage(self.browser)
        random_pick = np.random.randint(0, len(user_data))
        nickname = user_data[random_pick]['nickname']
        page.register_user('Test', nickname, 'password')
        self.assertIn('sign-in', self.browser.current_url)
        
    def tearDown(self):
        self.browser.quit()
        
if __name__ == "__main__":
        unittest.main()