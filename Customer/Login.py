from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

def test_Login():
    driver.maximize_window()
    driver.get('http://demo.guru99.com/V4/index.php')
    time.sleep(1)
    driver.find_element_by_name('uid').send_keys('71690')
    time.sleep(1)
    driver.find_element_by_name('password').send_keys('999999!11' + Keys.ENTER)
    time.sleep(1)

    Title = driver.title
    assert Title == 'Guru99 Bank Customer HomePage'

    time.sleep(1)
    driver.close()




