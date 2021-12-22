# import sys

n = int(input()) #입력된 숫자
x = 0 #갯수
for i in range(n) :
    m = i+1
    # print(m, "판단할 숫자")
    if m < 100 :
        x += 1
    else :
        o = str(m)
        o1 = int(o[0])
        o2 = int(o[1])
        o3 = int(o[2])
        if o1 - o2 == o2 - o3 :
            x += 1
print(x)





# import sys

# n = int(sys.stdin.readline())

# for i in range(n) :
#     oxlist = sys.stdin.readline()
#     oc = 0
#     oc_t = 0
#     for j in range(len(oxlist)) :
#         if oxlist[j] == "O" :
#             oc += 1
#         else : 
#             oc = 0
#         oc_t += oc
#     print(oc_t)