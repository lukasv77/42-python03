#!/usr/bin/env python3

import random
import typing

PLAYERS: list[str] = ["alice", "bob", "charlie", "dylan"]
ACTIONS: list[str] = ["run", "eat", "sleep", "grab", "move", "climb",
                      "swim", "use", "release"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        player = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (player, action)


def consume_event(events: list[tuple[str, str]]) \
                -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        yield (events.pop(random.randrange(len(events))))


def main() -> None:
    print("=== Game Data Stream Processor ===")
    gen = gen_event()
    for i in range(1000):
        player, action = next(gen)
        print(f"Event {i}: Player {player} did action {action}")
    events_lst: list[tuple[str, str]] = []
    while len(events_lst) < 10:
        events_lst.append(next(gen))
    print(f"Built list of 10 events: {events_lst}")
    for event in consume_event(events_lst):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events_lst}")


if __name__ == "__main__":
    main()
