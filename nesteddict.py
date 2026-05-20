dict= {
    "Student": "Rahul",
    "Subjects": {
        "Physics": 85,
        "Chemistry": 90,
        "Maths": 95,
    }
}
print(dict["Subjects"])
print(dict["Subjects"]["Maths"])
print(dict.keys())
print(dict.values())
pairs= list(dict.items())
print(pairs[0])
print(dict.get("Students"))# returns None if key is not found, while simple method directly shows error
dict.update({"Standard": 12})