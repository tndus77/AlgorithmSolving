n = int(input())
count = 0
dp = [0] * (n+1)

for i in range(2, n+1):
  dp[i] = dp[i-1] + 1
  if i % 3 == 0:
    dp[i] = min(dp[i], dp[i//3] + 1) #dp[i]는 이미 위에서 더해줬기 때문에
  if i % 2 == 0:
    dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[n])