import turtle #to import turtle module for graphics
import time #
import random # to generate random places for food
from playsound import playsound
#from goto import goto, label
#import cv2

mainScreen=turtle.Screen()
mainScreen.title("Snakely")
mainScreen.bgcolor("#00cc66")
mainScreen.setup(width=600, height=600)
mainScreen.tracer(0)


titlee=turtle.Turtle()
titlee.setpos(0,130)
titlee.write("Snakely",align="center", font=("Verdana",70, "normal", 'bold'))

rules=turtle.Turtle()
rules.goto(-235,70)
rules.write("Rules:",align="center", font=("Times New Roman",40, "normal"))

rule1=turtle.Turtle()
rule1.goto(-245,40)
rule1.write("1) There will be a ball and several bombs on the screen.", align="left", font=("Times New Roman",13, "normal"))

rule2=turtle.Turtle()
rule2.goto(-245,10)
rule2.write("2) You aim is to touch the ball and increase your body length which inceases the score. ",align="left",  font=("Times New Roman",13, "normal"))

rule3=turtle.Turtle()
rule3.goto(-245,-20)
rule3.write("3) Make sure you don't touch any bombs while moving. Each time you touch a bomb, you life  will be cut.", align="left", font=("Times New Roman",13, "normal"))


rule4=turtle.Turtle()
rule4.goto(-245,-50)
rule4.write("4) Press 2-move-down, 4-move-left, 6-move-right, 8-move-up. All the best!", align="left", font=("Times New Roman",13, "normal"))

button1=turtle.Turtle()
button1.shape("square")
button1.speed(0)
button1.color("yellow")
button1.penup()
button1.goto(-50,-150)

button2=turtle.Turtle()
button2.shape("square")
button2.speed(0)
button2.color("yellow")
button2.penup()
button2.goto(50,-150)

play=turtle.Turtle()
play.goto(0,-150)
play.write("Play Game?", align="center", font=("Times New Roman",45, "normal", "bold"))
playsound('screen1.wav')

score=0

