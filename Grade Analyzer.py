# Programmer: Brandon Hodgdon
# Program: sGrade Analyzer
# Date: 24OCT2024
# Class: CIT-115/115L Python


# Input:
sName = input("Name of the person that we are calculating the Grades for: ")
fTest1 = float(input("Test 1: "))
fTest2 = float(input("Test 2: "))
fTest3 = float(input("Test 3: "))
fTest4 = float(input("Test 4: "))
sDrop = input("Do you wish to drop the Lowest Grade Y or N? ").upper()

#Error Messages:
DROP_CONDITIONS = [sDrop != "Y" and sDrop != "N"]
if any (DROP_CONDITIONS):
    print("Enter Y or N to drop the Lowest Grade.")
    raise SystemExit
TEST_CONDITIONS = [fTest1 <= 0, fTest2 <= 0, fTest3 <= 0, fTest4 <= 0]
if any (TEST_CONDITIONS):
     print("Test scores must be greater than 0")
     raise SystemExit

#Logic:
if sDrop == "Y":
    if fTest1 < fTest2:
        smallest = fTest1
    else:
        smallest = fTest2
    if fTest3 < smallest:
        smallest = fTest3
    if fTest4 < smallest:
        smallest = fTest4
    fAvg = ((fTest1 + fTest2 + fTest3 + fTest4)-smallest)/3
else:
    fAvg = (fTest1 + fTest2 + fTest3 + fTest4)/4

 #Conversions:
if fAvg >= 97.0:
    sGrade = "A+"
elif fAvg >= 94.0:
    sGrade = "A"
elif fAvg >= 90.0:
    sGrade = "A-"
elif fAvg >= 87.0:
    sGrade = "B+"
elif fAvg >= 84.0:
    sGrade = "B"
elif fAvg >= 80.0:
    sGrade = "B-"
elif fAvg >= 77.0:
    sGrade = "C+"
elif fAvg >= 74.0:
    sGrade = "C"
elif fAvg >= 70.0:
    sGrade = "C-"
elif fAvg >= 67.0:
    sGrade = "D+"
elif fAvg >= 64.0:
    sGrade = "D"
elif fAvg >= 60.0:
    sGrade = "D-"
else:
    sGrade = "F"

#Output:
print(f"{sName} test average is: {fAvg:.1f}")
print(f"Letter Grade for the test is: {sGrade}")



