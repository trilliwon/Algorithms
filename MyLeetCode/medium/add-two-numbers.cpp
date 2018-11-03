/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.next = nil
 *     }
 * }
 */
class Solution {
	
	func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
		let ln: ListNode? = ListNode(0)
		var listNode: ListNode? = ln
		
		var l1 = l1
		var l2 = l2
		
		while true {
			
			var value = 0
			
			if let l1 = l1 {
				value += l1.val
			}
			
			if let l2 = l2 {
				value += l2.val
			}
			
			if l1 != nil {
				l1 = l1?.next
			}
			
			if l2 != nil {
				l2 = l2?.next
			}
			
			if value >= 10 {
				listNode?.val += value - 10
				listNode?.next = ListNode(1)
			} else {
				listNode?.val += value
				
				if (listNode?.val)! >= 10 {
					listNode?.val = (listNode?.val)! - 10
					listNode?.next = ListNode(1)
				} else if l1 != nil || l2 != nil {
					listNode?.next = ListNode(0)
				}
			}
			
			if listNode?.next != nil {
				listNode = listNode?.next
			}
			
			if l1 == nil && l2 == nil {
				break
			}
		}
		return ln
	}
}

