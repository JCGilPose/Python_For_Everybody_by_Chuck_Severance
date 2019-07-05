hrs = input("Enter Hours: ")
h = float(hrs)

rate = input("Enter Rate: ")
r = float(rate)

gross_pay = 0.0

if h <= 40.0:
    gross_pay = h * r
    print(gross_pay)
else:
    gross_pay = (40 * r) + ((h - 40.0) * (1.5 * r))
    print(gross_pay)
