"""
Binary Search Tree implementation with sum_all function
"""
from typing import Optional, Any, Union
from collections import deque


class TreeNode:
    """Клас для вузла дерева"""
    
    def __init__(self, value: Union[int, float]):
        self.value = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
    
    def __repr__(self) -> str:
        return f"Node({self.value})"


class BinarySearchTree:
    """Бінарне дерево пошуку з методом обчислення суми"""
    
    def __init__(self):
        self.root: Optional[TreeNode] = None
    
    def insert(self, value: Union[int, float]) -> None:
        """Ітеративна вставка значення в дерево"""
        if self.root is None:
            self.root = TreeNode(value)
            return
        
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = TreeNode(value)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(value)
                    break
                current = current.right
    
    def sum_all(self) -> Union[int, float]:
        """Обчислення суми всіх значень у дереві (використовує BFS)"""
        if self.root is None:
            return 0
        
        total_sum = 0
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            total_sum += node.value
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return total_sum
    
    def sum_all_recursive(self) -> Union[int, float]:
        """Рекурсивна версія обчислення суми"""
        def _sum_recursive(node: Optional[TreeNode]) -> Union[int, float]:
            if node is None:
                return 0
            return node.value + _sum_recursive(node.left) + _sum_recursive(node.right)
        
        return _sum_recursive(self.root)
    
    def count_nodes(self) -> int:
        """Підрахунок кількості вузлів у дереві"""
        if self.root is None:
            return 0
        
        count = 0
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            count += 1
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return count
    
    def average_value(self) -> Optional[float]:
        """Обчислення середнього значення всіх вузлів"""
        count = self.count_nodes()
        if count == 0:
            return None
        return self.sum_all() / count


def create_bst_and_sum(values: list) -> Union[int, float]:
    """Створює дерево та повертає суму всіх елементів"""
    if not values:
        return 0
    
    bst = BinarySearchTree()
    for value in values:
        bst.insert(value)
    return bst.sum_all()
