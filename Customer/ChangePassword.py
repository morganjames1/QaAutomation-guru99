from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
def test_changepassword():
    driver.get('http://demo.guru99.com/V4/index.php')
    driver.maximize_window()
    time.sleep(1)
    driver.find_element_by_name('uid').send_keys('71690')
    time.sleep(1)
    driver.find_element_by_name('password').send_keys('999999' + Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_link_text('Changepassword').click()
    time.sleep(1)
    driver.find_element_by_name('oldpassword').send_keys('999999')
    time.sleep(1)
    driver.find_element_by_name('newpassword').send_keys('999999!11')
    time.sleep(1)
    driver.find_element_by_name('confirmpassword').send_keys('999999!11')
    time.sleep(1)
    driver.find_element_by_name('sub').click()
    time.sleep(1)

    Title = driver.title
    assert Title == 'Guru99 Bank Customer HomePage'

    time.sleep(3)
    driver.close()