password = input("Enter the password: ")
length = 0
cont_digit = False
cont_upper = False
for x in password:
    length+=1
    if x >= '0' and x <= '9':
        cont_digit = True
    if x >='A' and x <= 'Z':
        cont_upper = True
if(length >= 8 and (cont_digit and cont_upper)) :
    print("Strong Password")
else:
    print("Weak Password")
