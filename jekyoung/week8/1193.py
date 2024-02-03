N=int(input())
i=1

# 대각선에 포함되는 요소의 수(i)만큼 N에서 빼준다.
# i는 1씩 증가
while N>i:
    N -= i
    i += 1

# N <= i 이므로, N은 i번째 대각선의 N번째 요소이다.
# 짝수번째 대각선은 N이 분자
if i%2 == 0:
    print("%d/%d" %(N,i-N+1))
# 홀수번째 대각선은 N이 분모
else:
    print("%d/%d"%(i-N+1,N))