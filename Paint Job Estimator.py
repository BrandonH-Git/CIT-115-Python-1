#Programmer: Brandon Hodgdon
#Project: Paint Job Estimate
#Class: Python 115/115L
#Date: 6DEC2024

#Importing math module
import math

#Data validation function
def getFloatInput(sPrompt: str) -> float:
    while True:
        try:
            fValue = float(input(f"{sPrompt} "))
            if fValue <= 0:
                print("Input must a positive numeric value")
            else:
                break
        except ValueError:
            print("Input must a positive numeric value")
    return fValue

# Functions from lines 23 - 33 will calculate what is needed for Total Cost
def getGallonsOfPaint(fFeetPerGallon: float, fWallSquareFootage: float) -> int:
    return math.ceil(fWallSquareFootage / fFeetPerGallon)

def getLaborHours(fLaborHoursPerGal: float, iTotalGal: int) -> float:
    return fLaborHoursPerGal * iTotalGal

def getLaborCost(fLaborHoursPerGal: float, fPaintingLaborCharge: float) -> float:
    return fLaborHoursPerGal * fPaintingLaborCharge

def getPaintCost(fTotalGal: float, fPaintPrice: float) -> float:
    return fTotalGal * fPaintPrice

#This Function gets the tax rate for the user inputted state
def getSalesTax(sState: str) -> float:
    if sState == "CT" or sState == "VT":
        TaxRate = 0.06
    elif sState == "MA":
        TaxRate = 0.0625
    elif sState == "ME":
        TaxRate = 0.085
    elif sState == "NH":
        TaxRate = 0
    elif sState == "RI":
        TaxRate = 0.07
    else:
        TaxRate = 0
    return TaxRate

# Functions on line 52 and 55 calculate tax in dollars and total job cost
def getTotalTax(fPaintCost: float, fLaborCost: float, fSalesTax: float,) -> float:
    return (fLaborCost + fPaintCost) * fSalesTax

def paintJobTotal(fSalesTax, fLaborTotal, fPaintTotal):
    return fLaborTotal+fPaintTotal+fSalesTax

#This function prints results and saves file to user computer
def showCostOutput(sName: str, sShowCostOutput: str):
    print(sShowCostOutput)
    with open(f"{sName}_PaintJobOutput.txt", "w") as file:
        file.write(sShowCostOutput)

#Main function will have all prompts, logic, and calls all the functions
def main():
    fSqrFeetWall = getFloatInput("Enter wall space in square feet: ")

    fPaintPrice = getFloatInput("Enter paint price per gallon: ")

    fFeetPerGal = getFloatInput("Enter feet per gallon: ")

    fLaborHours = getFloatInput("How many labor hours per gallon: ")

    fPaintingLaborCharge = getFloatInput("Labor charge per hour: ")

    sState = input("State Job is in: ").upper()

    sLastName = input("Customer Last Name: ")

    iGalNeeded = getGallonsOfPaint(fFeetPerGal, fSqrFeetWall)

    fLaborHourTotal = getLaborHours(fLaborHours, iGalNeeded)

    fLaborCost = getLaborCost(fLaborHourTotal, fPaintingLaborCharge)

    fPaintCost = getPaintCost(iGalNeeded, fPaintPrice)

    fSalesTax = getSalesTax(sState)

    fTotalTax = getTotalTax(fPaintCost, fLaborCost, fSalesTax)

    fPaintJobTotal = paintJobTotal(fTotalTax,fLaborCost,fPaintCost)

    results = f'''
Gallons of paint: {iGalNeeded}
Hours of Labor: {fLaborHourTotal}
Paint charges: ${fPaintCost:,.2f}
Labor charges: ${fLaborCost:,.2f}
Tax: ${fTotalTax:,.2f}
Total cost: ${fPaintJobTotal:,.2f}
File: {sLastName}_PaintJobOutput.txt
'''

    showCostOutput(sLastName,results)

#Calling main function
main()
