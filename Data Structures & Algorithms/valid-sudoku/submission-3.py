from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for col in range(9):
                current_value = board[row][col]
                
                if current_value == ".":
                    continue
                
                if current_value in rows[row]:
                    return False
                
                if current_value in cols[col]:
                    return False
                
                box = (row // 3, col // 3)
                if current_value in boxes[box]:
                    return False
                
                rows[row].add(current_value)
                cols[col].add(current_value)
                boxes[box].add(current_value)
        return True