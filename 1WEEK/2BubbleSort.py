#BubbleSort O(n^2)
#매번 연속된 두 개의 값을 비교하여, 정한 기준의 값을 뒤로 넘겨준다.
#뒤에서부터 하나씩 결정된다.

def swap(n1, n2):
    return n2, n1

n=int(input())
d=[int(input()) for _ in range(n)]

for i in range(n): #실행횟수
    for j in range(1, n): #n-1개의 j, 그리고 j의 인덱스 번호는 수가 아닌 자리를 의미한.
        if d[j-1] > d[j] : #연속된 수를 의미하기 위해서, i가 아닌 j-1과 j로 표기
            d[j-1], d[j] = swap(d[j-1], d[j])
    print(*d)