# 딕셔너리 활용
# 각 장르마다 1 ~ 2개의 노래를 베스트 앨범으로 출시
def solution(genres, plays):
    genreDict = {}
    sumDict = {}
    
    # 딕셔너리 2개에 각각 장르의 재생 횟수 총합과, 인덱스와 재생 횟수를 리스트 형식으로 넣기
    for i in range(len(genres)):
        if genres[i] in genreDict:
            genreDict[genres[i]].append([i, plays[i]])
            sumDict[genres[i]] += plays[i]
        else:
            genreDict[genres[i]] = [[i, plays[i]]]
            sumDict[genres[i]] = plays[i]
    
    # 장르의 재생 횟수를 내림차순 정렬
    # 각 장르의 재생 횟수 내림차순, 고유 번호 오름차순으로 정렬
    # answer에 1 ~ 2개의 노래 넣기
    answer = []
    for genre, sumVal in sorted(sumDict.items(), key = lambda x : x[1], reverse = True):
        genreDict[genre] = sorted(genreDict[genre], key = lambda x: (-x[1], x[0]))
        answer += [idx for (idx, play) in genreDict[genre][:2]]
            
    return answer