def fun(xx,yy):
    if((xx<120 and xx>-120) and(yy<0 and yy>-140)):
        mainScreen.clearscreen()
        global count
        count=0
        global counter1
        counter1=0
        global temporary
        global scores
        direction="stop"
        global life
        life=3
        delay=0.1
        wn = turtle.Screen()
        wn.title("Play Game")
        wn.bgcolor("#80ffaa")
        wn.setup(width=600, height=600)
        wn.tracer(0)

        food= turtle.Turtle()
        food.speed(0)
        food.shape("circle")
        food.color("#ffff4d")
        food.penup()
        food.goto(100,0)

        bomb1= turtle.Turtle()
        bomb1.speed(0)
        bomb1.shape("square")
        bomb1.color("black")
        bomb1.penup()
        bx1=random.randint(1,250)
        by1=random.randint(1,250)
        while(bx1>80 and bx1<120 and by1==0):
            bx1=random.randint(1,250)
            by1=random.randint(1,250)
        bomb1.goto(bx1,by1)

        bomb2= turtle.Turtle()
        bomb2.speed(0)
        bomb2.shape("square")
        bomb2.color("black")
        bomb2.penup()
        bx2=random.randint(-250,-1)
        by2=random.randint(1,250)
        while(bx2>80 and bx2<120 and by2==0):
            bx2=random.randint(-250,-1)
            by2=random.randint(1,250)
        bomb2.goto(bx2,by2)

        bomb3= turtle.Turtle()
        bomb3.speed(0)
        bomb3.shape("square")
        bomb3.color("black")
        bomb3.penup()
        bx3=random.randint(-250,-1)
        by3=random.randint(-250,-1)
        while(bx3>80 and bx3<120 and by3==0):
            bx3=random.randint(-250,-1)
            by3=random.randint(-250,-1)
        bomb3.goto(bx3,by3)

        bomb4= turtle.Turtle()
        bomb4.speed(0)
        bomb4.shape("square")
        bomb4.color("black")
        bomb4.penup()
        bx4=random.randint(1,250)
        by4=random.randint(-250,-1)
        while(bx4>80 and bx4<120 and by4==0):
            bx4=random.randint(1,250)
            by4=random.randint(-250,-1)
        bomb4.goto(bx4,by4)

        pen = turtle.Turtle()
        pen.speed(0)
        pen.shape("square")
        pen.color("black")
        pen.penup()
        pen.hideturtle()
        pen.goto(-80, 260)
        pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

        lives = turtle.Turtle()
        lives.speed(0)
        lives.shape("square")
        lives.color("black")
        lives.penup()
        lives.hideturtle()
        lives.goto(80, 260)
        lives.write("Lives: 3", align="center", font=("Courier", 24, "normal"))

        class Node:
            def __init__(self,i):
                self.next=None
                self.prev=None
                self.score=0
                self.obj=turtle.Turtle()
                self.obj.shape("circle")
                self.obj.speed(0)
                self.obj.penup()
                self.obj.direction ="stop"
                if(i==0):
                    self.obj.goto(0,0)
                    self.obj.color("#ff5c33")
                else:
                    self.obj.color("#3399ff")

        class LinkedList:
            def __init__(self):
                self.head=None #initilaising head to none

            def insert(self,newNode):
                global count
                count=count+1
                if self.head is None:
                    self.head=newNode #if head is none, then making head point to the first nodde
                    self.prev=newNode
                    global temporary
                    if counter1==0:
                        global scoress
                        scoress=newNode
                    temporary=newNode

                else:
                    lastNode=self.head
                    while True:
                        if lastNode.next is None:
                            break
                        lastNode=lastNode.next
                    newNode.prev=lastNode
                    lastNode.next=newNode
                    move(temporary,newNode,2)
        linkedlist=LinkedList()
        linkedlist.insert(Node(count)) 
        def move(head,temp,i):
            if temporary.obj.direction=="up":
                y=temp.obj.ycor()
                if (y>=300):
                    if(i==0):
                        temp.obj.goto(temp.obj.xcor(),-290)
                else:
                    if(i==0):
                        temp.obj.goto(temp.obj.xcor(),y+20)
                    else:
                        temp.obj.goto(temporary.obj.xcor(), temp.prev.obj.ycor()-21)
            if temporary.obj.direction=="down":
                y=temp.obj.ycor()
                if(y<=-300):
                    if(i==0):
                        temp.obj.goto(temp.obj.xcor(),299)
                else:
                    if(i==0):
                        temp.obj.goto(temp.obj.xcor(),y-20)
                    else:
                        temp.obj.goto(temporary.obj.xcor(), temp.prev.obj.ycor()+21)
            if temporary.obj.direction=="left":
                x=temp.obj.xcor()
                if(x<=-300):
                    if(i==0):
                        temp.obj.goto(299, temp.obj.ycor())
                else:
                    if(i==0):
                        temp.obj.goto(x-20, temp.obj.ycor())
                    else:
                        temp.obj.goto(temp.prev.obj.xcor()+21, temporary.obj.ycor())
            if temporary.obj.direction=="right":
                x=temp.obj.xcor()
                if(x>=300):
                    if(i==0):
                        temp.obj.goto(-299, temp.obj.ycor())
                else:
                    if(i==0):
                        temp.obj.goto(x+20, temp.obj.ycor())
                    else:
                        temp.obj.goto(temp.prev.obj.xcor()-21, temporary.obj.ycor()) 

        def traverse():
            counter=0
            traverseNode=temporary
            while True:
                if traverseNode is None:
                    break
                else:
                    move(temporary, traverseNode,counter)
                    counter=counter+1
                    traverseNode=traverseNode.next

        def dir_up():
            temporary.obj.direction="up"

        def dir_down():
            temporary.obj.direction="down"
           
        def dir_left():
            temporary.obj.direction="left"
           
        def dir_right():
            temporary.obj.direction="right"

        def function():
            wn.clearscreen()
            wn2 = turtle.Screen()
            wn2.title("Game over")
            wn2.bgcolor("black")

            gameover1=turtle.Turtle()
            gameover1.goto(0,100)
            gameover1.color("white")
            gameover1.penup()
            gameover1.hideturtle()
            gameover1.write("Game Over",align="center", font=("Times New Roman",70, "normal", 'bold'))

            gameover2=turtle.Turtle()
            gameover2.goto(0,-50)
            gameover2.color("white")
            gameover2.penup()
            gameover2.hideturtle()
            gameover2.write("Score: {}".format(scoress.score),align="center", font=("Times New Roman",60, "normal", 'bold'))
            if(scoress.score<=60):
                playsound("victory1.mp3")
            elif(scoress.score>60 and scoress.score<=120):
                playsound("victory2.mp3")
            else:
                playsound("victory3.mp3")
            wn2.setup(width=600, height=600)
            wn2.tracer(0)
            # wn2.mainloop() 
        wn.listen()
        wn.onkeypress(dir_up, "8")
        wn.onkeypress(dir_down, "2")
        wn.onkeypress(dir_left, "4")
        wn.onkeypress(dir_right, "6")

        while True:
            if(temporary.obj.distance(bomb1)< 20 or temporary.obj.distance(bomb2)< 20 or temporary.obj.distance(bomb3)< 20 or temporary.obj.distance(bomb4)< 20):
                playsound('sound.mp3')
                life=life-1
                if(life==0):
                    playsound('gameover.mp3')
                    function()
                    break
                else:
                    wn.clearscreen()
                    wn = turtle.Screen()
                    wn.title("Play Game")
                    wn.bgcolor("#80ffaa")
                    wn.setup(width=600, height=600)
                    wn.tracer(0)

                    food= turtle.Turtle()
                    food.speed(0)
                    food.shape("circle")
                    food.color("#ffff4d")
                    food.penup()
                    food.goto(100,0)

                    bomb1= turtle.Turtle()
                    bomb1.speed(0)
                    bomb1.shape("square")
                    bomb1.color("black")
                    bomb1.penup()
                    bx1=random.randint(1,250)
                    by1=random.randint(1,250)
                    while(bx1>80 and bx1<120 and by1==0):
                        bx1=random.randint(1,250)
                        by1=random.randint(1,250)
                    bomb1.goto(bx1,by1)

                    bomb2= turtle.Turtle()
                    bomb2.speed(0)
                    bomb2.shape("square")
                    bomb2.color("black")
                    bomb2.penup()
                    bx2=random.randint(-250,-1)
                    by2=random.randint(1,250)
                    while(bx2>80 and bx2<120 and by2==0):
                        bx2=random.randint(-250,-1)
                        by2=random.randint(1,250)
                    bomb2.goto(bx2,by2)

                    bomb3= turtle.Turtle()
                    bomb3.speed(0)
                    bomb3.shape("square")
                    bomb3.color("black")
                    bomb3.penup()
                    bx3=random.randint(-250,-1)
                    by3=random.randint(-250,-1)
                    while(bx3>80 and bx3<120 and by3==0):
                        bx3=random.randint(-250,-1)
                        by3=random.randint(-250,-1)
                    bomb3.goto(bx3,by3)

                    bomb4= turtle.Turtle()
                    bomb4.speed(0)
                    bomb4.shape("square")
                    bomb4.color("black")
                    bomb4.penup()
                    bx4=random.randint(1,250)
                    by4=random.randint(-250,-1)
                    while(bx4>80 and bx4<120 and by4==0):
                        bx4=random.randint(1,250)
                        by4=random.randint(-250,-1)
                    bomb4.goto(bx4,by4)

                    pen = turtle.Turtle()
                    pen.speed(0)
                    pen.shape("square")
                    pen.color("black")
                    pen.penup()
                    pen.hideturtle()
                    pen.goto(-80, 260)
                    pen.write("Score: {}".format(scoress.score), align="center", font=("Courier", 24, "normal"))

                    lives = turtle.Turtle()
                    lives.speed(0)
                    lives.shape("square")
                    lives.color("black")
                    lives.penup()
                    lives.hideturtle()
                    lives.goto(80, 260)
                    lives.write("Lives: {}".format(life), align="center", font=("Courier", 24, "normal"))

                    count=0
                    linkedlist=LinkedList()
                    counter1=counter1+1
                    linkedlist.insert(Node(count))
                    wn.listen()
                    wn.onkeypress(dir_up, "8")
                    wn.onkeypress(dir_down, "2")
                    wn.onkeypress(dir_left, "4")
                    wn.onkeypress(dir_right, "6")

            else:
                wn.update()
                traverse()
                if temporary.obj.distance(food)< 20:
                    x=random.randint(-250,250)
                    y=random.randint(-250,250)
                    food.goto(x,y)
                    playsound('food.mp3')
                    b1x=random.randint(1,250)
                    b1y=random.randint(1,250)
                    while(abs(x-b1x)<=30 or abs(y-b1y)<=30):
                        b1x=random.randint(1,250)
                        b1y=random.randint(1,250)
                    bomb1.goto(b1x,b1y)

                    b2x=random.randint(-250,-1)
                    b2y=random.randint(1,250)
                    while(abs(x-b2x)<=30 or abs(y-b2y)<=30):
                        b2x=random.randint(-250,-1)
                        b2y=random.randint(1,250)
                    bomb2.goto(b2x,b2y)

                    b3x=random.randint(-250,-1)
                    b3y=random.randint(-250,-1)
                    while(abs(x-b3x)<=30 or abs(y-b3y)<=30):
                        b3x=random.randint(-250,-1)
                        b3y=random.randint(-250,-1)
                    bomb3.goto(b3x,b3y)

                    b4x=random.randint(1,250)
                    b4y=random.randint(-250,-1)
                    while(abs(x-b4x)<=30 or abs(y-b4y)<=30):
                        b4x=random.randint(1,250)
                        b4y=random.randint(-250,-1)
                    bomb4.goto(b4x,b4y)
                    scoress.score=scoress.score+10
                    pen.clear()
                    pen.goto(-80, 260)
                    pen.write("Score: {}".format(scoress.score), align="center", font=("Courier", 24, "normal"))
                    lives.clear()
                    lives.write("Lives: {}".format(life), align="center", font=("Courier", 24, "normal"))
                    linkedlist.insert(Node(count))
                    traverse()
                time.sleep(delay)
        wn.mainloop()

mainScreen.onscreenclick(fun)
mainScreen.mainloop()