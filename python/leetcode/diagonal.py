def checkState(state, grid, i, j):
            if state == 1:
                return True
            if grid[i][j] == state:
                return True
            return False

def dfs(grid, i, j, vis, count, m , n, state, res):
    
    if i >= 0 and i < m and j >= 0 and j < n and checkState(state, grid, i, j) and vis[i][j] == False:
        vis[i][j] = True
        
        if state == 1:
            state = 2
        elif state == 2:
            state = 0
        else:
            state = 2
        for row, col in [(-1,-1), (-1, 1), (1, 1), (1, -1)]:
            nrow = i + row
            ncol = j + col
            res[0] = max(res[0], count+1)
            
            dfs(grid, nrow, ncol, vis, count+1, m, n, state, res)
            
        vis[i][j] = False


# grid = [
#      [2,2,1,2,2],
#      [2,0,2,2,0],
#      [2,0,1,1,0],
#      [1,0,2,2,2],
#      [2,0,0,2,2]]

# grid = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
grid = [[2,2,2,2,2],[2,0,0,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
m = len(grid)
n = len(grid[0])


dia = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == 1:
            vis = [[False for _ in range(n)] for _ in range(n)]
            count = 0
            state = 1
            res = [0]
            dfs(grid, i, j, vis, count, m , n, state, res)
            dia = max(dia, res[0])
            
print(dia)
