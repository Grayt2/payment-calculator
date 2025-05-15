q = input('Hourly - Yearly or Yearly - Hourly? [H/Y]: ')
def yearly(yearly_pay, days, avetimeatwork):
    avetimeatwork = float(input('how long do you spend at work in hours?: '))
    yearly_pay = int(input('what is your salary? [ex: 123123]: '))
    days = 261
    return round((yearly_pay/days)/avetimeatwork)

def hourly(hourly_pay, days, avetimeatwork):
    avetimeatwork = float(input('how long do you spend at work in hours?: '))
    hourly_pay = float(input('what is your pay? [ex: 17.5]: '))
    days = 261
    return round(hourly_pay*avetimeatwork*days)

if q == "H":
    print(hourly(0, 0, 0), "$")

if q =="Y":
    print(yearly(0, 0, 0), "$")
