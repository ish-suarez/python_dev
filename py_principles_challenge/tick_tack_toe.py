def get_row_col(string):
    if len(string) == 2:
        coordinates = list(string)
        row = (int(coordinates[1]) - 1)
        col_letter = coordinates[0].upper()
        col_cor = {'A': 0, 'B': 1, 'C': 2}
                
        board = [
            ["X", "O", "X"],
            [" ", " ", " "],
            ["O", " ", " "],
        ]
        
        for g, i in enumerate(board):
            if g == row:
                for k, v in col_cor.items():
                    if col_letter == k:
                        return print((g, v))
    return 'Not a Coordinate on the board'

print(get_row_col('c3'))


# Here is an example of how the exercise can be solved:
# def get_row_col(choice):
#     translate = {"A": 0, "B": 1, "C": 2}
#     letter = choice[0]
#     number = choice[1]
#     row = int(number) - 1
#     column = translate[letter]
#     return (row, column)
