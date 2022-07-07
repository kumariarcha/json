import json
a={}
filename="merki7.file"
with open("merki7.txt")as f:
    for i in f:
        key,value=i.strip().split(None,1)
        a[key]=value
file=open("merki7.json","w")
json.dump(a,file,indent=4)
file.close()