class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix)
        # c=len(matrix[0])
        '''
        1. make row changes [[x,y]], which hold the smallest and largest ele in each row
        2. check if target lies inbetween these ranges x<=target<=y
        3. if yes, the index is the row, and for the contents of that row, perform binary search
        '''
        row = -1
        u,d = 0,r-1
        while u<=d:
            mid = (u+d)//2
            if target>=matrix[mid][0] and target<=matrix[mid][-1]:
                row = mid
                break
            elif target<matrix[mid][0]:
                d = mid-1
            else:
                u = mid+1
        if row==-1:
            return False
        l,r = 0,len(matrix[0])-1
        while l<=r:
            mid = (l+r)//2
            if target == matrix[row][mid]:
                return True
            elif target>matrix[row][mid]:
                l = mid+1
            else:
                r = mid-1
        return False

        # while r<len(matrix) and c<len(matrix[0]):
        #     mr=
        #     if matrix[r][c]==target:
        #         return True
        # return False
        