from tkinter import *

'''
Author: Breann Thiessen
CS3010: User Interfaces
Summary:
This file holds all error windows that are represented by different functions
depending on the user error the specific function is called from the shopHand script
MODULES USED
tkinter to create the UI for the errors
'''

#-------------------------------------------ALL ERROR WINDOWS------------------------------------------------

#Called when the user forgets to pick a unit number when generating a job repair list
def unitError():
    err = Tk()
    err.title("ERROR")
    err.geometry("250x150")
    message = Label(err, text = "UNIT NUMBER NOT SELECTED", font = ("Arial", 10), fg = "black")
    ok = Button(err, text="OK", font = ("Arial", 10), command=lambda: [err.destroy()], fg = "black", width = 8)
    message.place(x = 30, y = 50)
    ok.place(x = 90, y = 85)

#Called when the user forgets to choose a job when generating a job repair list
def jobError():
    err = Tk()
    err.title("ERROR")
    err.geometry("250x150")
    message = Label(err, text = "JOB TYPE NOT SELECTED", font = ("Arial", 10), fg = "black")
    ok = Button(err, text="OK", font = ("Arial", 10), command=lambda: [err.destroy()], fg = "black", width = 8)  
    message.place(x = 40, y = 50)
    ok.place(x = 90, y = 85) 

#Called when the user forgets to choose a job AND an unit when generating a job repair list
def jobListErr():
    err = Tk()
    err.title("ERROR")
    err.geometry("250x150")
    message = Label(err, text = "UNIT NUMBER NOT SELECTED", font = ("Arial", 10), fg = "black")
    message2 = Label(err, text = "JOB TYPE NOT SELECTED", font = ("Arial", 10), fg = "black")
    ok = Button(err, text="OK", font = ("Arial", 10), command=lambda: [err.destroy()], fg = "black", width = 8)
    message.place(x = 30, y = 40)
    message2.place(x = 40, y = 65)
    ok.place(x = 90, y = 95)

#Called when the user is generating a repair report and puts the end date before the start date
def dateError():
    err = Tk()
    err.title("ERROR")
    err.geometry("350x150")
    message = Label(err, text = "END DATE CANNOT BE BEFORE START DATE", font = ("Arial", 10), fg = "black")
    ok = Button(err, text="OK", font = ("Arial", 10), command=lambda: [err.destroy()], fg = "black", width = 8)
    message.place(x = 30, y = 50)
    ok.place(x = 135, y = 85)
