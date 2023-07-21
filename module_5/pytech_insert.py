from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.v5ddl1q.mongodb.net/"
client = MongoClient(url)
db = client.pytech
students = db["students"]


fred = { "student_id": "1007",
        "first_name": "Fred",
        "last_name": "Jones"
        }
fred_student_id = students.insert_one(fred).inserted_id
john = { "student_id": "1008", 
        "first_name": "john", 
        "last_name": "Jones" 
        }
john_student_id = students.insert_one(john).inserted_id
jane = { "student_id": "1009",
        "first_name": "Jane",
        "last_name": "Doe"
        }
jane_student_id = students.insert_one(jane).inserted_id

first_name1 = fred["first_name"] 
last_name1 = fred["last_name"]
first_name2 = john["first_name"] 
last_name2 = john["last_name"]
first_name3 = jane["first_name"] 
last_name3 = jane["last_name"]




print(f"Inserted student record {first_name1} {last_name1} into students collection with document_id {fred_student_id}")
print(f"Inserted student record {first_name2} {last_name2} into students collection with document_id {john_student_id}")
print(f"Inserted student record {first_name3} {last_name3} into students collection with document_id {jane_student_id}")
