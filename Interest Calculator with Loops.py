#Programmer: Brandon Hodgdon
#Program: Interest Calculator with Loops
#Class: CIT 115/115L Python
#Date: 21NOV2024

# Defining Functions
def get_info_principal_interest_months(sPrompt: str, fMinValue: float):
    """returns a value larger than 0 into this function"""
    iValue = -1
    while iValue < fMinValue:
        try:
            iValue = float(input(f"{sPrompt}: "))
            if iValue < fMinValue:
                print("Input must a positive numeric value")
                continue
        except ValueError:
            print("Input must a positive numeric value")
            continue
        return iValue

def get_info_goal(sPrompt: str, fMinValue: int):
    """returns a value equal to or larger than 0 into this function"""
    iValue = -1
    while iValue < fMinValue:
        try:
            iValue = float(input(f"{sPrompt}: "))
            if iValue < fMinValue:
                print("Input must be 0 or greater")
                continue
        except ValueError:
            print("Input must be 0 or greater")
            continue
        return iValue

def getMPR(fIntRate):
    """Converts interest rate into monthly interest rate"""
    return (fIntRate / 100)/12

def FutureValue(Principal, MPR, Months):
    """Calculates accrued interest with each month and outputs to screen"""
    for Months in range(1, Months + 1):
        Principal += (Principal * MPR)
        print(f"Month:  {Months}   Account balance is: $ {Principal:,.2f} ")

def Goal(Principal, MPR, Goal):
    """Calculates how many months to reach goal with provided interest rate & principal"""
    MonCounter = 0
    while Principal < Goal:
        Principal += (Principal * MPR)
        MonCounter += 1
    print(f"It will take: {MonCounter} months to reach the goal of $ {Goal:,.2f}")

def main():
    fOriginalDeposit = get_info_principal_interest_months("What is the Original Deposit (positive value): ", .01)

    fInterestRate = get_info_principal_interest_months("What is the Interest Rate (positive value): ", .01)

    iMonths = int(get_info_principal_interest_months("What is the Number of Months (positive value): ", .01))

    fGoals = get_info_goal("What is the Goal amount (can enter 0 but not a negative): ", 0)

    fMPR = getMPR(fInterestRate)

    FutureValue(fOriginalDeposit, fMPR, iMonths)

    if fGoals != 0:
        Goal(fOriginalDeposit,fMPR,fGoals)

# Calling Main function
main()
