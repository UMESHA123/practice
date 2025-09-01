def solve(board):
    def checkBox(board, i, j):
        check_value = board[i][j]
   
        start =  0 
        end = 0
        temp = 0
        new_temp = 0
        if i < 3:
            start = 0
            new_temp = 3
        elif i >= 3 and i < 6:
            start = 3
            new_temp = 6
        else:
            start = 6
            new_temp = 9
        
        if j < 3:
            temp = 0
            end = 3
        elif j>=3 and j < 6:
            temp = 3
            end = 6
        else:
            temp = 6
            end = 9

        for row in range(start, new_temp):
            for col in range(temp, end):
                if row == i and col == j:
                    continue
                if board[row][col] == '.':
                    continue
                if board[row][col] == check_value:
                    return True
        return False
            
    def checkRow(board, i, j):
        check_value = board[i][j]
        for col in range(9):
            if board[i][col] == ".":
                continue
            if col != j and board[i][col] == check_value:
                return True
        return False
            
    def checkCol(board, i, j):
        check_value = board[i][j]
        for row in range(9):
            if board[row][j] == '.':
                continue
            if row != i and board[row][j] == check_value:
                return True
        return False

    for i in range(len(board)):
        for j in range(len(board[0])):
            box_res = checkBox(board, i, j)
            if box_res:
                return False
            row_res = checkRow(board, i, j)
            if row_res:
                return False
            col_res = checkCol(board, i, j)
            if col_res:
                return False
    return True

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

res = solve(board)
print(res)