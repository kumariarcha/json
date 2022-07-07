import json
l='{"a":1,"a":2,"a":3,"a":4,"b":1,"b":2}'
print("original python object:")
print(l)
json_obj=json.loads(l)
print("Unique key")
# print(json_obj)
m=json.loads(l)
print(m)