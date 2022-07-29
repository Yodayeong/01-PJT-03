import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())

for i in range(1, T + 1):
    a, b, c = input().split()

    if a == b == c:
        #네 변의 길이가 모두 같은 경우
        print(f'#{i}', a)
    elif a == b:
        #여기서부터는 두 변씩 길이가 같은 경우
        print(f'#{i}', c)
    elif a == c:
        print(f'#{i}', b)
    else:
        print(f'#{i}', a)