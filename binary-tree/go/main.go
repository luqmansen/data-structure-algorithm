package main

import (
	"fmt"
	"github.com/luqmansen/data-structure-algorithm/utils"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

//Pre-order traversal is to visit the root first.
//Then traverse the left subtree.
//Finally, traverse the right subtree.
func preorderTraversal(root *TreeNode) []int {
	stack := make([]int, 0)
	preOrder(root, &stack)
	return stack
}

func preOrder(root *TreeNode, stack *[]int) {
	if root == nil {
		return
	}

	*stack = append(*stack, root.Val)
	preOrder(root.Left, stack)
	preOrder(root.Right, stack)
}

//In-order traversal is to traverse the left subtree first.
//Then visit the root.
//Finally, traverse the right subtree.
func inorderTraversal(root *TreeNode) []int {
	stack := make([]int, 0)
	inOrder := func(root *TreeNode, stack *[]int) {}
	inOrder = func(root *TreeNode, stack *[]int) {
		if root == nil {
			return
		}
		inOrder(root.Left, stack)
		*stack = append(*stack, root.Val)
		inOrder(root.Right, stack)
	}
	inOrder(root, &stack)
	return stack
}

//Post-order traversal is to traverse the left subtree first.
//Then traverse the right subtree.
//Finally, visit the root.
func postorderTraversal(root *TreeNode) []int {
	stack := make([]int, 0)
	postOrder := func(root *TreeNode, stack *[]int) {}
	postOrder = func(root *TreeNode, stack *[]int) {
		if root == nil {
			return
		}
		postOrder(root.Left, stack)
		postOrder(root.Right, stack)
		*stack = append(*stack, root.Val)
	}
	postOrder(root, &stack)
	return stack
}

func levelOrderQueue(root *TreeNode) (res [][]int) {
	if root == nil {
		return
	}

	queue := make([]*TreeNode, 0)

	res = append(res, []int{root.Val})

	queue = append(queue, root)

	for len(queue) > 0 {

		root = queue[0]
		queue = queue[1:]

		if root.Left != nil {
			queue = append(queue, root.Left)
		}
		if root.Right != nil {
			queue = append(queue, root.Right)

		}
	}

	return res
}

func levelOrder(root *TreeNode) (res [][]int) {

	if root == nil {
		return
	}

	levelDict := make(map[int][]int)
	maxLevel := 0

	travers := func(root *TreeNode, dict map[int][]int, level int) {}

	travers = func(root *TreeNode, dict map[int][]int, level int) {

		if root != nil {
			maxLevel = utils.Max(maxLevel, level)

			if _, found := dict[level]; !found {
				dict[level] = []int{root.Val}
			} else {
				dict[level] = append(dict[level], root.Val)
			}

			travers(root.Left, dict, level+1)
			travers(root.Right, dict, level+1)
		}

	}

	travers(root, levelDict, 0)
	res = make([][]int, maxLevel+1)
	for i := 0; i <= maxLevel; i++ {
		res[i] = levelDict[i]
	}

	return res
}
func main() {
	//tree := &TreeNode{Val: 1, Right: &TreeNode{Val: 2, Left: &TreeNode{Val: 3}}}
	tree := &TreeNode{Val: 1, Left: &TreeNode{Val: 2}, Right: &TreeNode{Val: 3}}

	//fmt.Println(preorderTraversal(tree))
	fmt.Println(inOrderTraversalIter(tree))
	//fmt.Println(inorderTraversal(tree))
	//fmt.Println(levelOrder(tree))
}
