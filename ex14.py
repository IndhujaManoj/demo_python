def prints():
    print("You die of starvation.......eventually.")

print("WELCOME TO MITCHELL'S ADVENTURE!")

print("you are in a creepy house! would you like to go" ' "upstairs" ' "or in to the " '"kitchen" '"?")
ans1=input()
print("\n")
if ans1=="kitchen":
    kitchens=input(" There is a long countertop with dirty dishes everywhere.Off to one side there is,as you'd expect, a refrigerator.you may open the" '"refrigerator"'"or look in a"'"cabinet"')
    if kitchens=="refrigerator":
        frige=input("Inside the refrigerator you see food and stuff.It looks pretty nasty.would you like to eat some of the food? "'("yes" or "no")')
        prints()
    elif kitchens=="cabinet":
        cabinet=input("There is a disty cabinet with unclean cloths.do you want to clean it."'("YES" OR "NO")')
        prints("choose correct one")
    else:
        print()
    
elif ans1=="upstairs":
    upstairs1=input("There you look some phtos.and some dirty unclean flowers.would tou like to choose"'"picture" or "flower"?' )
    if upstairs1=="picture":
        pictures=input("Do you want to clean the picture?."'"yes" or "no"')
        prints()
    elif upstairs1=="flower":
        flowers=input("There is a unclean dirty flower.Do you want to pick that?."'"yes" or "no"')
        prints()
    else:
        print("choose correctone")
                        
                    
else:
    print("select vali option")
     

   
