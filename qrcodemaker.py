import qrcode
import os
import tkinter
from tkinter import *

window = Tk()
# add widgets here
lb1 = Label(window, text="hello world")
lb2 = Label(window, text="this is another text")
bt = Button(window, text="ClickMe")
bt.place(x=100, y=80)
entry = Entry(window,text="enter you name",bd=2)
entry.place(x=80,y=140)
window.iconbitmap("qr.png")

def buttonClicked(self):
    # os.system("python ./sam.py")
      d= entry.get()
      print(d)


bt.bind('<Button-1>', buttonClicked)
lb1.place(x=100, y=50)
window.title('Hello Python')
window.geometry("300x200")
window.mainloop()
# img = qrcode.make("hello world")
# img.save('qr.png',"PNG")
