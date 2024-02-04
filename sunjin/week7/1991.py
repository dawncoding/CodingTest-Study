"""
Input: N(이진 트리의 노드의 개수) / 노드, 왼쪽 자식 노드, 오른쪽 자식 노드 N개씩 출력
Output: 전위순회, 중위순회, 후위순회 결과 출력
Constraints: 1 <= N <= 26

시간복잡도 -> O(N) + O(N) -> O(N)
N번 반복 -> O(N)
preorder, inorder, postorder 함수들은 각각 모든 노드를 방문하므로 전체 트리의 노드 수에 비례하는 시간이 소요된다. 각 함수의 시간 복잡도 -> O(N)
공간복잡도 -> O(N)
N: 정수 변수로 트리의 노드 수를 저장하기 위한 공간 -> O(1)
tree: 각 노드의 정보를 저장하기 위한 딕셔너리. 딕셔너리의 크기는 트리의 노드 수에 비례 -> O(N)
"""
import sys
input = sys.stdin.readline

N = int(input().strip())
tree = {}

for n in range(N): # 루프 N번 -> O(N)
  root, left, right = input().strip().split()
  tree[root] = [left, right]

def preorder(root):
  if root != '.':
    print(root, end='')
    preorder(tree[root][0]) # left
    preorder(tree[root][1]) # right

def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right
 
def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root
 
 
preorder('A')
print()
inorder('A')
print()
postorder('A')