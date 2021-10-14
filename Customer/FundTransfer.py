from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
def test_fundtransfer():
    driver.get('http://demo.guru99.com/V4/index.php')
    driver.maximize_window()
    time.sleep(1)
    driver.find_element_by_name('uid').send_keys('71690')
    time.sleep(1)
    driver.find_element_by_name('password').send_keys('999999!11' + Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_link_text('Fund Transfer').click()
    time.sleep(1)
    # driver.find_element_by_name('payersaccount').send_keys('98429')
    driver.find_element_by_name('payersaccount').send_keys('98431')
    time.sleep(1)
    driver.find_element_by_name('payeeaccount').send_keys('98431')
    time.sleep(1)
    driver.find_element_by_name('ammount').send_keys('150')
    time.sleep(1)
    driver.find_element_by_name('desc').send_keys('FundTransfer')
    time.sleep(1)
    driver.find_element_by_name('AccSubmit').click()
    time.sleep(1)

    # driver.refresh()
    
    Title = driver.title
    assert Title == 'Guru99 Bank Fund Page'


    time.sleep(3)
    driver.close()