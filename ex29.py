class calculator:
    def __init__(self):
        pass
    def add(self,num1,num2):
        return num1 + num2
    def subtraction(self,num1,num2):
        return num1 -  num2
    def multiply(self,num1,num2):
        return num1 * num2
    def division(self,num1,num2):
        if num2==0:
            print("can't divided by zero")
        return num1 / num2
    def square(self,num):
        return num ** 2
    def square_root(self,num):
        if num<0:
            print("cannot take the square root of negative numbers")
        return num**0.5
    def evaluate(self,operation):
        operation=operation.replace('of','**')
        result=eval(operation)
        return result
calculator=calculator()
print(calculator.add(2,3))
print(calculator.subtraction(5,2))
print(calculator.multiply(2,4))
print(calculator.division(10,5))
print(calculator.square(4))
print(calculator.square_root(16))
print(calculator.evaluate("(2*5)/7+6*9"))      

      
        
    
