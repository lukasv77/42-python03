#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        input_parts = input("Enter new coordinates as floats in format "
                            "'x,y,z': ").split(',')
        if len(input_parts) != 3:
            print("Invalid syntax")
            continue
        float_list = []
        try:
            for part in input_parts:
                float_list.append(float(part))
            pos = (float_list[0], float_list[1], float_list[2])
            return pos
        except ValueError as error:
            print(f"Error on parameter '{part}': {error}")


def distance(a: tuple[float, float, float],
             b: tuple[float, float, float]) -> float:
    return math.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2 + (b[2]-a[2])**2)


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    player_pos1 = get_player_pos()
    print(f"Got a first tuple: {player_pos1}")
    print(f"It includes: X={player_pos1[0]}, Y={player_pos1[1]}, "
          f"Z={player_pos1[2]}")
    print(f"Distance to center: "
          f"{round(distance(player_pos1, (0.0, 0.0, 0.0)), 4)}\n")
    print("Get a second set of coordinates")
    player_pos2 = get_player_pos()
    print(f"Distance between the 2 sets of coordinates: "
          f"{round(distance(player_pos1, player_pos2), 4)}")


if __name__ == "__main__":
    try:
        main()
    except EOFError:
        print()
