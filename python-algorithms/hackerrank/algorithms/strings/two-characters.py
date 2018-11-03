import collections

def removeDuplicatedLetters(s):
    """
    To remove consecutive same letters
    
    Arguments:
        s : original string

    Returns:
        newStr : a string that does not contains consecutive same letters
    
    """
    
    conseq_dupls = collections.Counter()
    
    newStr = ""

    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            conseq_dupls[s[i]] = 1
    for c in s:
        if conseq_dupls[c] is not 1:
            newStr += c
    return newStr


def isValid(s):
    """
    check valid composition of two character
    Arguments:
        s -- two character string
    Returns:
        valid -- boolean value to indicate valid string
    """
    return (len(removeDuplicatedLetters(removeDuplicatedLetters(s))) > 1)

def removeOthers(first, second, s):
    
    newStr = ""
    
    for c in s:
        if (c == first or c == second):
            newStr += c
    return newStr

def twoCharaters(s):
    # Complete this function
    s = removeDuplicatedLetters(s)
    ans = 0
    for first in s:
        for second in s:
            if first == second:
                continue
            else:
                selected = removeOthers(first, second, s)
                if isValid(selected):
                    ans = max(len(selected), ans)
    
    return ans
if __name__ == "__main__":
    l = int(input().strip())
    s = input().strip()
    result = twoCharaters(s)
    
    print(result)

