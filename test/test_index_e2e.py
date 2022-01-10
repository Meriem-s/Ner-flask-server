import unittest
from selenium import webdriver



class E2ETest(unittest.TestCase):
    
    
    def setUp(self):
        #create an instance of chrome browser and once done, we want to close this instance to avoid any 
        
        self.driver = webdriver.Chrome(executable_path=r'../chromedriver/chromedriver')
        self.driver.get('http://localhost:5010')
         
    def destroy(self):
        self.driver.quit()
        
    def test_browser_contains_app_name(self):
        self.assertIn('Named Entity',self.driver.title)
        
        
   