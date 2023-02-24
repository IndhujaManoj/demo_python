gender = input("Enter your gender (male/female): ")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))


if gender == "female":
    if age >= 20:
        married = input("Are you married? (yes/no): ")
        if married == "yes":
            title = "Mrs."
        else:
            title = "Ms."
    else:
        title = ""
else:
    if age >= 20:
        title = "Mr."
    else:
        title = ""


if title != "":
    print(title, last_name)
else:
    print(first_name, last_name)


	

