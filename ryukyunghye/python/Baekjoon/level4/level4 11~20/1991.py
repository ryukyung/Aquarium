# [1991] 트리 순회
n = int(input())
tree = [[0] * 3 for _ in range(26)]


def preorder(x):
    # root -> left -> right
    print(x, end='')
    if tree[ord(x)-65][1] != '.':
        preorder(tree[ord(x)-65][1])
    if tree[ord(x)-65][2] != '.':
        preorder(tree[ord(x)-65][2])


def inorder(x):
    # left -> root -> right
    if tree[ord(x)-65][1] != '.':
        inorder(tree[ord(x)-65][1])
    print(x, end='')
    if tree[ord(x)-65][2] != '.':
        inorder(tree[ord(x)-65][2])


def postorder(x):
    # left -> right -> root
    if tree[ord(x)-65][1] != '.':
        postorder(tree[ord(x)-65][1])
    if tree[ord(x)-65][2] != '.':
        postorder(tree[ord(x)-65][2])
    print(x, end='')


for i in range(n):
    node, left, right = map(str, input().split())
    ordNode = ord(node) - 65
    tree[ordNode][0], tree[ordNode][1], tree[ordNode][2] = node, left, right

preorder("A")
print()
inorder("A")
print()
postorder("A")
