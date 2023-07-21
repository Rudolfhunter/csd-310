from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.v5ddl1q.mongodb.net/"
client = MongoClient(url)
db = client.pytech
#students = db["students"]

#docs = students.find({})
 
#for doc in docs:
# print(doc)
 
doc = db.student.find_one({"student_id": "1008"})
 
print(doc["student_id"])