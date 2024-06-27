info = {
    "key": "value",
    "name": "Soumya",
    "learning": "coding",
    "age": 35,
    "adult": True,
    "marks": 89.5,
    "subjetc": ["java", "python", "c++", "c", "java Script"],
    "topic": ("dictonary", "set"),
}

print(info)

# acsses keys in dictonary
print(info["name"])
print(info["adult"])

# assining values

info["name"] = "adak"
print(info["name"])

##
info["surname"] = "dip"
print(info)

# we want to create empty dictonary

null_dict = {}

null_dict["name"] = "soumya"
print(null_dict)
