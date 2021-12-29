#호제법 테스트
def gcd(a,b) :
    if b == 0 :
        return a
    else :
        return gcd(b,a%b)

n = list(map(int, input().split()))
print(gcd(n[0],n[1]))