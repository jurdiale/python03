import math


def get_player_pos() -> tuple[float, ...]:
    while True:
        coords = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = coords.split(',')
        position = []
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        else:
            for parte in parts:
                try:
                    position.append(float(parte.strip()))
                except ValueError as e:
                    print(f"Error on parameter '{parte.strip()}': {e}")
                    break
            else:
                return tuple(position)


if __name__ == '__main__':
    set0 = (0, 0, 0)
    print("=== Game Coordinate System ===")
    print("")
    print("Get a first set of coordinates")
    set1 = get_player_pos()
    print(f"Got a first tuple: {set1}")
    print(f"It includes: X={set1[0]}, Y={set1[1]}, Z={set1[2]}")
    distance = round(
        math.sqrt(
            (set1[0] - set0[0])**2
            + (set1[1] - set0[1])**2
            + (set1[2] - set0[2])**2
            ), 4)
    print(f"Distance to center: {distance}")
    print()
    print("Get a second set of coordinates")
    set2 = get_player_pos()
    distance2 = round(
        math.sqrt(
            (set1[0] - set2[0])**2
            + (set1[1] - set2[1])**2
            + (set1[2] - set2[2])**2
            ), 4)
    print(f"Distance between the 2 sets of coordinates: {distance2}")
