"""
Алгоритм мінімізації витрат на з'єднання кабелів за допомогою купи (heap)
"""
import heapq
from typing import List, Tuple


def min_cost_to_connect_cables(cables: List[int]) -> int:
    """
    Знаходить мінімальні витрати на з'єднання всіх кабелів.
    
    Використовує жадібний алгоритм з мін-купою:
    - Завжди з'єднуємо два найкоротших кабелі
    - Результат з'єднання додаємо назад у купу
    - Продовжуємо до отримання одного кабеля
    
    Args:
        cables: Список довжин кабелів
        
    Returns:
        Мінімальні загальні витрати на з'єднання всіх кабелів
    """
    if not cables:
        return 0
    if len(cables) == 1:
        return 0
    
    heap = cables.copy()
    heapq.heapify(heap)
    
    total_cost = 0
    
    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        
        connection_cost = first + second
        total_cost += connection_cost
        
        heapq.heappush(heap, connection_cost)
    
    return total_cost


def min_cost_with_steps(cables: List[int]) -> Tuple[int, List[str]]:
    """
    Знаходить мінімальні витрати та показує кроки з'єднання.
    
    Args:
        cables: Список довжин кабелів
        
    Returns:
        Кортеж з (загальні витрати, список кроків)
    """
    if not cables:
        return 0, ["Немає кабелів для з'єднання"]
    if len(cables) == 1:
        return 0, [f"Лише один кабель довжиною {cables[0]}, з'єднання не потрібне"]
    
    heap = cables.copy()
    heapq.heapify(heap)
    
    total_cost = 0
    steps = []
    step_num = 1
    
    steps.append(f"Початкові кабелі: {sorted(cables)}")
    
    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        
        connection_cost = first + second
        total_cost += connection_cost
        
        steps.append(
            f"Крок {step_num}: З'єднуємо {first} + {second} = {connection_cost}, "
            f"витрати: {connection_cost}, загальні витрати: {total_cost}"
        )
        
        heapq.heappush(heap, connection_cost)
        step_num += 1
    
    steps.append(f"Фінальний кабель: {heap[0]}")
    steps.append(f"Загальні витрати: {total_cost}")
    
    return total_cost, steps


def compare_strategies(cables: List[int]) -> dict:
    """
    Порівнює різні стратегії з'єднання кабелів.
    
    Args:
        cables: Список довжин кабелів
        
    Returns:
        Словник з результатами різних стратегій
    """
    if len(cables) <= 1:
        return {
            "optimal": 0,
            "worst_case": 0,
            "sequential": 0
        }
    
    optimal_cost = min_cost_to_connect_cables(cables)
    
    heap_max = [-x for x in cables]
    heapq.heapify(heap_max)
    worst_cost = 0
    
    while len(heap_max) > 1:
        first = -heapq.heappop(heap_max)
        second = -heapq.heappop(heap_max)
        connection_cost = first + second
        worst_cost += connection_cost
        heapq.heappush(heap_max, -connection_cost)
    
    sequential_cost = 0
    current_length = cables[0]
    
    for i in range(1, len(cables)):
        current_length += cables[i]
        sequential_cost += current_length
    
    return {
        "optimal": optimal_cost,
        "worst_case": worst_cost,
        "sequential": sequential_cost,
        "savings_vs_worst": worst_cost - optimal_cost,
        "savings_vs_sequential": sequential_cost - optimal_cost
    }


def calculate_minimum_cost(cable_lengths: List[int]) -> int:
    """Обчислює мінімальну вартість з'єднання кабелів"""
    return min_cost_to_connect_cables(cable_lengths)
