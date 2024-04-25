import json

# task
# Mål: Arbeide med mer enn én JSON-fil og koble sammen data fra dem.
# 
#     Deloppgave 1: Last inn to JSON-filer (5_Studenter.json og 5_Kurs.json), hvor den ene inneholder studentinformasjon (navn, studentID) og den andre inneholder kursdetaljer (kursnavn, kursID, liste av studentIDer).
#     Deloppgave 2: Skriv en funksjon som kobler disse to datasettene for å vise hvilke studenter som er registrert i hvilke kurs.
#     Deloppgave 3: Utvid funksjonen for å tillate legging til en student i et kurs og oppdater begge JSON-filene.

with open("5_Studenter.json", "r") as file:
    students = json.load(file)

with open("5_Kurs.json", "r") as file:
    courses = json.load(file)

def show_students_in_courses():
    for course in courses:
        print("Course:", course["kursnavn"])
        print("Students:")
        for student_id in course["studenter"]:
            student = next((student for student in students if student["studentID"] == student_id), None)
            if student:
                print(student["navn"])
        print()
    
def add_student_to_course():
    course_name = input("Enter course name: ")
    student_name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    
    course = next((course for course in courses if course["kursnavn"] == course_name), None)
    student = next((student for student in students if student["navn"] == student_name and student["studentID"] == student_id), None)
    
    if course and student:
        course["studenter"].append(student_id)
        with open("5_Kurs.json", "w") as file:
            json.dump(courses, file, indent=4)
        print("Student added to course.")
    else:
        print("Course or student not found.")

show_students_in_courses()
add_student_to_course()