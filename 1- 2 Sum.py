class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}

        for index, number in enumerate(nums):
            complement = target - number
            if complement in found:
                return [found[complement], index]
            
            found[number] = index
        return []