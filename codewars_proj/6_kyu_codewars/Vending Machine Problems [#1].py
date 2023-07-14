def optimal_number_of_coins(n, coins):
    numers = [float('inf') for x in range(n+1)]
    numers[0] = 0
    for coin in coins:
        for amount in range(len(numers)):
            if coin <= amount:
                numers[amount] = min(numers[amount], 1 + numers[amount - coin])
    return numers[n] if numers[n] != float("inf") else -1