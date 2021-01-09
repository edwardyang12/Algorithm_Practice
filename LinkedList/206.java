/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {

    // Stack to keep track of linked list
    // pop elements in reverse order while connecting
    // O(n) time
    // O(n) space
    public ListNode reverseList(ListNode head) {
        if(head==null){
            return null;
        }
        ListNode temp = head;
        Stack<ListNode> reverse = new Stack<ListNode>();
        while(temp!=null){
            reverse.push(temp);
            temp = temp.next;
        }
        head = reverse.pop();
        temp = head;
        while(!reverse.isEmpty()){
            temp.next = reverse.pop();
            temp = temp.next;
        }
        temp.next = null;
        return head;
    }
}
