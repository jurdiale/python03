import random


def gen_player_achievements() -> set[str]:
    all_achievements = ['Crafting Genius', 'World Savior', 'Master Explorer',
                        'Collector Supreme', 'Untouchable', 'Boss Slayer',
                        'Strategist', 'Unstoppable', 'Speed Runner',
                        'Survivor', 'Treasure Hunter', 'First Steps',
                        'Sharp Mind', 'Dragon Slayer', 'Night Owl',
                        'Hidden Path Finder']
    n = random.randint(4, 10)
    return set(random.sample(all_achievements, n))


if __name__ == '__main__':
    print("=== Achievement Tracker System ===")
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print()
    all = alice | bob | charlie | dylan
    print(f"All distinct achievements: {all}")
    print()
    print(f"Common achievements: {alice & bob & charlie & dylan}")
    print()
    print(f"Only Alice has: {alice - bob - charlie - dylan}")
    print(f"Only Bob has: {bob - alice - charlie - dylan}")
    print(f"Only Charlie has: {charlie - alice - bob - dylan}")
    print(f"Only Dylan has: {dylan - alice - bob - charlie}")
    print()
    print(f"Alice is missing: {all - alice}")
    print(f"Bob is missing: {all - bob}")
    print(f"Charlie is missing: {all - charlie}")
    print(f"Dylan is missing: {all - dylan}")
