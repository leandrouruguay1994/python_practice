def how_sum(targetSum, numbers, memo={}):
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None

    for num in numbers:
        reminder = targetSum - num
        reminderResult = how_sum(reminder, numbers, memo)
        if reminderResult != None:
            memo[targetSum] = [*reminderResult, num]
            return memo[targetSum]

    memo[targetSum] = None
    return None



"""print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 4]))
print(how_sum(8, [2, 3, 5]))"""
print(how_sum(300, [7, 14]))