import numpy as np

# 1. Данные персонажей: [Сила, Ловкость, Интеллект]
# Представим массив из 4-х персонажей (Воин, Плут, Маг, Жрец)
squad_stats = np.array([
    [18, 14, 8],   # Воин
    [10, 18, 12],  # Плут
    [8, 12, 18],   # Маг
    [14, 10, 14]   # Жрец
])

# 2. Веса характеристик для конкретной задачи (например, "Штурм форта")
# Сила важнее всего (0.6), Ловкость (0.3), Интеллект (0.1)
task_weights = np.array([0.6, 0.3, 0.1])

# 3. Менеджмент ресурсов: Коэффициент усталости для каждого героя
# (1.0 - свеж, 0.5 - измотан)
fatigue_levels = np.array([0.9, 1.0, 0.7, 0.8])

def calculate_power(stats, weights, fatigue):
    """
    Расчет боевой мощи через векторизацию.
    """
    # Матричное умножение характеристик на веса задачи (Dot Product)
    base_power = np.dot(stats, weights)
    
    # Применение усталости (поэлементное умножение)
    final_power = base_power * fatigue
    
    return final_power

# Выполнение расчета
results = calculate_power(squad_stats, task_weights, fatigue_levels)

# Вывод результатов
classes = ["Воин", "Плут", "Маг", "Жрец"]
for name, power in zip(classes, results):
    print(f"Эффективность {name}: {power:.2f}")

# Демонстрация векторизации:
print(f"\nСредняя мощь отряда: {np.mean(results):.2f}")
