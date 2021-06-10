from collections import deque

def solution(bridge_length, weight, truck_weights):
    q = deque([0] * bridge_length)
    idx = 0
    time = 0
    sum = 0
    
    while q:
        sum -= q.popleft()
        if idx < len(truck_weights):
            if len(q) < bridge_length and sum + truck_weights[idx] <= weight:
                q.append(truck_weights[idx])
                sum += truck_weights[idx]
                idx += 1
            elif len(q) < bridge_length and sum + truck_weights[idx] > weight:
                q.append(0)
        time += 1
    return time

print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10, 20, 30]))