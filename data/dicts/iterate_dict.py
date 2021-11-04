def pattern():
    sequences = {"Short Sequence": 3, "Medium Sequence": 2, "Long Sequence": 1}
    return sequences

def display_keys(data):
    for key in data:
        print(key)

def display_values(data):
    for value in data.value():
        print(value)

def display_items(data):
    for key, value in data.items():
        print(value)

def run():
    print(pattern())
    print(display_keys(pattern()))
    print(display_values(pattern()))
    print(display_items(pattern()))
run()

