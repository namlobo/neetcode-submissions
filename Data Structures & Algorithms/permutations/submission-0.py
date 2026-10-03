class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path, used):
            # We have used every number
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                # Don't use the same element twice
                if used[i]:
                    continue

                path.append(nums[i])
                used[i] = True

                backtrack(path, used)

                # Undo the choice
                path.pop()
                used[i] = False

        backtrack([], [False] * len(nums))
        return result