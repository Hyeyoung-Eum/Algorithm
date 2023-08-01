n,m=map(int, input().split())
original=[] #원래 체스판
count=[] #바뀐 체스판 개수

for _ in range(n):
    original.append(list(input()))

#a,b는 전체 체스판에서 자를 수 있는 범위의 시작점을 나타낸다.
#index1은 W로 시작할 경우 바뀐 체스 판의 갯수를 세기 위함
#index2는 B로 시작할 경우 바뀐 체스 판의 갯수를 세기 위함
for a in range(n-7):
    for b in range(m-7):
        index1 = 0
        index2 = 0

        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0: #행열의 번호의 합(i+j)가 짝수면, 시작점과 색이 같아야한다.
                    if original[i][j] != 'W':
                        index1 += 1
                    if original[i][j] != 'B':
                        index2 += 1
                else: #i+j의 합이 홀수인 경우, 시작점의 색과 반대의 경우
                    if original[i][j] != 'B':
                        index1 += 1
                    if original[i][j] != 'W':
                        index2 += 1
        count.append(min(index1, index2))
print(min(count))

#참고 블로그 : https://bambbang00.tistory.com/43
# num=(M-8)*(N-8)

# #인식할 수 있어야 함.

# num_list=[]
# for i in range(num):
#     for j in range(i+8): #시작점 지정
#         semi_matrix=matrix[j:j+8]
#     #시작점 옮겨가면서 8번만 계산해주면 됨.
#     num_list.append()
#     #그리고 최솟값 출력하면 됨

#종이에다가 그려보면서 풀어보기

#230723 새로운 풀이법 생각남



def wb_change(num):
    if num=='W':
        return 'B'
    else: #num=='B'
        return 'W'

start_point=list(original[0][0])[0]
cnt=0

print('start_point는', start_point)
#1)각 row들의 시작점을 먼저 결정해준다.
for i in range(0, n, 2):
    if start_point != original[i][0]:
        cnt+=1
        print(i,'번째 row[0] 변경', sep='')
        original[i][0] = start_point

    #index 초과 오류 해결코드
    index=i+1
    if index > n:
        index=i-2
        
    if start_point == original[index][0]:
        cnt+=1
        print(i+1,'번째 row[0] 변경', sep='')
        original[i+1][0] = wb_change(start_point)
#2)시작점을 기준으로 계산해준다.
for row in original:
    for i in range(m-1):
        if row[i] == row[i+1]:
            cnt+=1
            row[i+1]=wb_change(row[i+1])

#3) 결과 출력
for row in original:
    print(*row, sep='')
print(cnt)
#스타트 포인트에 따라서, 짝수행은 모두 같아야한다.
#for row in matrix[0:N:2]: