# test_mini_homeworks.py
# Centralized tests for all mini_homeworks modules

import pytest
import mini_homeworks as hw


# ------------------ Array-based homeworks ------------------
class TestArrayFunctions:
    def test_insert_sorted(self):
        assert hw.insert_sorted([1, 3, 5], 4) == [1, 3, 4, 5]
        assert hw.insert_sorted([], 10) == [10]
        assert hw.insert_sorted([2, 4, 6], 1) == [1, 2, 4, 6]
        assert hw.insert_sorted([2, 4, 6], 10) == [2, 4, 6, 10]

    def test_find_min_max(self):
        assert hw.find_min_max([7, -2, 10, 4]) == (-2, 10)
        assert hw.find_min_max([5]) == (5, 5)
        assert hw.find_min_max([3, 3, 3]) == (3, 3)

    def test_merge_sorted(self):
        assert hw.merge_sorted([1, 4, 6], [2, 3, 5, 7]) == [1, 2, 3, 4, 5, 6, 7]
        assert hw.merge_sorted([], [1, 2]) == [1, 2]
        assert hw.merge_sorted([1, 2], []) == [1, 2]

    def test_middle_element(self):
        assert hw.middle_element([5, 6, 7, 8]) == 6
        assert hw.middle_element([10, 20, 30]) == 20
        assert hw.middle_element([42]) == 42


# ------------------ Linked list homeworks ------------------
class TestLinkedListFunctions:
    def test_merge_lists(self):
        a = hw.Node(1); a.next = hw.Node(2)
        b = hw.Node(3); b.next = hw.Node(4)
        merged = hw.merge_lists(a, b)
        result = []
        while merged:
            result.append(merged.data)
            merged = merged.next
        assert result == [1, 2, 3, 4]

    def test_find_middle(self):
        head = hw.Node(10)
        head.next = hw.Node(20)
        head.next.next = hw.Node(30)
        head.next.next.next = hw.Node(40)
        mid = hw.find_middle(head)
        assert mid.data == 30
        head.next.next.next.next = hw.Node(50)
        mid = hw.find_middle(head)
        assert mid.data == 30


# ------------------ String homeworks ------------------
class TestStringFunctions:
    def test_palindrome(self):
        assert hw.is_palindrome("madam") is True
        assert hw.is_palindrome("hello") is False
        assert hw.is_palindrome("") is True

    def test_balanced_brackets(self):
        assert hw.is_balanced("()") is True
        assert hw.is_balanced("([{}])") is True
        assert hw.is_balanced("(]") is False
        assert hw.is_balanced("(((()") is False


# ------------------ Queue / extra homeworks ------------------
class TestQueueFunctions:
    def test_parking_queue(self):
        q = hw.hw9_parking_queue.ParkingLot(capacity=2)
        q.arrive("car1")
        q.arrive("car2")
        assert len(q.queue) == 2
        q.depart()
        assert len(q.queue) == 1
        q.depart()
        q.depart()
        assert len(q.queue) == 0


# ------------------ Tree homeworks ------------------
class TestTreeFunctions:
    def test_traversals(self):
        root = hw.hw10_trees.build_sample_tree()
        assert hw.hw10_trees.preorder(root) == ["A", "B", "D", "E", "C"]
        assert hw.hw10_trees.inorder(root) == ["D", "B", "E", "A", "C"]
        assert hw.hw10_trees.postorder(root) == ["D", "E", "B", "C", "A"]

    def test_count_and_height(self):
        root = hw.hw10_trees.build_sample_tree()
        assert hw.hw10_trees.count_nodes(root) == 5
        assert hw.hw10_trees.height(root) == 3

    def test_expression_tree(self):
        expr_root = hw.hw10_trees.build_expression_tree()
        post = hw.hw10_trees.postorder(expr_root)
        assert post == ["4", "6", "2", "+", "*"]
        value = hw.hw10_trees.eval_postorder(post)
        assert value == 32
