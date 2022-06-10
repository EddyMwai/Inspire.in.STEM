from tkinter import *
#creating the window
window = Tk()
window.title("Weather To You")
window.configure(bg = 'Black')
window.geometry("800x800")

#inserting labels
date = Label(window, text = "DATE ", font = ("Arial", 30))
city = Label(window, text = "CITY ", font = ("Arial", 30)) 

#positioning labels
date.grid(column = 10, row = 10)
city.grid(column = 10, row = 20)
 
#Insertng textboxes
date_box = Entry(window, width = 30)
date_box.grid(column = 30, row = 10 )

city_box = Entry(window, width = 30)
city_box.grid(column = 30, row = 20)

#making a button and a pop up

def popup():
    top = Toplevel(window)
    top.showinfo("Your day is cloudy. ")
    top.title('WEATHER')
    top.configure(bg = 'blue')
    top.geometry('400x400')
btn= Button(window, text = "OK", bg = 'green', command=popup ,height=5, width=10)

#positioning the button

btn.grid(column=80, row=100)
window.mainloop()