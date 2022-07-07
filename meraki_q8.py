import json

i=["neelam","programer",24,2400]
m=["komal","trainer",24,20000]
n=["anuradha","HR",25,40000]
p=["Abhishek","manger",29,63000]
r=[i,m,n,p]
list=['name','designation','age','salary']
f=['emp1','emp2','emp3','emp4']
x={}
i=0
while i<len(r):
    j=0
    s={}
    while j<len(r[i]):
        s[list[j]]=r[i][j]
        j=j+1
    x[f[i]]=s
    i=i+1
with open('meraki8.json',"w")as dict:
    json.dump(x,dict,indent=4)