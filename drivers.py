from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def get_chrome_driver(user_data_path, profile_dir):
    service = ChromeService(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument(f'--user-data-dir={user_data_path}')
    options.add_argument(f'profile-directory={profile_dir}')
    options.add_argument("--remote-debugging-port=9222")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return webdriver.Chrome(service=service,options=options)