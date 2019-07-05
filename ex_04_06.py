def computepay(h,r):
    if h <= 40:
        return h * r
    else:
        return (40 * r) + (((h - 40) * r) * 1.5)

hrs = input("Enter Hours: ")
try:
    fl_hrs = float(hrs)
except:
    print("Error. Please enter a numeric value.")
    quit()

rate = input("Enter Rate: ")
try:
    fl_rate = float(rate)
except:
    print("Error.Please enter a numeric value.")
    quit()


p = computepay(fl_hrs, fl_rate)

print(p)
