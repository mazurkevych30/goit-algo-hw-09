import time
from first_task import find_coins_greedy
from second_task import find_min_coins


cost = 113
coins = [50, 25, 10, 6, 5, 2, 1]

start_time = time.time()
greedy_result = find_coins_greedy(cost, coins)
greedy_time = time.time() - start_time

start_time = time.time()
dp_result = find_min_coins(cost, coins)
dp_time = time.time() - start_time

print(f"Greedy Algorithm Time: {greedy_time:.6f} seconds")
print(f"DP Algorithm Time: {dp_time:.6f} seconds")

print("Greedy Algorithm Result:", greedy_result)
print("DP Algorithm Result:", dp_result)