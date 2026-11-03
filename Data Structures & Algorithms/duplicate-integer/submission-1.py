class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency = {}

        for number in nums:
            if number in frequency:
                frequency[number] += 1
            else:
                frequency[number] = 1

        for count in frequency.values():
            if count > 1:
                return True

        return False