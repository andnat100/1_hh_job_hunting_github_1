
#############################################################################################
#                                     FULL CODE
#############################################################################################

import sqlite3





#                    КЛАСС Company - for info about new company where i send my CV
#######################################################################################


class Company:
    company_id = 0

    def __init__(self, comp_name, position, requirements, salary):
        self._comp_name = comp_name
        self._position = position
        self._requirements = requirements
        self._salary = salary

    @property
    def comp_name(self):
        return self._comp_name

    @property
    def position(self):
        return self._position

    @property
    def requirements(self):
        return self._requirements

    @property
    def salary(self):
        return self._salary

    def __str__(self):
        return f"'{self._comp_name}': position is {self._position}, salary is {self._salary}"

    def __repr__(self):
        return f"Company({self._comp_name}, {self._position}, {self._requirements}, {self._salary})"

    def __lt__(self, other):
        return self._comp_name < other._comp_name

    def __eq__(self, other):
        if isinstance(other, Company):
            return self._comp_name == other._comp_name
        return False

    def __hash__(self):
        return hash(self._comp_name)









#          КЛАСС BinaryTreeAu
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






#                                КЛАСС HashTable
#######################################################################################

# for New Vacancy from new Company I am sending CV to
# Using HashTable class for adding a new object

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for i in range(size)]
        print(f"{self.table} created")

    def _hash_function(self, key):
        """Простая хеш-функция: сумма ASCII-кодов символов ключа, по модулю размера таблицы."""
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        """Вставка пары ключ-значение в хеш-таблицу"""
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # Обновление значения, если ключ уже существует
                return
        self.table[index].append([key, value])  # Добавляем новую пару

    def get(self, key):
        """Получение значения по ключу."""
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        raise KeyError(f"Ключ '{key}' не найден.")

    def remove(self, key):
        """Удаление пары ключ-значение по ключу."""
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return
        raise KeyError(f"Ключ '{key}' не найден.")

    def __str__(self):
        """Строковое представление хеш таблицы"""
        return "\n".join(str(bucket) for bucket in self.table)





# Create a .db file and table if it's not yet exist
def create_db_and_table():
    conn = sqlite3.connect('companies.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS companies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        comp_name TEXT NOT NULL,
        position TEXT NOT NULL,
        requirements TEXT NOT NULL,
        salary INTEGER NOT NULL
    )
    ''')

    conn.commit()
    return conn, cursor



# Load info from .db file to BinaryTreeAu class
def load_from_db(cursor):
    tree = BinaryTreeAu()
    cursor.execute("SELECT comp_name, position, requirements, salary FROM companies")
    rows = cursor.fetchall()
    for row in rows:
        company = Company(*row)
        tree.insert(company)
    return tree



# insert a New info about company to HashTable class and compare its name with names in BinaryTreeAu class
def main():
    conn, cursor = create_db_and_table()
    tree = load_from_db(cursor)
    hash_table = HashTable(size=10)

    while True:
        comp_name = input("Введите название новой компании (или 'exit' для выхода): ")
        if comp_name.lower() == 'exit':
            break
        else:
            comp_name = comp_name[0] + (len(comp_name)-2) * "*" + comp_name[-1]
        position = input("Введите позицию: ")
        requirements = input("Введите требования: ")
        salary = int(input("Введите зарплату: "))

        new_company = Company(comp_name, position, requirements, salary)
        hash_table.insert(comp_name, new_company)

        # Проверка наличия компании в бинарном дереве
        if tree.search(comp_name) is None:
            tree.insert(new_company)
            cursor.execute("INSERT INTO companies (comp_name, position, requirements, salary) VALUES (?, ?, ?, ?)",
                           (comp_name, position, requirements, salary))
            conn.commit()

    conn.close()

if __name__ == "__main__":
    main()
