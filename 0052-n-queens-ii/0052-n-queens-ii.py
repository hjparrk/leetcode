class Solution:
    def totalNQueens(self, n):
        # 현재 row 기준으로 위쪽만 체크하는 걸로 수정
        def col_attacked(queens, position):
            _, col = position
            for queen in queens:
                _, queen_col = queen
                if col == queen_col:
                    return True
            return False
        
        def row_attacked(queens, position):
            row, _ = position
            for queen in queens:
                queen_row, _ = queen
                if row == queen_row:
                    return True
            return False
        
        def diagonal_attacked(queens, position):
            row, col = position
            for queen in queens:
                queen_row, queen_col = queen
                if queen_row + queen_col == row + col or\
                queen_row - queen_col == row - col:
                    return True
            return False

        def attacked(queens, position):
            if col_attacked(queens, position):
                return True
            if row_attacked(queens, position):
                return True
            if diagonal_attacked(queens, position):
                return True
            return False

        
        def backtrack(queens, row):
            if row == n:
                return 1

            ans = 0
            for col in range(n):
                position = (row, col)
                if not attacked(queens, position):
                    queens.add(position)
                    ans += backtrack(queens, row + 1)
                    queens.remove(position)
            return ans
        
        return backtrack(set(), 0)