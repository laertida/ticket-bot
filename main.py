from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

login_button_class = 'sc-10c8igm-1 blwTMT'

driver = webdriver.Firefox()
driver.get("https://www.ticketmaster.com.mx/")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

