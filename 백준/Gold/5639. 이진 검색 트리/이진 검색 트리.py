import sys
sys.setrecursionlimit(2*10**5)


class Node: 
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BST:
  def __init__(self, root):
    self.root = root

  def insert(self, value):
    self.current_node = self.root
    while True:
      if value < self.current_node.value: # 루트 노드보다 파라미터로 받은 값이 작으면 -> left에 위치해야 됨.
        if self.current_node.left != None: # 루트 노드 왼쪽 노드가 이미 차 있다면?
          self.current_node = self.current_node.left # 루트 노드를 기존 루트 노드의 왼쪽 노드로 바꿔주고 다시 반복문 돌기
        else:
          self.current_node.left = Node(value) # 루트 노드 왼쪽에 파마미터로 받은 값 넣어주기
          break
      else:
        if self.current_node.right != None:
          self.current_node = self.current_node.right
        else:
          self.current_node.right = Node(value)
          break

# 후위 순회 출력

def post_order(node):
  if node.left != None:
    post_order(node.left)
  if node.right != None:
    post_order(node.right)
  print(node.value)

# 입력 끝날때까지
arr = []

while True:
  try:
      n = int(sys.stdin.readline().rstrip())
      if n == "":
          break
      arr.append(n)
  except:
      break


## 이진 탐색 트리 만들기
root = Node(arr[0])
bst = BST(root)

for i in range(1,len(arr)):
  bst.insert(arr[i])

post_order(root)

