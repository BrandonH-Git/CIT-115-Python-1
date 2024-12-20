#Programmer: Brandon Hodgdon
#Project: Real Estate Analyzer
#Class: Python 115/115L
#Date: 16Dec2024

#Data Validation for list entry
def getFloatInput(sPrompt: str):
    fSalesValue = []
    sContinue ="Y"
    while sContinue == "Y":
        try:
            fSaleValPrompt = float(input(f"{sPrompt} "))
            if fSaleValPrompt <= 0:
                print("Input a number that is greater than 0!")
                continue
            else:
              fSalesValue.append(fSaleValPrompt)
            sContinue = YesorNoDataValidation("Enter another value Y or N: ")
        except ValueError:
            print("Input a number that is greater than 0!")
    return fSalesValue

#Data Validation for Y/N Prompt
def YesorNoDataValidation (sPrompt):
    while True:
        sContinue = input(sPrompt).upper()
        if sContinue == "N" or sContinue == "Y":
            break
        else:
            print("Input must be a Y or N!")
            continue
    return sContinue

#Function to calculate median property price
def getMedian(list):
    remainder = len(list) % 2
    halfway = len(list) // 2
    if remainder == 0:
        listmedian = (list[halfway] + list[halfway -1]) / 2
    else:
        listmedian = list[halfway]
    return listmedian

#Function w/ loop to output each entry and their length number
def listOutput(Propertylist):
    iCounter = 1
    for value in Propertylist:
        print(f"Property  {iCounter}  $    {value:,.2f}")
        iCounter += 1

#Main function with all logic in the function
def main():
    PropertySales = getFloatInput("Enter Property sales value:")
    PropertySales.sort()
    listOutput(PropertySales)
    print(f"Minimum:      $     {min(PropertySales):,.2f}")
    print(f"Maximum:      $     {max(PropertySales):,.2f}")
    print(f"Total:        $     {sum(PropertySales):,.2f}")
    print(f"Average:      $     {sum(PropertySales)/len(PropertySales):,.2f}")
    print(f"Median:       $     {getMedian(PropertySales):,.2f}")
    print(f"Commission:   $     {(sum(PropertySales) * .03):,.2f}")

#Calling main function
main()