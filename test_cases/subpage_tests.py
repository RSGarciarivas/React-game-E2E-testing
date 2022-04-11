import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
import time
from poms.HomePage import HomePageNotSignedIn, HomePageSignedIn
from poms.HallOfFamePage import HallOfFamePageNotSignedIn, HallOfFamePageSignedIn
from poms.SignInPage import LoginPage
from poms.DashboardPage import DashboardPage
from poms.PlayersPage import PlayersPageNotSignedIn, PlayersPageSignedIn
from poms.EditProfilePage import EditProfilePage

class SubpageTests(unittest.TestCase):
    
    def setUp(self):
        service = r'C:\Users\Rafael\Documents\Projects\Universe Gods\react_game_app_e2e\chromedriver.exe'
        ser = Service(service)
        self.browser = webdriver.Chrome(service = ser)
        self.addr = 'http://18.209.14.86'
        
    def test_home_page(self):
        '''
        Check "get started" button takes user to sign-in page and "My Hero"
        button takes user to dashboard
        '''
        self.browser.get(self.addr)
        page = HomePageNotSignedIn(self.browser)
        page.click_get_started()
        page = LoginPage(self.browser)
        self.assertIn('sign-in', self.browser.current_url)
        page.log_in('rsg2703', 'password')
        page = DashboardPage(self.browser)
        page.click_home()
        page = HomePageSignedIn(self.browser)
        page.click_my_hero()
        page = DashboardPage(self.browser)
        self.assertIn('dashboard', self.browser.current_url)
    
    def test_hall_of_fame_page(self):
        '''
        Check hall of fame shows the top ten players in order. Sign-in
        and check again
        '''
        self.browser.get(self.addr)
        self.browser.implicitly_wait(1)
        page = HomePageNotSignedIn(self.browser)
        page.click_hall_of_fame()
        self.browser.implicitly_wait(1)
        page = HallOfFamePageNotSignedIn(self.browser)
        self.assertTrue(page.check_top_players())
        
        page.click_signIn()
        page = LoginPage(self.browser)
        page.log_in('rsg2703', 'password')
        page = DashboardPage(self.browser)
        page.click_hall_of_fame()
        page = HallOfFamePageSignedIn(self.browser)
        self.assertTrue(page.check_top_players())
        
    def test_players_page(self):
        '''
        Check overall performance of the search engine, attempt to find a
        non-existent user, filter players by status, search for a
        particular player and scroll through several pages of the results
        '''
        self.browser.get(self.addr)
        self.browser.implicitly_wait(1)
        page = HomePageNotSignedIn(self.browser)
        page.click_players()
        self.browser.implicitly_wait(5)
        page = PlayersPageNotSignedIn(self.browser)
        page.look_up_player('esto es una prueba')
        page = PlayersPageNotSignedIn(self.browser)
        self.assertEqual(page.num_players_shown(), 0)
        
        page = PlayersPageNotSignedIn(self.browser)
        page.select_status('plata')
        page = PlayersPageNotSignedIn(self.browser)
        page.click_submit()        
        page = PlayersPageNotSignedIn(self.browser)
        for player in page.table_data:
            status = player['Status']
            self.assertEqual(status, 'Silver')
        
        page.click_signIn()
        page = LoginPage(self.browser)
        page.log_in('rsg2703', 'password')
        page = DashboardPage(self.browser)
        page.click_players()
        page = PlayersPageSignedIn(self.browser)
        page.look_up_player('Dolf0')
        self.browser.implicitly_wait(5)
        page = PlayersPageSignedIn(self.browser)
        self.assertEqual(page.num_players_shown(), 1)
        
        page.click_reset()
        for _ in range(10):
            page = PlayersPageSignedIn(self.browser)
            page.click_random_num()
        self.assertEqual(page.num_players_shown(), 100)
    
    def test_dashboard_page(self):
        '''
        Check edit player page is reachable through dashboard
        '''
        self.browser.get(self.addr)
        self.browser.implicitly_wait(1)
        page = HomePageNotSignedIn(self.browser)
        page.click_signIn()
        self.browser.implicitly_wait(1)
        page = LoginPage(self.browser)
        page.log_in('rsg2703', 'password')
        page = DashboardPage(self.browser)
        page.click_update_user()
        page = EditProfilePage(self.browser)
        self.assertIn('update-user', self.browser.current_url)
        
    def test_edit_profile_page(self):
        '''
        Attempt to change user's name and check new name in dashboard page
        '''
        self.browser.get(self.addr)
        self.browser.implicitly_wait(1)
        page = HomePageNotSignedIn(self.browser)
        page.click_signIn()
        self.browser.implicitly_wait(1)
        page = LoginPage(self.browser)
        page.log_in('rsg2703', 'password')
        page = DashboardPage(self.browser)
        page.click_update_user()
        page = EditProfilePage(self.browser)
        new_name = str(time.time())
        page.update_user(new_name, 'rsg2703', 1)
        self.browser.implicitly_wait(5)
        page = EditProfilePage(self.browser)
        page.click_profile()
        page = DashboardPage(self.browser)
        self.assertEqual(page.name, new_name)
        
    def tearDown(self):
        self.browser.quit()
    
if __name__ == "__main__":
        unittest.main()
        