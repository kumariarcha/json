import json 
def is_complex_ob(object):
    if  '_complex_' in object:
        print(complex(object["real"],object["img"]))
    else:
        print(object)
a='{"_complex_": true, "real": 4, "img": 5}'
b='{"real": 4, "img": 5}'
x=json.loads(a)
is_complex_ob(x)
x=json.loads(b)
is_complex_ob(x)