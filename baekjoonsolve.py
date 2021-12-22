# 2557 hello world
# print("Hello World")

# 10718 we love kriii
# print("""강한친구 대한육군
# 강한친구 대한육군""")

# 10171 고양이
# print("""\    /\\
#  )  ( ')
# (  /  )
#  \(__)|""")

# 10172 개
# print("""|\\_/|
# |q p|   /}
# ( 0 )\"\"\"\\
# |"^"`    |
# ||_/=\\\\__|""")

# 1000 A+B
# a, b = map(int, input().split())
# print(a+b)

# 1001 A-B
# a, b = map(int, input().split())
# print(a-b)

# 10998 A*B
# a, b = map(int, input().split())
# print(a*b)

# 1008 A/B
# a, b = map(int, input().split())
# print(a/b)

# 10869 사칙연산
# a, b = map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)

# 10430 나머지
# a, b, c = map(int, input().split())
# print((a+b)%c)
# print(((a%c) + (b%c))%c)
# print((a*b)%c)
# print(((a%c) * (b%c))%c)

# 2588 곱셈
# a = int(input())
# b = int(input())

# b100 = b//100
# b10 = (b%100)//10
# b1 = b%10
# print(a*b1)
# print(a*b10)
# print(a*b100)
# print(a*b)

# step 2 if
# 1330 두수 비교하기
# a, b = map(int, input().split())
# compat = a-b
# if compat == 0 :
#     print("==")
# elif compat >=0 :
#     print(">")
# elif compat <=0 :
#     print("<")

# 9498 시험성적
# a = int(input())
# if a >=90 : print("A")
# elif a >=80 : print("B")
# elif a >=70 : print("C")
# elif a >=60 : print("D")
# else : print("F")

# 2753 윤년
# a = int(input())

# a4 = a%4 == 0 
# a100 = a%100 != 0
# a400 = a%400 == 0

# if a4 and a100 and a400:
#     print("1")
# elif a4 and a400 :
#     print("1")
# elif a4 and a100 :
#     print("1")
# else :
#     print("0")
# # 따라한것
# a = int(input())
# if a%4==0 and a%100!=0 or a%400==0 :
#     print("1")
# else :
#     print("0")

# 14681 사분면 고르기
# x = int(input())
# y = int(input())
# if x>0 :
#     if y>0 :
#         print("1")
#     else :
#         print("4")
# else :
#     if y>0 :
#         print("2")
#     else :
#         print("3")

# 2884 알람시계
# x, y = map(int, input().split())
# A = x*60+y-45
# if A>0 :
#     Ax = A//60
#     Ay = A%60
#     print(f'{Ax} {Ay}')
# else :
#     Ax = (A+1440)//60
#     Ay = (A+1440)%60
#     if Ax==24:
#         print(f'0 {Ay}')
#     else :
#         print(f'{Ax} {Ay}')

# step3 for
# 2739 구구단
# a = int(input())
# for b in range(1,10):
#     c=a*b
#     print(f'{a} * {b} = {c}')

# 10950 A+B -3
# a = int(input())
# for b in range(0,a) :
#     x, y = map(int, input().split())
#     print(x+y)
#다른사람코드
# import sys
# t = int(sys.stdin.readline())
# for i in range(t) :
#     readList = sys.stdin.readline()
#     a,b = list(map(int,readList.split()))
#     print(a+b)

# 8393 1~n까지의 합
# import sys
# z = 0
# x = int(input())

# for i in range(1,x+1) :
#     z += int(i)
# print(z)
# 다른사람 코드
# x = int(input())
# print(x*(x+1)//2)

# 15552 빠른 A+B
# import sys
# t = int(sys.stdin.readline())
# for i in range(t) :
#     readList = sys.stdin.readline()
#     a,b = list(map(int,readList.split()))
#     print(a+b)

# 2741 N찍기 1부터 N까지 쓰기
# x = int(input())
# for i in range(1,x+1) :
#     print(i)

# 2742 기찍N N부터 1까지 쓰기
# x = int(input())
# for i in range(x,0,-1) :
#     print(i)
# x = int(input())
# for i in reversed(range(1,x+1)) :
#     print(i)

# 11021 A+B -7
# a = int(input())
# for b in range(0,a) :
#     x, y = map(int, input().split())
#     print(f'Case #{b+1}: {x+y}')

# 11022 A+B -8
# a = int(input())
# for b in range(0,a) :
#     x, y = map(int, input().split())
#     print(f'Case #{b+1}: {x} + {y} = {x+y}')

# 2438 별찍기 -1
# a = int(input())
# for b in range(1,a+1) :
#     print('*'*b)

