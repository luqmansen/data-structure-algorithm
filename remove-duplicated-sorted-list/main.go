package main

import (
	"fmt"
	"github.com/luqmansen/data-structure-algorithm/utils"
)

func deleteDuplicates(head *utils.ListNode) *utils.ListNode {

	curr := head
	nodeMap := make(map[int]int)
	mapKeys := make([]int, 0)
	for curr != nil {
		if _, found := nodeMap[curr.Val]; found {
			nodeMap[curr.Val] += 1
		} else {
			mapKeys = append(mapKeys, curr.Val)
			nodeMap[curr.Val] = 1
		}
		curr = curr.Next
	}
	update := &utils.ListNode{}
	curr = update

	for _, i := range mapKeys {
		if cnt, found := nodeMap[i]; found {
			if cnt == 1 {
				curr.Next = &utils.ListNode{Val: i}
				curr = curr.Next
			}
		}
	}
	return update.Next
}

func main() {

	//l1 := utils.CreateLinkedList([]int{0,1,1,2,2,3}) // 0 3
	//l1 := utils.CreateLinkedList([]int{1, 2, 3, 3, 4, 4, 5}) // 1 2 5
	//l1 := utils.CreateLinkedList([]int{1, 1, 1, 2, 3}) //  2 3
	//l1 := utils.CreateLinkedList([]int{0,0,0,0,3}) //   3
	l1 := utils.CreateLinkedList([]int{1, 2, 3, 3, 4, 4, 5}) //   3

	x := deleteDuplicates(l1)
	fmt.Println(x)
}
