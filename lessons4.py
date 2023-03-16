#                                                        УРОК НОМЕР 4

#                                                       изменяемые 

# списки (list) l = []
# мноества (set)
# словари (dict)

#                                                        неизменяемые 

# числа (int)
# строки (str)
# кортежи (tuple) t = ()


# name = ("Nurik", "Zhalgas", )

#List

# lists = []
# COUNT()  считает сколько в массиве одинаковых элементов 

# SORT()    сортирует 

# reverse  переварачивает 
# append -  добавить в лист 



# list_login = ['zheexen']
# list_password = ['123']

# login = input('Ввидите логин: ')
# passwaord = input('пароль: ')

# if login in list_login:
#     if passwaord in list_password:
#         secret_user = ['secret']

#         secret_user.append(login)
#         print(secret_user)
#     else:
#         print('не правильный пароль')
# else:
#     print('не правильный логин')            


#extend добавить внутрь листа другой лист 

# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8,]

# # a.append(b)

# a.extend(b)
# print(a)


# list = [1, 2, 3, 4, 5, 6, 7, ]
# list.insert(1,"zhexen")
# print(list)

# list = [1, 2, 3, 4, 5, 6, 7, ]

# list.remove(6)
# print(list)

# pop удаляет по индексу и если ничего не указать удаляет последний элемент 


# clear  очистка

# list = ["png", 'jpg', 'jpeg', 'gif', 'svg']
# file_list = []
# file_name = input().split('.')[-1]

# if len(file_name) >= 3:
#     file_list = file_name.lower()
#     print(file_list)
#     if file_name.lower() in list :
#         print('расширение доступно')
#     else:
#         print('не доступно')
# else:
#     pass                