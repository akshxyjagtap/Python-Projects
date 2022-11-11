import turtle
import random
import math

screen = turtle.Screen()
tt = turtle.Turtle()


tt.pendown()

tt.setheading(90)
tt.forward(200)
tt.setheading(330)
tt.forward(200)
tt.goto(0, 0)

# #         B(0,200)
# #         | \
#           |   \
#           |    /C(173.20,100)
#           |  /
# #  A(0,0) |/


# coordinates on the sides
# i have taken scale as 10 as more points will make the visualisation shabby

ab = [(0, x) for x in range(0, 210, 10)]


# coordinates on ac
# line equatioin  y = mx + c
# here m = tan(60) and c = 0
# for each x we will get the y

ac = []
for i in range(0, 174, 10):
    x = int(math.sqrt(3)*i)
    ac.append((x, i))

# coordinates on bc
# line equatioin  y = mx + c
# here m = -0.57735 and c = 200
# for each x we will get the y
bc = []
for i in range(0, 174, 10):
    y = int(-1/math.sqrt(3)*i +200)
    bc.append((i, y))


sides = [ab, bc, ac]




def area(x1, y1, x2, y2, x3, y3):

    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)


def isInside(x1, y1, x2, y2, x3, y3, x, y):

    # Calculate area of triangle ABC
    A = area(x1, y1, x2, y2, x3, y3)

    # Calculate area of triangle PBC
    A1 = area(x, y, x2, y2, x3, y3)

    # Calculate area of triangle PAC
    A2 = area(x1, y1, x, y, x3, y3)

    # Calculate area of triangle PAB
    A3 = area(x1, y1, x2, y2, x, y)

    # Check if sum of A1, A2 and A3
    # is same as A
    if (A == A1 + A2 + A3):
        return True
    else:
        return False


# for points inside a triangle 
points = []
for i in range(0,173):
    for j in range(0,200):
           point = (i,j) 
           points.append(point)

inside = []
for i in range(0,len(points)):
    if (isInside(0, 200, 173.20, 100, 0, 0,points[i][0], points[i][1])):
        inside.append(points[i])





for i in range(0,len(inside)):
    x_random = random.randint(0, 174)
    y_random = random.randint(0, 200)
    a = random.choice(random.choice(sides))
    b = random.choice(random.choice(sides))

    random_point = (x_random, y_random)
    tt.pendown
    tt.goto(a)
    tt.pendown
    tt.goto(x_random, y_random)
    tt.dot()
    tt.goto(b)
    print(f"coordintes of triangle (0,0),{b}, {random_point}")






screen.exitonclick()
tt.hideturtle()
