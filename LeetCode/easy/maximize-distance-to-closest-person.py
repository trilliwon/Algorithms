class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        
        """
        [1,0,0,0,1,0,1]
           ^   ^   ^
        
        """
        a = 0
        b = 0

        running = False
        
        m = 0

        for i, seat in enumerate(seats):
            if seat == 0 and not running:
                a = i
                running = True
            
            if seat == 1 and i != 0 and running:
                b = i - 1
                running = False
                if a == 0:
                    m = b-a
                else:
                    if m < (b - a)//2:
                        m = (b - a)//2
            
            if seat == 0 and i == len(seats) - 1 and running:
                b = i
                if m < b - a:
                    m = b-a
        return m + 1
