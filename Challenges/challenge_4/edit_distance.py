# A Dynamic Programming based Python program for edit
# distance problem


def edit_distance(str1, str2, m, n):
    """Given two strings str1 and str2 and below operations that can performed
    on str1. Find minimum number of edits (operations) required to convert
    ‘str1’ into ‘str2’.
    1.Insert
    2.Remove
    3.Replace
    All of the above operations are of equal cost.

    Args:
        str1(str): First string(word)
        str2(str): Second string(word)
        m(int): length of 1st string
        n(int): length of 2nd string

    Returns:
        changes(int): number of changes need to be made in order to make two
        strings equal
    """
    # Create a table to store results of subproblems
    recursion_table = [[0 for x in range(n+1)] for x in range(m+1)]

    # Fill d[][] in bottom up manner
    for i in range(m+1):
        for j in range(n+1):

            # If first string is empty, only option is to
            # insert all characters of second string
            if i == 0:
                recursion_table[i][j] = j    # Min. operations = j

            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                recursion_table[i][j] = i    # Min. operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i-1] == str2[j-1]:
                recursion_table[i][j] = recursion_table[i-1][j-1]

            # If last character are different, consider all
            # possibilities and find minimum
            else:
                recursion_table[i][j] = 1 + min(recursion_table[i][j-1],  # Insert
                                   recursion_table[i-1][j],        # Remove
                                   recursion_table[i-1][j-1])    # Replace

    return recursion_table[m][n]


# Driver program
str1 = "cat"
str2 = "cut"
print(edit_distance(str1, str2, len(str1), len(str2)))
