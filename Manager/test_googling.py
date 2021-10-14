from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_googlingg():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    driver.find_element_by_name('q').send_keys('Ronaldus Morgan James' + Keys.ENTER)
    assert 'Ronaldus Morgan James' in driver.find_element_by_css_selector('h3').text
    assert 'Ronaldus Morgan James' in driver.title
    driver.quit()

