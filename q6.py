#student id：1201200152
#student name:tey mei qun

import math
radius=float(input("Please enter the radius:"))
area=4*math.pi*math.pow(radius,2) #4*math.pi*radius*radius
volume=4/3*math.pi*math.pow(radius,3)

print("The radius is {:.2f}cm \nthe volume of it is {:.2f}cm^2 \nthe area of it is {:.2f}cm^3".format(radius,volume,area))