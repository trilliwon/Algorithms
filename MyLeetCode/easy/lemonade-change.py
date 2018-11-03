class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """

        changes = collections.Counter()
        for b in bills:
            if b == 20:
                if changes[10] > 0 and changes[5] > 0:
                    changes[10] -= 1
                    changes[5] -= 1
                elif changes[5] > 3:
                    changes[5] -= 3
                else:
                    return False
            elif b == 10:
                if changes[5] > 0:
                    changes[5] -= 1
                    changes[10] += 1
                else:
                    return False
            elif b == 5:
                changes[5] += 1
        return True
