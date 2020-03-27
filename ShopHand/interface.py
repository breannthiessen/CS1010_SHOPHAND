'''
Interface:
This file holds all the functions and modules that are used to interact with the user who
is using shopHand. The user is able to enter the data they wish to retrieve from this 
interface and it allows the user to generate repair lists depending on the job, and it allows
them to generate repair reports depending on the date.
The user is able to generate printable job lists and printable repair reports for their choices.
tkinter: used for the interface
shopHand: the main file used to interact with the database and save the user data
tkcalendar: used to make a visual date entry for the user
datetime: allows the calendar to block of dates that are not allowed to be chosen

Author: Breann Thiessen
'''

from tkinter import *
from shopHand import * 
from tkcalendar import * 
from datetime import date

printReport = False
printJob = False


#if a checkbutton is clicked then this function checks if there is a value
#if there is a value then the int is sent to the shopHand script where the
#unit number is saved in an array so that that the database can be queried
def unit():
    if (u95.get()):
        addUnit(95)
    else:
        delUnit(95)
    if (u97.get()):
        addUnit(97)
    else:
        delUnit(97)
    if(u99.get()):
        addUnit(99)
    else:
        delUnit(99)

#gets the repair job from the drop down menu and then sends the string
#to the shopHand script where it is assigned to chosenJob so it can be
#used to query the database
def getJob(repairJob):
    if(repairJob):
        saveJob(repairJob)

#if a date is selected then the date will be sent to the shopHand
#script and will be saved as a string for the start date
def getStartDate(e):
    setStartDate(cal.get_date())

#if a date is selected then the date will be sent to the shopHand
#script and will be saved as a string for the end date
def getEndDate(e):
    setEndDate(cal2.get_date())

#main window with buttons
root = Tk()
root.title("ShopHand")
root.geometry("500x500")
#display title
title = Label(root, text = "ShopHand", font = ("Copperplate Gothic Bold", 32, "bold"), fg = "red", justify = "center")

u95 = IntVar()
u97 = IntVar()
u99 = IntVar()
#assign variables to their check boxes
unit95 = Checkbutton(root,text = "Unit 95", variable = u95,
                     font = ("Arial", 12), fg = "black", height = 0, width = 20, command = unit)
unit97 = Checkbutton(root,text = "Unit 97", variable = u97, 
                     font = ("Arial", 12), fg = "black", height = 0, width = 20, command = unit)
unit99 = Checkbutton(root,text = "Unit 99", variable = u99, 
                     font = ("Arial", 12), fg = "black", height = 0, width = 20, command = unit)

#display repair job drop down menu
repairJob = StringVar()
chooseJob = OptionMenu(root, repairJob, *jobs, command = getJob) 
chooseJob.configure(font = ("Arial", 12), fg = "black", height = 1)
jLabel = Label(root, text = "Repair Job:", font = ("Arial", 12), fg = "black", height = 2)

#display the calendar and allow for date selection

sDate = StringVar()
eDate = StringVar()

rLabel = Label(root, text = "Repair Report:", font = ("Arial", 12), fg = "black", height = 2)
sLabel = Label(root, text = "Start:", font = ("Arial", 12), fg = "black", height = 2)
eLabel = Label(root, text = "End:", font = ("Arial", 12), fg = "black", height = 2)

#set the calendar max date that the user is allowed to pick
today = date.today()
cal = DateEntry(root, maxdate = today, width=12, background='red', variable = sDate,
                    foreground='white', borderwidth=1, selectbackground ="red")
cal.bind("<<DateEntrySelected>>", getStartDate)
cal2 = DateEntry(root, maxdate = today, width=12, background='red', 
                    foreground='white', borderwidth=1, selectbackground ="red")
cal2.bind("<<DateEntrySelected>>", getEndDate)

#display a print buttons
printJ = Button(root, text = "Print Job List", font = ("Arial", 12), fg = "black", width = 11)
printJ.bind("<Button-1>", getToolPart)

printR = Button(root, text = "Print Report", font = ("Arial", 12), fg = "black", width = 11)
printR.bind("<Button-1>", getReport)


#title and unit check boxes
title.place(x = 125, y=10)
unit95.place(x = 0, y = 100)
unit97.place(x = 150, y = 100)
unit99.place(x = 300, y = 100)
#drop down menu for job choice
chooseJob.place(x = 150, y = 150)
jLabel.place(x = 65, y = 150)
#label for repair report
rLabel.place(x = 65, y = 250)
#calendar for start date
sLabel.place(x = 65, y = 300)
cal.place(x = 115, y = 310)
#calendar for end date
eLabel.place(x = 65, y = 330)
cal2.place(x = 115, y = 340)
#print buttons
printJ.place(x = 340, y = 150)
printR.place(x = 340, y = 305)

root.mainloop()

