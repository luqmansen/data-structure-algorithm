package main

func inOrderTraversalIter(root *TreeNode) []int {
	var result []int
	if root == nil {
		return result
	}

	var nodeStack []*TreeNode
	nodeStack = append(nodeStack, root)

	for len(nodeStack) > 0 {

		if root.Val != nodeStack[len(nodeStack)-1].Val {
			nodeStack = append(nodeStack, root)
		}

		if root.Left != nil {
			root = root.Left
			continue

		} else if root.Left == nil {

			result = append(result, root.Val)

			// pop from stack
			nodeStack = nodeStack[:len(nodeStack)-1]
			root = nodeStack[len(nodeStack)-1]
			root.Left = nil

		} else if root.Right != nil {
			root = root.Right
		} else {
			break
		}

	}
	return result
}
