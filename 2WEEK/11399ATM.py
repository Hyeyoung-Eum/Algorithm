N=int(input())
time_list=list(map(int, input().split()))
sum=0
i=0
time_list.sort()
for time in time_list:
    # print('time=',time,'N-i=',N-i)
    sum+=((N-i)*time)
    i+=1

print(sum)