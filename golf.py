# importing everything from tkinter
from textwrap import fill
from tkinter import *
from cmath import sqrt

tk = Tk()
tk.title("Golf")
tk.resizable(False, False)

#create canvas and ball
WIDTH, HEIGHT = 1050, 500
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()


#set background color to green
canvas.create_rectangle(0, 0, WIDTH+20, 450, fill="green")
canvas.create_rectangle(20, 410, 50, 440, fill="black")
canvas.create_line(20, 440, 440, 0, fill="white")

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
canvas.create_rectangle(195, 400, 205, 450, fill="blue")
canvas.create_rectangle(395, 400, 405, 450, fill="red")
canvas.create_rectangle(595, 400, 605, 450, fill="orange")
canvas.create_rectangle(795, 400, 805, 450, fill="purple")

ball = canvas.create_oval(10, 430, 30, 450, fill="white")

canvas.create_line(50, 450, 1050, 450, fill="white")

canvas.create_line(950, 450, 950, 200, fill="white")
canvas.create_polygon(950, 200, 900, 225, 950, 250, fill="red")

xSpeed = 0
ySpeed = 0

dragCoeff = 0.47
dragArea = 0.9
gravity = 9.81
airDensity = 1.225
mass = 46

#calculate drag coefficient 
airResCoeff = (airDensity * dragCoeff * dragArea) / 2
dragAcc = (mass - airResCoeff) / mass

def MoveBall():
    global xSpeed, ySpeed
    canvas.move(ball, xSpeed, ySpeed)
    (x1, y1, x2, y2) = canvas.coords(ball)
    
    #gradually decrease speed in x and y direction
    
    if y2 == 450:
        xSpeed = 0
        ySpeed = 0
        return

    canvas.after(30, MoveBall)
    canvas.after(30, airRes)
    

def airRes():
    global xSpeed, ySpeed
    xSpeed = xSpeed - dragAcc
    ySpeed = ySpeed * -.28
    
    

label = Label(tk, text="Select Club", font=("Arial", 30))
label.pack()

#change label text when button is clicked
def driver():
    label['text'] = "Driver"
    global xSpeed, ySpeed
    xSpeed = 15
    ySpeed = -13

def fiveIron():
    label['text'] = "5 Iron"
    global xSpeed, ySpeed
    xSpeed = 1
    ySpeed = -1

def sixIron():
    label['text'] = "6 Iron"

def sevenIron():
    label['text'] = "7 Iron"

def eightIron():
    label['text'] = "8 Iron"

def nineIron():
    label['text'] = "9 Iron"

def pitchingWedge():
    label['text'] = "Pitching Wedge"

def sandWedge():
    label['text'] = "Sand Wedge"

def lobWedge():
    label['text'] = "Lob Wedge"

def threeWood():
    label['text'] = "Fairway Wood"

def resetBall():
    global xSpeed, ySpeed
    canvas.coords(ball, 10, 430, 30, 450)
    xSpeed = 0
    ySpeed = 0
    #stop moveball function
    canvas.after_cancel(MoveBall)
    canvas.after_cancel(airRes)
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
#click screen to exit program
tk.bind("<Key-q>", lambda event:tk.destroy())
tk.bind("<Key-r>", lambda event:resetBall())
tk.bind("<Button-1>", lambda event:())

tk.mainloop()

