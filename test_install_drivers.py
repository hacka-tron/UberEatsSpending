from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

USER_DATE_DIR = 'C:/Code/UberEatsSpending/User Data' # EDIT THIS
PROFILE_DIR =  'Default' # MAYBE EDIT THIS

def get_chrome_driver():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument(f'--user-data-dir={USER_DATE_DIR}')
    options.add_argument(f'profile-directory={PROFILE_DIR}')
    options.add_argument("--remote-debugging-port=9222")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return webdriver.Chrome(service=service,options=options)