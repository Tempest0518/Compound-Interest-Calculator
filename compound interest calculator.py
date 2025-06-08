while True:
    principle = float(input("Please enter the principle: "))
    if principle < 0:
        print("The principle can't be less than zero.")
    else:
        break

while True:
    rate = float(input("Please enter the interest rate: "))
    if rate < 0:
        print("The interest rate can't be less than zero.")
    else:
        break

while True:
    time = int(input("Please enter an amount of time in years: "))
    if time < 0:
        print("The time can't be less than zero.")
    else:
        break

total = principle * pow((1 + rate / 100 * time), time)

if time == 1:
    print(f"Your interest rate over {time} year will be ${total:,.2f}")
else:
    print(f"Your interest rate over {time} years will be ${total:,.2f}")
