correct_pin = input("Enter the correct pin: ")
access = False
for i in range(3):
    attempt = input("Enter your attempt: ")

    if attempt == correct_pin:
        access = True
        break

if access:
    print("ACCESS GRANTED")
else:
    print("LOCKED")

