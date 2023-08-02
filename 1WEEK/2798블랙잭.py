#브루트포스 알고리즘
#: 이론적으로 가능한 모든 경우의 수를 다 검색해보는 것
#: 중첩 FOR문으로, 시간복잡도가 엄청나다.

N,M=map(int, input().split())

card_list=list(map(int, input().split()))

result_list=[]
for i in card_list:
    for j in card_list:
        for k in card_list:
            sum=i+j+k
            if sum <=M:
                if (i!=j)and(i!=k)and(j!=k):
                    result_list.append(sum)

print(max(result_list))