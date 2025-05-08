def min_coins(coins: list[int], V: int) -> list[int]:
    coins.sort(reverse=True)
    result = []
    for coin in coins:
        while V >= coin:
            V -= coin
            result.append(coin)
    return result

# Example usage
if __name__ == "__main__":
    coins = [1, 2, 5, 10, 20, 50, 100, 500, 2000]
    V = 93
    print(min_coins(coins, V))  # Output: [50, 20, 20, 2, 1]
