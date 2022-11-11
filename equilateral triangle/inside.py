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


points = []
for i in range(0,173):
    for j in range(0,200):
           point = (i,j) 
           points.append(point)

inside = []
for i in range(0,len(points)):
    if (isInside(0, 200, 173.20, 100, 0, 0,points[i][0], points[i][1])):
        print(f" random point inside triangle ")
        inside.append(points[i])


    else:
        print( 'Not Inside')

print(inside)        