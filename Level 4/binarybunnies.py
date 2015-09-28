from collections import defaultdict
from math import factorial

def buildTree(seq):
	tree = defaultdict(lambda : [None, None])
	tree[seq[0]]
	def insert(root, val):
		if root < val:
			if tree[root][1] is None:
				tree[root][1] = val
			else:
				insert(tree[root][1], val)
		else:
			if tree[root][0] is None:
				tree[root][0] = val
			else:
				insert(tree[root][0], val)
	for i in xrange(1, len(seq)):
		insert(seq[0], seq[i])
		tree[seq[i]]
	return tree

def C(n, k):
	return factorial(n) / (factorial(n - k) * factorial(k))

def answer(seq):
	if not seq:
		return str(0)
	tree = buildTree(seq)
	size = {}
	def Count(root):
		if root is None:
			size[root] = 0
			return 1
		leftRoot, rightRoot = tree[root]
		lCount = Count(leftRoot)
		rCount = Count(rightRoot)
		size[root] = 1 + size[leftRoot] + size[rightRoot]
		return C(size[root] - 1, size[leftRoot]) * lCount * rCount
	return str(Count(seq[0]))
