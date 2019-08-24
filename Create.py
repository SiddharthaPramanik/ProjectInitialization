import sys
from selenium import webdriver

def create():
    username = ''
    password = ''

    driver = webdriver.Firefox(executable_path='./geckodriver')

    def fill_text_field(id, keys):
        text_field = driver.find_element_by_id(id)
        text_field.clear()
        text_field.send_keys(keys)

    # Login Automation
    driver.get('https://github.com/login')
    fill_text_field('login_field', username)
    fill_text_field('password', password)
    button = driver.find_element_by_name('commit')
    button.click()

    # Create new repository
    driver.get('https://github.com/new')
    fill_text_field('repository_name', sys.argv[1])
    if len(sys.argv) == 3:
        fill_text_field('repository_description', sys.argv[2])
    button = driver.find_element_by_class_name('first-in-line')
    button.submit()
    driver.quit()

if __name__ == '__main__':
    create()