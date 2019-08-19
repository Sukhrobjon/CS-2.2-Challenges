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
        print(items[n-1])
        return knapsack(capacity, items, n-1)

    else:
        no_item = knapsack(capacity, items, n-1)
        in_item = items[n-1][2] + knapsack((capacity - items[n-1][1]), items, n-1)
        print("no", no_item)
        print("in", in_item)
        return max(in_item, no_item)


if __name__ == "__main__":

    items = (("boot", 10, 60),
             ("tent", 20, 100),
             ("water", 30, 120),
             ("first aid", 15, 70))

    n = len(items)
    capacity = 50
    opt_val = knapsack(capacity, items, n)
    # printing the output
    # print("For this input: \nitems = ", end="")
    # print(*items, sep="\n")
    # print(f"Capacity of Knapsack: {capacity}")
    print(f"The value of the optimal solution to the knapsack problem is V = {opt_val}")

    print("The items included in the knapsack for this optimal solution are")
