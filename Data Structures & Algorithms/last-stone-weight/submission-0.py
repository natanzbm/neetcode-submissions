class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()

            y = stones.pop()
            x = stones.pop()

            if y != x:
                stones.append (y - x)

        if len(stones) == 1:
            return stones[0]

        return 0
        