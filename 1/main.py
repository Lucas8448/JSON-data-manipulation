import json

data = {
    "name": "Lucas",
    "age": 17,
    "hobbies": ["programming", "gaming"],
    "location": {
        "city": "Oslo",
        "state": "Oslo"
    }
}

with open("data.json", "w") as outfile:
    json.dump(data, outfile, indent=4)

with open("data.json", "r") as infile:
    my_new_dict = json.load(infile)

print("Name:", my_new_dict["name"])
print("Age:", my_new_dict["age"])
print("Hobby 0:", my_new_dict["hobbies"][0])
print("City:", my_new_dict["location"]["city"])
print("State:", my_new_dict["location"]["state"])