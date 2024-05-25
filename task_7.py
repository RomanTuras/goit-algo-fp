import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    '''Симуляції кидків двох кубиків'''
    sums = [0] * 13  # Ініціалізуємо список для підрахунку кількості випадків кожної суми (від 2 до 12)

    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        roll_sum = roll1 + roll2
        sums[roll_sum] += 1

    return sums[2:]  # Повертаємо частину списку з сумами від 2 до 12

def calculate_probabilities(sums, num_rolls):
    '''Обчислення ймовірностей'''
    return [count / num_rolls for count in sums]

# Симуляція 1,000,000 кидків двох кубиків
num_rolls = 1000000
sums = simulate_dice_rolls(num_rolls)
probabilities = calculate_probabilities(sums, num_rolls)

# Аналітичні ймовірності
analytical_probabilities = [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]

# Виведення результатів
sums_values = list(range(2, 13))
for sum_value, prob, analytical_prob in zip(sums_values, probabilities, analytical_probabilities):
    print(f"Сума: {sum_value}, Імовірність (Монте-Карло): {prob:.5f}, Аналітична ймовірність: {analytical_prob:.5f}")

# Побудова графіку
plt.figure(figsize=(10, 6))
plt.bar(sums_values, probabilities, width=0.4, label='Монте-Карло', color='blue', alpha=0.6, align='center')
plt.plot(sums_values, analytical_probabilities, 'ro-', label='Аналітичні ймовірності', markersize=8)

plt.xlabel('Сума на кубиках')
plt.ylabel('Ймовірність')
plt.title('Ймовірність сум при киданні двох кубиків')
plt.legend()
plt.grid(True)
plt.show()
