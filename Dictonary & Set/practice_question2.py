# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.

marks = {}

python = int(input("Enter marks of python:"))
marks.update({"Python": python})

java = int(input("Enter marks of Java:"))
marks.update({"Java": java})

java_script = int(input("Enter marks of Javascript:"))
marks.update({"Javascript": java_script})

print(marks)
