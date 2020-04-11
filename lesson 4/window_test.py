from tkinter import *

window = Tk()
window.title("Моё первое оконное приложение")
window.geometry("700x500")

lab = Label(window, text = "1", 
            bg = "yellow", fg = "#e20eed", 
            font = "16")

lab.place(x = 100, y = 300)

def changeLabel():
    a = int(lab["text"])
    a = a + 1
    lab["text"] = a


btn = Button(window, text = "Hello", 
            command = changeLabel)

btn.place(x=200, y=100)

img = PhotoImage(file = "/Users/paveltravkin/Desktop/Maximum/python/lesson 4 preparinng/logo.png")
pic = Label(window, image = img)
pic.place(x=0, y=0)

window.mainloop()