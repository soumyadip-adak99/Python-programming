# return all keys

student = {
    "name": "soumya",
    "age": 78,
    "cgpa": 89,
    "subjects": {"phy": 87, "chem": 78, "bio": 77},
}

print(student.keys())

# type casting
print(list(student.keys()))

# print lenght
print(len(list(student.keys())))
