import sys

if __name__ == '__main__':
    print("=== Inventory System Analysis ===")
    invent: dict[str, int] = {}
    for arg in sys.argv[1:]:
        parts = arg.split(':')
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        key = parts[0]
        value_str = parts[1]
        if key in invent:
            print(f"Redundant item '{key}' - discarding")
            continue
        try:
            invent[key] = int(value_str)
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")
            continue
    print(f"Got inventory: {invent}")
    items = list(invent.keys())
    print(f"Item list: {items}")
    total = sum(invent.values())
    print(f"Total quantity of the {len(items)} items: {total}")
    if total > 0:
        for key, value in invent.items():
            print(
                f"Item {key} represents "
                f"{round((value / total) * 100, 1)}%")
    if not items:
        sys.exit()
    most_item = items[0]
    least_item = items[0]
    for key in items:
        if invent[key] > invent[most_item]:
            most_item = key
        if invent[key] < invent[least_item]:
            least_item = key
    print(f"Item most abundant: {most_item} with quantity {invent[most_item]}")
    print(
        f"Item least abundant: {least_item} with quantity "
        f"{invent[least_item]}")
    invent['magic_item'] = 1
    print(f"Updated inventory: {invent}")
