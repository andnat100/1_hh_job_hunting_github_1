
#                                КЛАСС HashTable
#######################################################################################
# print("\nHASH TABLE")

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


