import turtle   #using for more classes and make objects 
import random   #this is use for changing the food for snake on random position
import time     #speed ko managed karne k liye

delay=0.1       #delay kam karne se hi speed badegi
sc=0            #scoring card
hs=0            #highest score
bodies=[]

#creating a screen

s=turtle.Screen()                  #module k under class hai & S ye reference variable hai
s.title("Snake Game by Manish")
s.bgcolor("light blue")           #functions hai sab turtle me
s.setup(width=600,height=600)

#creating a head

head=turtle.Turtle()            #turtle module hai Turtle class hai use object banaya hai
head.speed(0)                   #head chale na isiliye
head.shape("circle")
head.color("blue")              #color function hai 
head.fillcolor("red")
head.penup()
head.goto(0,0)
head.direction='stop'           #direction naam variable use karna padega use rukvane k liye

#creating a food for snake

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.fillcolor("blue")
food.penup()
food.ht()                       #for hinding a turtle
food.goto(150,200)
food.st()                       #food show


#creating a score board

sb = turtle.Turtle()    #Note the parentheses to instantiate the Turtle class
sb.penup()              #kisi bhi jagah par bhejna
sb.ht()                 #hide karna
sb.goto(-250, 250)      #jaha par dikhana chahiye score card dikhana chahiye
sb.write("Score: 0     |    Highest Score: 0")  #to print a score on the screen for the 1st time


#creating function for moving in all direction
def moveUp():
    if head.direction!="down":
        head.direction="up"
def moveDown():
    if head.direction!="up":
        head.direction="down"
def moveLeft():
    if head.direction!="right":
        head.direction="left"
def moveRight():
    if head.direction!="left":
        head.direction="right"
def moveStop():
        head.direction="stop"


def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)


#event handling

s.listen()
s.onkey(moveUp,"Up")
s.onkey(moveDown,"Down")
s.onkey(moveLeft,"Left")
s.onkey(moveRight,"Right")
s.onkey(moveStop,"space")

#mainloop

while True:
    s.update()    #to update the screen

    #check collision with border (kahi border se takra to nhi rahi hai)

    if head.xcor()>290:
        head.setx(-290)
    if head.xcor()<-290:
        head.setx(290)
    if head.ycor()>290:
        head.sety(-290)
    if head.ycor()<-290:
        head.sety(290)

    #check collision with food

    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        #increase the body of snake

        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        bodies.append(body)  #append the new body in list

        sc=sc+100            #increase the score
        delay=delay-0.001

        if sc>hs:
            hs=sc       #update highest score
        sb.clear()
        sb.write("Score:{}  |  Highest Score:{}".format(sc,hs))

    #move snake bodies
    for i in range(len(bodies)-1,0,-1):
        x=bodies[i-1].xcor()
        y=bodies[i-1].ycor()
        bodies[i].goto(x,y)
    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    move()

#check collision with snake body--

    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            #hide bodies

            for body in bodies:
                body.ht()
            bodies.clear()
            sc=0
            delay=0.1
            sb.clear()
            sb.submit("Score:{}   |  Highest Score:{}".format(sc,hs))
    time.sleep(delay)
s.mainloop()   #it is use for dont close game output





















        





































