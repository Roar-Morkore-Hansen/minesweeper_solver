import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

def cookieNotConsent():
    notConsentButton = driver.find_element(By.CLASS_NAME, "fc-cta-do-not-consent")
    notConsentButton.click()

def openMineSweeper():
    driver.get("https://minesweeperonline.com/#beginner")
    cookieNotConsent()

# SOLVER
def solve(x:int, y:int):
    middle = (math.ceil(x/2), math.ceil(y/2))
    print(middle)

openMineSweeper()
solve(9, 9)
