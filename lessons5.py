# изменяемые
#   списки (list)
#   множества (set)
#   словари (dict)

# неизменяемыe:
#   числа (int, float)
#   строки (str)
#   кортежи (tuple)

# t = ([1])
# t[0].append('Hello')

# SET = {1,2,3,1}
# LIST = [1,2,3,1, 1,1,1,1,1]
# print(LIST)
# g = set(LIST)
# print(list(g))
# ________________________________________________
# a = {2,2,1,3,4,5,6,7,8,9,10,11,12,13, 'Hello'}
# b = {1,2,3,4,90,'Hello'}
# print(a)
# # print(a <= b)
# print(a.issubset(b))

# # print(a >= b)
# print(a.issuperset(b))

# print(a.isdisjoint(b)) # Не пересекаются

# print(a.union(b))

# print(a.intersection(b))
# print(a & b)

# print(a.difference(b))
# print(b - a)

# print(a.symmetric_difference(b))
# print(a ^ b)

# ____________________________________________________



# _____________________DICT___________________________

# users = {'name': 'John'}
# users = {
#     'name': 'John',
#     'age': 18,
#     1: 23,
# }
# [
#     {
#         'name': 'John',
#         'age': 18,
#     }
# ]

# print(users.get('age'))
# print(users.items())
# print(users.keys())
# print(users.values())
# kv = list(users.values())
# print(kv)

# n = ('name', 'marselle')
# k, v = n
# print(v)

# users = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'd': 4,
# }
# d = {
#     'e': 5
# }
# users['e'] = 10
# users['a'] = 23
# # users.update(e='hello')
# print(users.pop('a'))
# # print(users.popitem())
# # users.clear()
# print(users)

# menu = {

# 'lagman': 120, 
# 'plov': 120, 
# 'borsh': 100,    

# }

# menu['besh_barmak'] = 130
# menu['lagman'] = 135
# menu.pop('borsh')
    
# print(menu)

# menu['drinks'] = ['Coca-Cola', 'Sprite', 'Fanta']

# print(menu)


# s1 = {'add', 'clear', 'remove', 'update', 'difference', 'discard', 'intersection', 'intersection_update', 'pop', }
# s2 = {'clear', 'key', 'get', 'values', 'items', 'update', 'tuple', 'set', 'list', 'dict' }

 
# print(s1.intersection(s2))


# users = {}

# login = input('Ввидите логин: ')
# password = input('Ввидите пароль: ')
# password2 = input('Подтвердите пароль: ')
# if password == password2:
#     users[login] = password2
#     print(users)
# else:         
#     print('Пароль не совпадает')