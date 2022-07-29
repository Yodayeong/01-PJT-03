import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input())

for i in range(1, T + 1):
    word = input()

    word = word[::-1]
    #문자열을 한번 뒤집어 준 다음에

    #'p'와 'q'를 서로 바꿀때, 하나를 우선 x로 바꿔줘서 혼동이 없게 한다.
    word = word.replace('q', 'x')
    word = word.replace('p', 'q')
    word = word.replace('x', 'p')

    #'b'와 'd'를 서로 바꿔줄 때도, 하나를 우선 x로 바꿔준다.
    word = word.replace('d', 'x')
    word = word.replace('b', 'd')
    word = word.replace('x', 'b')

    print(f'#{i}', word)