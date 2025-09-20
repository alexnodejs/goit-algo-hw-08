"""
Демонстрація роботи алгоритмів для двійкового дерева пошуку
"""
import sys
import time
import random
from tasks.task1 import BinarySearchTree as BST1, create_bst_and_find_min
from tasks.task2 import BinarySearchTree as BST2, create_bst_and_sum
from tasks.task3 import min_cost_to_connect_cables, min_cost_with_steps, compare_strategies


def test_find_min():
    """Тестування функції find_min для бінарного дерева пошуку (Завдання 1)"""
    print("=" * 70)
    print("ЗАВДАННЯ 1: ТЕСТУВАННЯ АЛГОРИТМУ ПОШУКУ МІНІМУМУ В BST")
    print("=" * 70)
    
    print("\n✅ Тест 1: Базовий тест")
    test_values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35]
    print(f"Вхідні дані: {test_values}")
    
    bst = BST1()
    for value in test_values:
        bst.insert(value)
    
    min_val = bst.find_min()
    expected = min(test_values)
    print(f"Знайдений мінімум: {min_val}")
    print(f"Очікуваний мінімум: {expected}")
    assert min_val == expected, f"Помилка: очікувалось {expected}, отримано {min_val}"
    print("✅ Тест пройдено!")
    
    print("\n✅ Тест 2: Порожнє дерево")
    empty_bst = BST1()
    min_empty = empty_bst.find_min()
    print(f"Мінімум порожнього дерева: {min_empty}")
    assert min_empty is None, "Помилка: мінімум порожнього дерева повинен бути None"
    print("✅ Тест пройдено!")
    
    print("\n✅ Тест 3: Дерево з одним елементом")
    single_bst = BST1()
    single_bst.insert(42)
    min_single = single_bst.find_min()
    print(f"Єдиний елемент: 42")
    print(f"Знайдений мінімум: {min_single}")
    assert min_single == 42, "Помилка: мінімум повинен дорівнювати єдиному елементу"
    print("✅ Тест пройдено!")
    
    print("\n✅ Тест 4: Від'ємні числа")
    negative_values = [0, -5, 5, -10, -3, 3, 7, -15, -8]
    print(f"Вхідні дані: {negative_values}")
    
    negative_bst = BST1()
    for value in negative_values:
        negative_bst.insert(value)
    
    min_negative = negative_bst.find_min()
    expected_negative = min(negative_values)
    print(f"Знайдений мінімум: {min_negative}")
    print(f"Очікуваний мінімум: {expected_negative}")
    assert min_negative == expected_negative, f"Помилка: очікувалось {expected_negative}, отримано {min_negative}"
    print("✅ Тест пройдено!")
    
    print("\n✅ Тест 5: Допоміжна функція create_bst_and_find_min")
    helper_values = [15, 7, 22, 3, 9, 18, 27]
    print(f"Вхідні дані: {helper_values}")
    
    min_helper = create_bst_and_find_min(helper_values)
    expected_helper = min(helper_values)
    print(f"Знайдений мінімум: {min_helper}")
    print(f"Очікуваний мінімум: {expected_helper}")
    assert min_helper == expected_helper, f"Помилка: очікувалось {expected_helper}, отримано {min_helper}"
    print("✅ Тест пройдено!")