# 2439 별찍기 -2
# a = int(input())
# for b in range(1,a+1) :
#     a -=1
#     print(' '*a + '*'*b)

# 10871 X보다 작은수
# import sys
# n, x = map(int, sys.stdin.readline().split()) #n, x 입력받기
# data = list(map(int, sys.stdin.readline().split())) # data list 리스트 만들기
# for a in range(n) : # a를 n 까지 증가하면서 확인
#     if data[a] <x : # data의 a 번째 있는 숫자가 x보다 작은지 확인
#         print(data[a], end=" ") #위의 값이 참인경우 data의 a번째 숫자를 적고 한칸 띄기

# step 4 while문
# 10952 A+B -5
# import sys
# while True :
#     x, y = map(int, sys.stdin.readline().split())
#     if x or y != 0 :
#         print(x+y)
#     else :
#         break

# 10951 A+B -4
# import sys
# while True :
#     try :
#         x, y = map(int, sys.stdin.readline().split())
#         print(x+y)
#     except :
#         break

# 1110 더하기 사이클
# import sys
# x = int(sys.stdin.readline()) # 숫자 입력 받기
# z = x # x를 z에 복사
# i = 0 # 반복횟수를 측정하기 위한 i
# while True :
#     x10 = z//10 # 10의 자리
#     x1 = z%10 # 1의 자리
#     y = (x10+x1)%10 # 새로만들어질 1의 자리
#     z = x1*10 + y # 새로만들어질 숫자 == 기존숫자의 1의자리*10 + y
#     i += 1 # 반복횟수 리턴
#     if x == z : # x와 새로만든 z가 같을경우
#         break # 멈추기
# print(i)

# step5 1차원 배열
# 10818 최소, 최대
# import sys
# x = int(input())
# data = list(map(int, sys.stdin.readline().split()))
# print(min(data), max(data))

# 2562 최댓값
# n = list(int(input()) for i in range(9)) #서로다른 9개의 자연수를 받아서 리스트에 넣기
# print(max(n)) # 최댓값 찾기
# print(n.index(max(n))+1) # 최댓값의 위치+1 반환 (0부터 시작하기때문에 1 더하기)

# 2577 숫자의 개수
# numlist = list(int(input()) for i in range(3)) # 숫자 3개 받아서 리스트에 넣기
# product = numlist[0]*numlist[1]*numlist[2] # 각 숫자 곱하기
# for i in range(10) : # 0~9 까지 10가지 숫자를 넣기
#     print(str(product).count(str(i))) # 문자열 product 에서 문자열i가 쓰여진 횟수 반환

# 3052 나머지 (42로 나눳을때 나머지가 다른 것의 갯수)
# numlist = list(int(input()) for i in range(10)) # 10개의 숫자를 받아서 list화
# div42 = set([]) # 나머지를 넣을곳을 만들기 set 특성상 같은숫자가 들어올 경우 다른것은 없애버림
# for i in range(10) : # 10번 하기
#     div42.add(numlist[i]%42) # div42에 numlist[i]를 42로 나눈 나머지 넣기
# print(len(div42)) # set의 길이(갯수) 프린트
# # 다른사람이 한것
# div42 = set([]) # 나머지 넣을곳 만들기 set 특성상 같은숫자가 들어올 경우 다른것은 없애버림
# for i in range(10) : #10번 하기
#     div42.add(int(input())%42) # 들어온 숫자를 42로 나누기
# print(len(div42)) # set의 길이(갯수) 프린트


# 1546 평균 (내 가장 점수 높은 것을 기준으로 다른점수를 %로 올리고 평균내기)
# import sys
# n = int(input()) # 시험 점수 갯수 받기 n개
# realscore = list(map(int, sys.stdin.readline().split())) # 시험점수를 계속 받기
# maxscore = max(realscore) # 최대값 찾기
# fakescore = [0]*n #가짜점수가 들어갈 list 만들기, list 공간은 n개
# for i in range(n) : # n번 반복
#     fakescore[i] = (realscore[i]/maxscore)*100 #가짜점수 만들어서 입력
# print(sum(fakescore)/n) #가짜 평균 출력

