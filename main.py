
#                              ПОИСК РАБОТЫ НА HH.RU
########################################################################################
import sqlite3
import csv

# Company (open second window with company_class.py code on the right side)
###############################################################################
from company_class import *

# BinaryTreeAu (open second window with binary_trees.py code on the right side)
###############################################################################
from binary_trees import *


# HashTable (open second window with hash_tables.py code on the right side)
###############################################################################
from hash_tables import *



with open("companies.csv", "w") as f:
    writer2 = csv.writer(f)
    writer2.writerow([1, 2, 3])






# Create a .db file and table if it's not yet exist
###################################################

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






# Load info from .db file, create new Company class instances, put them into Bi-Tree using BinaryTreeAu class
#############################################################################################################
def load_from_db(cursor):
    tree = BinaryTreeAu()
    cursor.execute("SELECT comp_name, position, requirements, salary FROM companies")
    rows = cursor.fetchall()
    for row in rows:
        company = Company(*row)
        tree.insert(company)
    return tree



# Write to a .csv file new company we found on hh.ru
####################################################
def write_to_csv(c_name, pos, req, sal):
    with open('companies.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            x = int(row[0])  # элемент на 0 индексе в каждой строке

    with open("companies.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([x+1, c_name, pos, req, sal])



# insert a New info about company to HashTable class and compare its name with names in BinaryTreeAu class
###########################################################################################################
def main():
    conn, cursor = create_db_and_table()
    tree = load_from_db(cursor)
    hash_table = HashTable(size=10)

    while True:
        comp_name = input("\nВведите название новой компании (или 'exit' для выхода): ")
        if comp_name.lower() == 'exit':
            break
        else:
            comp_name = comp_name[0] + (len(comp_name)-2)*"*" + comp_name[-1]
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

            write_to_csv(comp_name, position, requirements, salary)
        else:
            print("\n!!!!  YOU'VE ALREADY SENT THEM YOUR CV  !!!!")

    conn.close()

if __name__ == "__main__":
    main()

