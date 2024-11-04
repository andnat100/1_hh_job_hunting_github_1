
#####################################    BINARY TREES     ############################################
# print("\nBINARY TREES")



#                                  КЛАСС BinaryTreeAu
#######################################################################################

# for Companies I applyed for (which are already in DB)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTreeAu:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def inorder(self):
        if self.root is not None:
            self._inorder(self.root)

    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            print(node.value)
            self._inorder(node.right)

    def display_tree_diagram(self):
        self._display_recursive(self.root, 0)

    def _display_recursive(self, node, level):
        if node is not None:
            self._display_recursive(node.right, level + 1)
            print("   " * level + str(node.value))
            self._display_recursive(node.left, level + 1)

    def display(self):
        self._display_recursive2(self.root, 0)

    def _display_recursive2(self, node, level):
        if node is not None:
            self._display_recursive2(node.right, level + 1)
            print("   " * level + "|__" + str(node.value))
            self._display_recursive2(node.left, level + 1)

    def search(self, comp_name):
        return self._search(self.root, comp_name)

    def _search(self, node, comp_name):
        if node is None:
            return None
        if node.value.comp_name == comp_name:
            return node.value
        elif comp_name < node.value.comp_name:
            return self._search(node.left, comp_name)
        else:
            return self._search(node.right, comp_name)

    def save_to_db(self, cursor):
        self._save_recursive(self.root, cursor)

    def _save_recursive(self, node, cursor):
        if node is not None:
            cursor.execute("INSERT INTO companies (comp_name, position, requirements, salary) VALUES (?, ?, ?, ?)",
                           (node.value.comp_name, node.value.position, node.value.requirements, node.value.salary))
            self._save_recursive(node.left, cursor)
            self._save_recursive(node.right, cursor)