import json

with open("2_Books.json", "r") as file:
    data = json.load(file)

price = input("Enter the minimum price of the books: ")

for book in data:
    if book["pris"] >= int(price):
        print("Title:", book["tittel"])
        print("Author:", book["forfatter"])
        print("Price:", book["pris"])

title = input("Enter the title of the book: ")
author = input("Enter the author of the book: ")
price = input("Enter the price of the book: ")

new_book = {
    "tittel": title,
    "forfatter": author,
    "pris": int(price)
}

data.append(new_book)

with open("2_Books.json", "w") as file:
    json.dump(data, file, indent=4)