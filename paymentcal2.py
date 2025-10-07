qu = input('Wage to salary, or salary to wage format: [w > s/s > w]: ')
def WagetoSalary(HourlyPay):
    return (HourlyPay * 8) * 260
def SalaryToWage(SalaryPay):
    return (SalaryPay/260)/8
if "w > s" in qu:
    HourlyPay = float(input("Enter wage: "))
    print(WagetoSalary(HourlyPay))
if "s > w" in qu:
    SalaryPay = float(input("Enter salary: "))
    print(SalaryToWage(SalaryPay))
#do note this code relies on a 9-5 work scheduled so 8 hours 260 days a year ie this may not give the correct output for you.