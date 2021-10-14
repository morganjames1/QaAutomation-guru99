from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
def test_customised():
    driver.get('http://demo.guru99.com/V4/index.php')
    driver.maximize_window()
    time.sleep(1)
    driver.find_element_by_name('uid').send_keys('mngr355808')
    time.sleep(1)
    driver.find_element_by_name('password').send_keys('AvYzypU!11' + Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_link_text('Customised Statement').click()
    time.sleep(1)
    driver.find_element_by_name('accountno').send_keys('98433')
    time.sleep(1)
    driver.find_element_by_name('fdate').send_keys('23-09-2021')
    time.sleep(1)
    driver.find_element_by_name('tdate').send_keys('28-09-2021')
    time.sleep(1)
    driver.find_element_by_name('amountlowerlimit').send_keys('150')
    time.sleep(1)
    driver.find_element_by_name('numtransaction').send_keys('1')
    time.sleep(1)
    driver.find_element_by_name('AccSubmit').click()

    Title = driver.title
    assert Title == 'Guru99 Bank Customised Statement Page'

    time.sleep(3)
    driver.close()