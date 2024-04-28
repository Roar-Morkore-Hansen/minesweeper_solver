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


class Coordinate:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
        self.id = f'{self.x}_{self.y}'

class AdjacentCells:
    def __init__(self, numBlanks:int, listBlanks:list[Coordinate], numFlagged:int):
        self.numBlanks = numBlanks
        self.listBlakns = listBlanks
        self.numFlagged = numFlagged
        

def createMatrix(x:int, y:int):
    matrix = list()
    for j in range(y):
        matrix.append(list())
        for i in range(x):
            matrix[j].append(0)
    print(matrix)
    return matrix

# SOLVER

def OOBfilter(coord) -> bool:
    OOB_x = (coord.x < 1 or coord.x > size_x)
    OOB_y = (coord.y < 1 or coord.y > size_y)
    if (OOB_x or OOB_y) == True:
        return False
    else:
        return True

def getCandidates(coord:Coordinate) -> list[Coordinate]:
    candidateList = [Coordinate(coord.x, coord.y - 1), Coordinate(coord.x + 1, coord.y - 1), 
                     Coordinate(coord.x + 1, coord.y), Coordinate(coord.x + 1, coord.y + 1), 
                     Coordinate(coord.x, coord.y + 1), Coordinate(coord.x - 1, coord.y + 1), 
                     Coordinate(coord.x - 1, coord.y), Coordinate(coord.x - 1, coord.y - 1)]
    return list(filter(OOBfilter, candidateList))

def getCellState(coord:Coordinate):
    print(driver.find_element(By.ID, f'{coord.x}_{coord.y}').get_attribute("CLASS"))

def checkAdjCells(coord:Coordinate) -> AdjacentCells:
    print(getCandidates(coord))

    numBlanks = 0
    listBlanks = []
    numFlagged = 0

    for candCoord in getCandidates(coord):
        candState = getCellState(candCoord)
        if candState == "square bombflagged":
            numFlagged += 1
        elif candState == "square blank":
            numBlanks += 1
            listBlanks.append(coord)
        else:
            pass
        return AdjacentCells(numBlanks, listBlanks, numFlagged)


def solve(x:int, y:int):
    global size_x
    global size_y
    size_x = x
    size_y = y
    # driver.find_element(By.ID, math.ceil(x/2), math.ceil(y/2)).click()

    #While loop trough grid
    # end stop when id face == class facewin or id face == class facedead

    # WHAT ACTION
    # flag as bomb if numBombs - numFlagged == numBlanks
    # click blanks if numBombs - numFlagged == 0
    # pass

openMineSweeper()

size_x = 9
size_y = 9

getCellInfo(1,1)


