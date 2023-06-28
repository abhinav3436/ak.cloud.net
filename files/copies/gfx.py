import serial
import turtle
c=input("ser: ")
ser = serial.Serial(c, 9600)
turtle.screensize(canvwidth=256, canvheight=240)
t = turtle.Turtle()
t.speed(0)
turtle.title("RPI GRAPHICS")

gtx = 0
gty = 0
r=1
g=1
b=1
screen = turtle.Screen()

# Setting the screen color-mode
screen.colormode(255)
while True:
     r=100
     cc=str(ser.readline())
     ff=  cc[2:][:-5]
    
     if ff[0:1] == "f":
        t.forward(int(ff[1:5]))

     if ff[0:1] == "r":
        t.right(int(ff[1:5]))

     if ff[0:1] == "b":
        t.backward(int(ff[1:5]))

     if ff[0:1] == "l":
        t.left(int(ff[1:5]))
     if ff[0:1] == "h":
        t.hideturtle()
     if ff[0:1] == "s":
        t.showturtle()
     if ff[0:2]== "gx":
        gtx = int(ff[2:6])
     if ff[0:2]== "gy":
        gty = int(ff[2:6])
     if ff[0:2]== "gr":
        t.setpos(gtx,gty)
     if ff[0:2]== "pu":
        t.up()
     if ff[0:2]== "pd":
        t.down()
     if ff[0:2]=="cl":
        t.clear()
     if ff[0:2]=="st":
        t.stamp()
     if ff[0:2] == "pw":
        t.width(int(ff[2:5]))
     if ff[0:2] == "sr":
        r=int(ff[2:5])
        print(r)
     if ff[0:2] == "sg":
        g=int(ff[2:5])
     if ff[0:2] == "sb":
        b=int(ff[2:5])
     if ff[0:2] == "sc":
        t.color((r,g,b))
     if ff[0:2] == "il":
        t.begin_fill()
     if ff[0:2] == "ul":
        t.end_fill()
     else:
        print(ff)
turtle.done()      
