from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

def test_Login():
    driver.maximize_window()
    driver.get('http://demo.guru99.com/V4/index.php')
    time.sleep(1)
    driver.find_element_by_name('uid').send_keys('mngr355808')
    time.sleep(1)
    driver.find_element_by_name('password').send_keys('AvYzypU!11' + Keys.ENTER)
    time.sleep(1)

    # Title = driver.title
    # assert Title == 'Guru99 Bank Manager HomePage'

    assert 'Manger Id : mngr355808' in driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[3]/td').text

    time.sleep(1)
    driver.close()




