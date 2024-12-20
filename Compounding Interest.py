#Programmer: Brandon Hodgdon
#Date: 05OCT2024
#Class: CIT-115 Python Programming
#Project: Compound Interest Calculator

#Input
fStartingPrinciple = float(input("Enter the starting principal: "))
fRate = float(input("Enter the annual interest rate: "))
iTimesCompounded = int(input("How many times per year is the interest compounded? "))
fYears = float(input("For how many years will the account earn interest? "))

#Logic
fFinalVal = fStartingPrinciple*((1+((fRate/100)/iTimesCompounded)) ** (iTimesCompounded * fYears))

#Output
print(f"At the end of {fYears} years you will have $ {fFinalVal:,.2f}")


