class Solution {

    // iterate through grid and for every "1" call DFS and increment number of islands
    // DFS set all 1's in the island to 0
    // O(m x n) time
    // O(m x n) space 

    public void dfs(char[][] grid, int i, int j){
        grid[i][j]='0';
        if(i-1>=0 && grid[i-1][j]=='1'){
            dfs(grid,i-1,j);
        }
        if(i+1<grid.length && grid[i+1][j]=='1'){
            dfs(grid,i+1,j);
        }
        if(j-1>=0 && grid[i][j-1]=='1'){
            dfs(grid,i,j-1);
        }
        if(j+1<grid[0].length && grid[i][j+1]=='1'){
            dfs(grid,i,j+1);
        }
    }

    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) {
            return 0;
        }
        int islands = 0;
        for(int i =0; i <grid.length;i++){
            for(int j=0; j< grid[0].length;j++){
                if(grid[i][j]=='1'){
                    islands++;
                    dfs(grid,i,j);
                }
            }
        }
        return islands;
    }
}
