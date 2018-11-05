def permutations(word):
    if len(word) <= 1:
        return [word]
    perms = permutations(word[1:])
    c = word[0]
    result = []
    for perm in perms:
        for i in range(len(perm) + 1):
            result.append(perm[:i] + c + perm[i:])
    return result

if __name__ == '__main__':
    word = input('input a word ==> ')
    result = permutations(word)
    for line in result:
        print(line)
