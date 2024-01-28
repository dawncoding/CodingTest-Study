"""
Input: word
Output: count(주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져있는지)
Constraints: len(word) <= 100
Edges: 'dz=', 'z='

문제 풀이
입력받은 문자에서 2~3글자로 이루어진 8개의 알파벳이 있는 경우 한 글자로 변환하고서 이후에 변환된 문자열의 총 글자 수를 센다.
* 구현할 때 dz=가 z=보다 앞에 있지 않으면 z=을 우선으로 바꿔버리게 되므로 dz=가 z=보다 앞에 있어야 한다.

시간 복잡도
croatia 안에 있는 단어 개수만큼 반복 -> O(N)
공간 복잡도
croatia 배열의 길이 -> O(N)
"""
# import sys
# input = sys.stdin.readline -> 입력: dz=ak / 출럭: 4 -> ?

word = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia:
    word = word.replace(i, "*")

print(len(word))