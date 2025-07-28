###############Miniproject for selenium python with pytest
from selenium.webdriver.common.by import By

class GooglePage:

    def __init__(self,driver):
        self.driver=driver
        self.search_id =(By.ID,"APjFqb")

    def load(self):
        self.driver.get("https://www.google.com")

    def search(self, text):

        self.driver.find_element(*self.search_id).send_keys(text)

