A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

# Time complexity: o(n^2) n is the size of the array
#  Space complexity: 0(l) l is the constant
def buy_and_sell_once(A):
    max_profit = 0
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            if A[j] - A[i] > max_profit:
                max_profit = A[j] - A[i]
    return max_profit

def buy_and_sell_secondapproach(A):
    min_buy = A[0]
    profit = 0
    for i in range(len(A)):
        if A[i] < min_buy:
            min_buy = A[i]
        else:
            if A[i] - min_buy > profit:
                profit = A[i] - min_buy
    return profit

# Time complexity: o(n) n is the size of the array
#  Space complexity: 0(l) l is the constant
def buy_and_sell_thirdapproach(A):
    min_price = A[0]
    max_profit = 0
    for price in A:
        min_price = min(min_price, price)
        compare_profit = price - min_price
        max_profit = max(max_profit, compare_profit)

    return max_profit

print(buy_and_sell_once(A))
print(buy_and_sell_secondapproach(A))
print(buy_and_sell_thirdapproach(A))