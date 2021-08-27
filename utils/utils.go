package utils

import (
	sort "sort"
	"strings"
)

func Max(x, y int) int {
	if x < y {
		return y
	}
	return x
}

func ListToSetString(input []string) []string {
	sets := make(map[string]bool, 0)
	output := make([]string, 0)

	for _, val := range input {
		if _, found := sets[val]; !found {
			sets[val] = true
			output = append(output, val)
		}
	}
	return output
}

func ListToSetInt(input []int) []int {
	sets := make(map[int]bool, 0)
	output := make([]int, 0)

	for _, val := range input {
		if _, found := sets[val]; !found {
			sets[val] = true
			output = append(output, val)
		}
	}
	return output
}

func IsAnagram(a, b string) bool {

	m := strings.Split(a, "")
	n := strings.Split(b, "")

	sort.Strings(m)
	sort.Strings(n)

	if strings.Join(m, "") == strings.Join(n, "") {
		return true
	}
	return false
}

func SumTwoArray(arrA, arrB []int) (sumA, sumB int) {

	for idx, _ := range arrB {
		sumB += arrB[idx]
		if idx < len(arrA) {
			sumA += arrA[idx]
		}
	}
	return sumA, sumB
}

type ListNode struct {
	Val  int
	Next *ListNode
}

func (receiver ListNode) String() string {
	return string(rune(receiver.Val))
}

func CreateLinkedList(arr []int) *ListNode {
	dummy := &ListNode{}
	curr := dummy

	for _, val := range arr {
		newNode := &ListNode{Val: val}
		curr.Next = newNode
		curr = curr.Next
	}

	return dummy.Next
}
