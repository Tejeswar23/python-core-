import math

def calculate_quadratic(a,b,c):
    delta = (b**2)-(4*a*c)
    if delta > 0:
        root_1 = (-b + math.sqrt(delta))/(2*a)
        root_2 = (-b - math.sqrt(delta))/(2*a)
        return root_1,root_2
    elif delta == 0:
        root_1 = -b/(2*a)
        return root_1,root_1
    else:
        return None, None

a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
c=int(input("Enter c value: "))
res_1,res_2 = calculate_quadratic(a,b,c)

if res_1 is None and res_2 is None:
    print("No real roots exist.")
else:
    print(f"The roots value are {res_1} and {res_2}")