def test_sum_all():
    """Тестування функції sum_all для бінарного дерева пошуку (Завдання 2)"""
    print("\n" + "=" * 70)
    print("ЗАВДАННЯ 2: ТЕСТУВАННЯ АЛГОРИТМУ ОБЧИСЛЕННЯ СУМИ В BST")
    print("=" * 70)
    
    print("\n✅ Тест 1: Базовий тест")
    test_values = [50, 30, 70, 20, 40, 60, 80]
    print(f"Вхідні дані: {test_values}")
    
    bst = BST2()
    for value in test_values:
        bst.insert(value)
    
    sum_val = bst.sum_all()
    expected = sum(test_values)
    print(f"Знайдена сума: {sum_val}")
    print(f"Очікувана сума: {expected}")
    assert sum_val == expected, f"Помилка: очікувалось {expected}, отримано {sum_val}"
    print("✅ Тест пройдено!")
    
    print("\n✅ Тест 2: Порожнє дерево")
    empty_bst = BST2()
    sum_empty = empty_bst.sum_all()
    print(f"Сума порожнього дерева: {sum_empty}")
    assert sum_empty == 0, "Помилка: сума порожнього дерева повинна бути 0"
    print("✅ Тест пройдено!")
    
    print("\n✅ Тест 3: Дерево з одним елементом")
    single_bst = BST2()
    single_bst.insert(100)
    sum_single = single_bst.sum_all()
    print(f"Єдиний елемент: 100")
    print(f"Знайдена сума: {sum_single}")
    assert sum_single == 100, "Помилка: сума повинна дорівнювати єдиному елементу"
    print("✅ Тест пройдено!")
    
    print("\n✅ Тест 4: Від'ємні числа")
    negative_values = [10, -5, 20, -10, 0, 15, 30]
    print(f"Вхідні дані: {negative_values}")
    
    negative_bst = BST2()
    for value in negative_values:
        negative_bst.insert(value)
    
    sum_negative = negative_bst.sum_all()
    expected_negative = sum(negative_values)
    print(f"Знайдена сума: {sum_negative}")
    print(f"Очікувана сума: {expected_negative}")
    assert sum_negative == expected_negative, f"Помилка: очікувалось {expected_negative}, отримано {sum_negative}"
    print("✅ Тест пройдено!")
    
    print("\n✅ Тест 5: Дробові числа")
    float_values = [5.5, 2.3, 7.8, 1.1, 3.4, 6.6, 9.9]
    print(f"Вхідні дані: {float_values}")
    
    float_bst = BST2()
    for value in float_values:
        float_bst.insert(value)
    
    sum_float = float_bst.sum_all()
    expected_float = sum(float_values)
    print(f"Знайдена сума: {sum_float:.1f}")
    print(f"Очікувана сума: {expected_float:.1f}")
    assert abs(sum_float - expected_float) < 0.001, f"Помилка: очікувалось {expected_float}, отримано {sum_float}"
    print("✅ Тест пройдено!")
    
    print("\n✅ Тест 6: Порівняння ітеративної та рекурсивної версій")
    compare_values = [25, 15, 35, 10, 20, 30, 40, 5, 12, 18, 22]
    print(f"Вхідні дані: {compare_values}")
    
    compare_bst = BST2()
    for value in compare_values:
        compare_bst.insert(value)
    
    sum_iterative = compare_bst.sum_all()
    sum_recursive = compare_bst.sum_all_recursive()
    print(f"Сума (ітеративна): {sum_iterative}")
    print(f"Сума (рекурсивна): {sum_recursive}")
    assert sum_iterative == sum_recursive == sum(compare_values), "Помилка: результати не збігаються"
    print("✅ Обидві версії дають однаковий результат!")
    
    print("\n✅ Тест 7: Допоміжні функції")
    helper_values = [8, 4, 12, 2, 6, 10, 14]
    print(f"Вхідні дані: {helper_values}")
    
    helper_bst = BST2()
    for value in helper_values:
        helper_bst.insert(value)
    
    node_count = helper_bst.count_nodes()
    average = helper_bst.average_value()
    helper_sum = create_bst_and_sum(helper_values)
    
    print(f"Кількість вузлів: {node_count}")
    print(f"Середнє значення: {average:.2f}")
    print(f"Сума через допоміжну функцію: {helper_sum}")
    
    assert node_count == len(helper_values), "Помилка: неправильна кількість вузлів"
    assert abs(average - sum(helper_values)/len(helper_values)) < 0.001, "Помилка: неправильне середнє"
    assert helper_sum == sum(helper_values), "Помилка: неправильна сума від допоміжної функції"
    print("✅ Всі допоміжні функції працюють правильно!")


