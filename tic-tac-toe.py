boarder = [" ", " ", " ",
           " ", " ", " ",
           " ", " ", " "
]

winnings = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


def display_board():
    row_length = 3
    count = 1
    for item in boarder:
        if (count % row_length) == 0:
            print("_") if item == " " else print(item)
            count += 1
        else:
            print("_", end="|") if item == " " else print(item, end="|")
            count += 1


display_board()
