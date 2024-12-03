def print_world(world, n):
    for _ in range(n):
        print(world[_])
    print("* * * * * * * * * * * * *")

class Node:
    def __init__(self, x, y, data):
        self.data = data
        self.x = x
        self.y = y
        self.next = None
        self.tail = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail=None
    def add_node(self,x,y, data):
        new_node = Node(x,y,data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        current = self.head
        while current:
            print(current.x, current.y, current.data, end=" -> ")
            current = current.next
        print("None")

    def change_world(self):

list1 = LinkedList()
list2 = LinkedList()

list1.add_node(1,2,3)
list1.add_node(4,5,6)
list1.add_node(9,8,7)

list2.add_node(10,20,30)
list2.add_node(20,30,40)
list2.add_node(30,40,50)

# Display both linked lists
print("List 1:")
list1.display()

print("List 2:")
list2.display()
# 다음 노드에 현재 노드의 위치 정보만 전달
# 노드 정보들을 바탕으로 grid update
#
# def prev(world, x, y):
#
#     if world[y][x] == 1:
#     # find_near_4
#     # change_4_to_1
#     elif world[y][x] == 2:
#     # result = find_near_1 or 2 or 3
#     # change_1_to_2 or change 2_to_3
#     elif world[y][x] == 3:
#     # find_near_2
#     # change 3_to_4
#     else:  # skip
#
#     for _ in range(4):
#         nx, ny = x + dx[_], y + dy[_]
#
#         world[y][x]
#
#
# def next_(world):
#
#
# import sys
#
# input = sys.stdin.readline
#
# n, m, k = map(int, input().split())
#
# world = [list(map(int, input().split())) for _ in range(n)]
#
# print_world(world, n)
#
# dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]