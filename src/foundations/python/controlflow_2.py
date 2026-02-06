#Nested condtions
age = 70
if age < 18:
    if age < 13:
        print("You are a child.")
    else:
        print("You are a teenager.")

if age >= 18:
    if age < 65:
        print("You are an adult.")
    if age >= 65:
        print("You are a senior citizen.")