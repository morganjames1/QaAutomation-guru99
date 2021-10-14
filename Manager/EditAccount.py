from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
def test_editaccount():
    driver.get('http://demo.guru99.com/V4/index.php')
    driver.maximize_window()
    time.sleep(1)
    driver.find_element_by_name('uid').send_keys('mngr355808')
    time.sleep(1)
    driver.find_element_by_name('password').send_keys('AvYzypU!11' + Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_link_text('Edit Account').click()
    time.sleep(1)
    driver.find_element_by_name('accountno').send_keys('98433')
    time.sleep(1)
    driver.find_element_by_name('AccSubmit').click()
    time.sleep(1)

    Title = driver.title

    assert Title == 'Guru99 Bank Edit Account Entry Page'

    time.sleep(1)
    driver.close()