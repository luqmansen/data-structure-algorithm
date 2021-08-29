package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func detectCycle(head *ListNode) *ListNode {

	seen := make(map[*ListNode]int)
	startIdx := 0

	for head != nil {

		if idx, found := seen[head]; found {
			fmt.Printf("tail connects to node index %d\n", idx)
			return head
		} else {
			seen[head] = startIdx
		}
		startIdx++
		head = head.Next

	}

	fmt.Println("no cycle")
	return head

}
