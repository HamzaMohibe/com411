def directions ():
    direction = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return direction

def menu():
    print("Please select a direction:")
    dirs = directions()
    for index in range(len(dirs)):
        print(f"{index}: {dirs[index]}")
    response = int(input())
    return dirs[response]

def run():
    route = []
    print("Working out escape route...")
    for x in range(5):
        route.append(menu())
    print(f"Escape route:{route}")


if __name__ == "__main__":
    run()