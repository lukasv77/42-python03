#!/usr/bin/env python3
import random

PLAYERS: list[str] = ["Alice", "bob", "Charlie", "dylan", "Emma",
                      "Gregory", "john", "kevin", "Liam"]


def main() -> None:
    print("=== Game Data Alchemist ===")
    print(f"Initial list of players: {PLAYERS}")
    all_capitalized = [name.capitalize() for name in PLAYERS]
    print(f"New list with all names capitalized: {all_capitalized}")
    only_capitalized = [name for name in PLAYERS if name[0].isupper()]
    print(f"New list of capitalized names only: {only_capitalized}")
    scores = {name: random.randint(0, 1000) for name in all_capitalized}
    print(f"Score dict: {scores}")
    avg = sum([scores[name] for name in scores]) / len(scores)
    print(f"Score average is {round(avg, 2)}")
    high_scores = {name: scores[name] for name in scores if scores[name] > avg}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
