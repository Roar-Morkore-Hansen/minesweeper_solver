import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
actionChains = ActionChains(driver)


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
        self.id = f'{self.y}_{self.x}'

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

def OOBfilter(coord:Coordinate) -> bool:
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
    cellClass = getElementByCoordinate(coord).get_attribute("CLASS")
    lastChar = cellClass[-1]
    if lastChar.isdecimal():
        return int(lastChar)
    else:
        return cellClass

def checkAdjCells(coord:Coordinate) -> AdjacentCells:
    numBlanks = 0
    listBlanks = []
    numFlagged = 0

    for candCoord in getCandidates(coord):
        candState = getCellState(candCoord)
        if candState == "square bombflagged":
            numFlagged += 1
        elif candState == "square blank":
            numBlanks += 1
            listBlanks.append(candCoord)
        else:
            pass
    return AdjacentCells(numBlanks, listBlanks, numFlagged)


def getElementByCoordinate(coord:Coordinate):
    return driver.find_element(By.ID, coord.id)

def click(coord:Coordinate):
    element = getElementByCoordinate(coord)
    element.click()

def flag(coord:Coordinate):
    element = getElementByCoordinate(coord)
    ActionChains(driver)\
            .context_click(element)\
            .perform()

def checkNumCell(numBombs:int, coord:Coordinate):
    print(coord.id)
    adjcells = checkAdjCells(coord)
    numFlagged = adjcells.numFlagged
    numBlanks = adjcells.numBlanks
    print(f'numBombs {numBombs}, numFlagged {numFlagged}, numBlanks {numBlanks}')

    if (numBombs - numFlagged == numBlanks):
        for blankCoord in adjcells.listBlakns:
            print(f'flag blank coord {blankCoord.id}')
            flag(blankCoord)
    elif (numBombs - numFlagged == 0):
        print("CLICK!")
        for blankCoord in adjcells.listBlakns:
            click(blankCoord)
     

def solve():
    global size_x
    global size_y
    # Click middle val
    middle = Coordinate(math.ceil(size_x/2), math.ceil(size_y/2))
    click(middle)

    #While loop trough grid
    # end stop when id face == class facewin or id face == class facedead

    faceStatus = driver.find_element(By.ID, "face").get_attribute("CLASS")

    y = 0
    while faceStatus == "facesmile":
        x = 0
        while x < 9:
            coord = Coordinate(x + 1, y%size_y + 1)
            cellState = getCellState(coord)
            if (isinstance(cellState, int)):
                if (cellState != 0):
                    checkNumCell(cellState, coord)
            #iterate
            x += 1
        y += 1


# DRIVER CODE

size_x = 9
size_y = 9
openMineSweeper()
solve()



