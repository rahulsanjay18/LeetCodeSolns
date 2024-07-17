from heapq import heappop, heappush, heapify

class Solution(object):
    def minimumCost(self, m, n, horizontalCut, verticalCut):
        """
        :type m: int
        :type n: int
        :type horizontalCut: List[int]
        :type verticalCut: List[int]
        :rtype: int
        """
        if m == 1:
            return sum(verticalCut)
        elif n == 1:
            return sum(horizontalCut)
        
        # print(horizontalCut)
        # print(verticalCut)
        # print()
        ans = 0

        horizontalCut = [-1 * i for i in horizontalCut]
        verticalCut = [-1 * i for i in verticalCut]

        heapify(horizontalCut)
        heapify(verticalCut)

        while len(horizontalCut) != 0 and len(verticalCut) != 0:
            # print(horizontalCut)
            # print(verticalCut)
            # print()
            if horizontalCut[0] < verticalCut[0]:
                ans += heappop(horizontalCut)
                ans += sum(verticalCut)
            else:
                ans += heappop(verticalCut)
                ans += sum(horizontalCut)

        if len(horizontalCut) != 0:
            ans += sum(horizontalCut)
        elif  len(verticalCut) != 0:
            ans += sum(verticalCut)

        return -ans