from sys import argv
work_hours, hourly_pay, premium = argv[1:]
print("ЗП сотрудника: ",int(work_hours)*int(hourly_pay) + int(premium))

