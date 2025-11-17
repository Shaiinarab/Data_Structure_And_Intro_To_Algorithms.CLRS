"""
mini_homeworks package
Author: Shahin Arab
Student ID: 401433113
Data Architecture & Algorithms Homeworks
"""

from .hw1_insert_sorted import insert_sorted
from .hw2_min_max import find_min_max
from .hw3_merge_lists import merge_sorted
from .hw4_middle_element import middle_element
from .hw5_linked_merge import Node, merge_lists
from .hw6_linked_middle import find_middle
from .hw7_palindrome import is_palindrome
from .hw8_brackets import is_balanced
from .hw9_parking_queue import main as parking_queue

__all__ = [
    "insert_sorted",
    "find_min_max",
    "merge_sorted",
    "middle_element",
    "Node",
    "merge_lists",
    "find_middle",
    "is_palindrome",
    "is_balanced",
    "parking_queue",
]

__author__ = "Shahin Arab"
__student_id__ = "401433113"
__version__ = "1.0.1"