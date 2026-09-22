#!/usr/bin/env python3
import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    inventory = {}
    for pair in args:
        parts = pair.split(':')
        if len(parts) != 2:
            print(f"Error - invalid parameter '{pair}'")
        else:
            name, qty = parts
            if len(name) == 0:
                print("Empty name - discarding")
            elif name in inventory:
                print(f"Redundant item '{name}' - discarding")
            else:
                try:
                    if int(qty) <= 0:
                        print(f"Bad value '{qty}' - discarding")
                    else:
                        inventory[name] = int(qty)
                except ValueError as error:
                    print(f"Quantity error for '{name}': {error}")
    return inventory


def display_inventory(inventory: dict[str, int]) -> None:
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(dict.keys(inventory))}")
    print(f"Total quantity of the {len(inventory)} "
          f"items: {sum(dict.values(inventory))}")
    qtys_sum = sum(dict.values(inventory))
    for name in inventory:
        qty = inventory[name]
        print(f"Item {name} represents {round(qty / qtys_sum * 100, 1)}%")
    first = list(inventory.keys())[0]
    max_name = first
    max_value = inventory[first]
    for name in inventory:
        qty = inventory[name]
        if qty > max_value:
            max_name = name
            max_value = qty
    print(f"Item most abundant: {max_name} with quantity {max_value}")
    first = list(inventory.keys())[0]
    min_name = first
    min_value = inventory[first]
    for name in inventory:
        qty = inventory[name]
        if qty < min_value:
            min_name = name
            min_value = qty
    print(f"Item least abundant: {min_name} with quantity {min_value}")


def main() -> None:
    """Build the inventory from sys.argv[1:] and report on it."""
    print("=== Inventory System Analysis ===")
    inventory = parse_inventory(sys.argv[1:])
    if len(inventory) == 0:
        print("Empty inventory")
        return
    display_inventory(inventory)
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
