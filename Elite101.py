# Round Rock Department of Education Chatbot

import time

options = ["Best Schools in Round Rock", "Student Support Services", "City Holidays", "Educational Resources", "Exit"]

print("Welcome to the Round Rock Department of Education chatbot! Let me get to know you:")
print()

name = input("What is your name? ")

# Validate grade input
while True:
    grade_input = input("What grade is the student you will enquire about today in? ")
    try:
        grade = int(grade_input)
        if 0 < grade <= 12:
            break
        else:
            print("That is not a valid grade, sorry.")
    except ValueError:
        print("That is not a valid grade, sorry.")

print(f"\nHELLO {name}! Welcome!")

# Function responses

# School lists by grade groups

schools_elementary = [
    "Laurel Mountain Elementary",
    "Cactus Ranch Elementary",
    "Patsy Sommer Elementary",
    "Forest Creek Elementary",
    "Blackland Prairie Elementary"
]

schools_middle = [
    "Canyon Vista Middle School",
    "Cedar Valley Middle School",
    "Chisholm Trail Middle School",
    "Walsh Middle School",
    "Ridgeview Middle School"
]

schools_high = [
    "Westwood High School",
    "Round Rock High School",
    "McNeil High School",
    "Stony Point High School",
    "Cedar Ridge High School"
]

support_services = [
    "Counseling programs",
    "Special education resources",
    "After-school tutoring",
    "Gifted and talented opportunities"
]

city_holidays = [
    "New Year's Day",
    "Memorial Day",
    "Independence Day",
    "Labor Day",
    "Thanksgiving Break",
    "Winter Holiday Break"
]

educational_resources = [
    "Online library access",
    "Math & Reading practice portals",
    "Parent learning guides",
    "College and career readiness tools"
]


def show_best_schools():
    print("Top-rated schools in Round Rock for this grade level:")

    if grade <= 5:
        level_schools = schools_elementary
    elif 6 <= grade <= 8:
        level_schools = schools_middle
    else:
        level_schools = schools_high

    for school in level_schools:
        print(f"- {school}")
    print("These schools are known for high academic performance and strong student support.")
    print()


def show_student_support():
    print("Student Support Services:")
    for service in support_services:
        print(f"- {service}")
    print("Visit the RRISD website for more details.")
    print()


def show_city_holidays():
    print("City Holidays in Round Rock:")
    for holiday in city_holidays:
        print(f"- {holiday}")
    print("Dates may vary yearly.")
    print()


def show_educational_resources():
    print("Educational Resources:")
    for resource in educational_resources:
        print(f"- {resource}")
    print("These resources are free for all Round Rock ISD students.")
    print()

# Chatbot loop

while True:
    print("How can I help you today?")
    for option in options:
        print(f"- {option}")

    choice = input("\nType your choice here: ").lower().strip()

    if choice == "best schools in round rock":
        show_best_schools()
        time.sleep(5)


    elif choice == "student support services":
        show_student_support()
        time.sleep(5)

    elif choice == "city holidays":
        show_city_holidays()
        time.sleep(5)

    elif choice == "educational resources":
        show_educational_resources()
        time.sleep(5)

    elif choice == "exit":
        print("\nThank you for using the Round Rock Department of Education chatbot! Goodbye!")
        break

    else:
        print("\nSorry, I didn't understand that option. Please choose from the list.\n")
        time.sleep(2)
