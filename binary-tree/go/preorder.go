package main

func preOrderTraversalIter(root *TreeNode) []int {
	var result []int
	var nodestack []*TreeNode

	if root == nil {
		return result
	}

	nodestack = append(nodestack, root)

	for len(nodestack) > 0 {

		node := nodestack[len(nodestack)-1]
		nodestack = nodestack[:len(nodestack)-1]

		if node != nil {
			result = append(result, node.Val)
		}

		if node.Right != nil {
			nodestack = append(nodestack, node.Right)
		}

		if node.Left != nil {
			nodestack = append(nodestack, node.Left)
		}

	}
	return result
}
