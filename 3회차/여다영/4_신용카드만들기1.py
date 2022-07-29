import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())

for i in range(1, T + 1):
    nums = list(map(int, input().split()))
    #15자리의 숫자를 받고

    odd_nums = sum(nums[0:15:2]) * 2
    #홀수는 다 더한 후, 2를 곱해주고
    even_nums = sum(nums[1:15:2])
    #짝수는 그냥 다 더한다.
    total_sum = odd_nums + even_nums
    #홀수와 짝수를 모두 더한 것을 total_sum에 넣어주고

    if total_sum % 10 == 0:
        #total_sum이 10으로 딱 나누어 떨어지면 0을 출력
        print(f'#{i}', 0)
    else:
        #그렇지 않으면, 10에서 나머지를 빼준 수를 출력한다.
        print(f'#{i}', 10 - (total_sum % 10))