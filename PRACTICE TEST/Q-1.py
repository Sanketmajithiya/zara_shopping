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

Explanation 1:
Operation 1: Replace d with c.

ANS :-
""" 
x = "abad"
y = "1234"

list1 = list(x)
list2 = list(y)
list3 = []
operation = []
step = 0

if len(x)==len(y):
    for i in range(len(x)):
        if list1[i]==list2[i]:
            list3.append(list2[i])
        else:
            list3.append(list2[i])
            step += 1
            operation.append(f"{list1[i]} is replace with {list2[i]}")

print("operations: ",operation)
print("step: ",step)





"""
Input 2:
X = "Insa"
Y = "India"

Output 2:

Explanation 2:
=> Operation 1: Replace s with d.
=> Operation 2: Insert i.

# """
def edit_distance(X, Y):
    m = len(X)
    n = len(Y)

    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
    print(dp)
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j    

            elif j == 0:
                dp[i][j] = i   
           
            elif X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1],        
                                   dp[i-1][j],        
                                   dp[i-1][j-1])    

    return dp[m][n]

X = "Insa"
Y = "India"
print(edit_distance(X, Y))
