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

# 1316 그룹단어 체커  not in 참조
# N = int(input()) #시행횟수 N 입력
# countN = 0 #나중에 뺄값 0으로 지정
# for i in range(N) : #i를 N회 반복
#     word = input() #문자열 입력
#     sepword = [] #문자열을 나누어서 입력할곳 따로 만듬
#     checker = [] #체커 따로 만듦
#     for j in range(len(word)) : #j를 word의 길이만큼 반복
#         sepword += word[j] # sepword에 word를 차례로 입력
#     for k in range(len(sepword)) : #k를 sepword의 길이만큼 반복
#         if sepword[k] not in checker : #sepword의 k번째 문자가 checker안에 없을경우
#             checker += sepword[k] # checker에 sepword를 추가
#         elif sepword[k] in checker : #sepword의 k번째 문자가 checker에 있을경우
#             if sepword[k] == sepword[k-1] : #sepword의 k번째 문자와 k-1번째 문자가 같은경우
#                 pass #패스
#             else : #다른경우 즉, checker안에서 이미 한번 언급되엇고 다시 언급됨
#                 countN +=1 #나중에 뺄값인 countN을 1증가시킨다
#                 break #for문을 중지 시킨다
# print(N-countN)

#다시 짠것 필요없는거 제거
# N = int(input()) #시행횟수 N 입력
# countN = 0 #나중에 뺄값 0으로 지정
# for i in range(N) : #i를 N회 반복
#     word = input() #문자열 입력
#     # sepword = [] #문자열을 나누어서 입력할곳 따로 만듬 ## 필요없는것 기존 word로도 사용가능
#     checker = [] #체커 따로 만듦
#     # for j in range(len(word)) : #j를 word의 길이만큼 반복 ##기존 word로 사용함으로 인하여 제거
#     #     sepword += word[j] # sepword에 word를 차례로 입력 ##기존 word로 사용함으로 인하여 제거
#     for k in range(len(word)) : #k를 sepword의 길이만큼 반복 ##기존 sepword에서 word로 변경
#         if word[k] not in checker : #sepword의 k번째 문자가 checker안에 없을경우 ##기존 sepword에서 word로 변경
#             checker += word[k] # checker에 sepword를 추가 ##기존 sepword에서 word로 변경
#         elif word[k] in checker : #sepword의 k번째 문자가 checker에 있을경우 ##기존 sepword에서 word로 변경
#             if word[k] == word[k-1] : #sepword의 k번째 문자와 k-1번째 문자가 같은경우 ##기존 sepword에서 word로 변경
#                 pass #패스
#             else : #다른경우 즉, checker안에서 이미 한번 언급되엇고 다시 언급됨
#                 countN +=1 #나중에 뺄값인 countN을 1증가시킨다
#                 break #for문을 중지 시킨다
# print(N-countN)
# #코드가 더러워서 다시씀
# N = int(input()) #시행횟수 N 입력
# countN = 0 #나중에 뺄값 0으로 지정
# for i in range(N) : #i를 N회 반복
#     word = input() #문자열 입력
#     checker = [] #체커 따로 만듦
#     for k in range(len(word)) : #k를 word의 길이만큼 반복
#         if word[k] not in checker : #word의 k번째 문자가 checker안에 없을경우
#             checker += word[k] # checker에 word를 추가
#         elif word[k] in checker : #word의 k번째 문자가 checker에 있을경우 
#             if word[k] == word[k-1] : #word의 k번째 문자와 k-1번째 문자가 같은경우 
#                 pass #패스
#             else : #다른경우 즉, checker안에서 이미 한번 언급되엇고 다시 언급됨
#                 countN +=1 #나중에 뺄값인 countN을 1증가시킨다
#                 break #for문을 중지 시킨다
# print(N-countN)

# 다른사람 코드
# def group_word(s):  #group_word라는 함수 정의 s는 input받은 문자로 아래서 input으로 들어올 값
#     l = [] # 체크할곳 내가 만든곳의 체커와 동일
#     for i in s: # i에 s의 문자열을 처음부터 입력
#         k = s.find(i) #k에 s의 i문자의 위치를 찾아서 넣음 숫자로 나옴
#         if k not in l or k == l[-1]: #k가 l에 없거나 k가 l의 마지막과 다를경우(직전 추가한숫자와 같을경우) 즉 새롭게 나온것이거나 기존과 같을경우
#             l.append(k) # l에 추가한다
#         else: # if가 아닐경우
#             return False # if를 종료하고 for로 탈출한다
#     return True #for을 반복한다

# t = int(input())
# sum = 0
# for i in range(t):
#     if group_word(input()):
#         sum +=1
# print(sum)

