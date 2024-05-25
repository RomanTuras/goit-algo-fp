def greedy_algorithm(items, budget):
    '''Жадібний алгоритм'''
    # Список страв з їх співвідношенням калорій до вартості
    item_list = [(name, info['cost'], info['calories'], info['calories'] / info['cost']) for name, info in items.items()]
    # Сортування списку за спаданням співвідношення калорій до вартості
    item_list.sort(key=lambda x: x[3], reverse=True)

    total_calories = 0
    selected_items = []

    for name, cost, calories, ratio in item_list:
        if budget >= cost:
            selected_items.append(name)
            total_calories += calories
            budget -= cost

    result = f"Перелік страв: {selected_items}" \
        + '\n' + f"Загальна калорійність: {total_calories}" \
        + '\n' + f"Решта: {budget}"
    return result


def dynamic_programming(items, budget):
    '''Алгоритм лінійного програмування'''
    # Створюємо dp[i][j], де i - калорійність, j - ціна
    n = len(items)
    item_names = list(items.keys())
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name = item_names[i - 1]
        cost = items[name]['cost']
        calories = items[name]['calories']
        for j in range(budget + 1):
            if j >= cost:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + calories)
            else:
                dp[i][j] = dp[i-1][j]

    # Відновлення обраних страв
    selected_items = []
    total_calories = dp[n][budget]
    w = budget

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(item_names[i-1])
            w -= items[item_names[i-1]]['cost']

    result = f"Перелік страв: {selected_items}" \
        + '\n' + f"Загальна калорійність: {total_calories}" \
        + '\n' + f"Решта: {w}"
    return result

# Приклад використання
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
budget = 100

print()
print("Бюджет: ", budget)
print()
print("Результати застосування жадібного алгоритма:")
print(greedy_algorithm(items, budget))
print()
print("--------------")
print()
print("Результати застосування алгоритма лінійного програмування:")
print(dynamic_programming(items, budget))
