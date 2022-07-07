import json
data={"name":"Rajiv sharma","website":"technicaldirector in"}
with open("demo.json","w")as json_file:
    json.dump(data,json_file)



with open("demo.json","r")as json_file:
    data=json.load(json_file)
    data["website"]="vixpipeline in"
    print(data)
with open("demo.json","w")as json_file:
    json.dump(data,json_file)


