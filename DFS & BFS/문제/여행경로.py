## 여행경로
"""
* 문제
주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.
항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 
방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

* 제한사항
모든 공항은 알파벳 대문자 3글자로 이루어집니다.
주어진 공항 수는 3개 이상 10,000개 이하입니다.
tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
주어진 항공권은 모두 사용해야 합니다.
만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
"""

# 아이디어
# DFS로 경로 탐색

from collections import defaultdict

# 재귀
def solution(tickets):
    graph = defaultdict(list)
    # 어휘순으로 방문해야 하므로 그래프를 정렬
    for i, j in sorted(tickets, reverse=True):
        graph[i].append(j)

    def dfs(x):
        while graph[x]:
            dfs(graph[x].pop())
        result.append(x)

    result = []
    dfs("ICN")

    return result[::-1]

# stack
def solution2(tickets):
    graph = defaultdict(list)
    # 어휘순으로 방문해야 하므로 그래프를 정렬
    for i, j in sorted(tickets, reverse=True):
        graph[i].append(j)

    stack = ["ICN"]
    result = []
    while stack:
        top = stack[-1]
        if top not in graph or not graph[top]:
            result.append(stack.pop())
        else:
            stack.append(graph[top].pop())

    return result[::-1]


if __name__ == '__main__':
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])) # ["ICN", "JFK", "HND", "IAD"]
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])) # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
    print(solution2([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])) # ["ICN", "JFK", "HND", "IAD"]
    print(solution2([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])) # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
