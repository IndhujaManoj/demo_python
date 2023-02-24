option=input("Are you ready for a quiz?:")
if option=="yes":
    print("ok...,here it comes!")
else:
    print("ok.. I think You are not redy for this quiz")
print("Q1) What is the capital of Alaska?")
print("      1) Melbourne")
print("      2) Anchorage")
print("      3) Juneau")

q1=input()
if q1=="1":
    print("Sorry...,Melbourne is not a capital of Alaska")
elif q1=="2":
    print("Sorry...,Anchorage is not a capital of Alaska")
elif q1=="3":
    print("That's right!")
else:
    print(" please  enter Valid number")

print("Q2) Can you store the value ""cat""in a variable of type int?")
print("      1) Yes")
print("      2) no")
q2=input()
if q2=="1":
    print("sorry,""cat""is a string.inits can only store numbers")
elif q2=="2":
    print("That's correct")
else :
    print("please  enter Valid number")

print("Q3) What is the result of 9+6/3?")
print("      1) 5")
print("      2) 11")
print("      2) 15/3")

q3=input()
if q3=="1":
    print("Sorry...,5 is not a correct answer ")
elif q3=="2":
    print("That's right!")
elif q3=="3":
    print("Sorry...,15/3 is not a correct answer")
else:
    print(" please  enter Valid number")
    
def result():
    if q1=="3" and q2=="2" and q3=="2":
        print("Overall ,you got 3 out of 3......congragulations!!!!")
    elif q1=="3" and q2=="2":
        print("Overall ,you got 2 out of 3")
    elif q1=="3" and q3=="2":
        print("Overall ,you got 2 out of 3")
    elif q3=="2" and q2=="3":
        print("Overall ,you got 2 out of 3")
    elif q1=="3" or q2=="2" or q3=="2":
        print("Overall ,you got 1 out of 3")
    else:
        print("OOPS!!!sorry yoo got 0 out of 3")
result() 

    
    
    
    
