#User function Template for python3
import heapq
from collections import defaultdict
class Solution:
        
    def MinimumEffort(self, heights):
        n = len(heights)
        m = len(heights[0])
        pqueue = [(0,0,0)]
        distance = [[float("inf")]*m for _ in range(n)]
        distance[0][0] = 0
        while pqueue:
            difference, i,j = heapq.heappop(pqueue)
            if i == n-1 and j == m-1:
                return difference
            directions = [0,-1,0,1,0]
            for k in range(4):
                dx, dy = i + directions[k],j + directions[k+1]
                if 0<= dx < n and 0<= dy < m:
                    diff = max(difference,abs(heights[dx][dy] - heights[i][j]))
                    if diff < distance[dx][dy]:
                        distance[dx][dy] = diff
                        heapq.heappush(pqueue,(diff, dx, dy))
        
        return distance[n-1][m-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n,m=map(int,input().split())
        a=[]
        for i in range(n):
            li=list(map(int,input().split()))
            a.append(li)
        ob = Solution()
        ans = ob.MinimumEffort(a)
        print(ans)
        tc -= 1
# } Driver Code Ends