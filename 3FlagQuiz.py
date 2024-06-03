import random
import  turtle
scn=turtle.Screen()
scn.bgcolor("blue")
bob=turtle.Turtle()


def lithuania():
    bob.fillcolor("yellow")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(0,-30)
    bob.pd()
    bob.fillcolor("green")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(0,-60)
    bob.pd()
    bob.fillcolor("red")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(0,-30)
    bob.pd()



def poland():
    bob.fillcolor("white")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(0, -30)
    bob.pd()
    bob.fillcolor("red")
    bob.begin_fill()
    for i in range(2) :
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(0, -30)
    bob.pd()

def ukraine():
    bob.fillcolor("blue")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(0, -30)
    bob.pd()
    bob.fillcolor("yellow")
    bob.begin_fill()
    for i in range(2) :
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(0, -30)
    bob.pd()

flags = [lithuania, ukraine, poland]
life=3
points=0
bob.speed(100)

while life > 0 and len(flags) > 0:
    bob.reset()
    flag =random.choice(flags)
    flag()

    answer = input("Which country is this flag?")

    if answer ==  flag.__name__:
        flags.remove(flag)
        print("Bravo")
        points +=1
        print("Your points:",points)
    else:
        flags.remove(flag)
        print("Wrong")
        life-=1
if points==3:
    print("you won")


turtle.done()

