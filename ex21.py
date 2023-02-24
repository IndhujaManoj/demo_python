name=input("enter your name:")
weight=float(input("enter your weight(kg):"))
height=float(input("enter your height(meter):"))
BMI=weight/height**2
print("your BMI is ",BMI)
if BMI<18.5:
    print("underweight")
elif BMI==18.5 or BMI<=24.9:
    print("normal weight")
elif BMI==25.0 or BMI<=29.9:
    print("overweight")
else:
    print("obese")
