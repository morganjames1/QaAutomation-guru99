from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.demoqa.com/elements')
driver.maximize_window()
time.sleep(2)

driver.save_screenshot('I:\TESTING\Python Automation\Manager\Image\coba.png')