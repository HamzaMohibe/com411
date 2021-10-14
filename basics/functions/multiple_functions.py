# def display_box(name):
#     message = f"* Hello {name} *"
#     print("*" * len(message))
#     print(message)
#     print("*" * len(message))
#
#
# def greet_user():
#     print("Please enter your name")
#     name = input()
#     display_box(name)
#
#
# greet_user()
def display_ladder(steps):
    for step in range(steps):
        print("| |")
        print("*" * int(steps))
    print("| |")

def create_ladder():
    print("How many steps remain?")
    steps = int(input())
    display_ladder(steps)

create_ladder()
