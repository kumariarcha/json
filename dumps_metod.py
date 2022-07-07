import json
data={"Name":"Archana","work":"studay","qulification":"BA1"}
with open("student_data.json","w")as json_file:
    data["work"]="software devloper"
    data["Name"]="bharti"
    data["name"]="devika"
    json.dump(data,json_file)