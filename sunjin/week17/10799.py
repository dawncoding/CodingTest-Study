"""
입력: 쇠막대기와 레이저의 배치를 나타내는 괄효 표현
출력: 잘려진 조각의 총 개수
제약: 괄호 문자의 개수 <= 100,000
"""
question = input()
stack=[]
count = 0
for i in range(len(question)):
    if question[i] == "(":
        stack.append("(")
    else :
        if question[i-1]=="(": # 해당 위치는 레이저를 의미한다.
            stack.pop()
            print(stack)
            count+=len(stack) # 스택에 남아있는 쇠막대기의 개수만큼 쇠막대기 조각의 개수를 더하게 된다.
            
        else : # 해당 위치는 쇠막대기의 끝을 의미한다.
            stack.pop()
            count+=1 # 쇠막대기 조각의 개수를 1개 더하게 된다.
print(count)