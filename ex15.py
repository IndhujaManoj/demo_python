# Ask the user two questions
print("TWO MORE QUESTIONS,BABY!")
print("Think of something and I'll try to guess it!")
q1 = input("Does it belong inside or outside or both?")
q2 = input("Is it 'alive' or 'not alive'?")
if q1=="inside" and q2=="alive":
    print("My guess is, houseplant")
elif q1=="inside" and q2=="not alive":
    print("My guess is, shower curatin")
elif q1=="outside" and q2=="alive":
    print("My guess is, bison")
elif q1=="outside" and q2=="not alive":
    print("My guess is, billboard")
elif q1=="both" and q2=="alive":
    print("My guess is, dog")
elif q1=="both" and q2=="not alive":
    print("My guess is, cell phone")
else:
    print("I Think You Choose out side of the box")





