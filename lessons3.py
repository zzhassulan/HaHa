                                                              # методы стринга 

# name = input('Введите имя: ')
# lower - Нижний регист 
# title - первая буква с большой буквой
# upper - все буквы в верхем регистре 
# swapcase -  большие  буквы станут маленькими а  маленькие большими
# capitalize - бишет только первую букву заглавную 
# isdigit - проверяет все ли состоит из цифр 
#  isalpha - проверяет все ли состоит из буквы 
# isidentifier - проверяет все ли пишется слитно 
# isupper - проверяет все ли с большими буквами
# islower - проверяет все ли с маленькими буквами
# istitle - проверяет все ли заглавные буквы с большими буквами
# isspace - проверяет есть ли пробел 

# name = input(" name ")


# if name.isalpha():
#     if len(name) > 5:
#         if name.istitle():
#             print('Все с именем хорошо')
#         else:
#             print('Начальная буква должна быть в вехрнем регистре')
#     else:
#         print('Имя должна быть больше 4')
# else:
#     print('Имя должна быть в буквах')

# strip - убирает пробелы  с право и с лево 
# center - цинтрует текст 

# text = "hello world "
# r =  text.rjust(15,"*")
# print(r.ljust(19,"#"))

# a = "hellow,\n world"
# print(a)

# text = "hello, world"
# print(text.replace("o", ' '))



# print(text.find("l")) # ищет индекс
# print(text.count("l"))
# split - это лист 
# print(text.partition())

#print(text.startswith)  находит начальную букву

# endswith c конца

 #                                                                 Срезы



# text = "https;//www.google.com"

# print(text[3])


# passwaord1 = input("Ввидите пароль: ")
# passwaord2 = input("Ввидите пароль: ")


# if passwaord1 == passwaord2:
#         if len(passwaord1)> 8:
#             if passwaord1.find("123"):
#                 if passwaord1:
#                     print("|*|".join(passwaord1))
#                 else:
#                     pass    
#             else:
#                 print("easy passwaord")
#         else:
#             print("your password have to be more 8 ")
# else:
#         print("your password not same")


# a = input()
# b = input()
# print(f"{a} {a} {b} {b} {b}")
