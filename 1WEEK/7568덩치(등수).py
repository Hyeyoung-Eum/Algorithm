N=int(input()) #전체 사람의 수 N

### 1.직관적으로, 키와 몸무게를 따로 받음 ###
# x_list=[] #키 x를 담을 리스트 생성
# y_list=[] #몸무게 y를 담을 리스트 생성
# for _ in range(N):
#     x, y = map(int, input().split()) #키 x와 몸무게 y를 입력 받는다
#     x_list.append(x) #리스트에 키 x추가
#     y_list.append(y) #리스트에 몸무게 y추가


# rank_list=[] #rank들을 담을 리스트 생성
# for i in range(N): #기준값 i
#     rank=1 #(덩치가 더 큰 사람의 수 + 1)이 결국 등수이므로 미리 1로 설정, 초기화 역할도 함
#     for j in range(N): #비교하고자 하는 대상 값 j
#         if (x_list[j]>x_list[i]) and (y_list[j]>y_list[i]): #i를 기준으로, i 인덱스 보다 j인덱스의 값이 더 큰 경우! 이므로 둘의 순서 주의하기
#             rank+=1 #if문 만족 시 rank를 1씩 더해줌
#     rank_list.append(rank)

# print(*rank_list)

### 2. 키와 몸무게를 튜플로 받는 방법 ###
student_list=[]
for _ in range(N):
    x, y = map(int, input().split()) #키 x와 몸무게 y를 입력 받는다
    student_list.append((x, y)) #이렇게 튜플로 받아도 됨


rank_list=[] #rank들을 담을 리스트 생성
for i in student_list: #기준값 i
    rank=1 #(덩치가 더 큰 사람의 수 + 1)이 결국 등수이므로 미리 1로 설정, 초기화 역할도 함
    for j in student_list: #비교하고자 하는 대상 값 j
        if (j[0]>i[0]) and (j[1]>i[1]): #i를 기준으로, i 인덱스 보다 j인덱스의 값이 더 큰 경우! 이므로 둘의 순서 주의하기
            rank+=1 #if문 만족 시 rank를 1씩 더해줌
    rank_list.append(rank)
print(*rank_list) # 별을 이용하여 리스트의 요소들만 출력