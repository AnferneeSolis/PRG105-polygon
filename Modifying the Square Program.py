import turtle

def square(t,length):
    t.fd(length)
    t.lt(90)
    t.fd(length)
    t.lt(90)
    t.fd(length)
    t.lt(90)
    t.fd(length)
def polygon(t,length,n):
    t.fd(length)
    t.lt(360/n)
    t.fd(length)
    t.lt(360/n)
    t.fd(length)
    t.lt(360/n)
    t.fd(length)
    t.lt(360/n)
    t.fd(length)
    t.lt(360/n)
    t.fd(length)

bob = turtle.Turtle()

polygon(bob,100,6)

turtle.done()