# step 8 기본수학1
# 1712 손익분기점
# test1 실패 c==b zero div 실패
# a,b,c = map(int, input().split())
# i = (a//(c-b))
# if i < 0 or c==b :
#     print(-1)
# else :
#     print(i+1)
# a,b,c = map(int, input().split())
# if c > b :
#     print(a//(c-b)+1)
# else :
#     print(-1)

# 2292 벌집
# room_num = int(input())-1
# if room_num == 0 :
#     print(1)
# else :
#     i = 1
#     n = 0
#     while room_num >= i :
#         n += 1
#         i += 6*n
#         # print(f'현재 {n+1}라인 훑는중 최대값 {i}') # 검증코드
#     print(n+1)
# 다른방식
# room_num = int(input())
# i = 1 # i 즉 현재 위치에서의 최대값 설정. for문은 0부터 시작하며, 문제에서는 1번라인(숫자1) 도 포함하므로 1로 설정함
# for j in range(room_num) : # 라인은 항상 room_num보다 크므로 room_num으로 최대값 러프하게 설정.
#     i = i + j*6 # i 즉 현재 위치에서의 최대값 찾기
#     # print(f'검산 코드임 : {j}라인 훑는중 라인내 최대값{i}, 찾는값 {room_num}')
#     if i >= room_num : # i 즉 j번째 라인의 최대값이 room_num 보다 클경우 답을 찾은것으로 라인 j 를 반환함
#         print(j+1) #라인 j가 있는곳 또한 포함하여야 하므로 j+1 반환 
#         break # 종료를 하지 않으면 room_num까지 for문 반복하므로 break 걸어줌

# 1193 분수찾기
# 아래와 같은 식으로 쭉 이어나가는 숫자의 위치를 구하라
# 2 - 1/1 (1)
# 3 - 1/2 2/1 (2,3)
# 4 - 3/1 2/2 1/3 (4, 5, 6)
# 5 - 1/4 2/3 3/2 4/1 (7, 8, 9, 10)
# 6 - 5/1 4/2 3/3 2/4 1/5 (11, 12, 13, 14, 15)
# 7 - 1/6 2/5 3/4 4/3 5/2 6/1 (16 ~ 21)

# 내가짠 코드 1, 2를 예외처리 해서 가져옴 
# X = int(input())
# T = 1 # 삼각형 위치
# if X == 1 :
#     print("1/1")
# elif X==2 :
#     print("1/2")
# else :
#     for j in range(1,X) :
#         if X-j > 0 :
#             T += 1
#             X = X-j
#             print(f"현재 {T}위치 계산중입니다 현재 팩토리얼 숫자는 {j}입니다.")
#         else :
#             print(f'현재 {T+1}위치에 있습니다.  남은 숫자는 {X}입니다')
#             if X !=0 : # 남아있는경우
#                 if (T+1)%2 ==0 : #현재 위치가 짝수 위치인 경우
#                     print(f"{T+1-X}/{X}")
#                 else :
#                     print(f"{X}/{T+1-X}")
#             else : #남아있지 않은경우
#                 if T%2 == 0 : #짝수인경우
#                     print(f"1/{T-1}")
#                 else :
#                     print(f"{T-1}/1")
#             break

#다른사람이 짠 코드
# X=int(input())
# i=1
# while X>i:
#     X -= i
#     i += 1
# if i%2==0:
#     print(f"{X}/{i+1-X}")
# else:
#     print(f"{i-X+1}/{X}")

# 2869 달팽이는 올라가고 싶다
# import sys
# import math
# a,b,v = list(map(int, sys.stdin.readline().split())) #올라가는 a, 미끄러지는b, 총높이 v
# v -= a
# day = 1
# if v>0 :
#     print(day + math.ceil(v/(a-b)))
# else :
#     print(1)
# math안쓰고 하기
# import sys
# a,b,v = list(map(int, sys.stdin.readline().split())) #올라가는 a, 미끄러지는b, 총높이 v
# if v-a >0 :
#     if (v-a)%(a-b) == 0 :
#         print(1 + ((v-a)//(a-b)))
#     else :
#         print(1 + ((v-a)//(a-b)) + 1)
# else :
#     print(1)

# 10250 acm호텔
# t = int(input())
# for i in range(t) :
#     h , w, n = list(map(int, input().split()))
#     if n%h == 0 :
#         num = n//h
#         floor = h
#     else :
#         num = (n//h)+1
#         floor = n%h
    
#     if n<h :
#         num = 1
#     print(f'{floor}{str(num).zfill(2)}')

