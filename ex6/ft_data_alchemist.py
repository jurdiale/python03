import random


if __name__ == "__main__":
    players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory',
               'john', 'kevin', 'Liam']
    print("=== Game Data Alchemist ===")
    print()
    print(f"Initial list of players: {players}")
    players_cap = []
    players_cap = [x.capitalize() for x in players]
    print(f"New list with all names capitalized: {players_cap}")
    result = []
    result = [x for x in players if x[0].isupper()]
    print(f"New list of capitalized names only: {result}")
    print()
    d = {}
    d = {x: random.randint(0, 1000) for x in players_cap}
    print(f"Score dict: {d}")
    total = sum(d.values())
    lenght = len(d)
    media = total / lenght
    print(f"Score average is {round((media), 2)}")
    d2 = {}
    d2 = {k: v for k, v in d.items() if v > media}
    print(f"High scores: {d2}")
