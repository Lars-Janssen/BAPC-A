import sys

class UnionFind:
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

def find_differences(samples, sample_amount, length):
    difference_array = []
    for i in range(len(samples)):
        for y in range(i):
            difference = 0
            for p in range(length):
                if(samples[i][p] != samples[y][p]):
                    difference += 1
            difference_array.append([i, y, difference])
            difference_array.append([y, i, difference])
    return difference_array

def Kruskal(sample_amount, difference_array):
    difference_array.sort(key = lambda x:x[2])
    edges = [0]

    UF = UnionFind(sample_amount)
    MST_weight = 0
    for a, b, w in difference_array:
        if not UF.same_set(a, b):
            UF.union(a,b)
            MST_weight += w
            edges.append([b,a])
    edges[0] = MST_weight
    return edges


firstline = sys.stdin.readline().split()
sample_amount = int(firstline[0])
length = int(firstline[1])
samples = [sys.stdin.readline().strip() for i in range(sample_amount)]
difference_array = find_differences(samples, sample_amount, length)
data = Kruskal(sample_amount, difference_array)

print(data[0])
for i in range(1, len(data)):
    print(data[i][0], end = " ")
    print(data[i][1])