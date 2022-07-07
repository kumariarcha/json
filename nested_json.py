import json
my_str='{"name":"mike","age":40}'
print(type(my_str))
json_str=json.loads(my_str)
print(json_str)
print(type(json_str))
location={}
state={}
location['country']='india'
state['name']="Delhi"
state['distict']='M bihar'
location['state']=state
json_str['location']=location
print(json_str)
json_format=json.dumps(json_str,indent=4)
print(json_format)
