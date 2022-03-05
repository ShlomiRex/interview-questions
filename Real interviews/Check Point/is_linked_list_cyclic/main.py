class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next


def isCyclic(head: Node) -> bool:
	if head is None or head.next is None:
		return False
	slow, fast = head, head

	# If either hare or tortoise are null, means there is no cyclce
	while head and fast:
		slow = slow.next
		fast = fast.next.next
		# Compare memory address (each node is stored in memory)
		if slow == fast:
			return True
	return False


if __name__ == "__main__":
	# 0 -> 1 -> 2 -> 3 -> None
	node3 = Node(3)
	node2 = Node(2, node3)
	node1 = Node(1, node2)
	head = Node(0, node1)
	res = isCyclic(head)
	assert res == False

	# Cycle at node 1
	# 0 -> 1 -> 2 -> |
	#      ^---------|
	node2 = Node(2)
	node1 = Node(1, node2)
	head = Node(0, node1)
	node2.next = node1
	res = isCyclic(head)
	assert res == True

	head = Node(0)
	res = isCyclic(head)
	assert res == False

	head = None
	res = isCyclic(head)
	assert res == False

	# Cycle 0 -> 1 and 1 -> 0
	node1 = Node(1)
	head = Node(0, node1)
	node1.next = head
	res = isCyclic(head)
	assert res == True
