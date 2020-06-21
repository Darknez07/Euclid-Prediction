from matplotlib import pyplot as plt
import numpy as np
xc = []
plt.scatter([-2,-1.5,-9,12,0],[1,2,1.2,3.5,6.7])


def eculid(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)


for i, j in zip([-2, -1.5, -9, 12, 0], [1, 2, 1.2, 3.5, 6.7]):
    xc.append(eculid(i, j, -9, 1.2))
plt.scatter([-2, -1.5, -9, 12, 0], xc, color='blue')
a = np.linspace(-10, 20)
b = a+9
plt.plot(a, b)


def compare(points):
    if(points[1]-points[0]-9) >= 0:
        plt.scatter(points[0], points[1])
        print("Above the Line")
    else:
        plt.scatter(points[0], points[1])
        print("Below the Line")


compare([1.23, 4.53])
plt.show()
