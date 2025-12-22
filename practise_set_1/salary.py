salary = int(input("Enter the salary: "))
late_days = int(input("Enter the number of late days: "))
absent_days = int(input("Enter the number of absent days: "))
ded = 0
if late_days > 10:
    ded += salary * 0.10
elif late_days > 5:
    ded += salary * 0.05
if absent_days > 2:
    ded += salary * 0.05

final_salary = salary - ded

print(int(final_salary))
