score = input("Enter Score: ")

try:
    fs = float(score)
except:
    print("Error. Please enter a score between 0.0 and 1.0. Thanks.")
    quit()

if fs < 0.0 or fs > 1.0:
    print("Invalid score. Please enter a score between 0.0 and 1.0. Thanks.")
else:
    grade = 0

    if fs >= 0.9:
        grade = "A"
        print(grade)
    elif fs >= 0.8:
        grade = "B"
        print(grade)
    elif fs >= 0.7:
        grade = "C"
        print(grade)
    elif fs >= 0.6:
        grade = "D"
        print(grade)
    else:
        grade = "F"
        print(grade)
