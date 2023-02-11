class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for b in board:
            print(b)
        # check row
        for i in range(9):
            filled = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in filled:
                    return False
                else:
                    filled.add(board[i][j])
        # check col
        for i in range(9):
            filled = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in filled:
                    return False
                else:
                    filled.add(board[j][i])
        # check sub-box
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                filled = set()
                for m in range(3):
                    for n in range(3):
                        if board[i+m][j+n] == ".":
                            continue
                        if board[i+m][j+n] in filled:
                            return False
                        else:
                            filled.add(board[i+m][j+n])
        return True
