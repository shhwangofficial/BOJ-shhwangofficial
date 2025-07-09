import sys

INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정
for _ in range(int(sys.stdin.readline())):

    # 노드의 개수 및 간선의 개수를 입력받기
    n, m, w = map(int, sys.stdin.readline().split())
    # 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0

    # 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
    for k in range(m):
        # A에서 B로 가는 비용은 C라고 설정
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a][b] = min(graph[a][b], c)
        graph[b][a] = min(graph[b][a], c)

    for k in range(w):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a][b] = min(graph[a][b], -c)

    # 점화식에 따라 플로이드 워셜 알고리즘을 수행
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    # 수행된 결과를 출력
    flag = 0
    for a in range(1, n + 1):
        if graph[a][a] < 0:
            flag = 1
            break
    if flag:
        print("YES")
    else:
        print("NO")
