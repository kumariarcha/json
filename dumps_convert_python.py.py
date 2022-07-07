import json
d='{"cname":"python","fees":15000,"duration":"2months"}'
x=json.loads(d)
print(type(x))
print(x)
for i in x:
    print(i,x[i])



# import json

# person_dict = {'name': 'Bob',
# 'age': 12,
# 'children': None
# }
# person_json = json.dumps(person_dict)
# print(type(person_dict))
# print(person_json)

