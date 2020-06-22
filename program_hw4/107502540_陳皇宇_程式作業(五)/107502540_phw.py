import sys
vnum, enum = input("").split(" ")
vnum, enum = int(vnum), int(enum)
Vset = []
Eset = {}
Vtmp = []
Anspath = []


class Vertex:
    def __init__(self):
        self.selfloop = 0
        self.edge = []


class Edge:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.visied = False

# sys.setrecursionlimit(10000)


def checkdone():
    for e in Eset:
        if not Eset[e].visied:
            return False
    return True


def DFSbyWhile():
    stack = []
    stack.append([list(Vset.keys())[0], Vset[list(Vset.keys())[0]].edge[0]])
    back = False
    while len(stack) != 0:
        recur = stack[-1]
        if back:
            Anspath.append(recur[1])
        ve = Vset[recur[0]].edge
        bre = False
        back = False
        if ve != []:
            stack[-1][1] = ve[0]
            stack.append([str(ve[0]), 0])
            Vset[str(ve[0])].edge.remove(int(recur[0]))
            del Vset[recur[0]].edge[0]
            bre = True
        if bre:
            continue
        stack.pop()
        back = True


for i in range(enum):
    v1, v2 = input("").split(" ")
    v1, v2 = int(v1), int(v2)
    Vset.append(v1)
    Vtmp.append(v2)
    Eset[str(i)] = Edge(v1, v2)
Vtmp.extend(Vset)
Vtmp = list(set(Vtmp))
Vset = {}
for v in Vtmp:
    Vset[str(v)] = Vertex()
for e in Eset:
    edg = Eset[e]
    if edg.v1 == edg.v2:
        Vset[str(edg.v1)].edge.append(edg.v2)
        Vset[str(edg.v1)].selfloop += 1
    else:
        Vset[str(edg.v1)].edge.append(edg.v2)
        Vset[str(edg.v2)].edge.append(edg.v1)
done = False
for v in Vset:
    vert = Vset[v]
    if (len(vert.edge) - vert.selfloop) % 2 != 0:
        done = True
        break
    else:
        vert.edge = sorted(vert.edge)
if done:
    print("not exist")
else:
    DFSbyWhile()
    # DFS(Vset[list(Vset.keys())[0]])
    if len(Anspath) == len(Eset):
        Anspath.append(int(list(Vset.keys())[0]))
        Anspath = Anspath[::-1]
        for i in Anspath:
            print(i, end=' ')
    else:
        print("not exist")
