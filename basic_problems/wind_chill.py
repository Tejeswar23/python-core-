import math
def wind_chill(t,v):
    if t < 50 and v < 3:    
        return 35.74 + (0.6215*t) - (35.75*(v**0.16)) + (0.4275*t*(v**0.16))
    else:
        return None
temp = float(input("Enter Temperature: "))
speed = float(input("Enter speed: "))
res = wind_chill(temp,speed)
print(res)
