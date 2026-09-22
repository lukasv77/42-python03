#!/usr/bin/env python3

import random

ACHIEVEMENTS: list[str] = [
    "Crafting Genius", "Strategist", "World Savior", "Speed Runner",
    "Survivor", "Master Explorer", "Treasure Hunter", "Unstoppable",
    "First Steps", "Collector Supreme", "Untouchable", "Sharp Mind",
    "Deep Diver", "Flawless Victory"]


PLAYERS: list[str] = ["Alice", "Bob", "Charlie", "Dylan"]


def gen_player_achievements() -> set[str]:
    ach_cnt = random.randint(8, 10)
    ach_set = set(random.sample(ACHIEVEMENTS, ach_cnt))
    return ach_set


def main() -> None:
    ach_collection = {}
    print("=== Achievement Tracker System ===")
    for player in PLAYERS:
        ach_collection[player] = gen_player_achievements()
        print(f"Player {player}: {ach_collection[player]}")
    print()
    temp_set: set[str] = set()
    for player in PLAYERS:
        temp_set = temp_set.union(ach_collection[player])
    print(f"All distinct achievements: {temp_set}")
    print()
    for player in PLAYERS:
        temp_set = temp_set.intersection(ach_collection[player])
    print(f"Common achievements: {temp_set}")
    print()
    for player in PLAYERS:
        temp_set = set()
        for other_player in PLAYERS:
            if other_player == player:
                continue
            temp_set = temp_set.union(ach_collection[other_player])
        print(f"Only {player} has: "
              f"{ach_collection[player].difference(temp_set)}")
    print()
    for player in PLAYERS:
        print(f"{player} is missing: "
              f"{set(ACHIEVEMENTS).difference(ach_collection[player])}")


if __name__ == "__main__":
    main()