def test_cable_connection():
    """Тестування алгоритму з'єднання кабелів (Завдання 3)"""
    print("\n" + "=" * 70)
    print("ЗАВДАННЯ 3: ТЕСТУВАННЯ АЛГОРИТМУ З'ЄДНАННЯ КАБЕЛІВ")
    print("=" * 70)
    
    print("\n✅ Тест 1: Базовий приклад")
    cables1 = [4, 3, 2, 6]
    print(f"Довжини кабелів: {cables1}")
    
    cost1, steps1 = min_cost_with_steps(cables1)
    print("\nКроки з'єднання:")
    for step in steps1:
        print(f"  {step}")
    
    assert cost1 == 29, f"Помилка: очікувалось 29, отримано {cost1}"
    print("✅ Тест пройдено!")
    
    print("\n✅ Тест 2: Більший приклад")
    cables2 = [8, 4, 6, 12, 2, 1, 3]
    print(f"Довжини кабелів: {cables2}")
    
    cost2 = min_cost_to_connect_cables(cables2)
    print(f"Мінімальні витрати: {cost2}")
    
    expected2 = 91
    assert cost2 == expected2, f"Помилка: очікувалось {expected2}, отримано {cost2}"
    print("✅ Тест пройдено!")
    
    print("\n✅ Тест 3: Граничні випадки")
    
    empty_cables = []
    cost_empty = min_cost_to_connect_cables(empty_cables)
    print(f"Порожній список: витрати = {cost_empty}")
    assert cost_empty == 0, "Помилка: порожній список повинен мати витрати 0"
    
    single_cable = [10]
    cost_single = min_cost_to_connect_cables(single_cable)
    print(f"Один кабель [10]: витрати = {cost_single}")
    assert cost_single == 0, "Помилка: один кабель не потребує з'єднання"
    
    two_cables = [5, 7]
    cost_two = min_cost_to_connect_cables(two_cables)
    print(f"Два кабелі [5, 7]: витрати = {cost_two}")
    assert cost_two == 12, f"Помилка: очікувалось 12, отримано {cost_two}"
    
    print("✅ Всі граничні випадки пройдено!")
    
    print("\n✅ Тест 4: Однакові довжини кабелів")
    same_cables = [5, 5, 5, 5]
    print(f"Довжини кабелів: {same_cables}")
    
    cost_same = min_cost_to_connect_cables(same_cables)
    print(f"Мінімальні витрати: {cost_same}")
    assert cost_same == 40, f"Помилка: очікувалось 40, отримано {cost_same}"
    print("✅ Тест пройдено!")
    
    print("\n✅ Тест 5: Порівняння різних стратегій")
    cables5 = [20, 4, 8, 2, 5, 15]
    print(f"Довжини кабелів: {cables5}")
    
    strategies = compare_strategies(cables5)
    print(f"\nРезультати різних стратегій:")
    print(f"  Оптимальна (min-heap): {strategies['optimal']}")
    print(f"  Найгірша (max-heap): {strategies['worst_case']}")
    print(f"  Послідовна: {strategies['sequential']}")
    print(f"  Економія vs найгірша: {strategies['savings_vs_worst']}")
    print(f"  Економія vs послідовна: {strategies['savings_vs_sequential']}")
    
    assert strategies['optimal'] <= strategies['worst_case'], "Помилка: оптимальна стратегія повинна бути кращою"
    assert strategies['optimal'] <= strategies['sequential'], "Помилка: оптимальна стратегія повинна бути кращою"
    print("✅ Оптимальна стратегія дає найкращий результат!")
    
    print("\n✅ Тест 6: Великий випадковий тест")
    random_cables = random.sample(range(1, 100), 50)
    print(f"Кількість кабелів: {len(random_cables)}")
    print(f"Діапазон довжин: від {min(random_cables)} до {max(random_cables)}")
    
    start_time = time.perf_counter()
    cost_random = min_cost_to_connect_cables(random_cables)
    elapsed = time.perf_counter() - start_time
    
    print(f"Мінімальні витрати: {cost_random}")
    print(f"Час виконання: {elapsed:.6f} сек")
    
    assert cost_random > 0, "Помилка: витрати повинні бути додатними"
    assert cost_random > sum(random_cables), "Помилка: витрати повинні бути більшими за суму всіх кабелів"
    print("✅ Тест пройдено!")


