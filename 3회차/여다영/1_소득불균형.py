import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())

for j in range(1, T + 1):
    n = int(input())
    #사람 수 입력
    incomes = list(map(int, input().split()))
    #소득 입력

    people = []
    average = sum(incomes) / n
    #평균을 구한 후
    for i in incomes:
        if i <= average:
            #평균 이하인 사람들을 people에 담는다.
            people.append(i)
    
    print(f'#{j}', len(people)) #평균 이하인 사람 수를 출력