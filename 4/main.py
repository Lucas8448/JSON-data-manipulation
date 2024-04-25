import json

with open("4_Varer.json", "r") as file:
    data = json.load(file)

def group_by_category():
    categories = {}
    for product in data:
        category = product["kategori"]
        if category not in categories:
            categories[category] = []
        categories[category].append({
            "navn": product["navn"],
            "pris": product["pris"]
        })
    with open("4_Grouped_Varer.json", "w") as file:
        json.dump(categories, file, indent=4)

group_by_category()