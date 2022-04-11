from selenium.webdriver.common.by import By
from poms.Page import PageNotSignedIn, PageSignedIn

class AboutPage():
    
    def __init__(self, browser):
        pass
    
class AboutPageNotSignedIn(PageNotSignedIn, AboutPage):
    
    def __init__(self, browser):
        PageNotSignedIn.__init__(self, browser)
        AboutPage.__init__(self, browser)
    
class AboutPageSignedIn(PageSignedIn, AboutPage):
    
    def __init__(self, browser):
        PageSignedIn.__init__(self, browser)
        AboutPage.__init__(self, browser)
