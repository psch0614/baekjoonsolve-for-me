import sys

a, b = list(map(int, sys.stdin.readline().split()))

ar = (a%10)*100 +   ((a//10)-((a//100)*10))*10   +   (a//100)
br = (b%10)*100 +   ((b//10)-((b//100)*10))*10   +   (b//100)

if ar > br :
    print(ar)
else :
    print(br)

# [A:B:C] 용법을 이용하면 쉽게 함
# N = input().split() # list N에 나누어 입력
# N = [int(i[::-1]) for i in N] # 리스트로 만들어서 N에 저장한다. 
#                                 저장시 처음부터(A=none) 끝까지(B=none) 역순으로(-1)
#                                 N번 반복한다
# print(max(N)) #리스트 N에서 가장 큰값을 출력한다
#  or
# a, b = list(map(int, sys.stdin.readline().split()))
# 