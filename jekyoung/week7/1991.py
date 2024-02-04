"""
import sys

arr = []
in_arr = []
post_arr = []

def preorder(root, left, right):
    global arr
    # root, left, right 순서대로 저장
    if not arr: 
       arr.append(root)
       arr.append(left)
       arr.append(right)
       
    # root를 기준으로 arr를 slice -> root, left, right 순서 되도록 삽입
    else:
        idx = arr.index(root)
        arr = arr[0:idx+1]+[left, right]+arr[idx+1: len(arr)]
        
def inorder(root, left, right):
    global in_arr
    # root, left, right 순서대로 저장
    if not in_arr:
          in_arr.append(left)
          in_arr.append(root)
          in_arr.append(right)
    
    # root를 기준으로 arr를 slice -> left, root, right 순서 되도록 삽입
    else:
        idx = in_arr.index(root)
        in_arr = in_arr[0:idx]+[left, root, right]+in_arr[idx+1:len(in_arr)]
        
    
def postorder(root, left, right):
    global post_arr
    # left, right, root 순서대로 저장
    if not post_arr:
        post_arr.append(left)
        post_arr.append(right)
        post_arr.append(root)
    
    # root를 기준으로 arr를 slice -> left, right, root 순서 되도록 삽입
    else:
        idx = post_arr.index(root)
        post_arr = post_arr[0:idx]+[left, right]+post_arr[idx: len(post_arr)]

N = int(input())

for _ in range(N):
    i, j, k = sys.stdin.readline().split()
    preorder(i, j, k)
    inorder(i, j, k)
    postorder(i, j, k)


for i in arr:
    if i != ".": print(i, end="")
print()
for i in in_arr:
    if i != ".": print(i, end="")
print()
for i in post_arr:
    if i != ".": print(i, end="")
"""

# 재귀함수, 딕셔너리(key, value) 자료형을 이용한 방법

import sys
 
N = int(input())
tree = {}
 
for n in range(N):
    root, left, right = sys.stdin.readline().split()
    # root를 key, left와 right을 value로 갖도록 저장
    tree[root] = [left, right]
 
 
def preorder(root):
    if root != '.':
        print(root, end='')  # root를 출력한다.
        preorder(tree[root][0])  # left 자식이 새로운 root가 된다. (왼쪽으로 끝까지 탐색하면서 root 출력)
        preorder(tree[root][1])  # right 자식이 새로운 root가 된다. (더 이상 left 자식이 없는 root 부터 시작)
 
 
def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left 자식이 새로운 root가 된다. (왼쪽으로 끝까지 탐색한다.)
        print(root, end='')  # 더 이상 left 자식이 없으므로 root를 출력한다.
        inorder(tree[root][1])  # right 자식이 새로운 root가 된다.
 
 
def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left 자식이 새로운 root가 된다.
        postorder(tree[root][1])  # right 자식이 새로운 root가 된다.
        print(root, end='')  # root를 출력한다.
 
 
preorder('A')
print()
inorder('A')
print()
postorder('A')