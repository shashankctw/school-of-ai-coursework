person = {"name": "John", "age": 30, "city": "New York"}

print(person)

if "age" in person:
    del person["age"]
    
person["country"] = "USA"
    
print(person)