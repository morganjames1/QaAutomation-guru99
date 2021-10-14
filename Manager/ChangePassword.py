from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
def test_changepassword():
    driver.get('http://demo.guru99.com/V4/index.php')
    driver.maximize_window()
    time.sleep(1)
    driver.find_element_by_name('uid').send_keys('mngr355808')
    time.sleep(1)
    driver.find_element_by_name('password').send_keys('AvYzypU!1' + Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_link_text('Change Password').click()
    time.sleep(1)
    driver.find_element_by_name('oldpassword').send_keys('AvYzypU!1')
    time.sleep(1)
    driver.find_element_by_name('newpassword').send_keys('AvYzypU!11')
    time.sleep(1)
    driver.find_element_by_name('confirmpassword').send_keys('AvYzypU!11')
    time.sleep(1)
    driver.find_element_by_name('sub').click()
    time.sleep(1)
    driver.find_element_by_name('uid').send_keys('mngr355808')
    time.sleep(1)
    driver.find_element_by_name('password').send_keys('AvYzypU!11' + Keys.ENTER)
    time.sleep(1)

    Title = driver.title
    assert Title == 'Guru99 Bank Manager HomePage'

    time.sleep(3)
    driver.close()