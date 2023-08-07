import sys
from collections import deque

input=sys.stdin.readline
 #python의 재귀 최대 깊이 기본 설정이 1,000회이기 때문에 런타임 에러가 발생하거나 오류가 나는 경우가 있다.
 #이것을 방지하기 위해서 반드시,  재귀 최대 깊이를 10**6으로 바꿔줘야한다.
 #단 PyPy에서는 임의로 재귀 최대 깊이 설정이 불가능하다.
sys.setrecursionlimit(10 **6)

def bfs(x, y):
    visited[x][y] = 1 #방문했으면 1로 바꿔준다.
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        dxdy = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for dx, dy in dxdy: #상하좌우 처리
            nx = x + dx
            ny = y + dy
            if -1 < nx < n and -1 < ny < n:
                if grid[nx][ny] == grid[x][y] and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

n=int(input())
grid = [list(map(str, input().strip())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)] #0으로 채운 grid 생성

ncw = 0 #색약x
for i in range(n):
    for j in range(n):
        if not visited[i][j]: #visited[i][j]가 0이면 = 아직 방문 안했으면
            bfs(i, j)
            ncw+= 1
print(ncw, end=' ')

cw = 0 #색약
visited = [[0 for _ in range(n)] for _ in range(n)]

#R을 G로 바꿔줍니다.
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'R':
            grid[i][j] = 'G' 

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cw +=1
print(cw)


#####열심히 시도했던 흔적#####
# n=int(input())
# matrix=[list(input()) for _ in range(n)]

# #1.각 자리 번호에 따른 인덱스 값을 받았다. (행 구분은 없음)
# graph=dict()
# idx=0
# for row in matrix:
#     for i in row:
#         graph[idx]=i
#         idx+=1

# print(matrix)
# print(graph)


# #2.상하좌우의 인접한 인덱스 숫자를 dict으로 나타냈다.
# G=dict() #G는 인접 인덱스 관계도
# #key는 matrix에서의 ij값.
# #value는 graph에서 idx번호
# for i in range(n):
#     for j in range(n):
#         append_list=[]
#         #상
#         if i-1>=0:
#             # A=graph[i-1][j]
#             append_list.append((i-1)*n+j)
#         #하
#         if i+1<=n-1:
#             # B=graph[i+1][j]
#             append_list.append((i+1)*n+j)
#         #좌
#         if j-1>=0:
#             # C=graph[i][j-1]
#             append_list.append(i*n+j-1)
#         #우
#         if j+1<=n-1:
#             # D=graph[i][j+1]
#             append_list.append(i*n+j+1)
        
#         G[str(i)+str(j)]=append_list
# print(G)


# visit_idx=list()
# # # start_node를 값으로 할 수 있게 한다.
# def DFS(g, i, j): #g는 G, i, j는 각각 graph의 인덱스 번호
#     visit_idx.append(str(i)+str(j)) #방문한 idx
#     for each_idx in g[str(i)+str(j)]: #시작 idx의 인접한 idx 번호를 리스트로 가지고 와서,
#         if (each_idx in visit_idx) == False: #방문하지 않았으면
#             if matrix[each_idx[0]][each_idx[1]]==matrix[i][j]: #그리고 색이 같으면
#                 DFS(g, each_idx)

# DFS(G,0,0)
# print(visit_idx)
# #[]는 통으로 list로 감싸주는거고, list()는 안에 것을 쪼개면서 감싸준다.
