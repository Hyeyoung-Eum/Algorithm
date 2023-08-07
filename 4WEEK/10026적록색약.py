n=int(input())
graph=[]
idx=0
#각 자리에 번호 idx를 매겨주면서 받았다.
for _ in range(n):
    row=[]
    for i in list(input()):
        row.append((idx,i))
        idx+=1
    graph.append(row)
print(graph)

G=dict()
#상하좌우의 인덱스 값 넣어줬음
for i in range(n):
    for j in range(n):
        append_list=[]
        #상
        if i-1>=0:
            A=graph[i-1][j]
            append_list.append(A[0])
        #하
        if i+1<=n-1:
            B=graph[i+1][j]
            append_list.append(B[0])
        #좌
        if j-1>=0:
            C=graph[i][j-1]
            append_list.append(C[0])
        #우
        if j+1<=n-1:
            D=graph[i][j+1]
            append_list.append(D[0])
        
        G[graph[i][j][0]]=append_list


print(G)

visit_idx=list()
# start_node를 값으로 할 수 있게 한다.

def DFS(g, start_idx): #g는 G, start_idx에는 0넣을 예정
    visit_idx.append(start_idx) #방문한 idx
    ㅑ

    for each_idx in g[start_idx]: #시작 idx의 인접한 idx 번호를 리스트로 가지고 와서,
        for node in graph: #전체 graph에서
            if node[0] == each_idx: #해당 인덱스 번호를 찾으면,
                if node[1] == 
                

        if (each_idx in visit) == False: #방문하지 않았으면
            
            DFS(g, each_idx)

# if A == graph[i][j]:



#[]는 통으로 list로 감싸주는거고, list()는 안에 것을 쪼개면서 감싸준다.
