class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letterLogs = list(filter(lambda x: x.split()[1].isalpha(), logs))
        digitsLogs = list(filter(lambda x: x.split()[1].isnumeric(), logs))
        letterLogs = sorted(letterLogs, key=lambda x: x.split()[1:])
        
        return letterLogs + digitsLogs
