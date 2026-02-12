import re

text="Hello, my name is John Doe. I am 30 years old. My contact number is 123-456-7890."
digits = re.findall(r'\d+', text)
print(digits)

updated_text = re.sub(r'\d', 'X', text)
print(updated_text)

