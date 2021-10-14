from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import time

driver = webdriver.Chrome()

def test_google():
    driver.maximize_window()
    driver.get('http://demo.guru99.com/V4/index.php')
    time.sleep(1)
    driver.find_element_by_name('uid').send_keys('mngr355808')
    time.sleep(1)
    driver.find_element_by_name('password').send_keys('AvYzypU!11')
    driver.find_element_by_name('btnLogin').click()

    # assert 'Guru99 Bank Manager HomePage' in driver.find_element_by_css_selector ('heading3').text()

    Title = driver.title
    assert Title == 'Guru99 Bank Manager HomePage'

    

