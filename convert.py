import json
from pickle import TRUE
dict={"corse":"python",
"fees":1500,
"months":True
}
dict=json.dumps(dict)
print(type(dict))
print(dict)




