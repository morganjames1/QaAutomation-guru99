from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

def test_balance():
    driver.maximize_window()
    driver.get('http://demo.guru99.com/V4/index.php')
    time.sleep(1)
    driver.find_element_by_name('uid').send_keys('71690')
    time.sleep(1)
    driver.find_element_by_name('password').send_keys('999999!11' + Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_link_text('Balance Enquiry').click()
    time.sleep(1)
    driver.find_element_by_name('accountno').send_keys('98400')
    time.sleep(1)
    driver.find_element_by_name('AccSubmit').click()
    time.sleep(1)

    driver.refresh()
    
    Title = driver.title
    assert Title == 'Guru99 Bank Balance Enquiry Page'

    time.sleep(1)
    driver.close()




