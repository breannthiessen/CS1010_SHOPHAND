'''
Interface:
This file holds all the functions and modules that are used to interact with the user who
is using shopHand. The user is able to enter the data they wish to retrieve from this 
interface and it allows the user to generate repair lists depending on the job, and it allows
them to generate repair reports depending on the date.
The user is able to generate printable job lists and printable repair reports for their choices.
MODULES USED
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


#main window with buttons
def mainPage():
    root = Tk()
    root.title("ShopHand")
    root.geometry("500x500")
    #display title
    title = Label(root, text = "ShopHand", font = ("Copperplate Gothic Bold", 48, "bold"), fg = "red", justify = "center")  
    #logo.image = photo # keep a reference!
    ask = Label(root, text = "I Would Like To", font = ("Arial", 12), fg = "black", justify = "center") 
    #display job list button choice
    goJob = Button(root, text = "Create a Job Checklist", font = ("Arial", 12), fg = "black", width = 20)
    goJob.bind("<Button-1>", generateJobList)
    #display repair list choice
    goReport = Button(root, text = "Create a Repair Report", font = ("Arial", 12), fg = "black", width = 20)
    goReport.bind("<Button-1>", generateRepairReport)
    title.place(x = 60, y=10)
    ask.place(x = 193, y = 150)  
    goJob.place(x = 155, y = 180)
    goReport.place(x = 155, y = 220)
    root.mainloop()

#repair job page
def generateJobList(e):
    #if a checkbutton is clicked then these 3 functions check if there is a value
    #if there is a value then the int is sent to the shopHand script where the
    #unit number is saved in an array so that that the database can be queried
    def toggle95():        
        if not(u95.get()):
            changeChosenUnits(95)    

    def toggle97():
        if not(u97.get()):
            changeChosenUnits(97)

    def toggle99():
        if not(u99.get()):
            changeChosenUnits(99)

    #send the job chosen to the ShopHand script
    def getJob(job):
        saveJob(job)
    
    #called when the printJob is hit and the options are cleared the user doesn't
    #make a mistake and generate two of the same lists
    def clearBoxes():
        unit95.deselect()
        unit97.deselect()
        unit99.deselect()
        repairJob = StringVar(root, 'None')


    root = Tk()
    root.title("ShopHand")
    root.geometry("500x500")
    #display title
    photo = PhotoImage(file="shophand_logo.png")
    logo = Label(image=photo)
    logo.image = photo
    title = Label(root, text = "ShopHand", font = ("Copperplate Gothic Bold", 48, "bold"), fg = "red", justify = "center")  
    #display the logo as the O in the title
    #assign variables to their check boxes
    u95 = BooleanVar()
    u97 = BooleanVar()
    u99 = BooleanVar()
    unit95 = Checkbutton(root,text = "Unit 95", variable = u95,
                         font = ("Arial", 12), fg = "black", height = 0, width = 20, command = toggle95)
   
    unit97 = Checkbutton(root,text = "Unit 97", variable = u97, 
                         font = ("Arial", 12), fg = "black", height = 0, width = 20, command = toggle97)

    unit99 = Checkbutton(root,text = "Unit 99", variable = u99, 
                         font = ("Arial", 12), fg = "black", height = 0, width = 20, command = toggle99)
 
    title.place(x = 60, y=10)
    #display repair job drop down menu
    repairJob = StringVar(root, 'None')
    chooseJob = OptionMenu(root, repairJob, *jobs, command = getJob) 
    chooseJob.configure(font = ("Arial", 12), fg = "black", height = 1)
    jLabel = Label(root, text = "Repair Job:", font = ("Arial", 12), fg = "black", height = 2)
    #unit check boxes
    unit95.place(x = 0, y = 150)
    unit97.place(x = 150, y = 150)
    unit99.place(x = 300, y = 150)
    #drop down menu for job choice
    chooseJob.place(x = 150, y = 200)
    jLabel.place(x = 65, y = 200)
    #display a print buttons
    printJ = Button(root, text = "Print Job List", font = ("Arial", 12), fg = "black", width = 11, command=lambda: [clearBoxes(), errorCheck()])
    printJ.place(x = 330, y = 200)   
    root.mainloop()

#repair report page
def generateRepairReport(e):  
    #if a date is selected then the date will be sent to the shopHand
    #script and will be saved as a string for the start date
    def getStartDate(e):
        setStartDate(cal.get_date())

    #if a date is selected then the date will be sent to the shopHand
    #script and will be saved as a string for the end date
    def getEndDate(e):
        setEndDate(cal2.get_date())

    root = Tk()
    root.title("ShopHand")
    root.geometry("500x500")
    #display title
    title = Label(root, text = "ShopHand", font = ("Copperplate Gothic Bold", 48, "bold"), fg = "red", justify = "center")  
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

    title.place(x = 60, y=10)
    #display the print button
    printR = Button(root, text = "Print Repair Report", font = ("Arial", 12), fg = "black", width = 15, command=lambda: [checkReport()])
    #label for repair report
    rLabel.place(x = 65, y = 140)
    #calendar for start date
    sLabel.place(x = 65, y = 180)
    cal.place(x = 115, y = 190)
    #calendar for end date
    eLabel.place(x = 65, y = 210)
    cal2.place(x = 115, y = 220)
    printR.place(x = 295, y = 190)
    root.mainloop()
mainPage()
