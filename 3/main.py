import json

# task
# Mål: Implementere søk og filtrering i en liste av JSON-objekter.
# 
#     Deloppgave 1: Last inn 3_Personer.json
#     Deloppgave 2: Skriv en funksjon som filtrerer ut og viser personer basert på yrke.
#     Deloppgave 3: Skriv en funksjon som finner den eldste personen i datasettet.

with open("3_Personer.json", "r") as file:
    data = json.load(file)

def filter_by_occupation(occupation):
    for person in data:
        if person["yrke"] == occupation:
            print("Name:", person["navn"])
            print("Occupation:", person["yrke"])
            print("Age:", person["alder"])
            print()

def find_oldest_person():
    oldest_person = data[0]
    for person in data:
        if person["alder"] > oldest_person["alder"]:
            oldest_person = person
    print("Name:", oldest_person["navn"])
    print("Occupation:", oldest_person["yrke"])
    print("Age:", oldest_person["alder"])

print("Teachers:")
filter_by_occupation("Lærer")

print("Oldest person:")
find_oldest_person()

