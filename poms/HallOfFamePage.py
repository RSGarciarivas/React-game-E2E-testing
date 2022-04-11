from selenium.webdriver.common.by import By
from poms.Page import PageNotSignedIn, PageSignedIn

class HallOfFamePage():
    
    def __init__(self, browser):
        rows = self.browser.find_elements(By.XPATH, '/html/body/div/main/div/div/div/table/tbody/*')
        self.top_ten = []
        for row in rows:
            row = row.text.split()
            self.top_ten.append({'Nickname': row[0], 'Name': row[1],
                                    'Ranking': row[2], 'Status': row[3],
                                    'Player ID': row[4]})
    
    def check_top_players(self):
        '''
        Make sure rankings of the players shown are 1, 2, ..., 10
        '''
        for i, player in enumerate(self.top_ten):
            if int(player['Ranking']) != (i + 1):
                return False
        return True
        
class HallOfFamePageNotSignedIn(PageNotSignedIn, HallOfFamePage):
    
    def __init__(self, browser):
        PageNotSignedIn.__init__(self, browser)
        HallOfFamePage.__init__(self, browser)

class HallOfFamePageSignedIn(PageSignedIn, HallOfFamePage):
    
    def __init__(self, browser):
        PageSignedIn.__init__(self, browser)
        HallOfFamePage.__init__(self, browser)
