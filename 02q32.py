n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    c, r, d, s = map(int, input().split())
    graph[c].append((d, s-r))
layovers = [0] + list(map(int, input().split()))
distance = [float('inf')] * (n+1)
distance[1] = 0
q = [1]
updated = [True] * (n+1)

for _ in range(n+1):
    if not any(updated):
        break
    updated = [False] * (n+1)
    for u in q:
        for v, w in graph[u]:
            arrival_time = distance[u] + w + layovers[u]
            if arrival_time < distance[v]:
                distance[v] = arrival_time
                updated[v] = True
                if updated[v]:
                    q.append(v)

for i in range(1, n+1):
    if distance[i] == float('inf'):
        print("-1")
    else:
        print(distance[i])