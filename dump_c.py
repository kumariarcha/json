import json
data={"name":"Archana",
"work":"devloper",
"living":"benglore"

}
with open("Archana.json","w")as json_file:
    data["name"]="devika"
    print(type(data))

    json.dump(data,json_file)


