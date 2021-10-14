from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
def test_newaccount():
    driver.get('http://demo.guru99.com/V4/index.php')
    driver.maximize_window()
    time.sleep(1)
    driver.find_element_by_name('uid').send_keys('mngr355808')
    time.sleep(1)
    driver.find_element_by_name('password').send_keys('AvYzypU!11' + Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_link_text('New Account').click()
    time.sleep(1)
    driver.find_element_by_name('cusid').send_keys('71690')
    time.sleep(1)
    driver.find_element_by_name('selaccount').click()
    time.sleep(1)
    driver.find_element_by_name('inideposit').send_keys('1000')
    time.sleep(1)
    driver.find_element_by_name('button2').click()
    time.sleep(1)

    Title = driver.title

    assert Title == 'Gtpl Bank Customer Registration Page'

    # time.sleep(1)
    # driver.close()





