/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

    // hashSet to store all boundary elements
    // preorder for left hand side elements
    // postorder for right hand side elements
    // O(n) time
    // O(n) memory
    // *simple solution would be arraylist concatention of left, leaves, reverse(right) all using preorder traversal

    public void postOrder(TreeNode root, List<Integer> output, HashSet<TreeNode> boundary, TreeNode curr){
        if(curr!=root && curr.left!=null){
            postOrder(root,output,boundary,curr.left);
        }
        if(curr.right!=null){
            postOrder(root,output,boundary,curr.right);
        }
        if(boundary.contains(curr)&&curr!=root){
            output.add(curr.val);
        }
    }

    public List<Integer> boundaryOfBinaryTree(TreeNode root) {

        List<Integer> output = new ArrayList<Integer>();
        HashSet<TreeNode> boundary = new HashSet<TreeNode>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode temp = root;

        if(root==null){
            return output;
        }

        boundary = getBoundary(root,boundary,stack);
        // preorder for left side and postorder for right side
        stack.push(temp);
        while(!stack.isEmpty()){
            temp = stack.pop();
            if(boundary.contains(temp)){
                output.add(temp.val);
            }
            if(temp!=root && temp.right!=null){
                stack.push(temp.right);
            }
            if(temp.left!=null){
                stack.push(temp.left);
            }
        }
        temp = root;
        postOrder(temp,output,boundary,temp);
        return output;
    }

    public HashSet<TreeNode> getBoundary(TreeNode root, HashSet<TreeNode> boundary, Stack<TreeNode> stack){
        TreeNode temp = root;
        boundary.add(temp);
        stack.push(temp);
        while(temp.left!=null || temp.right!=null){
            if(temp.left!=null){
                temp= temp.left;
            }
            else{
                if(temp==root){
                    boundary.add(temp);
                    break;
                }
                temp = temp.right;
            }
            boundary.add(temp);
        }
        temp = root;
        while(temp.left!=null || temp.right!=null){
            if(temp.right!=null){
                temp= temp.right;
            }
            else{
                if(temp==root){
                    boundary.add(temp);
                    break;
                }
                temp = temp.left;
            }
            boundary.add(temp);
        }
        while(!stack.isEmpty()){
            temp = stack.pop();
            if(temp.right==null && temp.left==null){
                boundary.add(temp);
            }
            else{
                if(temp.left!=null){
                    stack.push(temp.left);
                }
                if(temp.right!=null){
                    stack.push(temp.right);
                }
            }
        }
        return boundary;
    }
}
