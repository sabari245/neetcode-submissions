class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # horizontal case
        for i in range(9):
            row = set()
            for j in range(9):
                cell = board[i][j] 
                if cell != ".":
                    if cell in row:
                        return False
                    else:
                        row.add(cell)

        # vertical case
        for i in range(9):
            col = set()
            for j in range(9):
                cell = board[j][i] 
                if cell != ".":
                    if cell in col:
                        return False
                    else:
                        col.add(cell)
        # quadrant case
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                sqr = set()
                for i in range(3):
                    for j in range(3):
                        cell = board[x+i][y+j]
                        if cell != ".":
                            if cell in sqr:
                                return False
                            else:
                                sqr.add(cell)

        return True 