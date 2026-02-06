# While Loop Examples

# Count down from 5
count = 1
while count > 0:
    print(f"{count}")
    count -= 1
    
# Break Example
count = 10
while True:
    print(f"{count}")
    count -= 1
    if count == 3:
        break
    
print("Loop ended.")

# Continue Example
count = 10
while count > 0:
    count -= 1
    if count == 3:
        continue
    print(f"{count}")
    
print("Loop continued.")