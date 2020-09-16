'''
Aim is to find the minimum coins required to give change from given coins

ex: for amount 11 and coins = [1, 2, 5]
 one can give changes
 	=> 1, 1,1,1,1,1,1,1,1,1,1
 	=> 1, 5, 5
 	=> in many ways

 	answer is 3 because we need minimum coins
'''

# using recursion

def CoinsChanges(amount, coins):
	if amount in coins: return 1

	min_coins = 10000  # Some Large Number

	for i in [coin for coin in coins if coin <= amount]:
		num_coins = 1 + CoinsChanges(amount-i, coins)
		min_coins = min(min_coins, num_coins)


	return min_coins


# using Recursion with memorization
# this is Top Down Approach

def CoinsChange_memo(amount, coins, memo_dict = {}):
	if amount in memo_dict: return memo_dict[amount]

	#print(memo_dict)

	if amount in coins: return 1

	min_coins = 10000

	for i in [coin for coin in coins if coin <= amount]:
		num_coins = 1 + CoinsChange_memo(amount-i, coins, memo_dict)
		min_coins = min(min_coins, num_coins)

	memo_dict[amount] = min_coins	

	return min_coins


print("memo")

#print(CoinsChange_memo(30, [1, 2, 5]))


# next same problem using Tabular Approach
# using Bottom - Up


def CoinsChange_tabular(amount, coins):
	look_up = [-1] * (amount + 1)
	look_up[0] = 0

	for amt in range(1, amount + 1):
		for i in [coin for coin in coins if coin <= amt]:
			tot = 1 + look_up[amt - i]

		look_up[amt] = tot

	return look_up[-1]



print("Tabular")
print(CoinsChange_tabular(13, [1, 2, 5]))