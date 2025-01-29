class Solution {
    
    public int findMaxFish(int[][] grid) {
        int m=grid.length,n=grid[0].length;
        int[][] visit=new int[m][n];
        int ans=0;

        for (int i=0;i<grid.length;i++){
            for (int j=0;j<n;j++){
                if (visit[i][j]==0 && grid[i][j]>0)
               ans=Math.max(ans,dfs(grid,visit,i,j,0)) ;

            }
            System.out.println();
        }
        return ans;
        }
       
    
    public int dfs(int[][] grid,int[][] visit,int i,int j,int sum){
        if(i>=grid.length || j>=grid[0].length || i<0 || j<0 || grid[i][j]==0 )
        return 0;
        visit[i][j]=1;
        sum=grid[i][j];
        if(i+1 <grid.length && visit[i+1][j]==0 && grid[i+1][j]>0) 
        sum=sum+dfs(grid,visit,i+1,j,0);
        if (j+1 <grid[0].length &&visit[i][j+1]==0 && grid[i][j+1]>0)
        sum=sum+dfs(grid,visit,i,j+1,0);
        if(i>0 && visit[i-1][j]==0 && grid[i-1][j]>0) 
        sum=sum+dfs(grid,visit,i-1,j,0);
        if (j>0 && visit[i][j-1]==0 && grid[i][j-1]>0)
        sum=sum+dfs(grid,visit,i,j-1,0);
        
        return sum;
    }
 
}