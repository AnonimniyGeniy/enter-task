import json

f1 = open("f1.json", "r")
f2 = open("f2.json", "r")
f3 = open("f3.json", "w")


data = json.load(f1)
data2 = json.load(f2)

wdata = {"servlet-class" : data["servlet-class"], "init-param":data["init-param"]}
if data["servlet-name"] in data2["servlet-name"]:
    json.dump(wdata, f3, indent = 4)
    f3.close()