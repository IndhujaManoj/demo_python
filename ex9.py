
import datetime 

def daynumber1():
        print("weekday 1:sunday")
daynumber1()
def daynumber2():
         print("weekday 2:monday")
daynumber2()
def daynumber3():
         print("weekday 3:tuesday")
daynumber3()
def daynumber4():
         print("weekday 4:wednesday")
daynumber4()
def daynumber5():  
         print("weekday 5:thursday")
daynumber5()
def daynumber6():
         print("weekday 6:friday")
daynumber6()
def daynumber7():  
         print("weekday 7:saturday")
daynumber7()
def daynumber0():
         print("weekday 8:saturday")
daynumber0()
def today():
    today=datetime.datetime.now()
    weekday_name=today.strftime("%A")
    print("TODAY IS :",weekday_name)

number=int(input("enter number:"))

if number==1:
    daynumber1()
elif number==2:
    daynumber2()
elif number==3:
    daynumber3()
elif number==4:
    daynumber4()
elif number==5:
    daynumber5()
elif number==6:
    daynumber6()
elif number==7:
    daynumber7()
elif number==8:
    daynumber8()
else:
    print("weekday ",number,":error")
    today()
    
            
        



        
        
        
        
        
    
        
        
        
        
