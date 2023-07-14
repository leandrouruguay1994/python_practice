def best_sum(target, numbers, memo={}):
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None

    shortestCombination = None

    for num in numbers:
        reminder = target - num
        reminderCombo = best_sum(reminder, numbers, memo)
        if reminderCombo != None:
            combination = [*reminderCombo, num]
            if shortestCombination is None or len(combination) < len(shortestCombination):
                shortestCombination = combination

    memo[target] = shortestCombination
    return shortestCombination


print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(8, [1, 4, 5]))
print(best_sum(100, [1, 2, 5, 25]))