options = ["Best Schools in Round Rock", "Student Support Services", "City Holidays","Educational Resources", "Exit"]
print("Welcome to the Round Rock Department of Education chatbot! Let me get to know you:")
print()
name = input("What is your name? ")
grade = input("What grade is the student you will enquire about today in? ")
while not isinstance(grade, int):
    print("That is not a valid grade, sorry.")
    grade = input("What grade is the student you will enquire about today in? ")
while grade > 12:
    print("That is not a valid grade, sorry.")
    grade = input("What grade is the student you will enquire about today in? ")
print(f"HELLO {name}!")
print("How can I help you?")
for option in options:
    print(f"- {option}")
choice = input("Type your choice here: ")
if choice.lower == "exit":
    exit()
print(lol)
