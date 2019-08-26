


class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(['a', 'e', 'i', 'o', 'u']) # 'a' in vowels
        
        # ** Should ask
        #   - upper or lower case
        
        lst = list(s)
        
        i = 0
        j = len(s) - 1

        while i < j:  # base case
            if not (lst[i].lower() in vowels):
                i += 1
            
            if not (lst[j].lower() in vowels):
                j -= 1
            
            if lst[i].lower() in vowels and lst[j].lower() in vowels:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1        

        return ''.join(lst)
