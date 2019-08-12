def knapsack(capacity, items, n):
    """A  method to determine the maximum value of the items included in the
    knapsack without exceeding the capacity  C

    Args:
        capacity(int): full capacity of the bag can fit
        items(tuple of tuples): items with its capacity and value
        n(int): number of items, bag can have

    Returns:
        Max value(int) :
    """

    # base case
    if (n == 0 or capacity == 0):
        return 0
    if (items[n-1][1] > capacity):
        # print(items[n-1][1])
        return knapsack(capacity, items, n-1)

    else:
        no_item = knapsack(capacity, items, n-1)
        in_item = items[n-1][2] + \
            knapsack(capacity - items[n-1][1], items, n-1)
        return max(in_item, no_item)
