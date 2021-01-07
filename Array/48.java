class Solution {


    // rotating 90 degrees clockwise is the same as reflecting across diagonal (0,0) -> (length, length)
    // and then reflecting across center vertical line 
    // O(n^2) time
    // O(1) space
    public void rotate(int[][] matrix) {
        for(int i =0; i<matrix.length; i++){
            for(int j=i; j<matrix[0].length;j++){
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        for(int i =0; i<matrix.length; i++){
            for(int j=0; j<matrix[0].length/2;j++){
               int temp = matrix[i][j];
                matrix[i][j] = matrix[i][matrix[0].length-j-1];
                matrix[i][matrix[0].length-j-1] = temp;
            }
        }
    }
}
