# In the hostel, there are birthday celebrations every month. Given N number of days which are representing the birthday, find the number of days where there are an odd number of birthday celebrations.
# Input:
# The first line of the input consists of an integer days_size representing the number of birthdays celebrations (N).
# The second line of the input consists of N space-separated integers days representing the birthdays' celebrations in a month.
# Output:
# Print an integer representing the number of days where there is an odd number of birthday celebrations.
# Example:
# Input:
# 5
# 4 8 2 8 9

# Output:
# 3

# Explanation: 4, 2 and 9 occur only once (1 is odd). So, the answer is 3.

N = 5
birthdays = [4, 8, 2, 8, 9]

dic = {}

for i in birthdays:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

count = 0

for i in dic:
    if dic[i] % 2 != 0:
        count += 1
print(count)