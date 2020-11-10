import tkinter as tk
from selenium import webdriver
import pyautogui as gk
import time
from tkinter import messagebox

####################### Main Window ####################

win=tk.Tk()
win.geometry('300x300')
win.title("Viewbot")
win.configure(bg='bisque3')
win.resizable(0,0)
win.iconbitmap('youtube.ico')

###################### Messagebox ########################

def check():
    if url.get() !="************Enter Url Here **************":
        if var.get()>0:
            sub()
        else:
            messagebox.showerror("Error","Please Select Views")
    else:
        messagebox.showerror("Error","Please Enter Url") 

####################### View Function ##################
def sub ():
    for i in range(0,var.get()):
        driver=webdriver.Chrome()
        driver.get(url.get())
        time.sleep(1)
        gk.click(80,675)
        time.sleep(20)
        driver.quit()
####################### Clear Function ##################

def clear(event):
    url.delete(0,tk.END)

####################### Hover Function ##################

def enter(e):
    go.config(bg='Red')


def leave(e):
    go.config(bg='orange red')

####################### Variable ####################

var=tk.IntVar()
choice=["5","10","25","50","100"]
var.set("0")

####################### Option Menu ###################


tim=tk.OptionMenu(win,var,*choice)
tim.config(bg='bisque3',fg="firebrick4")
tim.pack()
tim.place(x=190,y=150,height=25,width=60)

####################### Main label #####################

m=tk.Label(win,text="Youtube Viewbot",bg="bisque3",fg="firebrick4",font=("Times New Roman",22))
m.place(x=40,y=30,height=30,width=210)

####################### Select Label ###################

v=tk.Label(win,text="Select Views",bg="bisque3",fg="firebrick4",font=("Times New Roman",16))
v.place(x=50,y=150,height=25,width=125)

####################### Url Entry #######################

url=tk.Entry(win)
url.config(bg="Ivory1")
url.insert(0,"************Enter Url Here **************")
url.pack()
url.bind("<Button-1>",clear)
url.place(x=50,y=90,height=25,width=200)

####################### Button ###########################


go=tk.Button(win,text="Start",font=("Times New Roman",18),bg="orange red",fg="White",command=check)
go.pack()
go.bind("<Enter>",enter)
go.bind("<Leave>",leave)
go.place(x=50,y=210,height=50,width=200)

####################### Mainloop ####################
tk.mainloop()