# 8958 ox퀴즈 (맞출수록 점수 가중되고 틀리면 리셋됨)
# n = int(input())
# oxlist = list((input()) for i in range(n))
# for i1 in range(n) :
#     sepoxlist = oxlist[i1]
#     preoxlist =[9]*len(sepoxlist)
#     for i2 in range(len(sepoxlist)) :        
#         if i2 == 0 :
#             if sepoxlist[i2] == "O" :
#                 preoxlist[i2] = 1
#             else :
#                 preoxlist[i2] = 0
#         elif sepoxlist[i2] == "O" :
#             preoxlist[i2] = preoxlist[i2-1] +1
#         else :
#             preoxlist[i2] = 0
#         oxlist[i1] = sum(preoxlist)
# print(*oxlist, sep='\n')
# 다른사람 코드 따라하기
# import sys
# n = int(sys.stdin.readline()) # n 정수로 입력받기
# for i in range(n) : #n 번 반복하기
#     oxlist = sys.stdin.readline() #ox리스트 입력 받기
#     sum = 0 #합계값 0 초기화
#     d = 0 #가중값 0 초기화
#     for j in oxlist : #oxlist 에서 앞에서부터 순서대로 반복하기
#         if j =="O" : # O일경우
#             d += 1 # 가중값 1 증가
#         else : # X일경우
#             d = 0 # 가중값 0 초기화
#         sum = sum + d # 합계갑에 가중값 더하기 ##가중값이 누적되며 증가하기 때문에 점수는 쭉 증가함
#     print(sum)

# 4344 평균은 넘겟지 (테스트케이스 및 테스트 점수 갯수, 점수 주어준뒤, 평균을 넘는 테스트 점수 갯수 출력, 소수점 3번째 자리까지 표기)
# import sys
# c = int(input()) # 케이스 입력
# for i in range(c) : # c회 반복
#     n = list(map(int, sys.stdin.readline().split())) #테스트 점수 갯수 및 점수 리스트 입력
#     n_ave = (sum(n)-n[0])/n[0] # (리스트 합계 - 테스트 점수 갯수) / 갯수 == 점수 평균
#     overstudent = 0 # 넘는 인원 카운트 초기화
#     for j in range(len(n)-1) : # n 회 반복 테스트 -1은 테스트 점수 갯수까지 카운팅되어 n을 뺌
#         if n[j+1] > n_ave : # n의 j+1위치의 값(점수) 가 평균보다 높은경우
#             overstudent += 1 # 인원 카운트 1 증가
#     studentper = overstudent/n[0]*100 # 넘는 인원 100분율 계산
#     print('%.3f%%' %studentper) # or print('%.3f%%' %(overstudent/n[0]*100))
# # 넘는 인원 소숫점 3번째 자리까지 표기후 % 추가 ## (%.3f %에 뒤의 %정의 값을 넣고 소수점 3자리까지 입력, %% 추가하여 % 문자까지 추가)

# step 6 함수
# 15596 정수 N개의 합
# def solve(a):
#     ans = 0
#     for i in range(len(a)) :
#         ans += a[i]
#     return ans

# 1065 한수
# n = int(input()) #입력된 숫자
# x = 0 #갯수
# for i in range(n) :
#     m = i+1
#     if m < 100 :
#         x += 1
#     else :
#         o = str(m)
#         o1 = int(o[0])
#         o2 = int(o[1])
#         o3 = int(o[2])
#         if o1 - o2 == o2 - o3 :
#             x += 1
# print(x)
# 다른사람이 한것
# n = int(input())
# c = 0
# if n < 100 :
#     print(n)
# else :
#     for i in range(100, n+1) :
#         if i//100 - i//10%10 == i //10%10 - i%10 : # i//100 = 100의자리, i//10%10 = 10의자리, i%10 = 1의자리
#             c += 1
#     print(99+c)

# 11654 아스키코드
# print(ord(input())) # 들어온 문자열을 아스키코드(ord)로 바꿔줌

# # 11720 숫자의 합 (자릿수 알려주고 숫자 알려준후 각 숫자 더함)
# n = int(input()) #자릿수 알려줌
# x = str(input()) #숫자 알려줌(문자열로 치환)
# total = 0 
# for i in range(n) : # n회 반복
#     total += int(x[i]) # 숫자 자릿수 더함
# print(total)

# 10809 알파벳 찾기 (알파벳 위치 찾기)
# s = str(input()) #문자열 입력
# for i in range(97,123) : # 문자열 반복 (아스키코드 기준)
#     print(s.find(chr(i)), end=" ") # 문자열에서 아스키코드 기준으로 찾아서 반환 및 한칸 띄기

# s = str(input())
# for i in range(ord("a"),ord("z")+1) : # 문자열 반복 아스키코드로 보기 쉽게 만듦
#     print(s.find(chr(i)), end=" ")

# 2675 문자열 반복
# T = int(input()) # 문제 갯수 입력
# A = [] # 빈 문자열 리스트 작성
# for i in range(T) : # 아래것들을 T회 반복
#     R = list(input().split()) # 반복 횟수 및 문자열 입력
#     B = R[1] # B에 문자열 입력
#     for j in R[1] : #R1의 문자열을 순서대로 j에 입력
#         A += j*int(R[0]) #A에 j*R[0] 즉 문자열 순서대로 반복횟수를 곱한만큼 누적입력
#     for k in A : #k에 A를 순서대로 입력
#         print(k, end="") #K를 순서대로 출력 출력후 띄어쓰기 없이 반복 (print(A)할경우 A가 리스트라 리스트 형식으로 표기되므로 각각을 반복하도록 짠것)
#     print() #줄바꿈을 위한 빈줄 출력
#     A = [] #리스트 리셋

