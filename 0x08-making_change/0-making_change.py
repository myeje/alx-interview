#!/usr/bin/python3
def makeChange(coins, total):
    if total < 0:
        return 0
    tp = [float('inf')] * (total + 1)
    tp[0] = 0
    
    for coin in coins:
        for i in range(coin, total + 1):
            tp[i] = min(tp[i], tp[i - coin] + 1)

    if tp[total] == float('inf'):
        return -1
    else:
        return tp[total]
