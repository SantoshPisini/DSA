from collections import deque
from typing import Union


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Build Tree
def build_tree_from_level_order(ip: list[int]) -> Union[Node, None]:
    if not ip:
        return None
    values = iter(ip)
    root = Node(next(values))
    queue = [root]
    while queue and values:
        node = queue.pop(0)
        left_value = next(values, None)
        if left_value:
            left_node = Node(left_value)
            node.left = left_node  # type: ignore
            queue.append(left_node)
        right_value = next(values, None)
        if right_value:
            right_node = Node(right_value)
            node.right = right_node  # type: ignore
            queue.append(right_node)
    return root


def inorder(node: Node):
    if node:
        inorder(node.left)  # type: ignore
        print(node.data)
        inorder(node.right)  # type: ignore


def preorder(node: Node):
    if node:
        print(node.data)
        preorder(node.left)  # type: ignore
        preorder(node.right)  # type: ignore


def postorder(node: Node):
    if node:
        postorder(node.left)  # type: ignore
        postorder(node.right)  # type: ignore
        print(node.data)


def levelorder(root: Node):
    if not root:
        return []
    queue = deque()
    queue.append(root)
    queue.append(None)  # Adding this for pretty print when None occurs
    while queue:
        node: Node = queue.popleft()
        if node is None:
            print()
            if queue:
                # This None if for next level flag
                queue.append(None)
            else:
                break
        else:
            print(node.data, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


def count_of_nodes(root: Node):
    if not root:
        return 0
    left = count_of_nodes(root.left)  # type: ignore
    right = count_of_nodes(root.right)  # type: ignore
    return left + right + 1


def sum_of_nodes(root: Node):
    if not root:
        return 0
    left = sum_of_nodes(root.left)  # type: ignore
    right = sum_of_nodes(root.right)  # type: ignore
    return left + right + root.data


def height_of_tree(root: Node):
    if not root:
        return 0
    left = height_of_tree(root.left)  # type: ignore
    right = height_of_tree(root.right)  # type: ignore
    return max(left, right) + 1


def diameter_of_tree(root: Node):
    if not root:
        # Diameter, Height
        return [0, 0]
    left = diameter_of_tree(root.left)  # type: ignore
    right = diameter_of_tree(root.right)  # type: ignore
    # Diameter = max of leftH+rightH+1, leftD, rightD
    return [max((left[1] + right[1] + 1), left[0], right[0]), max(left[1], right[1]) + 1]


def is_subtree(root: Node, subRoot: Node):
    def is_identical(root: Node, subRoot: Node):
        if root == None and subRoot == None:
            return True
        if root == None or subRoot == None:
            return False
        if root.data == subRoot.data:
            return is_identical(root.left, subRoot.left) and is_identical(root.right, subRoot.right) # type: ignore
        return False

    if subRoot is None:
        return True
    if root is None:
        return False
    if is_identical(root, subRoot):
        return True
    return is_subtree(root.left, subRoot) or is_subtree(root.right, subRoot) # type: ignore


def sum_at_level(root: Node, level: int):
    # Level is 1 indexed
    if not root:
        return []
    queue = deque()
    queue.append(root)
    queue.append(None)  # Adding this for pretty print when None occurs
    _sum = 0
    _index = 0
    while queue:
        node: Node = queue.popleft()
        if node is None:
            _index += 1
            # print("Sum: ", _sum) # type: ignore
            if _index == level:
                return _sum
            if queue:
                # This None if for next level flag
                queue.append(None)
                _sum = 0
            else:
                return 0
        else:
            # print(node.data, end=" ")
            _sum += node.data
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


# Level order input
ip = [1, 2, 3, 4, 5, 6, 7]
# ip = [1, 2, 3, 4, 5, None, 7]
# ip = [1, 2, 8, 5, 3, None, None, 6, None, None, 4, 7]
root: Node = build_tree_from_level_order(ip)  # type: ignore
# print("Inorder: ")
# inorder(root)
# print("Preorder: ")
# preorder(root)
# print("Postorder: ")
# postorder(root)
# levelorder(root)
# print(count_of_nodes(root=root))
# print(sum_of_nodes(root=root))
# print(height_of_tree(root))
# print(diameter_of_tree(root)[0])
# SubTree check
# subRoot: Node = build_tree_from_level_order([21, 4, 5])  # type: ignore
# print(is_subtree(root, subRoot))
print(sum_at_level(root, 3))
