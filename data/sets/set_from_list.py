def observed():
    observations = []
    for k in range(7):
        print("Please enter an observation")
        obs = input()
        observations.append(obs)
    return observations


def run():
    print("Counting observations...")
    observations = observed()
    set1 = set()
    for k in observations:
        data = (k, observations.count(k))
        set1.add(data)

    for data in set1:
        print(f"{data[0]} observed {data[1]} times.")




run()