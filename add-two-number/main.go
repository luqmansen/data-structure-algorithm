package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	dummy := &ListNode{}
	curr := dummy

	carry := 0
	for (l1 != nil) || (l2 != nil) || carry > 0 {

		var v1 int
		var v2 int

		if l1 != nil {
			if l1.Val != 0 {
				v1 = l1.Val
			} else {
				v1 = 0
			}
		}
		if l2 != nil {
			if l2.Val != 0 {
				v2 = l2.Val
			} else {
				v2 = 0
			}
		}
		val := v1 + v2 + carry
		carry = val / 10 // floor division
		val = val % 10

		curr.Next = &ListNode{Val: val}
		curr = curr.Next
		if l1 != nil {
			l1 = l1.Next
		} else {
			l1 = nil
		}
		if l2 != nil {
			l2 = l2.Next
		} else {
			l2 = nil
		}
	}
	return dummy.Next
}

func main() {
	l1 := &ListNode{Val: 2}
	l1.Next = &ListNode{Val: 4}
	l1.Next.Next = &ListNode{Val: 3}

	l2 := &ListNode{Val: 5}
	l2.Next = &ListNode{Val: 6}

	x := addTwoNumbers(l1, l2)
	fmt.Println(x)
}
