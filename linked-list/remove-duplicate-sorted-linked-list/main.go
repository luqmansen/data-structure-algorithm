package main

import (
	"fmt"
	"github.com/luqmansen/data-structure-algorithm/utils"
)

func deleteDuplicates(head *utils.ListNode) *utils.ListNode {

	curr := head
	var prevNode *utils.ListNode

	for curr != nil {
		if prevNode != nil {
			if prevNode.Val == curr.Val {
				tempNextNode := curr.Next
				curr = prevNode
				curr.Next = tempNextNode
			}
		}
		prevNode = curr
		curr = curr.Next
	}
	return head
}
func main() {

	//l1 := utils.CreateLinkedList([]int{0,1,1,2,2,3}) // 0 1 2 3
	l1 := utils.CreateLinkedList([]int{0, 0, 0}) // 0
	x := deleteDuplicates(l1)
	fmt.Println(x)

}
