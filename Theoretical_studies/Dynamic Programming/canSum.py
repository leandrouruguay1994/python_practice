def can_sum(target, numbers, memo={}):
    if target in memo: return memo[target]
    if target == 0: return True
    if target < 0: return False

    for num in numbers:
        reminder = target - num
        if can_sum(reminder, numbers, memo):
            memo[target] = True
            return True

    memo[target] = False
    return False


print(can_sum(300, [7, 14]))

