# json practice

import json

# parsing json string
json_str = '{"name": "Bekri", "age": 19, "city": "Astana"}'
data = json.loads(json_str)
print(data["name"])
print(data["age"])

# python to json
person = {
    "name": "Bekri",
    "age": 19,
    "subjects": ["Python", "Math", "English"]
}
result = json.dumps(person, indent=4)
print(result)

# writing json to file
students = {
    "students": [
        {"name": "Bekri", "score": 90},
        {"name": "Dana", "score": 85},
        {"name": "Aitu", "score": 78}
    ]
}
with open("students.json", "w") as f:
    json.dump(students, f, indent=4)
print("saved to students.json")

# reading json from file
with open("students.json", "r") as f:
    loaded = json.load(f)

for s in loaded["students"]:
    print(s["name"], "-", s["score"])

# working with data.json
try:
    file = open("data.json", "r")
    js = json.load(file)
    print("\nInterface Status")
    print("=" * 80)
    print("DN                                                 Description           Speed    MTU")
    print("-" * 80)
    for i in js["imdata"]:
        attr = i["l1PhysIf"]["attributes"]
        print(attr["dn"], "\t", attr["descr"], "\t", attr["speed"], "\t", attr["mtu"])
    file.close()
except:
    print("data.json not found")
