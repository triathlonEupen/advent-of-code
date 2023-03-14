class node(object):
    def __init__(self):
        self.name=None
        self.node=[]
        self.size=0
        self.prev=None
    def prev(self):
        return self.prev
    def goto(self,data):
        for child in self.node:
            if(child.name==data):
                return child
    def add(self,name,size):
        node1=node()
        node1.name=name
        node1.size=size
        self.node.append(node1)
        node1.prev=self
        return node1

def readTree(tree):
    for line in open('input07.txt'):
        current = line.strip().split()
        if (current[0] == '$'):
            if (current[1] == 'cd'):
                if (current[2] == '..'):
                    tree=tree.prev
                else:
                    tree=tree.goto(current[2])
        elif (current[0] == 'dir'):
            tree.add(current[1],0)
        else:
            tree.add(current[1],int(current[0]))
    tree=tree.prev
    tree=tree.prev

def find_dir_sizes(tree):
    if tree.size>0: return tree.size
    x=0
    for child in tree.node:
        x = x+find_dir_sizes(child)
    tree.size=x
    return x

def find_the_one(tree):
    if tree.size<2558312: return 42558312
    currentmin=tree.size
    for child in tree.node:
        current = find_the_one(child)
        if current<currentmin and current>=2558312:
            currentmin=current
    return currentmin

tree=node()
readTree(tree)
find_dir_sizes(tree)
print(find_the_one(tree))
