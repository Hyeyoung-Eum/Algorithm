#Selection Sort, O(n^2)
#앞에서부터, 특정 조건을 만족시키는 값을 찾아, 맨 앞과 바꿔준다.

def swap(n1, n2):
    return n2, n1

n=int(input())
d=[int(input()) for _ in range(n)]

for i in range(n): #인덱스 번호 자리 i
    tmp= i
    for j in range(i+1, n): #i의 뒤에 있는 애들만 비교를 할 것이다.
        if d[tmp] > d[j]: #만약 인덱스 j가 더 작다면,
            tmp = j #최솟값을 가지는 인덱스 픽
    d[tmp], d[i] = swap(d[tmp], d[i]) #특정 자리와, 최솟값을 자리를 바꾼다.
    print(*d)
