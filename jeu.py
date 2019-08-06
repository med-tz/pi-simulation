import turtle
from decimal import *
x=int(input('give the number of digits youu want to simulate')) 
D = Decimal
getcontext().prec = x
a = n = D(1)
g, z, half = 1 / D(2).sqrt(), D(0.25), D(0.5)
for i in range(18):
    x = [(a + g) * half, (a * g).sqrt()]
    var = x[0] - a
    z -= var * var * n
    n += n
    a, g = x    
b=a * a / z
c=len(str(b))
turtle.pendown()
l=["yellow","orange","red","pink","magenta","navy","blue","cyan","lightgreen","green"]
for i in range(0,c-1):
    a=int(((b*(10**i))%10))
    turtle.color(l[a])
    turtle.speed("fastest")
    turtle.left(90-(a*36))
    turtle.forward(10) 
    turtle.setheading(0)


