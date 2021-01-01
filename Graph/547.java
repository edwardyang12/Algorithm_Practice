class Solution {

    // for each element in the graph, dfs search through it and set every
    // "1" to "0" to signify that edge has been visited
    // O(n^2) time
    // O(n^2) space
    public void dfs(int[][] isConnected, int j){
        for(int i = 0;i<isConnected.length;i++){
            if(isConnected[j][i]==1){
                isConnected[j][i]= 0;
                isConnected[i][j] = 0;
                dfs(isConnected,i);
            }
        }
    }

    public int findCircleNum(int[][] isConnected) {
        int provinces = 0;
        for(int i =0; i< isConnected.length;i++){
            if (isConnected[i][i]==1){
                provinces++;
                dfs(isConnected,i);
            }
        }
        return provinces;
    }
}
