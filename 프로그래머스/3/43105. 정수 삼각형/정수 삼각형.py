def solution(triangle):
    height = len(triangle)
    width = len(triangle[height - 1])
    dp = [[0 for _ in range(width)] for _ in range(height)]
    
    dp[0][0] = triangle[0][0]
    for y in range(1, height):
        for x in range(y + 1):
            dp[y][x] = triangle[y][x] + max(dp[y - 1][x], dp[y - 1][x - 1])    
    
    return max(dp[height - 1])