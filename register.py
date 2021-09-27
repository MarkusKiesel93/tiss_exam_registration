from selenium import webdriver
from pathlib import Path
from yaml import safe_load

DRIVER = Path('./geckodriver').absolute()
CONFIG = Path('./config.yaml')
WAIT_TIME = 5

with open(CONFIG, 'r') as cfg:
    config = safe_load(cfg)

# open url and set waiting time
browser = webdriver.Firefox(executable_path=DRIVER)
browser.implicitly_wait(5)
browser.get(config['url'])

# login
browser.find_element_by_id('username').send_keys(config['user_name'])
browser.find_element_by_id('password').send_keys(config['user_pw'])
browser.find_element_by_id('samlloginbutton').click()

# wait until registration open
while True:
    try:
        # register
        exams = browser.find_elements_by_class_name('groupHeadertrigger')
        exam = exams[config['number']]
        exam.click()
        exam.click()

        browser.find_element_by_xpath("//input[@value='Register']").click()

        browser.find_element_by_xpath("//input[@value='Register']").click()
    except Exception:
        browser.refresh()
