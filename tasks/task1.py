"""
Binary Search Tree implementation with find_min function
"""
from abc import ABC, abstractmethod
from typing import Optional, Any


class TreeNode:
    """Базовий клас для вузла дерева"""
    
    def __init__(self, value: Any):
        self.value = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
    
    def __repr__(self) -> str:
        return f"Node({self.value})"


class AbstractTree(ABC):
    """Абстрактний базовий клас для дерева"""
    
    def __init__(self):
        self.root: Optional[TreeNode] = None
    
    @abstractmethod
    def insert(self, value: Any) -> None:
        """Абстрактний метод вставки"""
        pass
    
    def find_min(self) -> Optional[Any]:
        """
        Знаходження мінімального значення в дереві.
        В BST мінімум завжди в найлівішому вузлі.
        """
        if self.root is None:
            return None
        
        current = self.root
        while current.left is not None:
            current = current.left
        return current.value


class BinarySearchTree(AbstractTree):
    """Бінарне дерево пошуку"""
    
    def insert(self, value: Any) -> None:
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


def create_bst_and_find_min(values: list) -> Optional[Any]:
    """Створює дерево та знаходить мінімум"""
    if not values:
        return None
    
    bst = BinarySearchTree()
    for value in values:
        bst.insert(value)
    return bst.find_min()
