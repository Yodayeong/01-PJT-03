import sys

sys.stdin = open("_암호문1.txt")

def revise(code):
    times = int(input())
    orders = list(input().split())
    
    i = 0
    while orders[i] != 'I':
        point = orders[i + 1]
        n = orders[i + 1]
        i = i + 3
        for i in range(i, i + 5):
            


for i in range(1, 11):
    length = int(input())
    code = list(input().split())
    
    revise(code)




#def order(code, length):
#    I = input()
#    point, num = map(int, input().split())
#    
#    final = []
#    for i in range(0, point):
#        final.append(code[i])
#    for i in range(num):
#        temp = int(input())
#        final.append(temp)
#    for i in range(point, length):
#        final.append(code[i])

#    return final

#for i in range(1, 11):
#    length = int(input())

#    code = list(map(int, input().split()))
#    revise = int(input())
#    for j in range(revise):
#        code = order(code, length)
#        length = len(code)
#    
#    print(f'#{i}', code[0:10])