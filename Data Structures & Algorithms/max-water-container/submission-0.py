class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        final_area=0
        area=0
        while(l!=r):
            x = min(height[l],height[r])
            area = (r-l)*x
            final_area = max(area,final_area)
            if(height[l]>height[r]):
                r=r-1
            else:
                l=l+1
                
            
        return final_area
        