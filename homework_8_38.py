# Задача 38: Дополнить телефонный справочник возможностью 
#изменения и удаления данных. Пользователь также может 
#ввести имя или фамилию, и Вы должны реализовать функционал 
#для изменения и удаления данных

import os

def selectAllReadPhoneNumber ():
    phoneBook = readData('./phonebook.txt')
    for i in phoneBook:
        print (i)

def selectSomethingReadPhoneNumber ():
    phoneBook = readData('./phonebook.txt')
    findColumn = int(input('''
                    \n 1 - Фамилия
                    \n 2 - Имя
                    \n 3 - Отчество
                    \n 4 - Телефон
                    \nУкажите, по какой колонке нужно искать:'''))
    findWord = str(input('Укажите значение для поиска:'))
    for i in phoneBook:
        if (findColumn == 1 and i[1].count(findWord) != 0):
            print (i)
        elif (findColumn == 2 and i[2].count(findWord) != 0): 
            print (i)
        elif (findColumn == 3 and i[3].count(findWord) != 0):
             print (i)
        elif (findColumn == 4 and i[4].count(findWord) != 0):
             print (i)


def readData (fileName):
    with open (fileName) as f:
        phoneBook = []
        for line in f:
            phoneBook.append(line.split(','))
    return phoneBook

def writeData (fileName, phoneBook):
    with open (fileName, 'w') as f:
        for i in phoneBook:
            f.write (','.join(i))
        
        print ("!!! Файл перезаписан !!!")

def addPerson ():
    phoneBook = readData('./phonebook.txt')
    print ("Введите данные:")
    number = '\n'+str(len(phoneBook) + 1)
    surname = str(input("Укажите Фамилию:"))
    nameFirst = str(input("Укажите имя:"))
    nameSecond = str(input("Укажите отчество:"))
    phoneNumber = str(input("Укажите номер телефона:"))
    phoneBook.append([number, surname, nameFirst, nameSecond, phoneNumber])
    writeData('./phonebook.txt', phoneBook)
def editSomethingReadPhoneNumber ():
    phoneBook = readData('./phonebook.txt')
    for i in phoneBook:
        print (i)
    edit_num = int(input('Укажите номер записи, которую нужно заменить: '))
    findColumn = int(input('''
                    \n 1 - Фамилия
                    \n 2 - Имя
                    \n 3 - Отчество
                    \n 4 - Телефон
                    \nУкажите, какое поле нужно заменить: '''))
    edit_value = input("Укажите новое значение: ")
    
    for i in phoneBook:
            if (i[0] == str(edit_num) and findColumn == 1): 
                i[1] = edit_value
            elif (i[0] == str(edit_num) and findColumn == 2): 
                  i[2] = edit_value
            elif (i[0] == str(edit_num) and findColumn == 3):
                i[3] = edit_value
            elif (i[0] == str(edit_num) and findColumn == 4): 
                i[4]=edit_value+'\n'
     
    writeData('./phonebook.txt', phoneBook)
    

def deleteSomethingReadPhoneNumber ():
    
    phoneBook = readData('./phonebook.txt')
    for i in phoneBook:
        print (i)
    delete_num = int(input('Укажите номер записи, которую нужно удать:'))
    for i in phoneBook:
        if i[0] == str(delete_num): phoneBook.remove(i)
    
    writeData('./phonebook.txt', phoneBook)


def ShowMenu():
    print ('''HELLO, USER 
            \n [1] -- Вывод данных из файла
            \n [2] -- Добавить и сохранять данные в текстовом файле 
            \n [3] -- Поиск по характеристике (Например имя или фамилию человека)
            \n [4] -- Измененить данные
            \n [5] -- Удалить данные
            \n [9] -- Показать выбор команд
            \n [0] -- Выход''')

clear = lambda: os.system ('clear')
clear()

ShowMenu()
while True:
    try:
        print('\n Выберете пунтк меню. [9] -- Показать выбор команд: ')
        enteredNum = int(input())
        if (enteredNum == 1):
            selectAllReadPhoneNumber()
        elif (enteredNum == 2):
            addPerson ()
        elif (enteredNum == 3):
            selectSomethingReadPhoneNumber ()
        elif (enteredNum == 4):
            editSomethingReadPhoneNumber ()
        elif (enteredNum == 5):
            deleteSomethingReadPhoneNumber ()
        
        elif (enteredNum == 9):
            ShowMenu()
            
        elif (enteredNum == 0):
            break
        else: 
            print("Нет такого пункта меню. [9] -- Показать выбор команд")
    except:
        print('Некорректный ввод. Попробуйте еще раз! [9] -- Показать выбор команд')