import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())

for i in range(1, T + 1):
    credit_nums = input()
    if credit_nums[0] == '3' or credit_nums[0] == '4' or credit_nums[0] == '5' or credit_nums[0] == '6' or credit_nums[0] == '9':
        #credit의 첫째자리 조건 충족 후,
        credit_nums = credit_nums.replace('-', '')
        #'-'기호를 빼고
        if len(credit_nums) == 16:
            #credit의 길이 조건까지 충족하면
            print(f'#{i}', 1)
            #1 출력
        else:
            print(f'#{i}', 0)
    else:
        print(f'#{i}', 0)