# 2775 부녀회장이 될테야 #문제 자체는 이해하였지만 공식을 이해하지 못하고 따라 작성함
# t = int(input())
# for _ in range(t) :
#     k = int(input())
#     n = int(input())
#     num = 1
#     l = k+n
#     for i in range(1,l+1) :
#         num *= i
#     for i in range(1,k+2) :
#         num //= i
#     for i in range(1,n) :
#         num //= i
#     print(num)

# 2839 설탕배달
# t = int(input())
# all =[]
# for i in range(1001) :
#     for j in range(1667) :
#         if (i*5)+(j*3) == t :
#             all.append(i+j)
# if len(all) == 0 :
#     print(-1)
# else :
#     print(min(all))
# 다른사람 코드 1
# x = int(input())
# count = 0
# while(x%5 !=0):
#     x-=3
#     count +=1
# if(x<0):
#     print(-1)
# else:
#     print(count + x//5)
# #다른사람코드 2
# v = int(input())
# if v ==1 or v==2 or v==4 or v==7 :
#     print(-1)
# else:
#     if v%5==0:
#         print(v//5)
#     if v%5==1 or v%5==3:
#         print(v//5+1)
#     if v%5==2 or v%5==4:
#         print(v//5+2)

# 10757 큰수 A+B
# import sys

# a,b = map(int, sys.stdin.readline().split())
# print(a+b)

# 1011 Fly me to the Alpha Centauri # 보고 따라하며 풀긴했음 수학공식은 다시 나중에 한번더 검증해볼것
# t = int(input())
# for _ in range(t) :
#     x, y = map(int, input().split())
#     d = y-x
#     i = 0
#     while i**2 <= d :
#         i += 1
#     i -= 1
#     if i**2 == d :
#         print((2*i)-1)
#     elif ((i**2)<d) and (d<=((i**2)+i)) :
#         print(2*i)
#     elif (((i**2)+i)<d) and (d<=(i**2)+(2*i)) :
#         print((2*i)+1)

# step9 기본수학2
# 1978 소수찾기
# import sys
# N = int(input())
# numlist = list(map(int, sys.stdin.readline().split()))
# cnt = 0
# for i in range(N) :
#     # print(f'numlist중 {i}번째 숫자인 {numlist[i]} 를 판단')
#     if numlist[i] == 1 :    
#         # print(f'{numlist[i]}가 1이기 때문에 패스')
#         pass
#     if numlist[i] == 2 :
#         cnt +=1
#         # print(f'{numlist[i]}가 2이기 때문에 카운터 증가 현재 카운터값은 {cnt}')
#     if numlist[i] >= 3 :
#         # print(f'{numlist[i]}가 3이상이라 판단중')
#         notprime = 0
#         for j in range(2,numlist[i]) :
#             if numlist[i]%j == 0 :
#                 notprime += 1
#                 # print(f'{numlist[i]}가 {j}로 나누어져 소수가 아님 카운트 증가')
#             else :
#                 # print(f'{numlist[i]}가 {j}로 나누어지지 않아 계속 판단')
#                 continue
#         if notprime == 0 :
#             cnt += 1
#             # print(f'{numlist[i]}가 소수라 카운터 증가 현재 카운터값은 {cnt}')
# print(cnt)
# #다른사람 코드
# n=int(input())
# num=list(map(int,input().split( )))
# for i in num:
#     if i==1:
#         n-=1
#     for j in range(2,i): # 1과 자기자신인 i를 제외한 범위 설정
#         if i%j==0: # 한번이라도 나누어 떨어지면 소수가 아님 
#             n-=1 #  위의 조건문에 해당 되는 경우 n을 하나씩 제거      
#             break # 소수가 아닌 걸 체크 했으므로 break를 걸어줌
# print(n)

# 내꺼 다시 써보기
# N = int(input())
# numlist = list(map(int, input().split()))
# for i in numlist :
#     print(f'{i}를 판단중')
#     if i == 1 :
#         print(f'{i}가 1이므로 소수가 아님 전체 테스트 케이스에서 1을 뺌')
#         N -= 1
#     print(f'{i}가 1이 아니므로 재 판단중')
#     for j in range(2,i) :
#         print(f'2에서부터 {i-1}까지로 {i}를 나눠볼꺼임')
#         if i%j == 0 :        
#             print(f'{i}가 {j}로 나누어졋기때문에 케이스에서 1을 빼고 멈출꺼임')
#             N -= 1
#             print(f'현재 남은 테스트 케이스는 {N}번임')
#             break
#         else :
#             print(f'{i}는 {j}나누어지지 않아 계속함')

# print(N)

