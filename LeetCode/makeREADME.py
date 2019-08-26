
"""
File name should be part of leetcode url of problem
"""

import os 

filelist = []

emh = ['easy', 'medium', 'hard']

extensions = set(['.py', '.cpp', '.swift', '.java'])
dirs = {} 
existDirs = []

for filename in os.listdir('.'):
    if os.path.isdir(filename):
        existDirs.append(filename)    

isPy = lambda fn : os.path.splitext(fn)[-1] in extensions

for dirName in existDirs:
    pyfiles = list(filter(isPy, os.listdir(dirName)))
    if len(pyfiles) != 0:
        dirs[dirName] = sorted(pyfiles)

with open('README.md', 'w') as f:
    f.write('# My codes for LeetCode\n') 

githubRepoURL = 'https://github.com/trilliwon/Algorithms/blob/master/LeetCode/'
leetcodeProbURL = 'https://leetcode.com/problems/'

with open('README.md', 'a') as f:
    dirNames = emh + sorted(list(filter(lambda d: not(d in set(emh)), dirs.keys())))

    for dirName in dirNames:
        line = '- [' + dirName.upper() + '](#' + dirName + ')\n'
        f.write(line)
    f.write('\n---\n')

    for dirName in dirNames:
        f.write('\n## ' + dirName.upper() + '\n') 
        for x in dirs[dirName]:
            n, e = os.path.splitext(x)
            solURL = ' **[[' + e + '](' + githubRepoURL + dirName + '/' + x + ')]**'
            line = '- [' + n.upper() + '](' + leetcodeProbURL + n + ')  ' + solURL + '\n'

            f.write(line)

