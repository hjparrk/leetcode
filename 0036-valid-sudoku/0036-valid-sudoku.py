from collections import defaultdict
from pprint import pprint
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rows, cols = defaultdict(set), defaultdict(set)
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                cell = set()
                for row in range(i, i + 3):
                    for col in range(j, j + 3):
                        num = board[row][col]
                        if not num.isdigit(): continue
                        if num in rows[row] or num in cols[col]: return False
                        if num in cell: return False
                        rows[row].add(num)
                        cols[col].add(num)
                        cell.add(num)
        return True