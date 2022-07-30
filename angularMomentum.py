from tkinter import *

from setuptools import Command

tk = Tk()
tk.title("AM")
tk.resizable(False, False)

#create canvas and ball
WIDTH, HEIGHT = 700, 700
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()

#ball
ball = canvas.create_oval(330, 150, 370, 190)

xSpeed = 10
ySpeed = 0

dragCoeff = 0.47
dragArea = 0.9
gravity = .981
airDensity = 1.225
mass = .046

#calculate drag coefficient 
airResCoeff = (airDensity * dragCoeff * dragArea) / 2
dragAcc = (mass - airResCoeff) / mass

def MoveBall():
    global xSpeed, ySpeed
    canvas.move(ball, xSpeed, ySpeed)
    (x1, y1, x2, y2) = canvas.coords(ball)
    
    #make ball move in a circle
    if xSpeed > 0:
        xSpeed = xSpeed * dragAcc

    print(airResCoeff)
    canvas.after(30, MoveBall)
    

def popup(event):
    #define popup window position
    menu.tk_popup(event.x_root, event.y_root)

def MoveDown():
    global ySpeed
    ySpeed =ySpeed + 1

def MoveUp():
    global ySpeed
    ySpeed =ySpeed - 1

menu = Menu(tk)

menu.add_command(label="Exit", command=tk.quit)
tk.bind("<Button-1>", popup)
tk.bind('<Key-s>',lambda event:MoveDown())
tk.bind('<Key-w>',lambda event:MoveUp())

canvas.after(30, MoveBall)
tk.mainloop()
