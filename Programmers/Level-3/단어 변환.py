from collections import deque

def compareWord(word1, word2):
    differentCnt = 0

    for i in range(len(word1)):
        if (word1[i] != word2[i]):
            differentCnt += 1
    
    return differentCnt


def solution(begin, target, words):
    wordCheck = [0] * len(words)

    queue = deque()
    queue.append(begin)
    
    if (target in words):
        while queue:
            word = queue.popleft()

            for i in range(len(words)):
                if (wordCheck[i] == 0 and compareWord(word, words[i]) == 1):
                    if (word == begin):
                        wordCheck[i] = 1
                        queue.append(words[i])
                    else:
                        wordCheck[i] = wordCheck[words.index(word)] + 1
                        queue.append(words[i])
    
        return wordCheck[words.index(target)]
    else:
        return 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))