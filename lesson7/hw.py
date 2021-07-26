plane = [
    ["*", "*", "*"],  # 0
    ["*", "*", "*"],  # 1
    ["*", "*", "*"]   # 2
]


def print_plane(plane):
    for i in plane:
        print(f"{i[0]} | {i[1]} | {i[2]}")


def main():
    print_plane(plane)

    for i in range(9):
        if i % 2 == 0:
            player = "X"
        else:
            player = "0"

        player_x = int(input())
        player_y = int(input())
        plane[player_x][player_y] = player
        print_plane(plane)


main()
