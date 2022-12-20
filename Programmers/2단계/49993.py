def solution(skill, skill_trees):
    answer = 0
    for trees in skill_trees:
        right = True
        cash = skill
        for tree in list(trees):
            if tree in cash and tree != cash[0]:
                right = False
                break
            elif tree == cash[0]:
                if len(cash) == 1:
                    break
                cash = cash[1:]
        if right:
            answer += 1
    return answer
