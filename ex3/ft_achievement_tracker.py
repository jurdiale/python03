import random


def gen_player_achievements(all_achievements: list[str]) -> set[str]:
    n = random.randint(4, 10)
    return set(random.sample(all_achievements, n))


if __name__ == '__main__':
    all_achievements = ['Crafting Genius', 'World Savior', 'Master Explorer',
                        'Collector Supreme', 'Untouchable', 'Boss Slayer',
                        'Strategist', 'Unstoppable', 'Speed Runner',
                        'Survivor', 'Treasure Hunter', 'First Steps',
                        'Sharp Mind', 'Dragon Slayer', 'Night Owl',
                        'Hidden Path Finder']
    print("=== Achievement Tracker System ===")
    alice = gen_player_achievements(all_achievements)
    bob = gen_player_achievements(all_achievements)
    charlie = gen_player_achievements(all_achievements)
    dylan = gen_player_achievements(all_achievements)
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print()
    all_distinct = alice | bob | charlie | dylan
    print(f"All distinct achievements: {all_distinct}")
    print()
    print(f"Common achievements: {alice & bob & charlie & dylan}")
    print()
    print(f"Only Alice has: {alice - bob - charlie - dylan}")
    print(f"Only Bob has: {bob - alice - charlie - dylan}")
    print(f"Only Charlie has: {charlie - alice - bob - dylan}")
    print(f"Only Dylan has: {dylan - alice - bob - charlie}")
    print()
    print(f"Alice is missing: {set(all_achievements) - alice}")
    print(f"Bob is missing: {set(all_achievements) - bob}")
    print(f"Charlie is missing: {set(all_achievements) - charlie}")
    print(f"Dylan is missing: {set(all_achievements) - dylan}")
