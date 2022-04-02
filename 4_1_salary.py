from sys import argv

try:
    script_name, work_hours, hourly_pay, bonus = argv
    print("Salary of the employee: ", float(work_hours) * float(hourly_pay) + float(bonus))
except ValueError:
    print('First argument - working hours, second argument - payment per hour, third argument - bonus, numbers only')
