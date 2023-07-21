from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.v5ddl1q.mongodb.net/"
client = MongoClient(url)
db = client.pytech
studentsTable = db["students"]

students = studentsTable.find({})

print("-- Displaying Student Documents From find() Query --")

for student in students:
    idstring = str(student["student_id"])
    print("Student ID: " + idstring)
    print("First Name: " + student["first_name"])
    print("Last Name: " + student["last_name"])
    print()

print("-- Displaying Student Documents From find_one() Query --")
onestudent = studentsTable.find_one({"student_id": 1008})

idstring = str(onestudent["student_id"])
print("Student ID: " + idstring)
print("First Name: " + onestudent["first_name"])
print("Last Name: " + onestudent["last_name"])
print()