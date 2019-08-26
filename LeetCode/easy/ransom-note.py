class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        ransomNoteCount = collections.Counter()
        magazineCount = collections.Counter()

        for c in ransomNote:
            ransomNoteCount[c] += 1

        for c in magazine:
            magazineCount[c] += 1
            
        for k, v in ransomNoteCount.items():
            if magazineCount[k] < v:

                return False
        return True
        
