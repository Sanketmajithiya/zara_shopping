# Q-1) For a input of two strings X and Y, find the minimum number of steps required to convert X to Y. (each operation is counted as 1 step.)

""" 
You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example:

Input 1:
X = "abad"
Y = "abac"

Output 1:
1

Explanation 1:
Operation 1: Replace d with c.

Input 2:
X = "Insa"
Y = "India"

Output 2:


Explanation 2:
=> Operation 1: Replace s with d.
=> Operation 2: Insert i.

"""

s = "good"
m = "morning"

list1 = list(s)
list2 = list(m)


if len(s)==len(m):
    for i in range(len(s)):
        if s[i] != m[i]:
            print(1)




# even number only in list

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print (my_list[1::2])


# grocery = ["harpic","vim bar","deodrant","Bhindi","Lollypop",56]
# # print(grocery[5])

# # numbers = [2,7,9,11,3]
# numbers = [1,2,3,4,5,6,7,8,9,10]
# # numbers.sort()
# # numbers.reverse()
# print(numbers[::-1])


def minDistance(X, Y):
    m = len(X)
    n = len(Y)
    
    # Create a table to store results of sub-problems
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
    
    # Fill dp[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):
            
            # If first string is empty, only option is to insert all characters of second string
            if i == 0:
                dp[i][j] = j    # Min. operations = j
            
            # If second string is empty, only option is to remove all characters of first string
            elif j == 0:
                dp[i][j] = i    # Min. operations = i
            
            # If last characters are the same, ignore last character and recur for remaining string
            elif X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1]
            
            # If last character is different, consider all possibilities and find the minimum
            else:
                dp[i][j] = 1 + min(dp[i][j-1],      # Insert
                                   dp[i-1][j],      # Remove
                                   dp[i-1][j-1])    # Replace
    
    return dp[m][n]

# Example usage
X = "sitting"
Y = "kitten"
print("Minimum operations required:", minDistance(X, Y))
