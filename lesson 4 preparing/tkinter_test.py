from tkinter import *
 
root = Tk()
root.title("Моё приложение")
root.geometry("500x500")

lab = Label(root, text="1", bg="red", fg="gold", font="16")
lab.place(x=100, y=100)

#lab['text'] = "Поменяли"
lab['bg'] = "black"

#def changeLabel():
#	lab['text'] = "Вы нажали"

def changeLabel():
	count = int(lab['text'])
	count = count + 1
	lab['text'] = count

btn = Button(text="Hello", background="#555", foreground="#cca", font="16", command=changeLabel)
 
btn.place(x=200, y=200)

img = PhotoImage(file='/Users/paveltravkin/Desktop/Maximum/python/lesson 4 preparinng/logo.png')
pic = Label(root, image=img)
pic.place(x=300, y=300)

root.mainloop()
