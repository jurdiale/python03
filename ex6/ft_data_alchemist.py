import random


if __name__ == "__main__":
    players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory',
               'john', 'kevin', 'Liam']
    print("=== Game Data Alchemist ===")
    print()
    print(f"Initial list of players: {players}")
    players_cap = [x.capitalize() for x in players]
    print(f"New list with all names capitalized: {players_cap}")
    result = [x for x in players if x == x.capitalize()]
    print(f"New list of capitalized names only: {result}")
    print()
    scores = {x: random.randint(0, 1000) for x in players_cap}
    print(f"Score dict: {scores}")
    total = sum(scores.values())
    length = len(scores)
    media = total / length
    print(f"Score average is {round((media), 2)}")
    high_scores = {k: v for k, v in scores.items() if v > media}
    print(f"High scores: {high_scores}")
