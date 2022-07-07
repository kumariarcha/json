import json
data={"name":"Archana","class":"BA","work":"devloper"}
with open("student_string.json","w") as json_file:
    json.dump(data,json_file)