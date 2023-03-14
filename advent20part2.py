class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

ls = [Node(int(x)*811589153) for x in open('input20.txt')]

for i in range(len(ls)):
    ls[i].prev = ls[(i-1)%len(ls)]
    ls[i].next = ls[(i+1)%len(ls)]
    if ls[i].data == 0: zero_index = i

for _ in range(10):
    for node in ls:
        temp = node
        for _ in range(node.data%(len(ls)-1)):
            temp = temp.next
        if temp == node: continue
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = temp.next
        temp.next.prev = node
        temp.next = node
        node.prev = temp

answer = 0
node = ls[zero_index]
for _ in range(3):
    for _ in range(1000):
        node = node.next
    answer += node.data
print(answer)