class Node():
    def __init__(self, value=None, left=None, right=None, name=""):
        self.left = left
        self.right = right
        self.value = value
        self.name = name


def insertNode(NodeList, newnode):
    if len(NodeList) == 0:
        NodeList.append(newnode)
        return
    for index, n in enumerate(NodeList):
        if n.value < newnode.value:
            NodeList.insert(index, newnode)
            break
        if index == len(NodeList)-1:
            NodeList.append(newnode)
            break


def searchcode(node, code):
    if node.name != "":
        Codelist[node.name] = code
        return
    searchcode(node.left, code+"0")
    searchcode(node.right, code+"1")
    return


Nnum = int(input('Type number of Node:'))
Codelist = {}
NodeList = []
TreeNode = []
for i in range(Nnum):
    name, value = input().split(' ')
    newnode = Node(name=name, value=int(value))
    NodeList.append(newnode)
    if len(TreeNode) == 0:
        TreeNode.append(newnode)
    else:
        insertNode(TreeNode, newnode)
while(len(TreeNode) != 1):
    minnode1 = TreeNode.pop()
    minnode2 = TreeNode.pop()
    newnode = Node(value=minnode1.value + minnode2.value,
                   left=minnode1, right=minnode2)
    insertNode(TreeNode, newnode)
searchcode(TreeNode[0], "")

for n in NodeList:
    print(n.name, "  ", Codelist[n.name])
