#플러그 빼는 횟수를 최소화하는 방법
    #꽂혀있는 플러그 중 어떤 것을 제거하느냐가 관건

#input
N, K = map(int, input().split())
order_list=list(map(int, input().split()))

###계산 원리###
#처음 N개는 그냥 받을 수 있음 -> 집합 형태 같음. 같은 원소는 상관없이 받음.
#N개를 넘어갈 때는 플러그 빼는 연산 실행
    #어떤 플러그를 제거할 것인지 연산 실행

#연산 시작
# print('연산 시작합니다')
multitap_set=set() #꽂혀있는 멀티탭
rst=0

for _ in range(K):
    multitap_list=list(multitap_set)
    #멀티탭이 꽉차지 않았다면
    if len(multitap_set)<N:
        print('멀티탭 채우기 실행')
        multitap_set.add(order_list[0])
        del order_list[0]
    
    #멀티탭이 꽉찬 순간부터
    elif len(multitap_set)==N:
        print('멀티탭 새로 채우기 실행')
        #order_list[0]가 꽂혀있는 플러그라면
        if order_list[0] in multitap_set:
            print('선택한 order_list[0]:', order_list[0])
            # multitap_set.add(order_list[0])
            order_list.remove(order_list[0])
            del order_list[0]
            print('남은 order_list:',order_list)
            print('multitap_set현황:',multitap_set)
            print()

        #order_list[0]가 꽂혀있는 플러그가 아니라면
        elif order_list[0] not in multitap_set: #멀티탭에 꽂혀있지 않으면
            print('선택한 order_list[0]:', order_list[0])
            
            #가장 중요한 연산 부분
            #order_list에서 가장 적게 들어있는 코드를 뽑습니다

            #멀티탭 요소들 중 하나라도 없는 것이 발견되면 그것을 제거하고 그 곳에 꽂는다.
            #제거 1순위 : 뒤에 더이상 나오지 않는 콘센트
            tf=False
            multitap_list=list(multitap_set)
            
            for j in multitap_list:
                if j not in order_list: 
                    del multitap_list[multitap_list.index(j)]
                    multitap_set.add(order_list[0])
                    order_list.remove(order_list[0])
                    rst+=1
                    tf=True
                    print('multitap_set:', multitap_set)
                    print('multitap_list:',multitap_list)
                    break
            
            if tf==False:
                #제거 2순위 : 뒤쪽에 나오는 콘센트
                find_list=[]
                for j in multitap_list:
                    find_list.append(order_list.index(j))
                    #집합 요소별로 등장 인덱스를 기록. 그리고 가장 늦은 애(max) 제거
                    #max(find_list)를 인덱스로 가지는 값을 order_list에서 찾고, 그 값을 가지는 수를 멀티탭에서 제거
                multitap_set.remove(order_list[max(find_list)])
                multitap_set.add(order_list[0])
                order_list.remove(order_list[0])
                rst+=1 
                print('multitap_set:', multitap_set)
                print('multitap_list:',multitap_list)
                

                    # ##가장 적게 쓰인 수 제거하는 코드
                    # cnt_list=[]
                    # cnt_list.append(order_list.count(j))
                    # print('cnt_list:',cnt_list)

                    # multitap_list.remove(multitap_list[cnt_list.index(min(cnt_list))])
                    # multitap_set=set(multitap_list)
                    # rst+=1
                    # multitap_set.add(order_list[0])
                    # order_list.remove(order_list[0])
                    # print(order_list)
                    # print(multitap_set)
                    # print('현재rst:',rst)
                    # print()
        #(만약 집합의 수가 3개가 되었으면 4번째 부터는
            #안에 있는 것과 같으면 그냥 넣기
            #다른게 나오면 집합 안에 있는 것들을 뒤에 남은 것에서 새서 이용수가 가장 적은 것 뽑기
print(rst)


#알게된 set 특징
#인덱싱 X
#in으로 들어있는지 T/F출력 가능