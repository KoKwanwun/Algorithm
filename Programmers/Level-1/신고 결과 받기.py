def solution(id_list, report, k):
    report = list(set(report))
    report0_list = []
    report1_list = []

    # 신고 받은 사람을 report1_list에 저장
    for i in range(len(report)):
        mlist = report[i].split()
        report1_list.append(mlist[1])
    
    # 신고를 k이상으로 받은 사람을 리스트화(정지당한 사람들)
    bad = [ id_list[i] for i in range(len(id_list)) if report1_list.count(id_list[i]) >= k ]

    # 다시 report를 돌면서 자신이 신고한 사람이 정지당했으면 신고한 사람을 리스트에 추가
    for i in range(len(report)):
        mlist = report[i].split()
        
        if mlist[1] in bad:
            report0_list.append(mlist[0])
            
    # id_list를 돌면서 정지를 성공시킨 횟수를 리스트화 하여 출력
    result = [ report0_list.count(id_list[i]) for i in range(len(id_list)) ]
    
    return result