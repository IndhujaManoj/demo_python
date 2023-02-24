

name=input("Hey,what is your name?")

print("Ok,",name ,end="")
age=int(input(",how old are you?"))

if age<16:
    print("you can't drive,",name)
    print("you can't vote,",name)
    print("you can't rent a car,",name)
elif age<18:
    print("you can't vote,",name)
    print("you can't rent a car ,",name)
elif age<25:
    print("you can't rent a car ,",name)
    
else:
    print("you can do anything thats legal,",name)
    
    
