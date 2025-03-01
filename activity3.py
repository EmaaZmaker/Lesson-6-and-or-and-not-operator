w=float(input("enter you're weight"))
h=float(input("enter you're height"))
BMI=w/(h/100)**2
print("you're BMI is", BMI)
if BMI<=18.4:
    print("you're underweight")
elif BMI<=24.9:
    print("you are healthy")
elif BMI<=29.9:
    print("you are overweight ")
elif BMI<=34.9:
    print("you are severly overweight")
elif BMI<=39.9:
    print("you are obese")
else:
    print("you are severly obese")