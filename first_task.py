
def find_coins_greedy(cost: int, coins: list) -> dict:
    key = 0
    request_coins = {}

    while cost > 0:
        if coins[key] <= cost:
            cost -= coins[key]
            if coins[key] in request_coins:
                request_coins[coins[key]] += 1
            else:
                request_coins[coins[key]] =1
        else:
            key += 1

    return request_coins

