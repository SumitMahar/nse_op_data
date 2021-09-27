import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = r"C:\Users\Microsoft\Desktop\Error\nse_op\cdriver\chromedriver.exe"
options = Options()
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ 39.0.2171.95 Safari/537.36"
options.add_argument(f"user-agent={user_agent}")
#options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


driver = webdriver.Chrome(executable_path=path, options=options)
driver.get(r"https://www.nseindia.com/option-chain")
time.sleep(.4)
driver.delete_all_cookies()
time.sleep(1)
driver.refresh()
driver.quit()

for _ in range(3):
    print(_)
    chrome_prefs = {"download.default_directory": r"C:\Users\Microsoft\Desktop\Error\nse_op\Op_CSVs"} # (windows)
    options.experimental_options["prefs"] = chrome_prefs
    time.sleep(.4)
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.get(r"https://www.nseindia.com/option-chain")
    time.sleep(.4)
    # nifty_spot = driver.find_element_by_id("equity_underlyingVal")
    try:
        d_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "downloadOCTable"))
            )
        time.sleep(10)
        d_button.click()

        #d_button = driver.find_element_by_id("downloadOCTable")
        nifty_spot = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "equity_underlyingVal"))
        )
        if nifty_spot.text:
            print("file downloaded...")
            print(nifty_spot.text)
        else:
            print('Server denied your request')
        
    
    finally:
        time.sleep(10)
        print("Closing the current browser window")
        driver.quit()
        
        

