#!/usr/bin/python

###################################
# gui_examples using tkintinker
#  Date:07/06/2022
#  Name:Eddy Mwai
######################################

from tkinter import *

window = Tk()
window.title("Welcome to my App")
window.configure(bg='black')
window.geometry("400x400")   #fix the window sign

#making a label on the window
f_name = Label(window, text = "First name :", font = ("Arial " , 20))
s_name = Label(window, text = "Second name :", font = ("Arial " , 20))

#positioning the labels 
f_name.grid(column = 60 , row = 100)
s_name.grid(column = 60 , row = 120)

#making and positioning a button
def open_popup():
    top = Toplevel(window)
    top.geometry("300x300")
    top.title("Pop Up window")
    top.configure(bg='green')
    msg = Label(top,text = "Welcome to the pop up window ", font= 'Arial')
btn = Button(window, text = "click me" , bg = 'blue' , fg = 'red' , command = open_popup())
btn.grid(column = 100 , row = 180)

#making a text box 
f_name_box = Entry(window ,width= 20)
f_name_box.grid(column =100, row= 100)

s_name_box = Entry(window ,width= 20)
s_name_box.grid(column =100, row= 120 )




window.mainloop()
