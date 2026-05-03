class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # h and v case
        for i in range(9):
            row = set()
            col = set()
            for j in range(9):
                rcell = board[i][j] 
                ccell = board[j][i]

                if rcell != ".":
                    if rcell in row: return False
                    row.add(rcell)

                if ccell != ".":
                    if ccell in col: return False
                    col.add(ccell)

        # square case
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