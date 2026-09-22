#!/usr/bin/env python3


import sys


def parse_scores(args: list[str]) -> list[int]:
    scores = []
    for score in args:
        try:
            scores.append(int(score))
        except ValueError:
            print(f"Invalid parameter: '{score}'")
    return scores


def display_stats(scores: list[int]) -> None:
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores):.1f}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


def main() -> None:
    print("=== Player Score Analytics ===")
    scores = parse_scores(sys.argv[1:])
    if not scores:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
        return
    display_stats(scores)


if __name__ == "__main__":
    main()
