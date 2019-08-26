class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        ab = "abcdefghijklmnopqrstuvwxyz"
        abdict = { ab[i]:morse[i] for i in range(26) }
        morseCatDict = {}
        
        for w in words:
            morseWord = []
            for c in w:
                morseWord.append(abdict[c])
            morseWord = "".join(morseWord)
            morseCatDict[morseWord] = 1
            
        return len(morseCatDict)
