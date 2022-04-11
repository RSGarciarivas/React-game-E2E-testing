from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import numpy as np
from poms.Page import PageNotSignedIn, PageSignedIn

class PlayersPage():
    
    def __init__(self, browser):
        self.reset_search_btn = self.browser.find_element(By.XPATH, '/html/body/div/main/div/div/div[4]/button')
        self.status_select = Select(self.browser.find_element(By.ID, 'status-select'))
        self.nickname_box = self.browser.find_element(By.ID, 'nickname-input')
        self.submit_btn = self.browser.find_element(By.ID, 'submit-query-btn')
        # self.nav_buttons = self.browser.find_elements(By.XPATH,'/html/body/div/main/div/div/div[5]/*')
        self.nav_buttons = self.browser.find_elements(By.XPATH, '//*[@id="pagination-btns"]/*')
        # findElements(By. xpath("//[@id='Container']//*")
        
        self.prev_btn = self.nav_buttons[0]
        self.nav_buttons.pop(0)
        self.next_btn = self.nav_buttons[-1]
        self.nav_buttons.pop(-1)
        if len(self.nav_buttons) > 5:
            for btn in self.nav_buttons:
                if btn.text == '...':
                    self.nav_buttons.remove(btn)
        
        rows = self.browser.find_elements(By.XPATH, '//*[@id="root"]/main/div/div/div[3]/table/tbody/*')
        self.table_data = []
        for row in rows:
            row = row.text.split()
            self.table_data.append({'Nickname': row[0], 'Name': row[1],
                                    'Ranking': row[2], 'Status': row[3],
                                    'Player ID': row[4]})
        
    def click_reset(self):
        self.reset_search_btn.click()
        
    def select_status(self, status):
        '''
        All, oro, plata, bronce
        '''
        self.status_select.select_by_value(status)
        
    def type_nickname(self, nickname):
        self.nickname_box.clear()
        self.nickname_box.send_keys(nickname)
        
    def click_submit(self):
        self.submit_btn.click()
        
    def click_prev(self):
        self.prev_btn.click()
        
    def click_num_btn(self, slot):
        self.nav_buttons[slot - 1].click()
    
    def click_next(self):
        self.next_btn.click()
        
    def click_random_num(self):
        num = np.random.randint(0, len(self.nav_buttons))
        self.click_num_btn(num)
    
    def look_up_player(self, username):
        self.type_nickname(username)
        self.click_submit()
    
    def num_players_shown(self):
        return len(self.table_data)
    
class PlayersPageNotSignedIn(PageNotSignedIn, PlayersPage):
    
    def __init__(self, browser):
        PageNotSignedIn.__init__(self, browser)
        PlayersPage.__init__(self, browser)

class PlayersPageSignedIn(PageSignedIn, PlayersPage):
    
    def __init__(self, browser):
        PageSignedIn.__init__(self, browser)
        PlayersPage.__init__(self, browser)
