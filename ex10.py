name=input("Hey,whats your name?(sorry,I keep forgetting):")

age=int(input("Enter the age:"))
if age<16:
    print("you can't drive",name)
elif age==16 or age==17:
    print("you can drive but can't vote,",name)
elif age==18 or age<=24:
    print("you can vote but not rent a car,",name)
else:
    print("you can do property much anything,",name)
    
