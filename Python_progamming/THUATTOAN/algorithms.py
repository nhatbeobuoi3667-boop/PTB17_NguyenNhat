def largest_number(grid,k):
    # khoi tao kich thuoc ma tran
    m = len(grid)
    n = len(grid[0])
    
    a = []
    for i in range(m):
        row = []
        for j in range(n):
            if grid[i][j] == "A":
                row.append(1)
            else:
                row.append(-1)
        a.append(row)
        
    ps = []
    for i in range(m+1):
        ps.append([0]* (n+1))
    
    for i in range(m):
        row_sum = 0
        for j in range(n):
            row_sum += a[i][j]
            ps[i+1][j+1] = ps[i][j+1] + row_sum
        
    def rect_sum(r1,c1,r2,c2):
        return ps[r2+1][c2+1] - ps[r1][c2+1] - ps[r2+1][c1] + ps[r1][c1]
    max_area = 0
    for r1 in range(m):
        for r2 in range(r1,m):
            for c1 in range(n):
                for c2 in range(c1,n):
                    s = rect_sum(r1,c1,r2,c2)
                    if s < 0:
                        s = -s
                    
                    if s<=k:
                        area = (r2 - r1 + 1) * (c2 - c1 + 1)
                        if area > max_area:
                            max_area = area                                  
    return max_area
T = int(input().strip())
for t in range(T):
    m,n,k = map(int,input().strip().split())
    
    grid = []
    for i in range(m):
        row = input().strip()
        grid.append(row)
    print(largest_number(grid,k))