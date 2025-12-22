
year = int(input("Enter a year: "))
year_length = len(str(year))
if(year_length < 4):
    print("Enter a valid year...")
else:
    if(year%400 == 0) or  (year % 4 ==0 and year % 100 != 0 ):
        print("It's a leap year")
    else:
        print("It's not a leap year")
