class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check row
        for row in board:
            items = set()
            for i in row:
                if i in items and i != ".":
                    return False
                else:
                    items.add(i)
        
        # check col
        idx = 0
        for _ in board:
            items = set()
            for row in board:
                i = row[idx]
                
                if i in items and i != ".":
                    return False
                else:
                    items.add(i)
            idx +=1
            
        
        # converting each box into single array
        conv = [[] for i in range(9)]
        pos = 0
        for i in range(9):
            
            if i == 3:
                pos = 3
            elif i == 6:
                pos = 6
            
            rowX, rowY = 0, 3
            for j in range(3):
                
                this= board[i][rowX:rowY]
                # print(pos + j,i, rowX, rowY, this)

                conv[pos + j] = [*conv[pos + j], *this]
                              
                if rowY == 9:
                    break

                rowX, rowY = rowY, rowY + 3
       
    # checking duplicate in array box 
        for row in conv:
            items = set()
            for i in row:
                if i in items and i != ".":
                    return False
                else:
                    items.add(i)
                
        return True
                
            
            
            
            
        