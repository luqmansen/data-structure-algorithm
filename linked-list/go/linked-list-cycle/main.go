/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

// with hashmap solution
// time complexity O(n)
// space complexity O(n)
func hasCycle2(head *ListNode) bool {
    nodeMap := make(map[*ListNode]struct{})
    
    for head != nil {
        
        if _, found := nodeMap[head]; found {
            return true
        } else {
            nodeMap[head] = struct{}{}
        }
        head = head.Next
        
    }
    return false
}

// double pointer solution
// time complexity O(n)
// space complexity O(1)
func hasCycle(head *ListNode) bool {
    
    slow := head
    fast := head
    
    for slow != nil && fast != nil && fast.Next != nil {
                
        slow = slow.Next
        fast = fast.Next.Next
        if slow == fast {
            return true
        }
        
    }
    return false
    
}














