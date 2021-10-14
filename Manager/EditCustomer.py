from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

def test_editcustomer():
    driver.get('http://demo.guru99.com/V4/index.php')
    driver.maximize_window()
    time.sleep(1)
    driver.find_element_by_name('uid').send_keys('mngr355808')
    time.sleep(1)
    driver.find_element_by_name('password').send_keys('AvYzypU!11' + Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_link_text('Edit Customer').click()
    time.sleep(1)
    driver.find_element_by_name('cusid').send_keys('71690')
    time.sleep(1)
    driver.find_element_by_name('AccSubmit').click()

    Title = driver.title
    assert Title == 'Guru99 Bank Edit Customer Entry Page'

    time.sleep(1)
    driver.close()