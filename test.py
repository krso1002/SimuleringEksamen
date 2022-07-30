from cmath import *
from textwrap import fill
from tkinter import *
from turtle import window_height

tk = Tk()
tk.title("Golf")
tk.resizable(False, False)

#create canvas and ball
WIDTH, HEIGHT = 1050, 500
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()

#set background color to green
canvas.create_rectangle(0, 0, WIDTH+20, 450, fill="green")

#top right corner of screen
canvas.create_rectangle(800, 0, 925, 50, fill="blue")
label = Label(canvas, text="50m", font=("Arial", 20), bg="blue")
label.place(x=835, y=10)
canvas.create_rectangle(925, 0, 1050, 50, fill="red")
label = Label(canvas, text="100m", font=("Arial", 20), bg="red")
label.place(x=960, y=10)
canvas.create_rectangle(800, 50, 925, 100, fill="orange")
label = Label(canvas, text="150m", font=("Arial", 20), bg="orange")
label.place(x=835, y=60)
canvas.create_rectangle(925, 50, 1050, 100, fill="purple")
label = Label(canvas, text="200m", font=("Arial", 20), bg="purple")
label.place(x=960, y=60)

#avstandspinner
canvas.create_rectangle(215, 400, 225, 450, fill="blue")
canvas.create_rectangle(415, 400, 425, 450, fill="red")
canvas.create_rectangle(615, 400, 625, 450, fill="orange")
canvas.create_rectangle(815, 400, 825, 450, fill="purple")


#create ball
ball = canvas.create_oval(10, 430, 30, 450, fill="white")

#create flag
canvas.create_line(950, 450, 950, 200, fill="white")
canvas.create_polygon(950, 200, 900, 225, 950, 250, fill="red")

xSpeed = 0
ySpeed = 0

dragCoeff = 0.47
dragArea = 0.9
gravity = 9.81
airDensity = 1.225
mass = 46
weight = mass * gravity

def MoveBall():
    global xSpeed, ySpeed
    canvas.move(ball, xSpeed, ySpeed)
    (x1, y1, x2, y2) = canvas.coords(ball)

    #create line that follows ball
    canvas.create_oval(x1+9, y1+9, x2-9, y2-9, fill="white")

    if y2 >= 450:
        return
    
    canvas.after(30, MoveBall)
    canvas.after(150, airResistance)
    canvas.after(30, angle)
    
def airResistance():
    label['text'] = "Air Resistance"
    global xSpeed, ySpeed

    #air resistance for x-axis
    airResCoeffX = dragCoeff * ((airDensity * xSpeed ** 2) / 2) * dragArea
    dragAccX = airResCoeffX / mass
    xSpeed = xSpeed - dragAccX

    #air resistance for y-axis
    airResCoeffY = dragCoeff * ((airDensity * ySpeed ** 2) / 2) * dragArea
    dragAccY = (weight - airResCoeffY) / mass
    ySpeed = ySpeed + dragAccY
    return

def angle():
    #calculate angle of ball trajectory
    if xSpeed > ySpeed:
        angle = atan(ySpeed/xSpeed) * 180 / pi
        #print(angle)
        

label = Label(tk, text="Select Club", font=("Arial", 30))
label.pack()

def driver():
    label['text'] = "Driver (15 degrees)"
    global xSpeed, ySpeed
    xSpeed = 113
    ySpeed = -31
    
def fiveIron():
    label['text'] = "5 Iron"
    global xSpeed, ySpeed
    xSpeed = 72
    ySpeed = -32

def sixIron():
    label['text'] = "6 Iron"
    global xSpeed, ySpeed
    xSpeed = 64
    ySpeed = -33

def sevenIron():
    label['text'] = "7 Iron"
    global xSpeed, ySpeed
    xSpeed = 56.8
    ySpeed = -33.6

def eightIron():
    label['text'] = "8 Iron"
    global xSpeed, ySpeed
    xSpeed = 50
    ySpeed = -35

def nineIron():
    label['text'] = "9 Iron"
    global xSpeed, ySpeed
    xSpeed = 44
    ySpeed = -36

def pitchingWedge():
    label['text'] = "Pitching Wedge"
    global xSpeed, ySpeed
    xSpeed = 38
    ySpeed = -37

def sandWedge():
    label['text'] = "Sand Wedge"
    global xSpeed, ySpeed
    xSpeed = 24
    ySpeed = -36.5

def threeWood():
    label['text'] = "Fairway Wood"
    global xSpeed, ySpeed
    xSpeed = 100
    ySpeed = -31

def resetBall():
    canvas.coords(ball, 10, 430, 30, 450)
    global xSpeed, ySpeed
    xSpeed = 0
    ySpeed = 0
    return

#create button for every club
button = Button(tk, text="Driver", command=driver)
button2 = Button(tk, text="Wood", command=threeWood)
button3 = Button(tk, text="5 iron", command=fiveIron)
button4 = Button(tk, text="6 iron", command=sixIron)
button5 = Button(tk, text="7 iron", command=sevenIron)
button6 = Button(tk, text="8 iron", command=eightIron)
button7 = Button(tk, text="9 iron", command=nineIron)
button8 = Button(tk, text="Pitch", command=pitchingWedge)
button9 = Button(tk, text="Sand", command=sandWedge)
button10 = Button(tk, text="Reset Ball", command=resetBall)

#place buttons
button.place(x=10, y=470)
button2.place(x=100, y=470)
button3.place(x=190, y=470)
button4.place(x=280, y=470)
button5.place(x=370, y=470)
button6.place(x=460, y=470)
button7.place(x=550, y=470)
button8.place(x=640, y=470)
button9.place(x=730, y=470)
button10.place(x=910, y=470)


tk.bind("<Key-k>", lambda event:MoveBall())
tk.bind("<Key-q>", lambda event:tk.destroy())
tk.bind("<Key-r>", lambda event:resetBall())

tk.mainloop()

