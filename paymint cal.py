import sys

days = 260

text = input("yearly to hourly or hourly to yearly please ruspond with 1 or 2: ")

#yearly to hourly
if "1" in text:
    
    pay_yearly = float(input("enter pay per year: "))
    
    days_off = float(input("enter days off: "))
    
    full_pay_yearly = pay_yearly / days_off
    print("your hourly pay: ", full_pay_yearly)
    sys.exit()

#full-time hourly to yearly
text = input("are you full-time yes or no: ")

pay = float(input("enter pay per hour: "))

if text == "yes":
    full_time = 2080 * pay
    if full_time > 53000 / 0.15:
        if full_time > 53000 > 106000 / 0.205:
            if full_time < 106000 > 165000 / 0.26:
                if full_time > 165000 / 0.29:
                    print ("pay per year: ", full_time)
    sys.exit()

worked = float(input("enter hours you work per day: "))

total_pay = worked * days * pay

print ("pay per year: ", total_pay)