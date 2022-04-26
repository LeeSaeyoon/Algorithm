## 구간합
"""
- 𝑁개의 정수로 구성된 수열이 있다
- 𝑀개의 쿼리(Query)정보가 주어진다
    - 각 쿼리는 𝐿𝑒𝑓𝑡와 𝑅𝑖𝑔ℎ𝑡으로 구성된다
    - 각 쿼리에 대하여 [𝐿𝑒𝑓𝑡,𝑅𝑖𝑔ℎ𝑡] 구간에 포함된 데이터들의 합을 출력해야 한다
- 수행 시간 제한은 ***O(N + M)*** 이다
"""

# 아이디어
# 접두사의 합을 미리 구해두기
# - 접두사 합(Prefix Sum): 배열의 맨 앞부터 특정 위치까지의 합을 미리 구해 놓은 것
# - 𝑁개의 수 위치 각각에 대하여 접두사 합을 계산하여 𝑃에 저장한다
# - 매 𝑀개의 쿼리 정보를 확인할 때 구간 합은 𝑃[𝑅𝑖𝑔ℎ𝑡] - 𝑃[𝐿𝑒𝑓𝑡 - 1]이다

def solution(n, lst, left, right):
    sum_value = 0
    prefix_sum = [0]
    
    for i in lst:
        sum_value += i
        prefix_sum.append(sum_value)
        
    # 구간 합 계산
    return prefix_sum[right] - prefix_sum[left - 1]


if __name__ == '__main__':
    print(solution(5, [10, 20, 30, 40, 50], 3, 4)) # 70