def performance_test():
    """Тест продуктивності алгоритмів"""
    print("\n" + "=" * 70)
    print("ТЕСТ ПРОДУКТИВНОСТІ ВСІХ АЛГОРИТМІВ")
    print("=" * 70)
    
    test_sizes = [100, 1000, 10000, 50000]
    
    for size in test_sizes:
        print(f"\n📊 Розмір дерева: {size:,} елементів")
        
        random_values = random.sample(range(1, size * 10), size)
        
        bst1 = BST1()
        for val in random_values:
            bst1.insert(val)
        
        start_time = time.perf_counter()
        min_val = bst1.find_min()
        time_min = time.perf_counter() - start_time
        
        print(f"   Завдання 1 (find_min): {min_val}, час: {time_min:.6f} сек")
        assert min_val == min(random_values), "Помилка: неправильний мінімум"
        
        bst2 = BST2()
        for val in random_values:
            bst2.insert(val)
        
        start_time = time.perf_counter()
        sum_val = bst2.sum_all()
        time_sum = time.perf_counter() - start_time
        
        print(f"   Завдання 2 (sum_all): {sum_val}, час: {time_sum:.6f} сек")
        assert sum_val == sum(random_values), "Помилка: неправильна сума"
        
        cable_count = min(size // 10, 1000)
        random_cables = random.sample(range(1, cable_count * 10), cable_count)
        
        start_time = time.perf_counter()
        cable_cost = min_cost_to_connect_cables(random_cables)
        time_cable = time.perf_counter() - start_time
        
        print(f"   Завдання 3 ({cable_count} кабелів): витрати={cable_cost}, час: {time_cable:.6f} сек")


def complexity_analysis():
    """Аналіз складності алгоритмів"""
    print("\n" + "=" * 70)
    print("АНАЛІЗ СКЛАДНОСТІ АЛГОРИТМІВ")
    print("=" * 70)
    
    print("""
📚 ЗАВДАННЯ 1 - Алгоритм пошуку мінімуму в BST:
    
1. Принцип роботи:
   - Мінімальний елемент завжди знаходиться в найлівішому вузлі
   - Алгоритм просто йде ліворуч до кінця дерева
   
2. Часова складність:
   - Найкращий випадок: O(1) - корінь не має лівого піддерева
   - Середній випадок: O(log n) - збалансоване дерево  
   - Найгірший випадок: O(n) - виродження в список
   
3. Просторова складність: O(1)

📚 ЗАВДАННЯ 2 - Алгоритм обчислення суми всіх значень в BST:

1. Принцип роботи:
   - Обхід всіх вузлів дерева (BFS або DFS)
   - Додавання значення кожного вузла до загальної суми
   
2. Часова складність:
   - Всі випадки: O(n) - потрібно відвідати кожен вузол
   
3. Просторова складність:
   - Ітеративна версія (BFS): O(w), де w - максимальна ширина дерева
   - Рекурсивна версія (DFS): O(h), де h - висота дерева
   
4. Порівняння методів:
   - BFS краще для широких дерев (менша глибина стеку)
   - DFS краще для глибоких вузьких дерев (менша черга)
   - Обидва методи дають однаковий результат

📚 ЗАВДАННЯ 3 - Алгоритм з'єднання кабелів з мінімальними витратами:

1. Принцип роботи (жадібний алгоритм):
   - Завжди з'єднуємо два найкоротших кабелі
   - Використовується мін-купа (min-heap) для швидкого пошуку мінімумів
   - Новий кабель додається назад у купу
   
2. Часова складність:
   - O(n log n) - де n кількість кабелів
   - Кожна операція з купою: O(log n)
   - Виконується n-1 з'єднань
   
3. Просторова складність:
   - O(n) - для зберігання купи
   
4. Оптимальність:
   - Алгоритм гарантує мінімальні витрати
   - Це оптимальне рішення задачі (доведено математично)
   - Відомий як алгоритм Хаффмана для з'єднання
""")


def main():
    """Головна функція програми"""
    print("\n" + "🌳" * 35)
    print("\n       АЛГОРИТМИ ДЛЯ ДЕРЕВ ТА КУП (ДОМАШНЯ РОБОТА 8)")
    print("\n" + "🌳" * 35 + "\n")
    
    try:
        test_find_min()
        test_sum_all()
        test_cable_connection()
        performance_test()
        complexity_analysis()
        
        print("\n" + "=" * 70)
        print("✅ ВСІ ТЕСТИ ПРОЙДЕНО УСПІШНО!")
        print("✅ ЗАВДАННЯ 1: Пошук мінімуму в BST - працює правильно")
        print("✅ ЗАВДАННЯ 2: Обчислення суми в BST - працює правильно")
        print("✅ ЗАВДАННЯ 3: З'єднання кабелів з мін. витратами - працює правильно")
        print("=" * 70)
        return 0
        
    except AssertionError as e:
        print(f"\n❌ Помилка в тесті: {e}")
        return 1
    except Exception as e:
        print(f"\n❌ Несподівана помилка: {e}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
