# print(ord(input()))
# a = 97 z = 122

s = str(input())
for i in range(ord("a"),ord("z")+1) :
    print(s.find(chr(i)), end=" ")