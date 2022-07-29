import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input())

for i in range(T):
    grade = dict()
    #한 번 돌 때마다 grade 딕셔너리 새로 구성
    times = int(input())
    #몇 번째 test case 인지
    num = list(map(int, input().split()))
    #각 test case의 숫자들을 받아주고
    for j in num:
        #dictionary에 각 숫자들의 빈도 수를 적어준다.
        if j not in grade:
            grade[j] = 1
        else:
            grade[j] += 1

    most = (max(grade.values()))
    #가장 많은 빈도가 몇번인지 알고
    temp = []
    #그 빈도에 해당하는 수들을 temp에 담는다.
    for k in grade:
        if grade[k] == most:
            temp.append(k)
    print(f'#{times}', max(temp)) #그 중, 더 큰 값을 출력