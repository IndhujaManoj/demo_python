weight=float(input("Please enter your current earth weight:"))
print("I have information for the following planets:")
print("   1.Venus     2.Mars    3.Jupiter")
print("   4.Saturn    5.Uranus  6.Neptune")
visit=int(input("Which planet are you visiting:"))
venus=0.7*weight
mars=0.39*weight
jupiter=2.65*weight
saturn=1.17*weight
uranus=1.05*weight
neptune=1.23*weight
if visit==1:
  print("your weight would be",venus,"pounds on the planet.")
elif visit==2:
  print("your weight would be",mars,"pounds on the planet.")
elif visit==3:
  print("your weight would be",jupiter,"pounds on the planet.")
elif visit==4:
  print("your weight would be",saturn,"pounds on the planet.")
elif visit==5:
  print("your weight would be",uranus,"pounds on the planet.")
elif visit==6:
  print("your weight would be",neptune,"pounds on the planet.")
else:
    print("please select valid number.")
        
