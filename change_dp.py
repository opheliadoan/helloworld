
def change(money):
    min_num_coins = [0]
    denoms = [1, 3, 4]
    for m in range(1, money + 1):
        min_num_coins.append(float("inf"))
        for i in denoms:
            if m >= i:
                num_coins = min_num_coins[m - i] + 1
                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins
    return min_num_coins[money]


if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
