from collections import deque


def difference(word1, word2):
    word2 = list(word2)
    for word in word1:
        if word in word2:
            del word2[word2.index(word)]
    return len(word2)


def solution(begin, target, words):
    if target not in words:
        return 0
    else:
        visited = [False for _ in range(len(words))]
        queue = deque([(begin, 0)])
        while queue:
            cash = queue.popleft()
            if cash[0] == target:
                return cash[1]
            for j in range(len(words)):
                diff = difference(cash[0], words[j])
                if diff == 1 and not visited[j]:
                    queue.append((words[j], cash[1] + 1))
                    visited[j] = True