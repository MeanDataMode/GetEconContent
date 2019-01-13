import json
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def wait():
    # will randomly pick an amount to time to time.sleep
    seconds = random.choice(range(1,5))
    ms1 = random.choice(range(1,10))
    ms2 = random.choice(range(1,10))
    ms3 = random.choice(range(1,10))
    ms4 = random.choice(range(1,10))
    wait = ("{}.{}{}{}{}".format(seconds, ms1, ms2, ms3, ms4))
    return(float(wait))

# The line 17 through 33 was not developed by me. It is used to print to PDF the webpage.
#   Source of Code: ('https://stackoverflow.com/questions/31136581/ +
#                     automate-print-save-web-page-as-pdf-in-chrome-python-2-7')
appState = {
    "recentDestinations": [
        {
            "id": "Save as PDF",
            "origin": "local"
        }
    ],
    "selectedDestinationId": "Save as PDF",
    "version": 2
}
profile = {'printing.print_preview_sticky_settings.appState': json.dumps(appState)}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('prefs', profile)
chrome_options.add_argument('--kiosk-printing')

# Start webdriver
driver = webdriver.Chrome(executable_path=r"chromedriver_win32\chromedriver.exe", options=chrome_options)

# Go to Website
url = ('')  # the URL here
driver.get(url)

# get rid of left navigation menu
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/a[1]').click()

# Set Font Size
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/div[2]/a').click()
time.sleep(wait())

driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/button[1]').click()
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/button[1]').click()
time.sleep(wait())

# Loop Over all Pages and print each page as a PDF
count = 0
while True:
    start_page = driver.current_url
        
    # Select Window to Print
    # driver.find_element_by_xpath('//*[@id="section-"]').click()
    # time.sleep(wait())
    
    # Print Page
    driver.execute_script('window.print();')
    
    # Navigate to next page (the first page has a different layout compaired to all of the others
    if count < 1:
        # Find the 'Next Page' button and click it
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/a').click()
        time.sleep(wait())
        new_page = driver.current_url
        count += 1
    else:
        # Find the 'Next Page' button and click it
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/a[2]').click()
        time.sleep(wait())
        new_page = driver.current_url
        count += 1
    if new_page == start_page:
        break
