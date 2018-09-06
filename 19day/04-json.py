import json

d = {
"name":"laowang",
"age":12
}
print(type(d))

sd = json.dumps(d)
print(sd)
print(type(sd))


dd  =json.loads(sd)
print(dd)
print(type(dd))
