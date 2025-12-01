class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 1) Traversals: preorder, inorder, postorder (return list of values)
def preorder(root):
    if not root:
        return []
    return [root.value] + preorder(root.left) + preorder(root.right)

def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)

def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.value]

# 2) Count total nodes
def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# 3) Compute tree height (edges or levels). Here: levels (empty tree = 0)
def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

# 4) Expression tree for (4 * (6 + 2)) and postorder evaluation
def eval_postorder(tokens):
    """
    Evaluate expression given a postorder list of tokens, e.g. ['4','6','2','+','*'].
    Supports +, -, *, / for integers.
    """
    stack = []
    for t in tokens:
        if t in {"+", "-", "*", "/"}:
            b = stack.pop()
            a = stack.pop()
            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(a - b)
            elif t == "*":
                stack.append(a * b)
            elif t == "/":
                stack.append(a // b)  # integer division
        else:
            stack.append(int(t))
    return stack[-1]

def build_sample_tree():
    """
    Build sample tree:
          A
         / \
        B   C
       / \
      D   E
    """
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node("E")
    A.left, A.right = B, C
    B.left, B.right = D, E
    return A

def build_expression_tree():
    """
    Build expression tree for (4 * (6 + 2)):
            *
           / \
          4   +
             / \
            6   2
    """
    mul = Node("*")
    four = Node("4")
    plus = Node("+")
    six = Node("6")
    two = Node("2")
    mul.left = four
    mul.right = plus
    plus.left = six
    plus.right = two
    return mul

def main():
    # Task 1: traversals on sample tree
    root = build_sample_tree()
    print("Preorder:", " -> ".join(preorder(root)))
    print("Inorder:", " -> ".join(inorder(root)))
    print("Postorder:", " -> ".join(postorder(root)))

    # Task 2: count nodes
    print("Node count:", count_nodes(root))

    # Task 3: height (levels)
    print("Height (levels):", height(root))

    # Task 4: expression tree and evaluation via postorder
    expr_root = build_expression_tree()
    expr_post = postorder(expr_root)           # e.g. ['4','6','2','+','*']
    print("Expression postorder:", " ".join(expr_post))
    value = eval_postorder(expr_post)
    print("Expression value:", value)
