class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        class DuplicateException(Exception):
            pass

        try:
            def check_add(i, nums):
                if i != "." and i in nums:
                    raise DuplicateException
                if i != ".":
                    nums.add(i)
                

            for col in board:
                nums = set()
                for num in col:
                    check_add(num, nums)
                    
            for i in range(9):
                nums = set()
                for row in board:
                    num = row[i]
                    check_add(num, nums)
            
            nums = [
                [set(),set(),set()],
                [set(),set(),set()],
                [set(),set(),set()]
            ] 

            def curr_block(row, col):
                i = row // 3
                j = col // 3
                return nums[i][j]

            for i, row in enumerate(board):
                for j, num in enumerate(row):

                    block = curr_block(i, j)
                    check_add(num, block)

        except DuplicateException:
            return False

        return True
