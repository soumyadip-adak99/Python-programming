# inserts the specified items to the dictionary

student = {"name": "soumya", "subject": {"py": 67, "chem": 98, "math": 95}}

new_dict = {"city": "Kolkata"}
student.update(new_dict)

print(student)
