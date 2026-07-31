class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for j in range(9):
            vr = set()
            for i in board[j]:
                if i.isnumeric():
                    if i not in vr:
                        vr.add(i)
                    else:
                        return False
            vc = set()
            for k in range(9):
                if board[k][j].isnumeric():
                    if board[k][j] not in vc:
                        vc.add(board[k][j])
                    else:
                        return False
        """
        00 01 02   03 04 05
        10 11 12   13 14 15
        20 21 22   23 24 25 
        """
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = set()
                for row in range(3):
                    for col in range(3):
                        if board[row+box_row][col+box_col].isnumeric():
                            if board[row+box_row][col+box_col] not in box:
                                box.add(board[row+box_row][col+box_col])
                            else:
                                return False
        return True
            

        