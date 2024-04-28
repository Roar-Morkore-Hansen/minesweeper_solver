import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)

def cookieNotConsent():
    notConsentButton = driver.find_element(By.CLASS_NAME, "fc-cta-do-not-consent")
    notConsentButton.click()

def openMineSweeper():
    driver.get("https://minesweeperonline.com/#beginner")
    cookieNotConsent()

def createMatrix(x:int, y:int):
    matrix = list()
    for j in range(y):
        matrix.append(list())
        for i in range(x):
            matrix[j].append(0)
    print(matrix)
    return matrix

# SOLVER

def OOBfilter(coordinate):
    x = coordinate[0]
    y = coordinate[1]
    OOB_x = (x < 1 or x > size_x)
    OOB_y = (y < 1 or y > size_y)
    if (OOB_x or OOB_y) == True:
        return False
    else:
        return True

def getCandidates(x:int, y:int):
    candidateList = [(x, y - 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1), (x, y + 1),
                     (x - 1, y + 1), (x - 1, y), (x - 1, y - 1)]
    return list(filter(OOBfilter, candidateList))

def checkBoarder(x:int, y:int):
    print(getCandidates(x, y))

def solve(x:int, y:int):
    global size_x
    global size_y
    size_x = x
    size_y = y
    # driver.find_element(By.ID, math.ceil(x/2), math.ceil(y/2)).click()

# openMineSweeper()
# solve(9, 9)
# createMatrix(9,9)

size_x = 9
size_y = 9

checkBoarder(9,9)
