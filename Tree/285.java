class Solution {

    // sucessor is the next largest element
    // successor is always to the right of p
    // case 1: no right child -> go up until you reach first element greater than p
    // case 2: right child -> go right then all the way left
    // O(log(n)) time
    // O(n) space
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        TreeNode temp = root;
        Stack<TreeNode> stack = new Stack<TreeNode>();
        stack.push(null);
        while(temp!=p){
            stack.push(temp);
            if(p.val>temp.val){
                temp = temp.right;
            }
            else{
                temp = temp.left;
            }
        }
        while(temp!=null && temp.val<=p.val){
            if(temp.right!=null){
                temp = temp.right;
                while(temp.left!=null){
                    temp = temp.left;
                }
            }
            else{
                temp = stack.pop();
            }

        }
        return temp;
    }
}
