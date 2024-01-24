# 리스트 생성, 초기화
is_prime=[True]*(123456*2+1)
is_prime[0]=False
is_prime[1]=False

# 2부터 시작하여, 해당 수의 배수인 경우 is_prime[j]=False로 저장
for i in range(2,len(is_prime)):
    if is_prime[i]==False: continue
    for j in range(2*i, len(is_prime), i):
        is_prime[j]=False


while True:
    num = int(input())
    # 0을 입력하면 종료
    if num==0:
        break
    
    # 소수의 갯수 초기화
    count = 0
    # 입력받은 값을 기준으로 특정 범위 내의 소수 갯수를 구함
    for a in range(num+1, 2*num+1):
        if is_prime[a]: count += 1
    print(count)