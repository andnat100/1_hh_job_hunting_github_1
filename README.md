# Мой проект
Using OOP, Data Structures and Algorithms Example

  Этот проект предназначен для того чтобы продемонстрировать работу с языком Python: 
модель(парадигму) программирования OOP, умение работать с алгоритмами и структурами данных.
В этом проекте использованы хеш таблица и бинарное дерево.
Для хранения данных используем СУБД Sqlite.
В качестве системы контроля версий используется Git и Github 

  Проект позволяет отслеживать вакансии с hh.ru на которые я откликнулся. 
  При запуске программы в бинарное дерево загружаются все данные о компании,
  далее я вношу новые данные которые заносятся в хеш таблицу, 
  новые данные из хеш-таблицы сравниваются с данными из дерева(из СУБД изначально),
  если такой компании еще нет в базе данных, в базу данных добавляется новая компания.