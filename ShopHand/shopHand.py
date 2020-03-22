'''
ShopHand: all functions for the shophand program to run functionally
Author: Breann Thiessen
'''
import sqlite3 #holds the database for the repair reports

#jobs to be chosen from
jobs = ["None", "Brakes", "Head Lights", "Oil Change", "Tail Lights", "U-Joints", "Wheel Bearings"]
chosenJob = "" #holds the job chosen
chosenUnits = [] #holds all units
startDate = "" #holds the start date for repair report
endDate = "" #holds the end date for repair report
 

#will add the unit to the chosenUnits list
def addUnit(unit):
    if(unit not in chosenUnits):
        chosenUnits.append(unit)
        print(chosenUnits)

def delUnit(unit):
    if(unit in chosenUnits):
        chosenUnits.remove(unit)
        print(chosenUnits)

def saveJob(job):
    chosenJob = job
    print(chosenJob)

def setStartDate(date):
    startDate = str(date)
    print(startDate)

def setEndDate(date):
    endDate = str(date)
    print(endDate)
     