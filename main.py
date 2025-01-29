from tkinter import *
import random

win = Tk()

win.geometry("750x550")
win.title("color generator")

def rgb_color(rgb):
    return '#%02x%02x%02x' % rgb

myR = random.randrange(0, 256)
myG = random.randrange(0, 256)
myB = random.randrange(0, 256)

def myRandomColor():
    global myR, myG, myB, mycanvas, mylabel
    
    myR = random.randrange(0, 256)
    myG = random.randrange(0, 256)
    myB = random.randrange(0, 256)
    mycanvas.destroy()
    mycanvas = Canvas(win, bg=rgb_color((myR,myG,myB)))
    mycanvas.place(relx=0.5, rely=0.4, anchor=CENTER)
    mylabel.destroy()
    var = StringVar()
    mylabel = Label(win, textvariable=var)
    var.set("the color is {}".format(rgb_color((myR,myG,myB))))
    mylabel.place(relx=0.8, rely=0.9, anchor=CENTER)
    
        




# create rgb code color

mycanvas = Canvas(win, bg=rgb_color((myR,myG,myB)))
mycanvas.place(relx=0.5, rely=0.4, anchor=CENTER)



mybutton = Button(win, text="random color", command= myRandomColor)
mybutton.place(relx=0.5, rely=0.8, anchor=CENTER)




var = StringVar()
mylabel = Label(win, textvariable=var)
var.set("the color is {}".format(rgb_color((myR,myG,myB))))
mylabel.place(relx=0.8, rely=0.9, anchor=CENTER)


win.mainloop()