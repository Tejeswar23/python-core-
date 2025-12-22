import math
def calculate_distance(x,y):
    distance = math.sqrt(x**2 + y**2)
    return distance
x=int(input("Enter x value: "))
y=int(input("Enter y value: "))
result = calculate_distance(x,y)
print(f"The distance from origin to point ({x},{y}) is {result}")