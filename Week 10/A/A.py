import sys

class SmartestUnionFind:
    def __init__(self, N):
        """ A good and fast Union-Find data structure. """
        self.parent = list(range(N))
        self.sizes = [1] * N

    def find(self, i):
        """ Finds the root of the disjoint set that `i` is in. """
        if self.parent[i] == i:
            return i
        parent = self.find(self.parent[i])
        self.parent[i] = parent
        return parent

    def union(self, i, j):
        """ Unites the disjoint sets that `i` and `j` are in. """
        i_root, j_root = self.find(i), self.find(j)
        if i_root == j_root: return
        if self.sizes[i_root] <= self.sizes[j_root]:
            i_root, j_root = j_root, i_root
        # j_root is now the smaller tree, so hang it under i_root.
        self.parent[j_root] = i_root

        # TODO: update the sizes array accordingly.
        self.sizes[i_root] += self.sizes[j_root]

    def same_set(self, i, j):
        """ Returns whether `i` and `j` are in the same disjoint set. """
        return self.find(i) == self.find(j)

    def size(self, i):
        """ Returns the size of the tree that `i` is in. """
        root = self.find(i)
        return self.sizes[root]

firstline = sys.stdin.readline().split()
guests = int(firstline[0])
queries = int(firstline[1])
UF = SmartestUnionFind(guests + 1)

for i in range(queries):
    line = sys.stdin.readline().split()
    if(line[0] == 't'):
        UF.union(int(line[1]), int(line[2]))
    elif(line[0] == 's'):
        print(UF.size(int(line[1])))
