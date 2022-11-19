from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()

chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

assert "Selenium Easy Demo" in chrome_browser.title

message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
print(message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element(By.ID, "user-message")
user_message.clear()
user_message.send_keys("This actually works!")
time.sleep(4)
message_button.click()
