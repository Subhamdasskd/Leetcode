class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows = len(land)
        cols = len(land[0])

        done = [[False] * cols for _ in range(rows)]
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def go(x,y):
            if land[x][y] != 1 or done[x][y]:
                return 
            done[x][y] = True

            nonlocal mnx,mny,mxx,mxy
            mnx = min(mnx,x)
            mxx = max(mxx,x)
            mny = min(mny,y)
            mxy = max(mxy,y)

            for dx,dy in directions:
                nx,ny = x +dx, y + dy

                if 0 <= nx < rows and 0 <= ny <cols and land[nx][ny] == 1 and not done[nx][ny]:
                    go(nx,ny)

        ans = []
        for x in range(rows):
            for y in range(cols):
                if land[x][y] == 1 and not done[x][y]:
                    mnx,mny,mxx,mxy = x,y,x,y
                    go(x, y)
                    ans.append([mnx,mny,mxx,mxy])
        return ans                        
            


        