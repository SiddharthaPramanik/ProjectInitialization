from selenium import webdriver
from selenium.webdriver.common.keys import Keys

username = 'rks.siddhartha@gmail.com'
password = '#Writer248625'

driver = webdriver.Firefox(executable_path='./geckodriver')
driver.get('https://github.com/login')
login_field = driver.find_element_by_id('login_field')
login_field.clear()
login_field.send_keys(username)
pass_field = driver.find_element_by_id('password')
pass_field.clear()
pass_field.send_keys(password)
submit = driver.find_element_by_name('commit')
submit.click()
# driver.quit()
