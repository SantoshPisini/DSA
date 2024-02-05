from typing import Union

class Node:
    def __init__(self, value):
        self.value: int = value
        self.left: Union[Node, None] = None
        self.right: Union[Node, None] = None

class Heap:
    def __init__(self) -> None:
        self.arr = []
    

def heap_driver():
    h = Heap()
