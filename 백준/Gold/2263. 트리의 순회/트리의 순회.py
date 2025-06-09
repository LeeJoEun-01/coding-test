import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().rstrip())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# 노드의 인덱스 미리 저장
index_dic = {value: index for index, value in enumerate(inorder)}


def find_root(in_left, in_right, post_left, post_right):
    if in_left > in_right:
        return

    root = postorder[post_right]
    print(root)

    root_index = index_dic[root]
    diff = root_index - in_left  # inorder 배열에서 왼쪽 노드들의 수

    # 왼쪽 자식 탐색
    find_root(in_left, root_index-1, post_left, post_left+diff-1)
    # 오른쪽 자식 탐색
    find_root(root_index+1, in_right, post_left+diff, post_right-1)


find_root(0, N-1, 0, N-1)