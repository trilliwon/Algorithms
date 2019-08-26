class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        """

        Input: "I speak Goat Latin"
        Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
        """
        
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        S = S.split()
        for index in range(len(S)):
            
            if S[index][0].lower() in vowels:
                S[index] += 'ma'
            else:
                S[index] = S[index][1:] + S[index][0] +'ma'
            
            a = ''.join(['a' for _ in range(index+1)])
            S[index] += a
        
        return ' '.join(S)
