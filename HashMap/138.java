/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {

        // Hashmap{old Node: new Node}
        // make copy of all nodes to new nodes in hashmap
        // make connections between new nodes based on connectiosn of old nodes
        // O(n) time
        // O(n) space
        HashMap<Node,Node> map = new HashMap<Node,Node>();
        Node temp = head;
        while(temp!=null){
            Node deep = new Node(temp.val);
            map.put(temp,deep);
            temp = temp.next;

        }
        temp = head;
        while(temp!=null){
            Node random = temp.random;
            Node deep = map.get(temp);
            if(random==null){
                deep.random = null;
            }
            else{
                deep.random = map.get(random);
            }
            if(temp.next==null){
                deep.next = null;
            }
            else{
                deep.next = map.get(temp.next);
            }
            temp = temp.next;

        }

        return map.get(head);
    }
}
