# returns all (key,values) paires as tuples
student = {
    "name": "soumya",
    "age": 78,
    "cgpa": 89,
    "subjects": {"phy": 87, "chem": 78, "bio": 77},
}

print(student.items())

# acsses paire

pair = list(student.items())
print(pair[0])
