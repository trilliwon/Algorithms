class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """

        adic = collections.Counter()
        l = len(A[0])
        for a in A:
            evenA = sorted([a[c] for c in range(0, l, 2)])
            oddA = sorted([a[c] for c in range(1, l, 2)])
            a = ''.join([evenA[i//2] if i % 2 == 0 else oddA[i//2] for i in range(len(a))])
            adic[a] += 1
        return len(adic)
