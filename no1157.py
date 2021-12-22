# all = input().upper()
# print(all)

# for i in range(ord("A"), ord("Z")) :


# A = all.count("A")


# all = str(input().lower())
# print(all)
# # for i in range(ord("a"),ord("z")+1) :
# sep = []
# #     # print(all.count(chr(i)), end=" ")
# for j in range(26) :
#     sep.insert(j, all.count(chr(j+97)))
# print(sep)


all = str(input().upper())
sep = []
for i in range(26) :
    sep.append(all.count(chr(i+65))) #문자에 포함된 갯수 확인(대문자로)후, sep에 채워넣기
# print(sep)
# print(max(sep))
if sep.count(max(sep)) > 1 : #sep 안에서 가장큰수 찾아서 1개 이상일경우에는 다음문자 표기
    print("?")
else :
    print(chr(sep.index(max(sep))+65)) #sep안에서 가장 큰수 찾아서 대문자로 표기
