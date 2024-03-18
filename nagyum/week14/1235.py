"""
런타임 에러가 뜨는 코드임

student배열에 숫자 입력 받고 
diff 배열에 따로 하나씩 입력 받으면서 같으면 아웃 아니면 계속 적립해서 
diff 배열의 길이를 받으면 되는거 아님...?
student는 문잔디 바보처럼 int 해놈 ,,
"""

N=int(input()) 
student=[]
for _ in range(N):
    student.append(input())
    
for i in range(1, len(student[0])+1):
    diff=[]
    for j in range(N):
        if student[j][-i:] in diff:
            break
        else:
            diff.append(student[j][-i:])
    if len(diff)==N:
        print(i)
        break