# 2581 소수
# m = int(input())
# n = int(input())
# numlist = []
# for i in range(m,n+1) :
#     numlist.append(i)
# # print(f'숫자리스트는 다음과 같음 {numlist}')
# for i in numlist[::-1] : #역순으로 판단함 앞에서부터 지워나갈시 i증가함에 따라 순서가 꼬임
#     # print(f'{i}를 판단중')
#     if i == 1 :
#         numlist.remove(i)
#         break
#     for j in range(2,i) :
#         # print(f'{i}를 {j}로 나눠볼꺼임')
#         if i%j == 0 :
#             # print(f'{i}가 {j}로 나누어져 제거하고 멈출꺼임')
#             numlist.remove(i)
#             # print(f'남은 숫자 리스트는 {numlist}임')
#             break
#         else :
#             continue
# # print(numlist)
# if not numlist :
#     print(-1)
# else :
#     print(sum(numlist))
#     print(min(numlist))

# 11653 소인수 분해 --> 호제..법?
# N = int(input())
# i = 2
# while N != 1 :
#     if N%i == 0 :
#         print(i)
#         N = N/i
#     else :
#         i +=1
# 다른사람 코드
# N = int(input())
# i = 2
# primetest = int(N**0.5)
# while i <= primetest :
#     while N%i == 0 :
#         print(i)
#         N = N//i
#     else :
#         i += 1
# if N > 1 :
#     print(N)

# 1929 소수구하기 아라토스테네스의 체
# a = list(map(int, input().split()))
# is_prime = [True for _ in range(a[1]+1)]
# is_prime[0] = False
# is_prime[1] = False
# for i in range(2, int(a[1]**0.5)+1) :
#     if is_prime[i] == True :
#         for j in range(i*2, a[1]+1, i) :
#             is_prime[j] = False
# primenum = [i for i, j in enumerate(is_prime) if i>=a[0] and j==True]
# for k in range(len(primenum)) :
#     print(primenum[k])

# 4948 베르트랑 공준 3200ms 나옴 시벌;
# while True :
#     try :
#         a = int(input())
#         if a != 0 :
#             is_prime = [True for _ in range((a*2)+1)]
#             is_prime[0] = False #i값을 그대로 가져오기 위해 i = 0 부정 즉 소수가 아님
#             is_prime[1] = False #i값을 그대로 가져오기 위해 i = 1 부정 즉 소수가 아님
#             for i in range(2, int((2*a)**0.5)+1) :
#                 if is_prime[i] == True :
#                     for j in range(i*2, (2*a)+1, i) :
#                         is_prime[j] = False
#             primenum = [i for i, j in enumerate(is_prime) if i>a and j==True]
#             print(len(primenum))
#     except :
#         break

# 9020 골드 바흐의 추측 4<=n<=10,000
# 내가 한거 망함 타임아웃 걸림 처음에 체로 거르는것에서 타임아웃 걸린것으로 판단됨
# T = int(input())
# is_prime = [False, False] + [True] * 9999
# for i in range(2,int(10001**0.5)+1) :
#     if is_prime[i] == True :
#         for j in range(i*2, 10001, i) :
#             is_prime[j] = False
# primenum = [i for i, j in enumerate(is_prime) if i >=2 and j==True]
# for k in range(T) :
#     n = int(input())
#     prelist = []
#     halfn = n//2
#     for l in range(len(primenum)) :
#         if primenum[l] <= halfn :
#             if n-primenum[l] in primenum :
#                 prelist.append(primenum[l])
#                 prelist.append((n-primenum[l]))
#     print(prelist[-2],prelist[-1])

# 다시 시작 입력된 수 n에 대하여 반절을 하고 그 숫자에 대해여 소수 구한뒤 판단
# T = int(input())
# for i in range(T) :
#     n = int(input())
#     is_prime = [False, False] + [True] * (n-1)
#     for j in range(2, int(n**0.5)+1) :
#         if is_prime[j] == True :
#             for k in range(j*2, n+1, j) :
#                 is_prime[k] = False
#     primenum = [i for i, j in enumerate(is_prime) if i >=2 and j == True]
#     print(f'현재 소수 리스트는 {primenum}임')
#     for l in reversed(primenum) :
#         if n-l in primenum :
#             print(n-l, l)
#             break


# 다른 사람 코드 소수 구하는 것을 나누기법으로 실행
# T = int(input())

# def primenum(X) :
#     if X == 1 :
#         return False
#     for i in range(2, int(X**0.5)+1) :
#         if X%i == 0 :
#             return False
#     return True

