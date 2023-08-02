#캠핑장은 연속하는 P일 중 L일만 사용 가능
#V일짜리 휴가 시작(V는 남은 휴가 일 수)
case=0
while(True): #if문이 만족될 때가지 무한 반복
    case +=1
    L, P, V = map(int, input().split())
    if L==0 and P==0 and V==0 : #모두 0이 들어오면 정지
        break
#L일 동안 연속 P일 중 휴가는 V일 짜리 
    n=0
    while(L<V): #남은 휴가일 수가, L보다 크면 
        if L<=P: #그리고 L이 P보다 작으면,
            n+=L
            V=V-P
    #남은 휴가 일 수 V가 L보다 작으면
    if L<=P:
        n+=V
    
    print(f'Case {case}: {n}')