#오름차순 정렬

n = int(input())
d = [int(input()) for _ in range(n)]
print(d)
for i in range(n):
    for j in range(n):
        if d[i] < d[j]: #맨 마지막 경우는 4<5비교 임.
            print('i=',i,'d[i]=',d[i],'j=',j,'d[j]=',d[j],end=' ')
            d[i], d[j] = d[j], d[i]
            print('d=',d)
        else:
            print('i=',i,'d[i]=',d[i],'j=',j,'d[j]=',d[j], 'pass')

print(d)
###
#d=[3,2,1]

#i=0, j=0 #3>3
#i=0, j=1 #3>2, change
    #d=[2,3,1]
#i=0, j=2 #3>1, change
    #d=[2,1,3]

#i=1, j=0 #1>2, pass
#i=1, j=1 #2>2, pass
#i=1, j=2 #2>3, pass

#i=2, j=0 #3>2, change 0번자리 확정남
    #d=[3,1,2]
#i=2, j=1 #2>1, change 1번자리, 2번자리 확정남
    #d=[3,2,1]