# for _ in range(T) :
#     n = int(input())
#     a = n//2
#     b = n//2
#     while True :
#         if primenum(a) and primenum(b) :
#             print(a,b)
#             break
#         else :
#             a -= 1
#             b += 1

# 체법으로 변환

# primenum = [False, False] + [True] * 9999
# for i in range(2, int(5000**0.5)+1) :
#     if primenum[i] == True :
#         for j in range(i*2, 10001, i) :
#             primenum[j] = False
# # print(primenum)
# T = int(input())
# for _ in range(T) :
#     a = int(input())
#     m = a//2
#     # n = a//2
#     while True :
#         if primenum[m] and primenum[a-m] :
#             print(m,a-m)
#             break
#         else :
#             m -=1
#             # n +=1

# 1085 직사각형에서 탈출 - 가장 가까운 변까지의 거리 도출
# x,y,w,h = list(map(int, input().split()))
# xw = w-x
# yh = h-y
# ract = [x,y,xw,yh]
# print(min(ract))

# #더 짧게
# x,y,w,h = list(map(int, input().split()))
# print(min(x,y,w-x,h-y))

# 3009 네번째 점
# 풀이 1 list화 하여 1개만 있는것 찾아 리턴
# x_list =[]
# y_list =[]
# for _ in range(3) :
#     x, y = map(int, input().split())
#     x_list.append(x)
#     y_list.append(y)
# for i in range(3) :
#     if x_list.count(x_list[i]) == 1 :
#         x = x_list[i]
#     if y_list.count(y_list[i]) == 1 :
#         y = y_list[i]
# print(x,y)

# #풀이2 비교하여 다른것 리턴
# def cnt(n) :
#     if n[2] == n[0] :
#         return n[1]
#     elif n[2] == n[1] :
#         return n[0]
#     else :
#         return n[2]
# x1, y1 = map(int, input().split())
# x2, y2 = map(int, input().split())
# x3, y3 = map(int, input().split())
# print(cnt([x1,x2,x3]), cnt([y1,y2,y3]))

#4153 직각삼각형
# while True :
#     a = list(map(int, input().split()))
#     max_a = max(a)
#     if sum(a) == 0 :
#         break
#     a.remove(max_a)
#     if a[0]**2 + a[1]**2 == max_a**2 :
#         print("right")
#     else :
#         print("wrong")

#3053 택시 기하학 #택시 기하학 관련 이해 주소 https://m.blog.naver.com/alwaysneoi/100172516753
# import math
# r = int(input())
# print('%.6f' %(math.pi*r*r))
# print('%.6f' %(r*r*2))

#1002 터렛
# t = int(input())
# for _ in range(t) :
#     x1,y1,r1,x2,y2,r2 = map(int, input().split())
#     x_abs = max(x1,x2) - min(x1,x2)
#     y_abs = max(y1,y2) - min(y1,y2)
#     r_g = max(r1,r2)
#     r_l = min(r1,r2)
#     if x1==x2 and y1==y2 and r1==r2 : #일치할경우 1
#         print(-1)
#     elif x_abs**2 + y_abs**2 == (r1+r2)**2 : #외접할때 2
#         print(1)
#     elif (x_abs**2 + y_abs**2)**0.5 + r_l == r_g : #내접할때 3
#         print(1)
#     elif x_abs**2 + y_abs**2 > (r1+r2)**2 : #외부에 있고 안만날때 4
#         print(0)
#     elif (x_abs**2 + y_abs**2)**0.5 + r_l < r_g : #안에 있고 안만날때 5
#         print(0)
#     else :
#         print(2)

# t = int(input())
# def dis2(x1,x2,y1,y2) :
#     return ((x1-x2)**2 + (y1-y2)**2)
# for _ in range(t) :
#     x1,y1,r1,x2,y2,r2 = map(int, input().split())
#     if x1==x2 and y1==y2 and r1==r2 : #일치할경우 1
#         print(-1)
#     elif dis2(x1,x2,y1,y2) < (r1-r2)**2 or dis2(x1,x2,y1,y2) > (r1+r2)**2 :
#         print(0)
#     elif dis2(x1,x2,y1,y2) == (r1-r2)**2 or dis2(x1,x2,y1,y2) == (r1+r2)**2 :
#         print(1)
#     else :
#         print(2)

# 10872 팩토리얼 재귀로 풀기
# n = int(input())
# pre_n = 1
# while n != 0 :
#     pre_n = pre_n * n
#     n -=1
# print(pre_n)

# 10870 피보나치수5 재귀로 풀기
n = int(input())
pb = [0,1]
for i in range(2,n+1) :
    pb.append(pb[i-1]+pb[i-2])
print(pb[n])