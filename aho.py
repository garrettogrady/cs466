import time
import os
import resource

class Node:
	def __init__(self):
		self.goto = {}
		self.out = []
		self.fail = None


def aco_forecast(patterns):
	root_node = Node()

	for path in patterns:
		node = root_node
		for symbols in path:
			node = node.goto.setdefault(symbols, Node())
		node.out.append(path)
	return root_node


def aco_statemachine(patterns):
	root = aco_forecast(patterns)
	queue = []
	for node in root.goto.itervalues():
		queue.append(node)
		node.fail = root

	while len(queue) > 0:
		rnode = queue.pop(0)

		for key, u in rnode.goto.iteritems():
			queue.append(u)
			fnode = rnode.fail
			while fnode != None and not fnode.goto.has_key(key):
				fnode = fnode.fail
			u.fail = fnode.goto[key] if fnode else root
			u.out += u.fail.out

	return root


def aho_find_all(s, root, callback):
	node = root

	for i in xrange(len(s)):
		while node != None and not node.goto.has_key(s[i]):
			node = node.fail
		if node == None:
			node = root
			continue
		node = node.goto[s[i]]
		for pattern in node.out:
			callback(i - len(pattern) + 1, pattern)


############################
# Demonstration of work
def on_occurence(pos, patterns):
	x = ""
    #print "At pos %s found pattern: %s" % (pos, patterns)


def aho_main(patterns, sequence):
	root = aco_statemachine(patterns)
	aho_find_all(sequence, root, on_occurence)