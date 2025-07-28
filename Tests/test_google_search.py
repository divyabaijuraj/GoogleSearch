import time
import pytest
from Pages.google_page import GooglePage

def test_google_search(driver):
   search_text="python"
   google = GooglePage(driver)
   time.sleep(2)
   google.load()
   time.sleep(2)
   print(search_text)
   google.search(search_text)

   time.sleep(3)
   assert search_text.lower() in  driver.page_source.lower()