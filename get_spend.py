from test_install_drivers import get_chrome_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm

def get_receipt_info(driver, receipt_button):
    receipt_button.click()
    try:
        WebDriverWait(driver, 4).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe")))
    except:
        print('Receipt not loaded!')
        driver.find_element(By.CSS_SELECTOR, '[aria-label="Close"]').click()
        return (0, None)
    
    # Get receipt data
    receipt_text = driver.find_element(By.XPATH, "//table").text.split('\n')
    cost = float(receipt_text[0].strip().split(' ')[-1][1:])
    date_text = receipt_text[1]
    date_object = datetime.strptime(date_text, '%B %d, %Y')
    
    # Close receipt
    driver.switch_to.default_content()
    driver.find_element(By.CSS_SELECTOR, '[aria-label="Close"]').click()
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, "//iframe")))
    return (cost, date_object)
    

def do_navigation(days):
    driver= get_chrome_driver()
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.ubereats.com/orders")
    
    # Navigate to orders screen. 
    time.sleep(5)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'[id="main-content"]')))
    x_days_ago = datetime.now() - timedelta(days=days)
    
    print("\nLoading more orders until maximum date reached.")
    while True:
        print("Checking if current set of orders are within the date rangee...")
        wait.until(lambda spend_len: len(driver.find_elements(By.XPATH, "//a[text()='View receipt']")) != spend_len)
        spend_list = driver.find_elements(By.XPATH, "//a[text()='View receipt']")
        cost, date = get_receipt_info(driver, spend_list[len(spend_list)-1])
        if date !=None and date < x_days_ago:
            print(f'Reached {days} days of orders.')
            break
        
        try:
            show_more_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Show more']")))
        except:
            print(f'\nLoaded {days} days of orders!\n')
            break
        show_more_button.click()
    
    # Return to top of page
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
    time.sleep(3)
    
    # Get order totals
    print("\nGetting total sum of orders.")
    total = 0
    i = 0
    bar = tqdm(spend_list)    
    for receipt in bar:
        cost, date = get_receipt_info(driver, receipt)
        if date !=None and date < x_days_ago:
            bar.set_description('Finished!')
            bar.update(len(spend_list)-i)
            bar.close()
            break
        total += cost
        i += 1
        bar.set_description(f'Current Sum: ${total} -- Order Date: {date.date()}')
        
    print(f'\nFinal Sum: ${total}')
    driver.quit()

while True:    
    days = input("Number of days orders to get total for: ")
    if days.isdigit():
        break
    print("Only enter whole numbers!")
    
    
do_navigation(int(days))