# 1157 단어공부 (가장 많이 사용된 알파벳을 출력하고, 2개일경우 ? 출력)
# all = str(input().upper()) #입력된 문자를 대문자로 치환
# sep = [] # 빈 리스트 작성
# for i in range(26) : # a to z 반복
#     sep.append(all.count(chr(i+65))) #sep에 a to z 문자열 갯수 입력
# if sep.count(max(sep)) > 1 : # 가장 높은 숫자를 카운트하여 1개 이상일경우
#     print("?") # ? 출력
# else :
#     print(chr(sep.index(max(sep))+65)) #가장 많이 나온 문자열 출력 (가장 많이 나온 숫자를 찾은뒤, 인덱스로 위치를 찾고 65를 더하여 아스키코드로 반환한뒤, chr로 문자로 반환)

# 1152 단어의 갯수 (단어의 갯수를 구하는 문제 0인경우도 있기에 주의)
# a = input().split() #문자열을 받을때 나누어서 받음, 숫자가 주어질때 띄어쓰기로 주어지는것과 같음. 자동으로 리스트화됨
# print(len(a)) #a의 갯수, 길이 를 리턴

#2908 상수 (두 숫자를 앞뒤를 바꾸어 비교하여 큰수를 출력)
# import sys
# a, b = list(map(int, sys.stdin.readline().split()))
# # ar = (a%10)*100 +   ((a//10)-((a//100)*10))*10   +   (a//100) #예전
# ar = (a%10)*100 + (((a//10)%10)*10) + (a//100) #변경
# # br = (b%10)*100 +   ((b//10)-((b//100)*10))*10   +   (b//100) #예전
# br = (b%10)*100 + (((b//10)%10)*10) + (b//100) #변경
# if ar > br :
#     print(ar)
# else :
#     print(br)
# #다른사람 코드
# a , b = input().split() #a,b 나누어 받기
# a , b = a[::-1] , b[::-1] #역순으로 넣기 [x,y,z] => x부터 y까지 z의 순서대로 넣기 x,y=""일경우 시작과 끝을 정하지 않음. z=양수일경우 해당 숫자 만큼 띄어서 입력, 음수인경우 역순으로 입력 본 문제의 경우 문자열로 받았으므로 뒤에서부터 쓰게됨
# print(max(int(a),int(b)))

# 5622 다이얼 (문자열이 포함된 다이얼 패드(구형전화기)를 돌릴때 들어가는 시간 구하기 다이얼 하나당 1초로 계산)
# all = str(input())
# sep = []
# for i in range(26) :
#     if i < 3 : #abc
#         sep.append(all.count(chr(i+65))*3)
#     elif i < 6 : #def
#         sep.append(all.count(chr(i+65))*4)
#     elif i < 9 : #ghi
#         sep.append(all.count(chr(i+65))*5)
#     elif i < 12 : #jkl
#         sep.append(all.count(chr(i+65))*6)
#     elif i < 15 : #mno
#         sep.append(all.count(chr(i+65))*7)
#     elif i < 19 : #pqrs
#         sep.append(all.count(chr(i+65))*8)
#     elif i < 22 : #tuv
#         sep.append(all.count(chr(i+65))*9)
#     else : 
#         sep.append(all.count(chr(i+65))*10)
# print(sum(sep))
# 다른사람
# dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ'] #dial 정의
# a = input() #숫자 받기리스트로 받음
# ret = 0 #리턴값 초기화
# for i in range(len(a)) : #반복횟수 = a의 길이
#   for j in dial : # dial 안에 있는 리스트를 각각 j에 넣어음
#       if a[i] in j : # a의 i번째 문자열이 j(abc, def... 등 묶음) 에 포함되어있을경우
#         #   print(j) #j 확인용
#           ret += dial.index(j) +3 #j의 번호 +3 을 리턴
# print(ret)

# 2941 크로아티아 알파벳
# a = input() #문자열 리스트 입력
# # goal = a # 문자열 리스트 복사
# croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=' ] #쿠로아티아 알파벳 정의
# for i in croatia : #알파벳을 i에 입력
#     a = a.replace(i, 'a') # goal 안에 i가 포함되어있을경우 a로 문자 치환
# print(len(a)) #a의 길이 반환

# 1316 그룹단어 체커
