# T = int(input())
# for i in range(T) :
#     R = list(input().split())
#     A = []
#     B = R[1]
#     # print(R[0])
#     # print(R[1])
#     for j in R[1] :
#         A += j*int(R[0])
#     for k in A :
#         print(k, end="")
#     print()


T = int(input())
while T>0 :
    T = T-1
    R, S = input().split()
    for i in range(len(S)) :
        print(S[i]*int(R), end="")
    print()


    


# T=int(input())
# B=[]
# for i in range(T):
#     A=list(input().split())
#     C=A[1]
#     for j in C:
#         B+=j*int(A[0])
#     for i in B:
#         print(i,end="")
#         B=[]