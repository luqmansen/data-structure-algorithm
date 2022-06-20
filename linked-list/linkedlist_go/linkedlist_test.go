package linked_list

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestLinkedList_InsertHead(t *testing.T) {
	ll := LinkedList{}

	ll.InsertHead(1)
	ll.InsertHead(2)
	ll.InsertHead(3)

	assert.Equal(t, 3, ll.head.val)
	assert.Equal(t, 2, ll.head.next.val)
	assert.Equal(t, 1, ll.head.next.next.val)

	assert.Nil(t, ll.head.prev)
	assert.Equal(t, 3, ll.head.next.prev.val)
	assert.Equal(t, 2, ll.head.next.next.prev.val)

}
func TestLinkedList_DeleteHead(t *testing.T) {
	ll := LinkedList{}

	ll.InsertHead(1)
	ll.InsertHead(2)
	ll.InsertHead(3)

	ll.DeleteHead()
	assert.Equal(t, ll.head.val, 2)
	ll.DeleteHead()
	assert.Equal(t, ll.head.val, 1)
}
