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

        sVert = sum(verticalCut)
        sHor = sum(horizontalCut)

        while len(horizontalCut) != 0 and len(verticalCut) != 0:
            # print(horizontalCut)
            # print(verticalCut)
            # print()
            if horizontalCut[0] < verticalCut[0]:
                p = heappop(horizontalCut)
                sHor -= p
                ans += p
                ans += sVert
            else:
                p = heappop(verticalCut)
                sVert -= p
                ans += p
                ans += sHor

        if len(horizontalCut) != 0:
            ans += sHor
        elif  len(verticalCut) != 0:
            ans += sVert

        return -ans