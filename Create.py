import sys
import os
from selenium import webdriver

class ProjectInitialize:
    
    def __init__(self, app_path, username, password):
        
        self.driver = webdriver.Firefox(executable_path='./geckodriver')
        self.username = username
        self.password = password
        self.app_path = app_path

    def fill_text_field(self, id, keys):
        
        # Finding page elments by ID
        text_field = self.driver.find_element_by_id(id)
        text_field.clear()
        text_field.send_keys(keys)

    def github(self):

        # Login Automation
        self.driver.get('https://github.com/login')
        self.fill_text_field('login_field', self.username)
        self.fill_text_field('password', self.password)
        button = self.driver.find_element_by_name('commit')
        button.click()

        # Create new repository
        self.driver.get('https://github.com/new')
        self.fill_text_field('repository_name', sys.argv[1])
        if len(sys.argv) == 3:
            self.fill_text_field('repository_description', sys.argv[2])
        button = self.driver.find_element_by_class_name('first-in-line')
        button.submit()
        self.driver.quit()

    def create(self):

        # Create remote repository on Github
        self.github()

        # Directory creation and git initialization on local machine
        os.chdir(self.app_path)
        os.mkdir(sys.argv[1])
        os.chdir(sys.argv[1])
        os.system('git init')
        os.system(f'git remote add origin git@github.com:<Github Username>/{sys.argv[1]}.git')
        os.system('touch README.md')
        os.system('touch .gitignore')

if __name__ == '__main__':
    
    # Github Username & Password
    username = '' 
    password = ''

    # Path where you want your local project directory
    app_path= ''

    # Create object for ProjectInitialize class
    initializer = ProjectInitialize(app_path, username, password)
    initializer.create()