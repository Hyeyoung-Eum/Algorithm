INF=int(1e9)

n=int(input())
m=int(input())

graph = [ [INF] * (n+1) for _ in range(n+1)] #무한의 큰 숫자를 n+1개 집어넣은 리스트가 n=1줄
#무한의 행렬이 만들어져있다.

def print_all(): #전체 다, 출력하세요
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == INF:
                print("oo", end =" ")
            else:
                print(graph[i][j], end=" ")
        print()

for a in range(1, n+1): #출발지와 도착지 같은 것으 0
    graph[a][a]=0

for _ in range(m):#몇 개의 행? a행 b=열의 값을 c로 바꾼다.
    a, b, c = map(int, input().split())
    graph[a][b] = c

print_all()
for k in range(1, n+1):
    print()
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])
    print_all()