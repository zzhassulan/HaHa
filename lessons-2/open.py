#               Работа с файлами 

# open - откритие файла
# работа с файлами 
#  close -  закрития файла 



#                                     open


# f = open('lessons-2/text1.txt', 'r')

# print(f)

# file = open('lessons-2/text.py', 'w')
# file.write('hello world')
# file.close

# Режим  Описание
# r      - Только для чтения.
# w      - Только для записи. Создаст новый файл, 
#           если не найдет с указанным именем.

# a      - Откроет для добавления нового содержимого. 
#         Создаст новый файл для записи, если не найдет с указанным именем.

# rb  - Только для чтения (бинарный).
# wb  - Только для записи (бинарный). 
#        Создаст новый файл, если не найдет с указанным именем.



# file = open('lessons-2/text.py', 'w')
# file.write('hello world ')
# file.close

# name = input('Введите имя: ')

# file.write(name)

# with open('lessons-2/text.py', 'r') as file:
#     with open('lessons-2/text2.py', 'w') as file2:
#         all_text = file.read()
#         file2.write(str(all_text))

# with open('путь к файлу', 'как обработать') as file:
#     ' Работа с файлами'

# Методы файла в Python 

# file.close()      закрывает открытый файл
# file.fileno()      возвращает целочисленный дескриптор файла
# file.flush()      очищает внутренний буфер
# file.isatty()      возвращает True, если файл привязан к терминалу
# file.next()      возвращает следующую строку файла
# file.read(n)      чтение первых n символов файла
# file.readline()  читает одну строчку строки или файла
# file.readlines()  читает и возвращает список всех строк в файле
# file.seek(offset[,whene])  устанавливает текущую позицию в файле
# file.seekable()  проверяет, поддерживает ли файл случайный доступ. Возвращает True, если да
# file.tell()      возвращает текущую позицию в файле
# file.truncate(n)  уменьшает размер файл. Если n указала, 
                    # то файл обрезается до n байт, если нет — до текущей позиции
# file.write(str)  добавляет строку str в файл
# file.writelines(sequence)  добавляет последовательность строк в файл


# f = open('lessons-2/text.txt', 'r')
# print(f.readlines())(3)


# Напишите программу, которая считывает файл и выводит количество строк в нем. 
# Для решения задачи нужно использовать for и if.

# with open('lessons-2/text.txt', 'r') as file:
#     count = 0 
#     for line in file:
#         if line.strip():
#             count += 1
#             print('количес строкв файле:',count)



# Напишите программу, которая считывает файл и выводит количество слов в нем. 
# Для решения задачи нужно использовать for, if и метод строки .split().


# with open('lessons-2/text.txt', 'r') as file:
#     count = 0 
#     for line in file:
#         words = line.split()
#         count += len(words)
#     print('words in file: ', count)    

# Напишите программу, которая считывает файл и выводит сумму всех чисел, содержащихся в нем. 
# Для решения задачи нужно использовать for, if.

# with open('lessons-2/text.txt', 'r') as file:
#     count = 0
#     for line in file:
#         words = line.split()
#         for word in words:
#             if word.isdigit():
#                 count += int(word)
#             else:
#                 continue
# print("summ: " , count)               



# Напишите программу, которая считывает файл и выводит на экран только те строки, 
# которые содержат слово "python". 
# Для решения задачи нужно использовать for, if и метод строки .find().

# with open('lessons-2/text.txt', 'r') as file:
#     num_lines = 0
#     for line in file:
#        if line.find('Python') != -1 or line.find('python') != -1:
#            print(line.strip())
        

# Напишите программу, которая считывает файл и выводит на экран только те строки, 
# которые начинаются с символа "#". 
# Для решения задачи нужно использовать for, if и метод строки .startswith().

# with open('lessons-2/text.txt', 'r') as file:
#     num_lines = 0
#     for line in file:
#        if line.startswith('#'):
#            print(line.strip())

# Напишите программу, которая считывает файл и выводит на экран только те строки, 
# которые заканчиваются символом "!" или "?". 
# Для решения задачи нужно использовать for, if и метод строки .endswith().

with open('lessons2/text.txt', 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            if word.endswith('!') or word.endswith('?'):
                print(line.strip()) # ['!']
# Напишите программу, которая считывает файл и выводит на экран только уникальные строки. 
# Для решения задачи нужно использовать for, if и множества.

# Напишите программу, которая считывает файл и записывает все строки в новый файл в обратном порядке. 
# Для решения задачи нужно использовать for, while и списки.

# Напишите программу, которая считывает файл и заменяет все вхождения слова "python" на "Java". 
# Для решения задачи нужно использовать for, if и метод строки .replace().

# Напишите программу, которая считывает файл и выводит на экран только те строки, 
# которые содержат как минимум два слова. 
# Для решения задачи нужно использовать for, if и метод строки .count().