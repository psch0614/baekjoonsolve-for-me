all = str(input())
sep = []
for i in range(26) :
    if i < 3 : #abc
        sep.append(all.count(chr(i+65))*3)
    elif i < 6 : #def
        sep.append(all.count(chr(i+65))*4)
    elif i < 9 : #ghi
        sep.append(all.count(chr(i+65))*5)
    elif i < 12 : #jkl
        sep.append(all.count(chr(i+65))*6)
    elif i < 15 : #mno
        sep.append(all.count(chr(i+65))*7)
    elif i < 19 : #pqrs
        sep.append(all.count(chr(i+65))*8)
    elif i < 22 : #tuv
        sep.append(all.count(chr(i+65))*9)
    else : 
        sep.append(all.count(chr(i+65))*10)
print(sum(sep))


# 다른사람
# dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ'] #dial 정의
# a = input() #숫자 받기
# ret = 0 #리턴값 초기화
# for i in range(len(a)) : #반복횟수 = a의 길이
#   for j in dial : # 반복횟수 = dial 길이
#       if a[i] in j : # a의 i번째 문자열이 j 에 포함되어있을경우
#           ret += dial.index(j) +3 #j의 번호 +3 을 리턴
# print(ret)