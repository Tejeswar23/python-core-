m1,m2,m3,m4,m5 = map(int,input("Enter :\n").split())
if(m1 < 35 or m2 < 35 or m3 < 35 or m4 <35 or m5 < 35) :
    print("Fail")
else:
    avg = (m1+m2+m3+m4+m5) // 5
    if(avg >= 75):
        print("Distinction")
    else:
        print("Pass")
