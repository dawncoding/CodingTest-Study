A, B, C = map(int, input().split())

def cal(length):
    if length == 1:
        return A%C
    if length % 2 == 0:
        result = cal(length//2)
        return result*result %C
    else:
        result = cal(length//2)
        return result*result*A %C