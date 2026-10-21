student = {
    "name":"Nayan",
    "age": 21,
    "course":"Blockchain Technology",
    "city": "Pune"
}
print(student)
print(student["name"])
print(student["course"])
student.pop("city")
print(student)

#A dictionary stores information in key-value pairs.

#Think of a student record:     Student name = Key:"name" Value:"Nayan"
#Think of a Course record :     Course name = Key:"course" Value:"Blockchain Technology"
