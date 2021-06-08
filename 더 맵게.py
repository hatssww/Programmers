import heapq as hq

def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)
    while True:
        min_scoville = hq.heappop(scoville)
        if min_scoville >= K:
            return answer
        if len(scoville) == 0 and min_scoville < K:
            return -1
        sec_scoville = hq.heappop(scoville)
        new = min_scoville + sec_scoville * 2
        hq.heappush(scoville, new)
        answer += 1

print(solution([1, 2, 3, 9, 10, 12], 7))