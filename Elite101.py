options = ["thing1", "thing2", "thing3","thing4", "Exit"]
print("Welcome User! Let me get to know you:")
print()
name = input("What is your name? ")
age = input("How old are you? ")
print(f"HELLO {name}! {age} is a wonderful age to be.")
print("How can I help you?")
for option in options:
    print(f"- {option}")
choice = input("Type your choice here: ")
if choice.lower == "exit":
    exit()
print("ot not work")