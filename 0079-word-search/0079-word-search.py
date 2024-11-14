class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n

        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        def backtrack(row, col, seen, i):
            if len(word) == i:
                return True

            for dx, dy in directions:
                new_row, new_col = row + dy, col + dx
                if valid(new_row, new_col) and (new_row, new_col) not in seen:
                    if board[new_row][new_col] == word[i]:
                        seen.add((new_row, new_col))
                        if backtrack(new_row, new_col, seen, i + 1):
                            return True
                        seen.remove((new_row, new_col))
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                letter = board[row][col]
                if letter == word[0] and backtrack(row, col, {(row, col)}, 1):
                    return True
        return False