def solution(skill, skill_trees):
    answer = 0
    # 가능한 스킬트리를 담는 리스트
    # ex) "CBD" -> "C", "CB", "CBD"
    possibleSkill = []
    
    for i in range(len(skill), -1, -1):
        possibleSkill.append(skill[:i])
    
    # 각 스킬트리에 skill에 있는 스킬을 제외하고 삭제
    for skill_tree in skill_trees:
        tmp = []
        for each in skill_tree:
            if each in skill:
                tmp.append(each)

        # 제외한 후, 가능한 스킬트리에 있다면 +1 (스킬 중복이 없기 때문에 가능)    
        if ''.join(tmp) in possibleSkill:
            answer += 1
    
    return answer