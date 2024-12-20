#Programmer: Brandon Hodgdon
#Date: 02OCT2024
#Class: CIT-115 Python Programming
#Project: Solar System Weights

#Constants
nMERCURY = 0.38
nVENUS = 0.91
nMOON = 0.165
nMARS = 0.38
nJUPITER = 2.34
nSATURN = 0.93
nURANUS = 0.92
nNEPTUNE = 1.12
nPLUTO = 0.066

#Input
sName = input("What is your name: ")
nWeight = float(input("What is your weight: "))

#Logic
fMercAns = float(nWeight*nMERCURY)
fVenuAns = float(nWeight*nVENUS)
fMoonAns = float(nWeight*nMOON)
fMarsAns = float(nWeight*nMARS)
fJupiAns = float(nWeight*nJUPITER)
fSatuAns = float(nWeight*nSATURN)
fUranAns = float(nWeight*nURANUS)
fNeptAns = float(nWeight*nNEPTUNE)
fPlutAns = float(nWeight*nPLUTO)

#Output                 
print(sName,"here are your weights on our Solar System's planets:")
print(f"{"Weight on Mercury:":20s} {fMercAns:10,.2f}")
print(f"{"Weight on Venus:":20s} {fVenuAns:10,.2f}")
print(f"{"Weight on our Moon:":20s} {fMoonAns:10,.2f}")
print(f"{"Weight on Mars:":20s} {fMarsAns:10,.2f}")
print(f"{"Weight on Jupiter:":20s} {fJupiAns:10,.2f}")
print(f"{"Weight on Saturn:":20s} {fSatuAns:10,.2f}")
print(f"{"Weight on Uranus:":20s} {fUranAns:10,.2f}")
print(f"{"Weight on Neptune:":20s} {fNeptAns:10,.2f}")
print(f"{"Weight on Pluto:":20s} {fPlutAns:10,.2f}")





