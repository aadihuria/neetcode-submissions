class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        count = [0,0,0]
        for n in nums:
            count[n] += 1
        # count = [1,2,1]
        index = 0
        for i in range(3):
            # 
            while count[i]:
                count[i] -= 1
                # count = [0,1,1]
                nums[index] = i
                # nums[0, 1, 1, 2]
                index += 1

            
        