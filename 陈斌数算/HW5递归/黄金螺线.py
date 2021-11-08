import turtle

def fibonacci(n):
    if n == 1 :return 0
    elif n==2:return 1
    else:return (fibonacci(n-1)+fibonacci(n-2))

def golden_spiral(n):
    if n>=1:
        t.circle(5*fibonacci(n),90)
        golden_spiral(n-1)

t=turtle.Turtle()
t.penup()
t.bk(80)
t.lt(90)
t.bk(300)
t.pendown()
t.rt(90)
t.pensize(3)
golden_spiral(11)