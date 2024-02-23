N = list(map(int, list(input())))

# 내림차순 정렬
N.sort(reverse=True)

# 출력
for num in N: print(num, end="")