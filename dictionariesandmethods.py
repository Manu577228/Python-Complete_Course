# a = {}
# b = set()
# print(a, type(a))
# print(b, type(b))

# Difference between set and dictionaries are dictionary comes with key, value pair and set comes with only values.

dict1 = {"good": "something Pleasant", "fetch": "to search for something", "1": "The number 1"}

marks = {"Harshit": 34, "Naina": 87, "Gowri": 100, "Shivani": 33, "smriti": 17}

print(dict1["good"])
print(marks["Naina"])

marks["Priyanka"] = 34
print(marks)

print(marks.get("Priyanka Chopra"))
print(marks.get("Priyanka"))
print(marks.keys())
print(marks.values())
print(marks.items())

