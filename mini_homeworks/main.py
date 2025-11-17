# main.py
# Launcher for Shahin Arab's Data Architecture & Algorithms Homeworks

from mini_homeworks import (
    insert_sorted, find_min_max, merge_sorted, middle_element,
    Node, merge_lists, find_middle, is_palindrome, is_balanced,
    parking_queue
)

def banner():
    print("=" * 60)
    print("🌟 Shahin Arab | Student No: 401433113 🌟".center(60))
    print(" Data Architecture & Algorithms Mini Homeworks ".center(60))
    print("=" * 60)

def menu():
    print("\nChoose a homework to run:")
    print("1. Insert into sorted array")
    print("2. Find min & max in array")
    print("3. Merge two sorted arrays")
    print("4. Find middle element of array")
    print("5. Merge two linked lists")
    print("6. Find middle of linked list")
    print("7. Check palindrome string")
    print("8. Check balanced brackets")
    print("9. 🚗 Parking lot simulation using queue")

def main():
    banner()
    menu()
    choice = input("\nEnter choice (1-9): ")

    if choice == "1":
        arr = [1, 3, 5, 9]
        x = int(input("Enter a number: "))
        print("Result:", insert_sorted(arr, x))

    elif choice == "2":
        arr = [7, -2, 10, 4, 4]
        print("Min & Max:", find_min_max(arr))

    elif choice == "3":
        print("Merged:", merge_sorted([1, 4, 6], [2, 3, 5, 7]))

    elif choice == "4":
        print("Middle element:", middle_element([5, 6, 7, 8]))

    elif choice == "5":
        a = Node(1); a.next = Node(2)
        b = Node(3); b.next = Node(4)
        merged = merge_lists(a, b)
        print("Merged linked list:", end=" ")
        while merged:
            print(merged.data, end=" -> ")
            merged = merged.next
        print("None")

    elif choice == "6":
        head = Node(10)
        head.next = Node(20)
        head.next.next = Node(30)
        head.next.next.next = Node(40)
        mid = find_middle(head)
        print("Middle node:", mid.data)

    elif choice == "7":
        s = input("Enter a string: ")
        print("Palindrome?", is_palindrome(s))

    elif choice == "8":
        s = input("Enter a string with brackets: ")
        print("Balanced?", is_balanced(s))

    elif choice == "9":
        parking_queue()

    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()