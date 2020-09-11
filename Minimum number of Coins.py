# Greedy Algorithm to find Minimum number of Coins
# Given a value V, if we want to make a change for V Rs, and we
# have an infinite supply of each of the denominations in Indian currency, i.e.,
# we have an infinite supply of {1, 2, 5, 10, 20, 50, 100, 500, 1000} valued coins/notes,
# what is the minimum number of coins and / or notes needed to make the change?
# Examples:

# Input: V = 70
# Output: 2
# We need a 50 Rs note and a 20 Rs note.

# Input: V = 121
# Output: 3
# We need a 100 Rs note, a 20 Rs note and a 1 Rs coin.


def numberOfCoin(V):
    deno = [1, 2, 5, 10, 20, 50,
            100, 500, 1000]

    K = V
    num = 0
    for i in reversed(range(0, len(deno))):
        if(K == 0):
            return num
            break
        else:
            if(K >= deno[i]):
                num = num + 1
                K -= deno[i]


if __name__ == '__main__':
    V = int(input())
    print(numberOfCoin(V))
