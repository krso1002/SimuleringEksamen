from tkinter import *
from math import *

tk = Tk()
tk.title("Skyter")
tk.resizable(False, False)

#create canvas and ball
WIDTH, HEIGHT = 1400, 500
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()

#ball
ball = canvas.create_oval(10, 150, 50, 190, fill="red")

#box
box = canvas.create_rectangle(1390, 100, WIDTH, 400, fill="blue")
canvas.create_rectangle(1390, 175, WIDTH, 325, fill="white")
canvas.create_rectangle(1390, 225, WIDTH, 275, fill="red")

canvas.create_line(50, 450, 1400, 450, fill="white")
for i in range(1, 29):
    canvas.create_line(i*50, 400, i*50, 450, fill="white")
    i = i + 50

print(1400/50)
xSpeed = 0
ySpeed = 0

dragCoeff = 0.47
dragArea = 0.9
gravity = .981
airDensity = 1.225
mass = .046

airResCoeff = (airDensity * dragCoeff * dragArea) / 2
Vt = sqrt(mass * gravity) / airResCoeff

def airRes():
    global xSpeed, ySpeed, airResCoeff, mass
    canvas.move(ball, xSpeed, ySpeed)

    #xSpeed = xSpeed * Vt
    ySpeed = ySpeed * .99
    print(xSpeed)

    
def MoveBall():
    global xSpeed, ySpeed
    canvas.move(ball, xSpeed, ySpeed)

    canvas.after(30, MoveBall)
    canvas.after(30, airRes)

def shoot():
    global xSpeed, ySpeed
    (x1, y1, x2, y2) = canvas.coords(ball)
    (x3, y3, x4, y4) = canvas.coords(box)
    xSpeed = 10
    ySpeed = 0
    #if the ball leaves the screen, reset it
    if x2 >= x3 and y1 <= y3 and y2 >= y4 or  x2 >= WIDTH:
        canvas.coords(ball, 10, 150, 50, 190)
        xSpeed = 0
        ySpeed = 0
        

    canvas.after(100, shoot)

def magnum():
    # WB @ MV = 110 at 1300
    # Ballistic Coefficient = 0.131
    # 
    return
    

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
tk.bind("<Key-k>", lambda event:shoot())
tk.bind('<Key-s>',lambda event:MoveDown())
tk.bind('<Key-w>',lambda event:MoveUp())

canvas.after(30, MoveBall)
tk.mainloop()
