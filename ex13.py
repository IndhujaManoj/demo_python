print("TWO QUESTIONS!")
print("Think of an object,and I'll try to guess it.")
print("Question 1) Is it animal,vegitable,or mineral?")
q1=input()

print("Question 1) Is it bigger than breadbox?")
q2=input()

if q1=="animal":
    if q2=="no":
        print(" My guess is that you are thinking of a mouse.")
    else:
        print(" My guess is that you are thinking of a squirrel")    

elif q1=="vegitable":
    if q2=="yes":
        print(" My guess is that you are thinking of a watermelon")
    else:
        print(" My guess is that you are thinking of a carrot")     

elif q1=="mineral":
    if q2=="yes":
        print("My guess is that you are thinking of a  camaro")
    else:
        print(" My guess is that you are thinking of a  paper clip")
def result():
        print("I would ask you if I'm right, but I don't actually care.")

result()

