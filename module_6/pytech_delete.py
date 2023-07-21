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

jack = { "student_id": 1010,
        "first_name": "Jack",
        "last_name": "Panzer"
        }
jack_student_id = studentsTable.insert_one(jack).inserted_id

#print(jack_student_id)

first_name1 = jack["first_name"] 
last_name1 = jack["last_name"]   
print("-- Insert Statements --")
print(f"Inserted student record into the students collection with document_id {jack_student_id}")
print()

print("-- DISPLAYING STUDENT TEST DOC --")
onestudent = studentsTable.find_one({"student_id": 1010})

idstring = str(onestudent["student_id"])
print("Student ID: " + idstring)
print("First Name: " + onestudent["first_name"])
print("Last Name: " + onestudent["last_name"])
print()

print("-- Displaying Student Documents From find() Query --")
students = studentsTable.find({})
for student in students:
    idstring = str(student["student_id"])
    print("Student ID: " + idstring)
    print("First Name: " + student["first_name"])
    print("Last Name: " + student["last_name"])
    print()