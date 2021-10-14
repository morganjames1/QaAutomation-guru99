from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
def test_newcustomer():
    driver.get('http://demo.guru99.com/V4/index.php')
    driver.maximize_window()
    time.sleep(1)
    driver.find_element_by_name('uid').send_keys('mngr355808')
    time.sleep(1)
    driver.find_element_by_name('password').send_keys('AvYzypU!11' + Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_link_text('New Customer').click()
    time.sleep(1)
    driver.find_element_by_name('name').send_keys('Morgan James')
    # time.sleep(1)
    # driver.find_element_by_name('radl').click()
    time.sleep(1)
    driver.find_element_by_name('dob').send_keys('23-09-2021')
    time.sleep(1)
    driver.find_element_by_name('addr').send_keys('Indonesia')
    time.sleep(1)
    driver.find_element_by_name('city').send_keys('Indonesia')
    time.sleep(1)
    driver.find_element_by_name('state').send_keys('Indonesia')
    time.sleep(1)
    driver.find_element_by_name('pinno').send_keys('999999')
    time.sleep(1)
    driver.find_element_by_name('telephoneno').send_keys('999999')
    time.sleep(1)
    driver.find_element_by_name('emailid').send_keys('12340oq@mail.com')
    time.sleep(1)
    driver.find_element_by_name('password').send_keys('999999')
    time.sleep(1)
    driver.find_element_by_name('sub').click()

    time.sleep(1)
    # Title = driver.title
    # assert Title == 'Guru99 Bank Customer Registration Page'

    assert 'Customer Registered Successfully!!!' in driver.find_element_by_xpath('//*[@id="customer"]/tbody/tr[1]/td/p').text
    
    time.sleep(2)
    driver.save_screenshot('I:\TESTING\Python Automation\Manager\Image\coba1.png')
    time.sleep(2)
    driver.close()





