class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        
        emails = list(map(lambda x: x.split('@'), emails))
        emails = list(map(lambda x: (''.join(x[0].split('.')[0:]), x[1]), emails))
        emails = list(map(lambda x: x[0].split('+')[0] + '@' + x[1], emails))
        return len(collections.Counter(emails))
