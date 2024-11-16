from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n, rows, cols = len(board), defaultdict(set), defaultdict(set)
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                # (i, j) == top-left cell of each 3 x 3 box
                box = set()
                for row in range(i, i + 3):
                    for col in range(j, j + 3):
                        num = board[row][col]
                        if not num.isdigit(): continue
                        if num in rows[row] or num in cols[col]: return False
                        if num in box: return False
                        rows[row].add(num)
                        cols[col].add(num)
                        box.add(num)
        return True