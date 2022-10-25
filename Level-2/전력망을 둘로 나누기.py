def solution(n, wires):
    wires = list(set(map(tuple, wires)))
    answer = n
    
    for i in range(0, n-1):
        tree1 = set()
        tree1Cnt = 0
        tree2 = set()
        tree2Cnt = 0
        for wire in wires:
            if wire == wires[i]:
                continue
            if tree1 == set():
                tree1.add(wire[0])
                tree1.add(wire[1])
                tree1Cnt += 1
                continue
            if wire[0] in tree1 or wire[1] in tree1:
                tree1.add(wire[0])
                tree1.add(wire[1])
                tree1Cnt += 1
            else:
                tree2.add(wire[0])
                tree2.add(wire[1])
                tree2Cnt += 1
        if (abs(tree1Cnt - tree2Cnt) < answer):
            answer = abs(tree1Cnt - tree2Cnt)
    
    return answer

print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))