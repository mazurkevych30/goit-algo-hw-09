
def find_min_coins(cost: int, coins: list) -> dict:
    dp = [float('inf')] * (cost + 1)
    dp[0] = 0

    coin_count = [dict() for _ in range(cost + 1)]

    for i in range(1, cost + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_count[i] = coin_count[i - coin].copy()
                if coin in coin_count[i]:
                    coin_count[i][coin] += 1
                else:
                    coin_count[i][coin] = 1

    if dp[cost] == float('inf'):
        return {}

    return coin_count[cost]


