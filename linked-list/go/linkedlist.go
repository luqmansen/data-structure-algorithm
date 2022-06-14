package linked_list

// Doubly linked list
type Node struct {
	next *Node
	prev *Node
	val  int
}

type LinkedList struct {
	head *Node
	tail *Node
}

func (l *LinkedList) InsertHead(data int) {
	newNode := &Node{
		next: nil,
		val:  data,
	}

	if l.head == nil {
		newNode.prev = newNode
		l.head = newNode
		l.tail = newNode

	} else { //	 head exists
		// store existing head temporarily
		tempHead := l.head
		// point prev of existing head to new node
		tempHead.prev = newNode
		// set new head with new node
		l.head = newNode
		// set next node after head with previous head
		l.head.next = tempHead
	}
}

func (l *LinkedList) DeleteHead() {
	if l.head == nil {
		return
	} else {
		newHead := l.head.next
		l.head = newHead
	}
}
